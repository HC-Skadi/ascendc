# Issue #5834: [Refactor] Move AttentionSpec initialization to Attention module

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR refactors `get_kv_cache_spec` method to delegate AttentionSpec creation to each attention module's own `get_kv_cache_spec()` method, aligning with the vllm source code structure.

**Changes:**
- Simplify `get_kv_cache_spec` in `model_runner_v1.py` and `cpu_offload_connector.py`
- Remove manual `AttentionType` checks for `Attention` modules
- Delegate spec creation to each attention module's `get_kv_cache_spec` method directly
- Let `MambaBase` layers use their own `get_kv_cache_spec` method
- Keep `use_sparse` hack for `MLAAttention` (DeepSeek DSA mode) as Ascend-specific handling

This change follows RFC #5463 item 12: move AttentionSpec to Attention module.

- Fixes #5463 (item 12)

### Does this PR introduce _any_ user-facing change?

No. This is an internal refactoring that simplifies code structure without changing any external behavior.

### How was this patch tested?

- Syntax validation passed via `python -m 

## 基本信息
- **编号**: #5834
- **作者**: LICO1314
- **创建时间**: 2026-01-13T03:23:57Z
- **关闭时间**: 2026-01-19T06:22:19Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5834)
