# Issue #5477: [Feat][main] Supported to use full-graph with Qwen3-Next-MTP

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Supported to use full-graph with Qwen3-Next-MTP.

In detail, we adatpted `AscendAttentionState.ChunkedPrefill` in main model, and also adapted `AscendAttentionState.ChunkedPrefill` in mtp model.

### Does this PR introduce _any_ user-facing change?

N/A

### How was this patch tested?

We changed the test of Qwen3-Next-MTP in `tests/e2e/multicard/test_qwen3_next.py` to make it a test of `FULL_DECODE_ONLY`. Then run `pytest -s tests/e2e/multicard/test_qwen3_next.py::test_qwen3_next_distributed_mp_eager_mtp_similarity_tp4`.

And this test passed.

```text
.

================================================================================================================================= warnings summary =================================================================================================================================
<frozen importlib._bootstrap>:241
  <frozen importlib._bootstrap>:241: DeprecationWarning: builtin

## 基本信息
- **编号**: #5477
- **作者**: drslark
- **创建时间**: 2025-12-29T08:21:54Z
- **关闭时间**: 2026-01-04T04:03:22Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5477)
