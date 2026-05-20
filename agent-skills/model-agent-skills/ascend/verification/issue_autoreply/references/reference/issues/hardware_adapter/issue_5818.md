# Issue #5818: [Cleanup] Remove dead code make_attention_mask function

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR removes the unused `make_attention_mask` function from `vllm_ascend/worker/v2/attn_utils.py`.

**Why it's dead code:**
- After PR #4870 (attention mask unification refactor), attention mask generation has been centralized in the `AttentionMaskBuilder` singleton class
- The mask is now generated directly by metadata builders when needed (e.g., `AscendAttentionMetadataBuilder`, `AscendMLAMetadataBuilder`)
- The `make_attention_mask` function is no longer called anywhere in the codebase
- The function's parameters (including `attn_mask` and `spec_attn_mask`) were also removed from `build_attn_metadata` in the same refactor

**Changes:**
- Remove `make_attention_mask` function (24 lines) from `vllm_ascend/worker/v2/attn_utils.py`

### Does this PR introduce _any_ user-facing change?

No. This is a code cleanup that removes dead code. No user-facing behavior changes.

### How was this patch tested?

- Verified that `make_at

## 基本信息
- **编号**: #5818
- **作者**: LICO1314
- **创建时间**: 2026-01-12T11:22:06Z
- **关闭时间**: 2026-01-14T08:52:51Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5818)
