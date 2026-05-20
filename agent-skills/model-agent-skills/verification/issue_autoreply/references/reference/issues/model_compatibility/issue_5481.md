# Issue #5481: [Refactor] Formatting output types related to FuseMoE

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Currently in the Fused MoE module, functions of classes like MoECommMethod and MoETokenDispatcher output data in dictionary or tuple format, which hampers code maintainability, readability, and extensibility. This PR introduces dataclasses for these key output types to address these issues.

### Does this PR introduce _any_ user-facing change?

No

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/5326c89803566a131c928f7fdd2100b75c981a42


## 基本信息
- **编号**: #5481
- **作者**: jianzs
- **创建时间**: 2025-12-29T09:51:53Z
- **关闭时间**: 2025-12-31T06:24:37Z
- **标签**: module:tests, module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5481)
