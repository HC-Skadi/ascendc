# Issue #5755: [Feature] Adapt DispathGmmCombineDecode opertor to align with weight scale dtype of small operators. [RFC: issue 5476]

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

[Feature] Adapt DispathGmmCombineDecode opertor to align with weight scale dtype of small operators.
- **Before**: weight scale must be float32
- **After**: weight scale can be float32/float16 when x is float16, float32/bfloat16 when x is float32/bfloat16. And w1 scale can use different dtype with w2 scale.

More info about this operator, please refer to RFC: issue https://github.com/vllm-project/vllm-ascend/issues/5476

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?
#### Perf

> When scale is of type fp16 or bf16, it will be cast to fp32 internally within the operator, while the subsequent computations remain unchanged. Therefore, this PR will introduce an additional cast operation but halve the memory copy operations for scale . Furthermore, since the scale data is only a few KB in size and participates in relatively few computations, its impact is almost negligible compared to major operation

## 基本信息
- **编号**: #5755
- **作者**: wangqiankun13
- **创建时间**: 2026-01-09T03:56:38Z
- **关闭时间**: 2026-01-19T08:10:43Z
- **标签**: module:tests, module:quantization, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5755)
