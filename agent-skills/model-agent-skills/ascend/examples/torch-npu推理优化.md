# 通用昇腾优化 Skill

将优化工作分成三层：先判断瓶颈类型，再选择代码层、运行时层或 OS/内存层手段。只处理 **PyTorch 推理阶段** 的性能优化，不覆盖训练调优、C++/CANN 算子开发或编译器改造。

优先保留原始实现的 fallback。瓶颈不明确时，不要猜，改用同仓库中的 `ascend-profiling` skill 先确认是 compute-bound、host-bound 还是 memory/allocator-bound。

## 与 ascend-affinity-operator 的协同

保持与同仓库 [../ascend-affinity-operator/SKILL.md](../ascend-affinity-operator/SKILL.md) 的分工清晰：

- 用当前 skill 处理通用仓库里的瓶颈判断、`torch_npu` API 选择、运行时/OS 调优和最小必要代码修改。
- 当仓库已经有 `model_files/`、`accuracy_run.py`、`accuracy_run_perf.py`、`check_accuracy_run_perf.py`、`adaptation_status` / `benchmark_status` / `optimization_status` 之类的项目化流程时，同时读取 `ascend-affinity-operator` skill，复用它的目录约定、单卡选择、验收脚本和状态流转规则。
- 当两个 skill 都适用时，先用当前 skill 确定瓶颈类型和优化方向，再按 `ascend-affinity-operator` 的项目流程落地修改、跑 baseline/perf、做精度验收。
- 当仓库没有这些专项脚本或固定目录结构时，只使用当前 skill，不要强行套用 `ascend-affinity-operator` 的工程约束。

## 快速工作流

1. 判断瓶颈类型。
   - 算子耗时高、NPU 忙、热点集中在 attention、norm、FFN 等路径：优先做代码层优化。
   - 时间线存在明显 Free Time、Dequeue 阻塞、CPU 调度开销、NPU 等待 host：优先做运行时层优化。
   - 内存峰值高、malloc/free 频繁、碎片或锁竞争明显：优先做 OS/内存层优化。
   - 不清楚瓶颈：先做 profiling，再决定。
2. 选择最小必要改动。
   - 先改热点路径，不要全模型盲目替换。
   - 只有满足 dtype、shape、layout 约束时，才替换为 `torch_npu` 亲和 API。
   - 运行时和环境变量优化必须按瓶颈启用，不能当成默认模板到处套用。
3. 为每个优化保留验证口径。
   - 同输入、同精度、同设备、同 batch、同预热策略、同计时口径做 baseline/perf 对比。
   - 先确认精度可接受，再确认总耗时下降。
   - 如果仓库自带 `accuracy_run.py`、`accuracy_run_perf.py` 或 `check_accuracy_run_perf.py`，优先复用 `ascend-affinity-operator` 中的专项验证流程，不要另造一套通用脚本。

## 通用代码层优化

统一先写设备探测与 fallback 分支：

```python
import torch

try:
    import torch_npu
    _HAS_TORCH_NPU = True
except ImportError:
    torch_npu = None
    _HAS_TORCH_NPU = False


def _is_npu_tensor(x: torch.Tensor) -> bool:
    return (
        _HAS_TORCH_NPU
        and hasattr(torch, "npu")
        and torch.npu.is_available()
        and str(x.device).startswith("npu")
    )
```

优先考虑这些模式：

- Norm 路径：手写 RMSNorm 或 residual-add + LayerNorm，可评估 `npu_rms_norm`、`npu_add_layer_norm`。
- RoPE 路径：手写旋转位置编码，可评估 `npu_rotary_mul`。
- Attention 路径：手写 `QK^T -> mask -> softmax -> V`，可评估 `npu_fusion_attention` 或 `npu_prompt_flash_attention`。
- FFN / 门控路径：SwiGLU、GeGLU、两层 MLP，可评估 `npu_swiglu`、`npu_gelu_mul`、`npu_ffn`。
- Layout 路径：`permute`、`transpose` 后补 `contiguous()`，避免非连续张量造成额外拷贝或 fallback。
- Host-device sync：避免循环中频繁 `.item()`、`.cpu()`、同步计时；确需计时时再显式同步。

详细 API 约束、mask 语义和 dtype 限制，读取 [reference.md](reference.md)。

## 通用运行时优化

只在 profiling、时间线或 host 侧指标明确显示下发瓶颈时启用这些手段。

### 1. 一级流水优化

在 host-bound 严重、NPU 等待 host、Free Time 明显时，优先尝试：

```bash
export TASK_QUEUE_ENABLE=2
python infer.py
```

遵循这些规则：

- `TASK_QUEUE_ENABLE=2` 主要用于严重 host-bound 场景，不是默认配置。
- 如果 `ASCEND_LAUNCH_BLOCKING=1`，则 task queue 关闭，此优化视为不生效。
- 开启后可能因内存并发导致峰值内存上升，需要重新观察 OOM 风险。

### 2. Stream 级 TaskQueue 并行下发

只在 **多线程多流** 且 `Dequeue` 阻塞明显时推荐：

```bash
export TASK_QUEUE_ENABLE=2
export PER_STREAM_QUEUE=1
python infer.py
```

遵循这些规则：

- `PER_STREAM_QUEUE=1` 依赖 `TASK_QUEUE_ENABLE=1` 或 `2`。
- 只适用于多线程多流下发场景，其余场景通常不推荐。
- 开启后会有更多二级流水线程，可能带来额外资源抢占。
- 如果多流之间存在 event 交互，一级流水可能出现额外耗时。
- 不要把 `PER_STREAM_QUEUE=1` 与细粒度绑核作为默认组合；官方文档说明该特性不支持细粒度绑核。

### 3. CPU 绑核

在 CPU 调度开销高、线程漂移明显、跨 NUMA 干扰严重时再启用：

```bash
export CPU_AFFINITY_CONF=2
python infer.py
```

遵循这些规则：

- 默认优先考虑细粒度绑核 `CPU_AFFINITY_CONF=2`，因为它更适合热点线程隔离。
- 在 Docker、虚拟机、NUMA 映射不清晰或容器 cpuset 受限时，先检查拓扑，再决定是否启用。
- 需要自定义绑核区间时，优先使用粗粒度模式 `CPU_AFFINITY_CONF=1,...`；自定义区间不适用于细粒度模式。
- 如果代码会创建自定义线程，在线程拉起前后用 `torch_npu.utils.set_thread_affinity` 与 `torch_npu.utils.reset_thread_affinity` 管理亲和性，避免子线程继承错误配置。

## 通用 OS / 内存优化

### 1. 高性能内存库替换

只在 Python/host 侧 malloc/free 频繁、锁竞争明显或内存分配器成为瓶颈时尝试 `tcmalloc`：

```bash
LD_PRELOAD=/path/to/libtcmalloc.so python infer.py
```

遵循这些规则：

- 这是可选系统级优化，不是所有推理任务的默认配置。
- 优先使用单命令 `LD_PRELOAD=... python infer.py` 做局部验证，再决定是否导出到整个终端会话。
- 替换后用 `ldd "$(which python)"` 或等效方式确认动态库已生效。

### 2. PyTorch NPU 内存配置

在碎片化或大块分配失败时，尝试：

```bash
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:512
python infer.py
```

将其视为调参项而不是固定模板，结合显存峰值、碎片和分配失败日志调整。

### 3. 多流内存复用

只有在真实的多流场景、跨流依赖导致内存回收不及时、峰值显存偏高时，再考虑：

```bash
export MULTI_STREAM_MEMORY_REUSE=1
python infer.py
```

不要把它当作通用推理默认开关。它更适合存在跨流内存复用需求的场景。

## 验证规则

始终用同口径比较 baseline 与 perf：

```bash
# baseline
python infer.py

# optimized
TASK_QUEUE_ENABLE=2 python infer.py
```

验证时固定这些条件：

- 同一份输入数据与相同随机种子
- 同 dtype、同 batch、同序列长度或图像分辨率
- 同一张设备卡、同一套环境变量基线
- 同样的 warmup 次数与计时窗口

对代码层替换，至少检查：

- 数值精度是否在可接受范围内
- 输出 shape、dtype、mask 语义是否一致
- 总耗时是否下降，而不是只看单算子

## 使用说明
将[链接](https://gitcode.com/MoFixGo/optimization-agent/tree/main/ascend-optimization)中的skills，具体内容如上，加载到code agent工具对应目录下，并输入提示词：对xxx模型的进行性能优化，环境路径xxxx，大模型会自动对该模型进行优化

## 读取参考

需要以下信息时，读取 [reference.md](reference.md)：

- `torch_npu` 常用融合算子的适用模式和限制
- `TASK_QUEUE_ENABLE`、`PER_STREAM_QUEUE`、`CPU_AFFINITY_CONF`、`LD_PRELOAD` 的启用条件与风险
- 验证 checklist 与通用命令模板

需要以下信息时，同时读取 [../ascend-affinity-operator/SKILL.md](../ascend-affinity-operator/SKILL.md) 与 [../ascend-affinity-operator/reference.md](../ascend-affinity-operator/reference.md)：

- 仓库已具备 `model_files/`、`accuracy_run.py`、`accuracy_run_perf.py`、`check_accuracy_run_perf.py` 等专项目录或脚本
- 需要沿用单卡挑选、`--use-pretrained` 验收、baseline/perf 产物命名或状态流转规则
- 需要把通用优化策略映射到项目化落地流程，而不是只给出通用改法
