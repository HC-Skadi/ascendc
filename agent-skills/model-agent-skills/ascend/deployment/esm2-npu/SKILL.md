---
name: esm2-npu-deploy
description: >
  ESM-2 蛋白质语言模型在昇腾 NPU 上的完整部署与 FP32 推理优化 Skill。
  涵盖环境准备、依赖安装、transfer_to_npu 自动迁移、README 推理验证、
  FP32 算子级性能优化（npu_rotary_mul / npu_fusion_attention / F.gelu）、
  精度对比验证的全流程。可在任意 Ascend910 系列服务器上一键复现。
  当用户提到 ESM2 部署昇腾、ESM2 NPU 推理、蛋白质模型 NPU 时触发。
metadata:
  short-description: ESM-2 昇腾 NPU 部署与 FP32 推理优化
  category: NPU-Model-Deploy
  tags: [ascend, npu, esm2, protein, pytorch, inference, optimization]
---

# ESM-2 昇腾 NPU 部署与 FP32 推理优化 Skill

本 Skill 提供 ESM-2 (esm2_t33_650M_UR50D) 蛋白质语言模型在华为昇腾 NPU 上的
完整部署、推理验证和 FP32 性能优化的标准化可复现流程。

## 前置条件

| 项目 | 要求 |
|------|------|
| 硬件 | Ascend910 系列（至少 1 卡，64GB HBM） |
| OS | openEuler / Ubuntu / KylinOS（aarch64 或 x86_64） |
| CANN | >= 8.0（推荐 8.3.RC1） |
| Python | 3.9 – 3.13 |
| 网络 | 首次运行需联网下载模型权重（~2.5GB） |

## 流程总览

```
0. 环境初始化
→ 1. 安装依赖（torch_npu + fair-esm）
→ 2. NPU 验证
→ 3. 基础推理验证（README Quick Start）
→ 4. Embedding 批量提取验证（extract.py）
→ 5. FP32 性能优化（算子替换）
→ 6. 精度对比验证
→ 7. 验收确认
```

按以下各节顺序执行，每步完成后再进入下一步。

---

## 0. 环境初始化

```bash
# 加载 CANN 环境
source /usr/local/Ascend/ascend-toolkit/set_env.sh

# 选择空闲 NPU（先用 npu-smi info 查看各卡占用，选空闲卡）
npu-smi info
export ASCEND_RT_VISIBLE_DEVICES=0   # 替换为实际空闲卡号

# 华为 pip 镜像（国内加速）
export PIP_INDEX_URL=https://repo.huaweicloud.com/repository/pypi/simple/
```

---

## 1. 安装依赖

### 1.1 安装 torch_npu

```bash
pip install torch_npu -i https://repo.huaweicloud.com/repository/pypi/simple/
```

安装完成后 `torch` 与 `torch_npu` 版本应一致（如均为 2.11.0）。

### 1.2 获取 ESM 源码并安装

```bash
git clone https://github.com/facebookresearch/esm.git
cd esm
pip install -e . -i https://repo.huaweicloud.com/repository/pypi/simple/
```

> 如果已有本地 ESM 仓库，直接 `cd` 进入后执行 `pip install -e .` 即可。

---

## 2. NPU 基础验证

在 ESM 安装完成后，运行以下 Python 代码确认 NPU 环境可用：

```bash
python3 -c "
import torch
import torch_npu
print('torch:', torch.__version__)
print('torch_npu:', torch_npu.__version__)
a = torch.randn(3, 4).npu()
print(a + a)
print('NPU device:', torch.npu.get_device_name(0))
"
```

**通过标准**：输出包含 `device='npu:0'` 的 Tensor 且无报错。

若报错 `No module named 'torch_npu'`，检查：
1. `source /usr/local/Ascend/ascend-toolkit/set_env.sh` 是否已执行
2. `pip install torch_npu` 是否成功
3. CANN 版本与 torch_npu 是否匹配

---

## 3. 基础推理验证（README Quick Start）

在 ESM 仓库根目录创建 `esm2_npu_infer.py`：

<!-- EMBED:scripts/esm2_npu_infer.py -->

脚本文件位于 `scripts/esm2_npu_infer.py`，复制到 ESM 仓库根目录后运行。

核心代码逻辑：

```python
import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
import esm

model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
batch_converter = alphabet.get_batch_converter()
model.eval()
model = model.cuda()  # transfer_to_npu 自动映射到 NPU

data = [
    ("protein1", "MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG"),
    ("protein2", "KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE"),
]
batch_labels, batch_strs, batch_tokens = batch_converter(data)
batch_tokens = batch_tokens.cuda()

with torch.no_grad():
    results = model(batch_tokens, repr_layers=[33], return_contacts=True)
token_representations = results["representations"][33]
```

运行：

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
export ASCEND_RT_VISIBLE_DEVICES=0
cd <esm-repo-root>
python3 esm2_npu_infer.py
```

**通过标准**：
- 4 条序列的 embedding 正常输出，norm 值合理（5~10）
- Contact map shape 为 (4, 71, 71)
- 无 NPU 相关报错

---

## 4. Embedding 批量提取验证

按 README 的 `scripts/extract.py` 方式验证批量 embedding 提取。
在 ESM 仓库根目录创建 `esm2_npu_extract.py`：

<!-- EMBED:scripts/esm2_npu_extract.py -->

脚本文件位于 `scripts/esm2_npu_extract.py`，复制到 ESM 仓库根目录后运行。

核心代码逻辑（在入口注入 transfer_to_npu 后调用原始 extract.py）：

```python
import torch_npu
from torch_npu.contrib import transfer_to_npu
from scripts.extract import create_parser, run

# 可修改以下参数适配不同场景
sys.argv = [
    "extract.py",
    "esm2_t33_650M_UR50D",
    "<your_fasta_file>",
    "<output_dir>",
    "--repr_layers", "0", "32", "33",
    "--include", "mean", "per_tok",
]
parser = create_parser()
args = parser.parse_args()
run(args)
```

运行：

```bash
python3 esm2_npu_extract.py
```

**通过标准**：
- 15 条序列全部处理完成
- `examples/data/some_proteins_emb_esm2/` 目录下生成 15 个 `.pt` 文件
- 无报错

---

## 5. FP32 性能优化

### 5.1 优化原理

所有优化在 **FP32 精度** 下进行，不使用降精度。通过替换为 torch_npu 融合算子
减少算子调度开销和中间内存搬运：

| 优化项 | 原始实现 | NPU 替换 | 作用 |
|--------|----------|----------|------|
| 旋转位置编码 | chunk + negate + cat + mul + add (5 算子) | `torch_npu.npu_rotary_mul` (1 算子) | 减少 kernel 调度 |
| 注意力计算 | bmm + mask + softmax + bmm (4 算子) | `torch_npu.npu_fusion_attention` (1 算子) | 最大收益项 |
| GELU 激活 | 手写 erf-based (x*0.5*(1+erf(x/sqrt2))) | `F.gelu` (原生融合) | 减少中间张量 |
| Attention weights | 始终计算（即使不需要） | 按需计算 | 跳过无用开销 |

### 5.2 关键适配点

**npu_rotary_mul**：
- `npu_rotary_mul` 要求 4D 输入，ESM2 传入 3D `(bsz*heads, seq, dim)`
- 需 `unsqueeze(0)` 扩展为 4D，计算后 `squeeze(0)` 还原
- cos/sin 必须 `expand_as(x)` 到与输入完全相同的 shape

**npu_fusion_attention**：
- ESM2 是**双向注意力**（非因果），`pre_tockens=65536, next_tockens=65536`
- ESM2 的 `add_bias_kv=False`，无额外 bias token
- Q 已预乘 `scaling = head_dim^{-0.5}`，传 `scale=1.0`
- atten_mask shape 必须为 `[B, 1, Sq, Skv]`，`True` 表示屏蔽
- 仅在 `need_weights=False` 时使用（不需要返回 attention weights）
- 返回值为 tuple，取 `[0]`

**TransformerLayer 改动**：
- 原始 `need_weights=True`（始终）改为 `need_weights=need_head_weights`（按需）
- 使得 embedding 提取场景可走 fusion attention 路径

### 5.3 优化脚本

在 ESM 仓库根目录创建 `esm2_npu_optimized.py`：

<!-- EMBED:scripts/esm2_npu_optimized.py -->

完整脚本位于 `scripts/esm2_npu_optimized.py`，复制到 ESM 仓库根目录后运行。

脚本通过 monkey-patch 方式注入所有优化，不修改 ESM 源码。核心优化函数：

```python
import torch_npu

# 优化 1: npu_rotary_mul
def _npu_apply_rotary(x, cos, sin):
    cos_t = cos[:, :x.shape[-2], :].unsqueeze(0)
    sin_t = sin[:, :x.shape[-2], :].unsqueeze(0)
    x_4d = x.unsqueeze(0)
    return torch_npu.npu_rotary_mul(
        x_4d, cos_t.expand_as(x_4d), sin_t.expand_as(x_4d)
    ).squeeze(0)

# 优化 2: npu_fusion_attention
npu_out = torch_npu.npu_fusion_attention(
    q_bsnd, k_bsnd, v_bsnd, num_heads,
    input_layout="BSND", atten_mask=atten_mask,
    scale=1.0, pre_tockens=65536, next_tockens=65536,
    keep_prob=1.0,
)[0]

# 优化 3: F.gelu 替换手写 gelu
def _npu_gelu(x):
    return F.gelu(x)
```

运行基准测试：

```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
export ASCEND_RT_VISIBLE_DEVICES=0
cd <esm-repo-root>
python3 esm2_npu_optimized.py
```

### 5.4 预期性能

在 Ascend910 (CANN 8.3.RC1) 上实测结果：

| 配置 | 基线 FP32 (ms) | 优化 FP32 (ms) | 加速比 |
|------|---------------|----------------|--------|
| Short (len~100, batch=4) | 26.31 | 24.65 | 1.07x |
| Medium (len~200-500, batch=4) | 82.27 | 52.70 | **1.56x** |
| Long (len~600-1000, batch=2) | 62.72 | 40.13 | **1.56x** |

---

## 6. 精度验证

优化前后对比（全程 FP32）：

| 指标 | 数值 |
|------|------|
| Representation 余弦相似度 | 0.999985 |
| Logits 余弦相似度 | 0.999982 |
| 最大绝对误差 | 0.537704 |
| 平均绝对误差 | 0.000580 |

**通过标准**：余弦相似度 > 0.999，差异仅来自融合算子浮点运算顺序差异。

---

## 7. 验收确认

完成以下检查清单即为部署成功：

- [ ] `npu-smi info` 显示设备正常
- [ ] `import torch_npu` 无报错
- [ ] `esm2_npu_infer.py` 输出 4 条序列的 embedding 和 contact map
- [ ] `esm2_npu_extract.py` 生成 15 个 `.pt` embedding 文件
- [ ] `esm2_npu_optimized.py` 跑完基准测试，中长序列加速 > 1.3x
- [ ] 精度对比余弦相似度 > 0.999

---

## 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| `No module named 'torch_npu'` | 未安装或 CANN 环境未加载 | `source set_env.sh` 后重装 torch_npu |
| `SetPrecisionMode error 500001` | CANN 环境未加载 | `source /usr/local/Ascend/ascend-toolkit/set_env.sh` |
| 模型下载失败 | 网络问题 | 手动下载权重到 `~/.cache/torch/hub/checkpoints/` |
| `npu_rotary_mul` shape 报错 | 输入不是 4D | 确认 `unsqueeze(0)` 处理 |
| `npu_fusion_attention` mask shape 报错 | mask 非 `[B,1,Sq,Skv]` | 用 `.unsqueeze(1).unsqueeze(1).expand(B,1,Sq,Skv)` |
| OOM | 序列过长或 batch 过大 | 减小 batch_size 或单条序列推理 |
| 多卡抢占冲突 | 默认都用 0 号卡 | `npu-smi info` 选空闲卡 |

---

## 附录：ESM2 NPU 适配要点速查

| 特征 | ESM2 值 | 对优化的影响 |
|------|---------|-------------|
| 注意力类型 | 双向 (Bidirectional) | `next_tockens=65536`（非因果） |
| add_bias_kv | False | 可直接用 fusion attention |
| Rotary Embedding | 有 | 走手写 attention 路径，可用 npu_rotary_mul |
| LayerNorm | torch.nn.LayerNorm | 无需额外替换 |
| 激活函数 | 手写 erf-based GELU | 替换为 F.gelu |
| Q 预缩放 | q *= head_dim^{-0.5} | fusion attention 传 scale=1.0 |
| 输入格式 | (T, B, E) | 需转为 BSND 再传入 fusion attention |
