# Issue #5719: [Refactor]Refactor of vllm_ascend/distributed module

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Based on the RFC:https://github.com/vllm-project/vllm-ascend/issues/5604

This PR is a refactoring of vllm_ascend/distributed, moving all kv_transfer realtaed codes into a dedicated folder, which has already been done in vLLM

### Does this PR introduce _any_ user-facing change?
NA

### How was this patch tested?


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5719
- **作者**: luoxiaolin712
- **创建时间**: 2026-01-08T07:01:13Z
- **关闭时间**: 2026-01-15T00:57:40Z
- **标签**: ci/build, module:tests, module:ops

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5719)
