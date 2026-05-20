# Issue #5854: model runner v2 support triton of penalty

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Optimized operator performance and add ut test
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?
test in qwen2.5 7b vl, ops time approved 90%
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d

this pr is for
# https://github.com/vllm-project/vllm-ascend/issues/5208


## 基本信息
- **编号**: #5854
- **作者**: shiyuan680
- **创建时间**: 2026-01-13T09:21:19Z
- **关闭时间**: 2026-01-20T12:26:06Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5854)
