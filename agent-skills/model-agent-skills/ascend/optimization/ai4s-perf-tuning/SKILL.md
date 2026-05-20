---
name: ai-for-science-ai4s-perf-tuning
description: AI for Science 场景下的昇腾 NPU 通用性能调优 Skill，覆盖流水优化（TASK_QUEUE_ENABLE）、CPU 绑核优化（CPU_AFFINITY_CONF）、高性能内存库 tcmalloc 替换等调度与 OS 级调优手段，以及基于毕昇编译器的 Python / PyTorch / torch_npu 编译优化（LTO + PGO），适用于 PyTorch 训练或推理场景在 Ascend NPU 上的性能提升。
keywords:
  - ai-for-science
  - performance
  - tuning
  - ascend
  - scheduling
  - tcmalloc
  - cpu-affinity
  - lto
  - pgo
  - bisheng-compiler
---

# 昇腾 NPU 通用性能调优 Skill

本 Skill 提供在华为昇腾 NPU 上进行通用性能调优的标准化流程，
聚焦调度优化、OS 级优化与编译优化三个层次，覆盖流水优化、CPU 绑核、
高性能内存库替换和基于毕昇编译器的 Python/PyTorch/torch_npu 编译优化。
适用于 PyTorch 训练或推理场景，且模型已完成基本迁移并能正常跑通的阶段。

## 重要默认行为

1. **先确认可跑通**：本 Skill 假设模型已在 NPU 上正常运行。如果模型尚未迁移完成，
   请先使用 [ai4s-basic](../models/ai4s-basic/SKILL.md) 完成迁移后再进入调优。

2. **渐进式调优**：建议按"流水优化 → 绑核优化 → tcmalloc 替换"的顺序逐项开启，
   每次只变更一个配置，观察性能变化后再叠加下一项，方便定位收益来源。
   **如果某项优化叠加后性能不升反降，应将其去掉，用剩余项的组合重新测试，
   找到最优子集**。例如：若三项全开后发现绑核导致性能下降，应去掉绑核，
   单独测试"流水优化 + tcmalloc"的组合效果。

3. **编译优化为进阶手段**：通用调优手段（第 1–3 节）完成后，主动询问用户是否愿意
   进一步做编译优化。编译优化需要从源码重新编译 Python / PyTorch / torch_npu，
   耗时较长且需要毕昇编译器环境，因此仅在用户确认后再执行。
   - **Python 编译优化（第 5 节）**：适用于所有场景，询问用户是否需要。
   - **PyTorch + torch_npu 编译优化（第 6、7 节）**：仅当项目基于 PyTorch 时询问，
     且必须按 PyTorch → torch_npu 的顺序执行。

4. **配合 Profiling 使用**：调优前后建议各采集一次 Profiling 数据以量化收益，
   可配合 [ai4s-profiling](../ai4s-profiling/SKILL.md) 使用。

## 前置条件

| 项目 | 要求 |
|------|------|
| 硬件 | Ascend910 系列（至少 1 卡） |
| CANN | ≥ 8.0（推荐 8.2+） |
| Python | 3.8 – 3.10 |
| PyTorch | 与 CANN 版本匹配 |
| torch_npu | 与 PyTorch 版本一致 |

## 调优流程总览

```
0. 环境准备与基线性能采集
→ 1. 流水优化（TASK_QUEUE_ENABLE）
→ 2. CPU 绑核优化（CPU_AFFINITY_CONF）
→ 3. 高性能内存库替换（tcmalloc）
→ 4. 调优效果验证
→ 5. [进阶·询问用户] Python 编译优化（LTO + PGO）
→ 6. [进阶·Torch 模型·询问用户] PyTorch 编译优化（LTO + PGO）
→ 7. [进阶·Torch 模型·询问用户] torch_npu 编译优化（LTO + PGO）
→ 8. 最终效果验证
```

---

## 0. 环境准备与基线性能采集

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
npu-smi info
python3 -c "import torch; import torch_npu; print(torch.npu.is_available())"
```

建议在调优前先记录一次基线性能数据（如 epoch 耗时、吞吐量），
后续每开启一项优化后对比同一指标。

---

## 1. 流水优化（一级流水）

### 1.1 原理

一级流水优化将部分算子适配任务从 Host 侧一级流水迁移至 Device 侧二级流水，
使两级流水负载更均衡，减少 dequeue 唤醒时间。主要适用于 **host-bound 严重**的网络场景。

### 1.2 使能方法

```bash
export TASK_QUEUE_ENABLE=2
```

在启动训练/推理脚本**之前**设置此环境变量。

### 1.3 注意事项

- `ASCEND_LAUNCH_BLOCKING=1` 时 task_queue 算子队列关闭，`TASK_QUEUE_ENABLE` 设置不生效。
- `TASK_QUEUE_ENABLE=2` 时由于内存并发，可能导致运行中 **NPU 内存峰值上升**。
  如遇 OOM，可尝试适当减小 batch_size 或回退到 `TASK_QUEUE_ENABLE=1`。
- 该环境变量的详细说明见[《环境变量参考》TASK_QUEUE_ENABLE 章节](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0058.html)。

---

## 2. CPU 绑核优化

### 2.1 原理

通过设置处理器亲和性，将 CPU 端算子任务绑定到 NPU 对应 NUMA 节点的 CPU 核心上，
避免跨 NUMA 节点的内存访问，减少任务调度开销。

提供两种粒度：

| 模式 | 说明 |
|------|------|
| 粗粒度（mode=1） | 绑定到 NPU 对应 NUMA 的全部 CPU 核心，支持自定义绑核范围 |
| 细粒度（mode=2） | 在粗粒度基础上锚定主要任务到固定 CPU 核心，减少核间切换开销 |

### 2.2 使能方法

```bash
# 粗粒度绑核
export CPU_AFFINITY_CONF=1

# 细粒度绑核
export CPU_AFFINITY_CONF=2

# 自定义多张卡的绑核范围（粗粒度 + 自定义）
export CPU_AFFINITY_CONF=1,npu0:0-1,npu1:2-5,npu3:6-6
```

参数格式：`<mode>,npu<卡号>:<起始核>-<结束核>`

- `mode=0` 或未设置：不启用绑核。
- `mode=1`：粗粒度绑核，可附加自定义范围覆写特定卡。
- `mode=2`：细粒度绑核。

### 2.3 查看 NUMA 拓扑

```bash
lscpu
```

关注 NUMA node 与 CPU 核心的对应关系，用于决定自定义绑核范围。

### 2.4 注意事项

- 虚拟机（Docker 等）中 NUMA 拓扑可能与物理机不一致，建议根据实际映射关系自定义绑核范围。
- 绑核特性触发时机较后，一般会**覆盖**外界的绑核设置（如 `taskset`）。
- 对 CPU 瓶颈的模型有较大提升，对 NPU 瓶颈的模型能保证性能持平。
- **对 vLLM 等自带多进程/多线程调度的推理框架，绑核可能产生负优化**，
  因为强制绑核会限制框架自身的线程并行度和 worker 进程调度灵活性。
  此类场景建议先单独测试绑核效果，确认有正向收益后再保留。
- 详细说明见[绑核优化文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0059.html)。

---

## 3. 高性能内存库替换（tcmalloc）

### 3.1 原理

tcmalloc（Thread-Caching Malloc）通过多层次缓存结构、减少互斥锁竞争、
优化大对象处理流程等手段提升内存分配性能。对频繁内存操作的训练场景尤为有效，
在高并发场景下能显著改善系统响应速度。

### 3.2 安装 tcmalloc

**方法一：系统包管理器安装（推荐）**

```bash
# openEuler
yum install gperftools

# CentOS
yum install gperftools gperftools-devel

# Ubuntu
sudo apt update
sudo apt install libgoogle-perftools4 libgoogle-perftools-dev
```

**方法二：源码编译安装**

需要系统已安装 `libunwind`。

```bash
wget https://github.com/gperftools/gperftools/releases/download/gperftools-2.16/gperftools-2.16.tar.gz
tar -xf gperftools-2.16.tar.gz && cd gperftools-2.16
./configure --prefix=/usr/local/lib --with-tcmalloc-pagesize=64
make
make install
```

### 3.3 确认动态库位置

```bash
# openEuler
rpm -ql gperftools-libs

# 通用搜索
find /usr -name "libtcmalloc.so*"
```

### 3.4 使能 tcmalloc

```bash
# 全局生效（当前终端所有程序）
export LD_PRELOAD="$LD_PRELOAD:/usr/local/lib/lib/libtcmalloc.so"

# 仅对单个程序生效
LD_PRELOAD="/usr/local/lib/lib/libtcmalloc.so" python train_script.py
```

路径需替换为实际的 `libtcmalloc.so` 位置。

### 3.5 验证是否生效

```bash
ldd $(which python)
```

输出中包含 `libtcmalloc` 的动态库路径，说明配置已生效。

### 3.6 注意事项

- 动态库路径因安装方式和系统不同而异，务必先用 `find` 确认实际路径。
- 详细说明见[高性能内存库替换文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0067.html)。

---

## 4. 调优效果验证

### 4.1 推荐组合配置

以下为候选优化项，**需根据逐项测试结果选择最优子集**，
不建议盲目全部开启——某些项在特定场景下可能产生负优化。

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh

# 流水优化（通常有正向收益）
export TASK_QUEUE_ENABLE=2

# CPU 绑核（粗粒度）—— 需先单独验证效果，对 vLLM 等推理框架可能负优化
# export CPU_AFFINITY_CONF=1

# tcmalloc（路径按实际替换）
export LD_PRELOAD="$LD_PRELOAD:/usr/local/lib/lib/libtcmalloc.so"

# 启动训练/推理
python train.py
```

> **负优化回退**：如果三项全开后总体性能不如预期，应逐项去掉效果不佳的优化，
> 重新测试剩余组合。例如实测中"流水优化 + tcmalloc"（不绑核）的组合
> 往往优于三项全开的效果。

### 4.2 对比指标

| 指标 | 说明 |
|------|------|
| 单步耗时 | 对比调优前后的平均 step time |
| 吞吐量 | samples/sec 或 tokens/sec |
| NPU 内存峰值 | `npu-smi info` 观察，注意流水优化可能提升峰值 |
| CPU 利用率 | `top` / `htop` 观察绑核后 CPU 使用分布 |

### 4.3 Profiling 量化

建议使用 [ai4s-profiling](../ai4s-profiling/SKILL.md) 在调优前后各采集一次 L0 级 Profiling，
对比 host 等待时间、算子执行时间等指标，量化调优收益。

---

## 5. 编译优化 — Python（LTO + PGO）

> **交互指引**：完成第 1–4 节通用调优后，询问用户：
> "通用调优已完成，是否需要进一步做 Python 编译优化？此项需要从源码重编 Python（使用毕昇编译器 + LTO + PGO），耗时较长但可提升 Python 解释器本身的执行效率。"

### 5.1 原理

Python 3.6+ 支持 LTO（链接时优化）和 PGO（基于性能数据的优化），
通过毕昇编译器（clang/clang++）编译 Python 解释器可获得额外性能收益。

### 5.2 前置：安装编译依赖

```bash
# Fedora / RHEL / CentOS / openEuler
sudo dnf install gcc gcc-c++ gdb lzma glibc-devel libstdc++-devel openssl-devel \
  readline-devel zlib-devel libffi-devel bzip2-devel xz-devel \
  sqlite sqlite-devel sqlite-libs libuuid-devel gdbm-libs perf \
  expat expat-devel mpdecimal python3-pip

# Debian / Ubuntu
sudo apt-get install build-essential gdb lcov pkg-config \
  libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
  libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
  lzma lzma-dev tk-dev uuid-dev zlib1g-dev libmpdec-dev
```

### 5.3 前置：配置毕昇编译器

参考[安装毕昇编译器](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0063.html)文档配置环境，并设置：

```bash
export CC=clang
export CXX=clang++
```

### 5.4 编译安装

以 Python 3.8.17 为例：

```bash
tar -xvf Python-3.8.17.tgz
cd Python-3.8.17
mkdir -p <Python安装目录>
./configure --prefix=<Python安装目录> --with-lto --enable-optimizations
make -j
make install
```

- `--with-lto`：启用 LTO 链接时优化。
- `--enable-optimizations`：启用 PGO 优化（编译期自动完成 profile 采集与二次编译）。
- Python 源码下载：https://www.python.org/downloads/source/

### 5.5 使用 conda 管理

```bash
conda create -n env_name --offline -y
# 将 --prefix 指向 conda 环境目录即可
# 编译完成后进入 bin 目录创建软链接
cd <Python安装目录>/bin
ln -s python3 python
ln -s pip3 pip
conda activate env_name
```

### 5.6 注意事项

- 编译后的 Python 可跨服务器迁移，但需注意 glibc 版本（低→高可以，反之不行）。
- 如果运行时报 `.so` 或模块找不到，检查编译依赖是否安装完全。
- 详细说明见[编译优化-Python 文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0063.html)。

---

## 6. 编译优化 — PyTorch（LTO + PGO）

> **交互指引**：仅当项目基于 PyTorch 时，询问用户：
> "当前项目使用 PyTorch 框架，是否需要用毕昇编译器对 PyTorch 进行 LTO/PGO 编译优化？
> 此项需要从源码重编 PyTorch，耗时较长，推荐在容器中进行。"

### 6.1 原理

使用毕昇编译器（clang）对 PyTorch C++ 后端进行 LTO（链接时优化）和
PGO（基于性能数据的优化），可显著降低算子调度和框架层开销。

### 6.2 获取源码

以 PyTorch 2.1 为例：

```bash
git clone -b v2.1.0 https://github.com/pytorch/pytorch.git pytorch-2.1.0
cd pytorch-2.1.0
git submodule sync
git submodule update --init --recursive
pip install -r requirements.txt
```

### 6.3 修改 CMakeLists.txt

注释掉以下行以屏蔽告警错误：

```
append_cxx_flag_if_supported("-Werror=cast-function-type" CMAKE_CXX_FLAGS)
```

### 6.4 仅 LTO 优化

```bash
export CMAKE_C_FLAGS="-flto=thin -fuse-ld=lld"
export CMAKE_CXX_FLAGS="-flto=thin -fuse-ld=lld"
export CC=clang
export CXX=clang++
export USE_XNNPACK=0

cd pytorch-2.1.0
git clean -dfx
python3 setup.py bdist_wheel
pip3 install dist/*.whl --force-reinstall --no-deps
```

### 6.5 LTO + PGO 优化（两次编译）

**第一次编译（插桩）：**

```bash
export CMAKE_C_FLAGS="-flto=thin -fuse-ld=lld -fprofile-generate=/path/to/profile"
export CMAKE_CXX_FLAGS="-flto=thin -fuse-ld=lld -fprofile-generate=/path/to/profile"
export CC=clang
export CXX=clang++
export USE_XNNPACK=0
export OMP_PROC_BIND=false

cd pytorch-2.1.0
git clean -dfx
python3 setup.py bdist_wheel
pip3 install dist/*.whl --force-reinstall --no-deps
```

安装插桩包后正常跑模型，采集 Profile 数据（插桩包性能会偏低，属正常现象）。

可通过环境变量指定 profraw 生成位置：

```bash
export LLVM_PROFILE_FILE=/tmp/profile/default_%m.profraw
```

**Profile 数据转换：**

```bash
llvm-profdata merge /path/to/profile -o default.profdata
```

**第二次编译（使用 Profile 数据）：**

```bash
export CMAKE_C_FLAGS="-flto=thin -fuse-ld=lld -fprofile-use=/path/to/profile/default.profdata"
export CMAKE_CXX_FLAGS="-flto=thin -fuse-ld=lld -fprofile-use=/path/to/profile/default.profdata"

cd pytorch-2.1.0
git clean -dfx
python3 setup.py bdist_wheel
```

二次编译后的 whl 包为正式使用的高性能包。安装后运行模型前确认：

```bash
export OMP_PROC_BIND=false
```

### 6.6 注意事项

- 推荐在容器中编译，避免环境污染。
- 如运行时报 `libomp.so` 找不到，需安装毕昇编译器包并配置 `LD_LIBRARY_PATH`。
- 详细说明见[编译优化-PyTorch 文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0064.html)。

---

## 7. 编译优化 — torch_npu（LTO + PGO）

> **交互指引**：仅当已完成第 6 节 PyTorch 编译优化后，询问用户：
> "PyTorch 已用毕昇编译器重编完成，是否继续对 torch_npu 也做 LTO/PGO 编译优化？
> torch_npu 的编译依赖上一步编译好的 PyTorch。"

### 7.1 前置条件

**必须先完成第 6 节 PyTorch 编译优化并安装**，torch_npu 编译依赖毕昇编译的 PyTorch。

### 7.2 获取源码

以 torch_npu v2.1.0 为例：

```bash
git clone -b v2.1.0 https://gitee.com/ascend/pytorch.git torch_npu
```

### 7.3 仅 LTO 优化

```bash
export CC=clang
export CXX=clang++

cd torch_npu
git clean -dfx
bash ci/build.sh --python=3.8 --enable_lto
pip install dist/torch_npu-*.whl --force-reinstall --no-deps
```

### 7.4 LTO + PGO 优化（两次编译）

**一次编译（插桩）：**

```bash
export CC=clang
export CXX=clang++

cd torch_npu
git clean -dfx
bash ci/build.sh --python=3.8 --enable_lto --enable_pgo=1
pip3 install dist/*.whl --force-reinstall --no-deps
```

配置 profraw 生成路径并正常跑模型：

```bash
export LLVM_PROFILE_FILE=/tmp/profile/default_%m.profraw
# 正常运行模型采集 Profile 数据
```

**Profile 数据转换：**

```bash
llvm-profdata merge /path/to/profile -o default.profdata
```

**二次编译（使用 Profile 数据）：**

将 `default.profdata` 拷贝到 torch_npu 目录下：

```bash
cp default.profdata torch_npu/
cd torch_npu
git clean -dfx
bash ci/build.sh --python=3.8 --enable_lto --enable_pgo=2
```

二次编译后的 whl 包为正式使用的高性能包。

### 7.5 注意事项

- PyTorch 和 torch_npu 的 Profile 数据**可以使用相同路径**，合并后的 profdata 编译器会自动识别。
- 如运行时报未定义符号（含 `basic_string` 等字样），检查 PyTorch 和 torch_npu 的 `compile_commands.json` 中 `_GLIBCXX_USE_CXX11_ABI` 是否一致。不一致时设置 `export _GLIBCXX_USE_CXX11_ABI=0` 后重编 PyTorch。
- 如运行时报 `libomp.so` 找不到，需确保毕昇编译器的 `LD_LIBRARY_PATH` 已配置。
- 详细说明见[编译优化-torch_npu 文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0065.html)。

---

## 8. 最终效果验证

完成所有调优（含可选的编译优化）后，再次采集性能数据并与基线对比。

验证方式同第 4 节，重点关注：
- 编译优化后的吞吐量提升幅度
- 确认功能正确性未受影响（建议跑一次完整验证）
- 如开启了 PGO，确认 `OMP_PROC_BIND=false` 已设置

---

## 快速参考

| 优化项 | 环境变量 / 方式 | 适用场景 | 风险 |
|--------|----------------|----------|------|
| 流水优化 | `TASK_QUEUE_ENABLE=2` | host-bound 网络 | 内存峰值上升 |
| 粗粒度绑核 | `CPU_AFFINITY_CONF=1` | CPU 瓶颈模型 | 需确认 NUMA 拓扑；vLLM 等推理框架可能负优化 |
| 细粒度绑核 | `CPU_AFFINITY_CONF=2` | CPU 瓶颈 + 核间切换 | 同上 |
| tcmalloc | `LD_PRELOAD=...libtcmalloc.so` | 频繁内存分配 | 需安装 gperftools |
| Python 编译优化 | 毕昇编译器 + `--with-lto --enable-optimizations` | 所有场景 | 需从源码重编 Python |
| PyTorch 编译优化 | 毕昇编译器 + LTO + PGO | Torch 模型 | 需从源码重编，耗时长 |
| torch_npu 编译优化 | 毕昇编译器 + LTO + PGO | Torch 模型 | 依赖重编后的 PyTorch |

## 参考资料

- [流水优化 - 昇腾官方文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0058.html)
- [绑核优化 - 昇腾官方文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0059.html)
- [高性能内存库替换 - 昇腾官方文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0067.html)
- [编译优化-Python - 昇腾官方文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0063.html)
- [编译优化-PyTorch - 昇腾官方文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0064.html)
- [编译优化-torch_npu - 昇腾官方文档](https://www.hiascend.com/document/detail/zh/Pytorch/600/ptmoddevg/trainingmigrguide/performance_tuning_0065.html)
