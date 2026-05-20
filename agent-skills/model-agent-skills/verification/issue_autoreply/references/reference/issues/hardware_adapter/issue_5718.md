# Issue #5718: [Quantization] Support compressed tensors moe w8a8 int8 dynamic weight

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
While using the LLM Compressor quantization tool from the VLLM community to generate quantized weights, the VLLM Ascend engine needs to be adapted to support the compressed tensors quantization format.

1. Support Moe model W8A8 Int8 dynamic weight.
2. Specify W4A16 quantization configuration.

Co-authored-by: menogrey 1299267905@qq.com
Co-authored-by: kunpengW-code 1289706727@qq.com

### Does this PR introduce _any_ user-facing change?
No

### How was this patch tested?


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5718
- **作者**: LHXuuu
- **创建时间**: 2026-01-08T06:58:39Z
- **关闭时间**: 2026-01-14T01:17:26Z
- **标签**: module:quantization, ready, ready-for-test, model-download

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5718)
