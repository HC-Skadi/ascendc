# Issue #6657: [Feature] adapt to uva buffer and main2main

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
vllm model runner v2 use uva buffer to prepare input data, but npu doesn't support uva yet, this pr implement a uvawrapper class to mimic gpu's uva backend. what's more, this pr make some modifications to adapt to the newer main branch.

### Does this PR introduce _any_ user-facing change?
no
### How was this patch tested?
- vLLM main: https://github.com/vllm-project/vllm/commit/13397841ab469cecf1ed425c3f52a9ffc38139b5


## 基本信息
- **编号**: #6657
- **作者**: Ronald1995
- **创建时间**: 2026-02-10T07:21:30Z
- **关闭时间**: 2026-02-12T02:36:31Z
- **标签**: documentation, module:core

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6657)
