# Issue #6192: [Eagle3]enhance skipping dp allreduce and add it into eagle proposer

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR：

1.  Enhances the logic of `_skip_all_reduce_across_dp_group` to skip all cpu dp allreduce for dense models. This is also for purpose  2.
2. Adds `_skip_all_reduce_across_dp_group` into eagle_proposer. Now models like Qwen3-235b supports eagle3 spec decode. A typical setting for these moe models on pd disaggregation often introduce `dp_size > 1`. This requires `set_forward_context` to call a cpu dp allreduce to retrieve `num_tokens_across_dp` on all cases. Skipping this allreduce greatly improves performance.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6192
- **作者**: Angazenn
- **创建时间**: 2026-01-23T08:13:53Z
- **关闭时间**: 2026-01-24T03:29:42Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6192)
