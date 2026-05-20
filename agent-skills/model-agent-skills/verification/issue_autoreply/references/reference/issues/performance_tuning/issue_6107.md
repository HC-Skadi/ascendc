# Issue #6107: [Feature] Batch invariant torch.compile

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Building upon https://github.com/vllm-project/vllm-ascend/pull/5517 to enable batch-invariant in vllm-ascend, we observed that the performance of BI in eager mode remains suboptimal.

This PR further integrates batch-invariant with torch.compile, which improves inference performance by 350% when tested with Qwen3-0.6B.

### Does this PR introduce _any_ user-facing change?
Previously, enabling both aclgraph and Batch-Invariant would cause an "ub overflow" error. This occurred because transposed input tensors could produce incorrect stride() values.

To fix this, we now call .contiguous() on the input tensors before passing them to Triton kernels. This ensures a contiguous memory layout and prevents transposed tensors from causing incorrect stride calculations.

### Test Plan
pytest -sv --durations=0 tests/e2e/singlecard/test_aclgraph_batch_invariant.py

### Test Result
```
============================================================

## 基本信息
- **编号**: #6107
- **作者**: huangfeifei1995
- **创建时间**: 2026-01-21T14:24:31Z
- **关闭时间**: 2026-01-26T01:15:06Z
- **标签**: ci/build, module:tests, module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6107)
