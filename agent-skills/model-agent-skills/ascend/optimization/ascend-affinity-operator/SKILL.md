---
name: ascend-affinity-operator
description: 华为昇腾 NPU 上 PyTorch 模型的推理阶段 Python 层亲和算子优化。通过替换为 torch_npu 融合算子提升推理速度。触发词：ascend-affinity-operator、Ascend 亲和算子、torch_npu 推理优化、NPU 推理性能、算子替换、model_files 优化。
---

# 昇腾亲和算子优化 Skill

本 skill 指导在华为昇腾 NPU 上对 PyTorch 模型做**推理阶段**的 Python 层性能优化。仅涉及 API 替换与调用方式调整，不含训练、编译、C++ 或 CANN 算子开发。

**与 ascend-adaptation 的关系**：ascend-adaptation 负责「能跑」，本 skill 负责「跑得更快」。

## 常见优化项（示例，非穷举）

优化范围为 **torch 级别 API 替换**，可将 torch 操作替换为 torch_npu 亲和 API。可参考 `refer/torch_npu_list.md`、`refer/torch_npu-contrib_list.md` 扩展。

以下四项在 Qwen-7B (bf16) 实测中取得 **+37.7% 提速**，logits 余弦相似度 > 0.99，PPL 相对差异 < 10%。

### 1. RMSNorm → npu_rms_norm

最简单、收益稳定的替换。直接替换手写 RMSNorm 的 forward。

```python
# 原始实现
def forward(self, x):
    output = self._norm(x.float()).type_as(x)
    return output * self.weight

# NPU 优化
def forward(self, x):
    if _HAS_TORCH_NPU and str(x.device).startswith("npu"):
        return torch_npu.npu_rms_norm(x, self.weight, epsilon=self.eps)[0]
    output = self._norm(x.float()).type_as(x)
    return output * self.weight
```

**注意**：返回值是 tuple，取 `[0]` 获取结果张量。

### 2. SwiGLU → npu_swiglu

将 SiLU + 门控乘法替换为单个融合算子。注意 concat 顺序：`npu_swiglu(x, dim=-1)` 计算 `SiLU(first_half) * second_half`。

```python
# 原始：a1 * silu(a2)
intermediate = a1 * F.silu(a2)

# NPU 优化：concat 顺序 [a2, a1] 使得 SiLU(a2) * a1
gate_up = torch.cat([a2, a1], dim=-1)
intermediate = torch_npu.npu_swiglu(gate_up, dim=-1)
```

**关键**：concat 顺序必须正确。`npu_swiglu` 对前半做 SiLU，乘以后半。如果原始代码是 `a1 * silu(a2)`，需 concat `[a2, a1]`。

### 3. Rotary Position Embedding → npu_rotary_mul

替换手写的旋转位置编码计算。

```python
# 原始实现
def apply_rotary_pos_emb(t, freqs):
    cos, sin = freqs
    rot_dim = cos.shape[-1]
    t_, t_pass_ = t[..., :rot_dim], t[..., rot_dim:]
    t_ = (t_.float() * cos) + (_rotate_half(t_.float()) * sin)
    return torch.cat((t_, t_pass_), dim=-1).type_as(t)

# NPU 优化
def apply_rotary_pos_emb(t, freqs):
    cos, sin = freqs
    if _HAS_TORCH_NPU and str(t.device).startswith("npu"):
        rot_dim = cos.shape[-1]
        t_, t_pass_ = t[..., :rot_dim], t[..., rot_dim:]
        cos = cos.expand_as(t_)
        sin = sin.expand_as(t_)
        output = torch_npu.npu_rotary_mul(t_, cos, sin).type_as(t)
        if t_pass_.shape[-1] > 0:
            return torch.cat((output, t_pass_), dim=-1)
        return output
    # fallback to original
    ...
```

**注意**：
- cos/sin 必须 `expand_as(t_)` 到与输入相同 shape
- 处理 `t_pass_`（超出旋转维度的部分）需要 concat 回来
- `npu_rotary_mul` 内部实现 `x * cos + rotate_half(x) * sin`，其中 `rotate_half` 是 `[-x[D//2:], x[:D//2]]`

### 4. Attention → npu_fusion_attention（最复杂，收益最大）

替换手写的 Q@K^T → mask → softmax → @V 为单个融合算子。

```python
# query/key/value shape: (B, S, H, D) — 即 BSND 格式
scale = 1.0 / math.sqrt(head_dim)

# 构建 causal mask（bool，True = mask out）
seq_len_q = query.shape[1]
seq_len_k = key.shape[1]
causal_mask = torch.triu(
    torch.ones(seq_len_q, seq_len_k, dtype=torch.bool, device=query.device),
    diagonal=seq_len_k - seq_len_q + 1,
)
# 合并 padding mask（如果有）
if attention_mask is not None:
    # attention_mask 是 float 加法 mask (0.0=attend, -inf=mask)，转为 bool
    pad_mask = (attention_mask.squeeze(1).squeeze(1) < -1.0)
    causal_mask = causal_mask.unsqueeze(0) | pad_mask.unsqueeze(-2)
    atten_mask = causal_mask.unsqueeze(1)  # (B, 1, S_q, S_kv)
else:
    atten_mask = causal_mask.unsqueeze(0).unsqueeze(0)  # (1, 1, S_q, S_kv)

npu_out = torch_npu.npu_fusion_attention(
    query, key, value,
    num_heads,
    input_layout="BSND",
    pse=None,
    atten_mask=atten_mask,
    scale=scale,
    pre_tockens=65536,
    next_tockens=0,
    keep_prob=1.0 if not training else 1.0 - dropout_p,
)[0]
context_layer = npu_out.flatten(2, 3).contiguous()  # (B, S, H*D)
```

**关键注意事项**：

1. **必须使用显式 causal mask**。仅靠 `pre_tockens/next_tockens=0` 不足以正确实现因果注意力，实测去掉显式 mask 后 logits 余弦相似度从 0.999 暴跌至 0.5~0.8。
2. **mask 语义**：`atten_mask` 中 `True` 表示「屏蔽」（不参与注意力），`False` 表示「参与」。与 PyTorch 的 `float additive mask` 相反。
3. **padding mask 合并**：Transformer 层传入的 `attention_mask` 是 float 格式 `(0.0 = attend, -inf = mask)`，需转为 bool 后与 causal mask 做 OR 合并。
4. **input_layout="BSND"**：B=batch, S=seq_len, N=num_heads, D=head_dim。确认 query/key/value 从 `_split_heads` 出来的 shape 是 `(B, S, H, D)` 而非 `(B, H, S, D)`。
5. **返回值是 tuple**，取 `[0]`。
6. **decode 阶段**（seq_len_q=1）：`diagonal = S_kv - 1 + 1 = S_kv`，`torch.triu(..., diagonal=S_kv)` 全零，即不屏蔽任何 token，行为正确。

## 辅助优化项

### 内存：permute/transpose 后显式 contiguous

非连续张量在 NPU 上可能触发额外拷贝或 fallback。

```python
x = x.permute(0, 2, 1, 3).contiguous()
```

### 减少同步：避免频繁 .item() / .cpu()

推理阶段尽量在 NPU 上完成计算，仅在最终输出时做一次 `.cpu()`。循环中避免逐步 `.item()` 触发 D2H 同步。

## NPU 设备检测模式

在 modeling 文件顶部统一检测 NPU 可用性，用于所有优化分支的条件判断：

```python
try:
    import torch_npu
    _HAS_TORCH_NPU = True
except ImportError:
    _HAS_TORCH_NPU = False

def _is_npu(x: torch.Tensor) -> bool:
    return (_HAS_TORCH_NPU and hasattr(torch, "npu")
            and torch.npu.is_available()
            and str(x.device).startswith("npu"))
```

## 工作流

**前置条件**：optimization 任务仅在 `adaptation_status=completed` 且 `benchmark_status=completed` 后分配（链式依赖）。完成时需通过 `check_accuracy_run_perf.py`，否则 board_ops 拒绝 `optimization_status=completed`。

1. **创建 model_files**：在 adaptation 目录下创建 `model_files/`，复制并修改 `modeling_*.py`。
2. **逐项添加优化**：常见项可按 RMSNorm → SwiGLU → RotaryEmb → Attention 顺序，每项加完可单独验证。
3. **多卡环境限制单卡测试**：
   ```bash
   npu-smi info
   export ASCEND_RT_VISIBLE_DEVICES={selected_npu}
   uv run python accuracy_run_perf.py run --use-pretrained --max-samples 50
   ```
   `device_map="auto"` 在多卡环境下会将模型分布到多个 NPU，可能导致 `SetPrecisionMode` 错误。用环境变量限制到单卡可解决；但开始前必须先检查各卡占用，优先选空闲或低占用卡，**不要默认抢 0 号卡**。
4. **对比验证**（**精度对比必须使用 pretrained 权重**，baseline 与 perf 均需 `--use-pretrained`）：
   ```bash
   # 先看卡占用并选一张空闲卡；baseline/perf 整轮复用同一张
   npu-smi info
   export ASCEND_RT_VISIBLE_DEVICES={selected_npu}

   # 先跑 baseline（必须 --use-pretrained）
   uv run python accuracy_run.py --use-pretrained --max-samples 50
   # 再跑优化版（必须 --use-pretrained，产出 outputs_*_perf.pt）
   uv run python accuracy_run_perf.py run --use-pretrained --max-samples 50
   # 对比 baseline vs perf（均在 pretrained 权重下）
   uv run python accuracy_run_perf.py compare
   ```
5. **精度验收标准**：
   - **必须**使用 pretrained 权重，与 NPU 上 accuracy_run 的产出对比
   - Logits 余弦相似度 > 0.99
   - PPL 平均相对差异 < 15%
   - 文本匹配率低是正常的（bf16 自回归解码中微小数值差异会放大）

**严格规则（新增，必须执行）**：

- 若 `accuracy_run.py` / `accuracy_run_perf.py` 在 `--use-pretrained` 下加载失败，必须直接失败并修脚本，严禁 silent fallback 到 config
- `mode` / `mode_str` 必须记录真实执行模式，不能把“请求 pretrained”误写成“实际 pretrained”
- config-only 结果只能作诊断，不得作为 optimization completed 的正式结论
- `speedup_ratio` 只能基于同模式、同数据集、同口径的 baseline/perf 计算；不得用 config 结果冒充 pretrained 提速
- baseline、perf、warmup、profiling 必须尽量复用同一个 `selected_npu`；若因 OOM/抢占换卡，必须从受影响阶段重跑
- 多个 agent 并发时，若 0 号卡已忙或显存更高，必须直接换其他卡，不得都抢 0 号卡

## 已知问题与排错

- **多卡 SetPrecisionMode 错误**：先 `npu-smi info` 查看占用，再设置 `ASCEND_RT_VISIBLE_DEVICES={selected_npu}` 限制单卡
- **多个 agent 都抢 0 号卡**：容易 OOM 或互相干扰；运行前先看卡占用，优先选空闲或低占用卡
- **npu_fusion_attention 去掉 mask 后精度崩塌**：必须保留显式 causal bool mask
- **flash_attn 不可用**：NPU 环境无需安装 flash_attn，用 `npu_fusion_attention` 替代
- **SiLU**：NPU 已原生支持 `torch.nn.SiLU` 和 `F.silu`，无需额外替换

## 不包含

- 训练优化（优化器、梯度裁剪、fuse_add_softmax_dropout）
- C++ / CANN 算子开发
- 编译器级优化

## 参考文档

本 skill 提供本地 API 文档（`refer/` 目录）及速查表：

| 文档 | 说明 |
|------|------|
| [reference.md](reference.md) | 推理优化 API 速查（核心算子、参数、mask 构建） |
| [refer/torch_npu_list.md](refer/torch_npu_list.md) | torch_npu 接口列表 |
| [refer/torch_npu-contrib_list.md](refer/torch_npu-contrib_list.md) | torch_npu.contrib 亲和库接口列表 |
