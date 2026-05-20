# Issue #5889: [Quantization][Feature] Support compressed tensors moe w4a8 dynamic weight

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

While using the LLM Compressor quantization tool from the VLLM community to generate quantized weights, the VLLM Ascend engine needs to be adapted to support the compressed tensors quantization format.

1. Support Moe model W4A8 dynamic weight.

### Does this PR introduce _any_ user-facing change?

No

### How was this patch tested?


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/bde38c11df0ea066a740efe9b77fff5418be45df


## 基本信息
- **编号**: #5889
- **作者**: LHXuuu
- **创建时间**: 2026-01-14T06:21:45Z
- **关闭时间**: 2026-02-02T08:39:32Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5889)
