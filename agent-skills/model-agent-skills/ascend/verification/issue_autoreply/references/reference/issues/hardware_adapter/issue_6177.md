# Issue #6177: [Lint]Style: Convert `vllm-ascend/` to ruff format(Batch #12)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
**Scope of Changes**:
| File Path |
| :--- |
| `vllm_ascend/ops/triton/activation/swiglu_quant.py` |
| `vllm_ascend/ops/triton/batch_invariant/matmul.py` |
| `vllm_ascend/ops/triton/batch_invariant/mean.py` |
| `vllm_ascend/ops/triton/batch_invariant/rmsnorm.py` |
| `vllm_ascend/ops/triton/fla/chunk.py` |
| `vllm_ascend/ops/triton/fla/chunk_delta_h.py` |
| `vllm_ascend/ops/triton/fla/chunk_o.py` |
| `vllm_ascend/ops/triton/fla/chunk_scaled_dot_kkt.py` |
| `vllm_ascend/ops/triton/fla/cumsum.py` |
| `vllm_ascend/ops/triton/fla/fused_qkvzba_split_reshape.py` |
| `vllm_ascend/ops/triton/fla/l2norm.py` |
| `vllm_ascend/ops/triton/fla/layernorm_guard.py` |
| `vllm_ascend/ops/triton/fla/sigmoid_gating.py` |
| `vllm_ascend/ops/triton/fla/solve_tril.py` |
| `vllm_ascend/ops/triton/fla/utils.py` |
| `vllm_ascend/ops/triton/fla/wy_fast.py` |
| `vllm_ascend/ops/triton/fused_gdn_gating.py` |
| `vllm_ascend/ops/triton/layernorm_gated.py` |

## 基本信息
- **编号**: #6177
- **作者**: MrZ20
- **创建时间**: 2026-01-23T03:08:02Z
- **关闭时间**: 2026-01-23T06:59:19Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6177)
