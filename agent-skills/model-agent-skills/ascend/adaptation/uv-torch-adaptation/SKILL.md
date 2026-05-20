---
name: uv-torch-adaptation
description: Multi-hardware adaptation for PyTorch (Ascend NPU & NVIDIA CUDA) using uv. Use when configuring or troubleshooting pyproject.toml and env for cross-platform GPU/NPU. Short triggers: "uv适配", "torch适配", "按适配清单执行", "uv 昇腾+CUDA 适配", "昇腾NPU配置", "CUDA配置", "记录适配问题", "更新适配规则".
license: Complete terms in LICENSE.txt
---

# uv + Torch Dual-Hardware Adaptation

This skill provides procedural knowledge for configuring `uv` to handle PyTorch on both NVIDIA GPUs and Ascend NPUs using a single `pyproject.toml`.

## 简短触发与执行

**一句话触发示例**（任选其一即可让模型执行完整适配流程）：

- 「按 uv-torch 双硬件适配做一遍」
- 「uv 昇腾+CUDA 适配」
- 「按适配清单执行」

**精简执行清单**（模型按此顺序执行即可完成迁移）：

1. 检查/安装 uv，确认 `pyproject.toml` 存在。
2. 配置 `[tool.uv]`：index、sources、conflicts（参考 `templates/pyproject_template.toml`）。
3. 按当前硬件执行：昇腾 → `source set_env.sh` 后 `uv sync --extra ascend`；CUDA → `uv sync --extra cuda`。
4. 代码中按「5. Python Implementation」加入 `torch_npu` 与 `get_device()`。
5. 可选：在项目根目录运行本 skill 自带的 `scripts/adapt_sync.sh ascend` 或 `scripts/adapt_sync.sh cuda`，做一次带关键节点日志的同步验证（脚本位于 `.cursor/skills/uv-torch-adaptation/scripts/`）。

## 关键节点与日志

适配/迁移过程中建议在以下节点输出简短日志，便于确认当前进度（脚本或人工执行均可沿用）：

| 节点 | 建议输出（或等价中文） |
|------|------------------------|
| 开始 | `[adapt] 开始 uv-torch 双硬件适配` |
| 环境检查 | `[adapt] 检查 uv 与 pyproject.toml` |
| 配置就绪 | `[adapt] pyproject.toml 已配置 index/sources` |
| 加载昇腾环境 | `[adapt] 加载 Ascend set_env.sh`（仅昇腾） |
| 同步依赖前 | `[adapt] 正在同步 --extra ascend|cuda` |
| 同步完成 | `[adapt] 同步完成，可选用 npu:0 / cuda:0` |
| 代码检查 | `[adapt] 已加入 torch_npu 与 get_device()` |
| 结束 | `[adapt] 适配流程结束` |

出错时建议输出：`[adapt] 失败: <步骤名> - <简短原因>`。

## 1. Initial Setup & Tools

### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Automation (~/.bashrc or ~/.zshrc)

Add the following to your shell config for automatic Ascend environment loading:

```bash
export ASCEND_HOME=/usr/local/Ascend/ascend-toolkit/latest
[ -f "$ASCEND_HOME/set_env.sh" ] && source "$ASCEND_HOME/set_env.sh" > /dev/null 2>&1
```

## 2. Project Configuration (pyproject.toml)

Use `tool.uv.index` and `tool.uv.sources` to isolate hardware-specific dependencies. Avoid using exact version constraints (`==`) in `optional-dependencies` to allow for better dependency resolution, prefer `>=` instead.

### Implementation Guide

1. **Define Indices**: Set up separate indices for CUDA and Ascend.
2. **Map Sources**: Use conditional sources based on extras.
3. **Handle Conflicts**: Prevent simultaneous installation of CUDA and Ascend extras.

For a complete boilerplate, see `templates/pyproject_template.toml`.

## 3. Hardware Synchronization

Synchronize the project environment based on the available hardware.

### NVIDIA CUDA

```bash
uv sync --extra cuda
```

### Ascend NPU

Requires driver environment loading before synchronization (see Step 1).

```bash
# Load toolkit environment if not in shell config
source /usr/local/Ascend/ascend-toolkit/latest/set_env.sh

# Sync with ascend extra
uv sync --extra ascend
```

## 4. Python Implementation

Always use `torch_npu` in Ascend environments to register NPU members.

```python
import torch
try:
    import torch_npu
except ImportError:
    pass

def get_device():
    if hasattr(torch, "npu") and torch.npu.is_available():
        torch.npu.set_device("npu:0")
        return "npu:0"
    return "cuda:0" if torch.cuda.is_available() else "cpu"
```

## 5. Static Analysis & IDE

Exclude history and specify venv for optimal IDE performance.

```toml
[tool.ruff]
exclude = [".history"]

[tool.pyright]
exclude = [".history"]

```

## Troubleshooting

- **`torch-npu` not found**: Verify `ascend-repo` index is marked `explicit = true`.
- **NPU member error**: Ensure `import torch_npu` is called before accessing `torch.npu`.
- **Memory not releasing**: Call `torch.npu.empty_cache()` or `torch.cuda.empty_cache()`.

## Self-Update Policy

Update this skill when:

- New hardware-specific mirror URLs are discovered.
- Dependency conflict resolution patterns are improved.
- New environment variables are required for Ascend toolkit.

**Note**: Integrate improvements directly into the relevant sections above. Use the Change Log below for event tracking only.

### Change Log
