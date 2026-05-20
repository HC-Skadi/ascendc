# Issue #5720: [Feature] implenment set_additional_forward_context for model runner v2

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
we implement  set_additional_forward_context in platform, it's necessary to reuse code of gpu in model runner v2 by inheriting method in gpu model runer v2. please see model runner v2's plan #5208 

### Does this PR introduce _any_ user-facing change?
no

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5720
- **作者**: Ronald1995
- **创建时间**: 2026-01-08T07:44:26Z
- **关闭时间**: 2026-01-15T01:18:28Z
- **标签**: module:core

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5720)
