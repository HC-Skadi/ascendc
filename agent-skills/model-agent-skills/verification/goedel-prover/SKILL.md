---
name: ai-for-science-goedel-prover
description: Goedel-Prover 昇腾 NPU 迁移 Skill，适用于将基于 vLLM 的 Lean 4 自动定理证明模型从 CUDA 迁移到华为 Ascend 910 系列，覆盖环境搭建、vLLM-Ascend 安装、Lean 4 构建和推理验证全流程。
keywords:
    - ai-for-science
    - goedel-prover
    - vllm
    - lean4
    - theorem-proving
    - ascend
---

# Goedel-Prover 昇腾 NPU 迁移 Skill

## 前置条件

| 项目 | 要求 |
|------|------|
| 硬件 | Ascend910 系列（至少 2 卡用于 tensor_parallel） |
| OS | openEuler / Ubuntu（aarch64） |
| CANN | ≥ 8.2.RC1 |
| NNAL (ATB) | 与 CANN 版本匹配（如 8.2.RC1） |
| Python | 3.10 |
| conda | 已安装 |

## 迁移流程

### 1. 环境初始化

**检查 NNAL/ATB 是否已安装：**

```bash
find /usr/local/Ascend /home/Ascend -name 'libnnal*' -o -name 'libatb*' 2>/dev/null | head -5
find /usr/local/Ascend /home/Ascend -path '*/nnal/atb/set_env.sh' 2>/dev/null
```

若上述命令无输出，说明 NNAL 未安装。NNAL 是 vllm-ascend 推理的必要依赖（rotary embedding 等算子依赖 ATB 加速库），**必须手动下载安装**：

1. 前往昇腾社区下载页：https://www.hiascend.com/developer/download/community/result?module=cann
2. 选择与当前 CANN 版本匹配的 NNAL 包（如 CANN 8.2.RC1 对应 `Ascend-cann-nnal_8.2.RC1_linux-aarch64.run`）
3. 上传到服务器后执行安装：
   ```bash
   chmod +x Ascend-cann-nnal_8.2.RC1_linux-aarch64.run
   ./Ascend-cann-nnal_8.2.RC1_linux-aarch64.run --install
   ```

> **NNAL 与 CANN 版本必须匹配**：如果 NNAL 版本与当前 CANN 版本不一致（如 CANN 8.3.RC1 搭配了 NNAL 8.5.0），
> 运行时会报 `undefined symbol` 或 `Please check the version of the NNAL package` 错误。
> 此时需要先确认 CANN 版本（`cat /usr/local/Ascend/ascend-toolkit/latest/version.cfg`），
> 然后前往昇腾社区下载对应版本的 NNAL 包重新安装。

**定位 NNAL set_env.sh 路径：**

NNAL 的安装路径因环境而异（可能在 `/usr/local/Ascend/nnal/`、`/home/Ascend/nnal/`
或带版本号的子目录如 `/home/Ascend/8.5.0/nnal/`），不要硬编码路径，应先动态定位：

```bash
NNAL_ATB_ENV=$(find /usr/local/Ascend /home/Ascend -path '*/nnal/atb/set_env.sh' 2>/dev/null | head -1)
NNAL_ASDSIP_ENV=$(find /usr/local/Ascend /home/Ascend -path '*/nnal/asdsip/set_env.sh' 2>/dev/null | head -1)
echo "ATB set_env: $NNAL_ATB_ENV"
echo "ASDSIP set_env: $NNAL_ASDSIP_ENV"
```

**初始化环境变量：**

> **注意 CXX ABI 匹配**：`set_env.sh` 会自动检测当前 Python 环境中 torch 的 CXX11_ABI 值
> 来选择 `cxx_abi_0` 或 `cxx_abi_1` 目录。torch 2.5.1 pip 包默认使用 ABI=0，因此需要确保
> **先激活 conda 环境再 source set_env.sh**，否则会误判 ABI 导致 `undefined symbol` 错误。
> 如果仍然出错，可显式指定 `--cxx_abi=0`。

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source $NNAL_ATB_ENV          # 如 ABI 检测异常，改用: source $NNAL_ATB_ENV --cxx_abi=0
source $NNAL_ASDSIP_ENV
export PIP_INDEX_URL=https://repo.huaweicloud.com/repository/pypi/simple/
```

### 2. 克隆仓库

```bash
git clone --recurse-submodules https://github.com/Goedel-LM/Goedel-Prover.git
cd Goedel-Prover
```

若子模块克隆失败，可手动初始化：
```bash
git submodule update --init --depth 1
```

### 3. 创建 conda 环境并安装依赖

```bash
conda create -n goedel-prover python=3.10 -y
conda activate goedel-prover

pip install torch==2.5.1 torch_npu==2.5.1.post1 numpy==1.26.4 \
    -i https://repo.huaweicloud.com/repository/pypi/simple/

pip install pytz==2022.1 termcolor==2.4.0 easydict==1.13 tabulate==0.9.0 \
    'transformers>=4.51.1,<4.53.0' 'accelerate==0.33.0' pandas==1.4.3 \
    decorator attrs psutil absl-py cloudpickle ml-dtypes scipy tornado \
    'setuptools<71' \
    -i https://repo.huaweicloud.com/repository/pypi/simple/
```

> **setuptools 版本说明**：vllm-ascend 依赖的 `torchair`（打包在 torch_npu 内部）需要
> `pkg_resources` 模块，而 `setuptools >= 71` 已移除该模块，因此必须限制 `setuptools < 71`。

### 4. 安装 vLLM + vLLM-Ascend

```bash
git clone --depth 1 --branch v0.9.1 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install -v -e .
cd ..

pip install vllm-ascend==0.9.1rc2 -i https://repo.huaweicloud.com/repository/pypi/simple/
```

安装后确认 transformers 版本兼容：
```bash
pip install 'transformers>=4.51.1,<4.53.0' -i https://repo.huaweicloud.com/repository/pypi/simple/
```

### 5. 代码适配

**5.1 修改 `eval/step1_inference.py`**

在文件顶部（所有 import 之前）添加：
```python
import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
```

**5.2 修改 `eval/eval.sh`**

在脚本开头添加环境初始化（NNAL 路径需替换为实际路径）：
```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source <NNAL_ATB_SET_ENV_PATH> --cxx_abi=0
source <NNAL_ASDSIP_SET_ENV_PATH>
export PYTHONPATH=$(python -c "import torch_npu; import os; print(os.path.join(os.path.dirname(torch_npu.__file__), 'dynamo'))"):$PYTHONPATH
```

> **torchair PYTHONPATH 说明**：vllm-ascend 依赖 `torchair`，它打包在
> `torch_npu/dynamo/torchair/` 目录下，但不在默认 Python 搜索路径中。
> 必须将 `torch_npu/dynamo` 加入 `PYTHONPATH`，否则运行时会报
> `ModuleNotFoundError: No module named 'torchair'`。

**5.3 修改 `requirements.txt`**

移除以下 CUDA 特有依赖：
- `flash-attn==2.6.3`
- `vllm==0.6.3.post1`
- `vllm_nccl_cu12==2.18.1.0.4.0`

更新 torch 相关版本：
- `torch==2.5.1`
- 新增 `torch_npu==2.5.1.post1`
- `transformers>=4.51.1,<4.53.0`

### 6. 安装 Lean 4

下载 elan（Lean 版本管理器）：
```bash
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none
```

手动安装 Lean 4 toolchain（如网络受限，可手动下载 `lean-4.9.0-rc1-linux_aarch64.tar.zst`）：
```bash
mkdir -p ~/.elan/toolchains/leanprover--lean4---v4.9.0-rc1
cd ~/.elan/toolchains/leanprover--lean4---v4.9.0-rc1
tar --zstd -xf /path/to/lean-4.9.0-rc1-linux_aarch64.tar.zst --strip-components=1
```

添加到 PATH：
```bash
export PATH=$HOME/.elan/toolchains/leanprover--lean4---v4.9.0-rc1/bin:$HOME/.elan/bin:$PATH
```

### 7. 构建 mathlib4

```bash
cd Goedel-Prover/mathlib4
lake build
cd ..
```

`proofwidgets:optRelease` 构建失败不影响证明验证，可忽略。

### 8. 验证

验证 Lean 4 环境：
```bash
python prover/lean/verifier.py
```

使用单题快速验证（NPU 卡号按需调整）：
```bash
export ASCEND_RT_VISIBLE_DEVICES=2,3
sh eval/eval.sh -i datasets/mathd_algebra_338.jsonl -s test \
    -m /path/to/model -o results/mathd_algebra_338/Godel-Prover-SFT \
    -n 32 -g 2 -c 32
```

验证通过标准：
- `results/mathd_algebra_338/Godel-Prover-SFT/compilation_summarize.json` 中 `accuracy` 为 `100.00`
- 三步（推理 → 编译 → 汇总）均正常退出

完整 miniF2F 评测：
```bash
sh eval/eval.sh -i datasets/minif2f.jsonl -s test \
    -m /path/to/model -o results/minif2f/Godel-Prover-SFT \
    -n 32 -g 2 -c 128
```

## 适配要点总结

| 项目 | 原始 | 适配后 |
|------|------|--------|
| torch | 2.4.0 | 2.5.1 |
| vllm | 0.6.3.post1 (CUDA) | 0.9.1+empty + vllm-ascend 0.9.1rc2 |
| flash-attn | 2.6.3 | 移除（vllm-ascend 内置 NPU 注意力） |
| vllm_nccl_cu12 | 2.18.1 | 移除（NPU 使用 HCCL） |
| setuptools | 无限制 | < 71（torchair 依赖 pkg_resources） |
| 设备迁移 | transfer_to_npu 自动映射 cuda→npu | |
| NNAL/ATB | 无 | 必须安装，版本须与 CANN 匹配，注意 CXX ABI 选择 |
| torchair | 无需配置 | 需将 torch_npu/dynamo 加入 PYTHONPATH |

## 配套参考资料

- 版本矩阵、代码改动清单和常见报错排查：[`references/runtime-checklist.md`](references/runtime-checklist.md)
