# Issue #5698: [Refactor] Replace the implementations of o_proj, q_b_proj, and kv_b_proj with custom_op for sharded CP

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

>Extracted from PR https://github.com/vllm-project/vllm-ascend/pull/5513
Based on the Sharded-CP feature PR:https://github.com/vllm-project/vllm-ascend/pull/4702; RFC:https://github.com/vllm-project/vllm/issues/30055

This PR officially integrates Deepseek V3.2's DSA-CP support on the basis of https://github.com/vllm-project/vllm-ascend/pull/4702, improving inference efficiency and scalability under mixed prefill-decode workloads. The main improvements include:
- Replace the implementations of o_proj, q_b_proj, and kv_b_proj with custom_op for TP=1.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5698
- **作者**: zzhx1
- **创建时间**: 2026-01-07T10:34:44Z
- **关闭时间**: 2026-01-09T07:58:41Z
- **标签**: documentation, module:tests, module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5698)
