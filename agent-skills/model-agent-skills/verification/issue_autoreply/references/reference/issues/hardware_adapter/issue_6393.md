# Issue #6393: [Feature] DispatchGmmCombineDecode support bf16/float16 gmm1/gmm2 weight and support gmm weight with ND format

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. support ND format gmm weight input.
Before this pr, gmm1_weight and gmm2_weight could only be passed as input to the DispatchGmmCombineDecode operator in NZ data format. After the modification, they are allowed to be passed in ND data format.
2. support bf16/float16 gmm weight
The current PR modification enables the DispatchGmmCombineDecode operator to support non-W8A8 scenarios, allowing gmm1_weight and gmm2_weight to be passed as float16/bfloat16 which is correspond with input token data type.

### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6393
- **作者**: lih827
- **创建时间**: 2026-01-29T12:32:04Z
- **关闭时间**: 2026-02-12T02:37:41Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6393)
