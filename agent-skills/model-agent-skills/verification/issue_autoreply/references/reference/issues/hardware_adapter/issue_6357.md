# Issue #6357: [Fix] Pads query_start_loc to satisfy FIA/TND constraint

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This handles both uniform and mixed batches (by inserting a dummy request for mixed batches), consolidates ad-hoc padding into a single helper, copies the updated buffer to the device, and asserts the layout constraint before building the attention metadata. Together, these changes prevent kernel mismatches or failures and ensure correct shapes for FIA/TND execution in full graph modes.

We currently place this helper in `execute_model`. My original design was to include it in `_prepare_inputs`, but that doesn’t work because it must run after padding. While I’d prefer to minimize the impact and reuse as much of the base class as possible in the future, it doesn’t seem achievable at the moment.

### Does this PR introduce _any_ user-facing change?
None.

### How was this patch tested?
Test cases added.

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6357
- **作者**: yiz-liu
- **创建时间**: 2026-01-28T09:30:25Z
- **关闭时间**: 2026-01-30T08:41:44Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6357)
