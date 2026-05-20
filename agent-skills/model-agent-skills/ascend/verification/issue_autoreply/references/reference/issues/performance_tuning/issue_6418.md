# Issue #6418: [RFC]: vllm-ascend supports MXFP8 quantization

**类型**: Issue

## 问题背景
### Motivation.

The quantization format currently supported by vllm-ascend has some performance loss compared to the floating-point format. After A5 supports the 8-bit floating-point format, we hope that vllm-ascend will support the MXFP8 quantization format to improve model performance.

### Proposed Change.

We plan to integrate the MXFP8 quantized operator, first enabling the MXFP8-W8A8 quantization capability for dense models, and then enabling the MXFP8-W8A8 quantization capability for sparse models.
Preliminary solution PR#5723

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_

## 基本信息
- **编号**: #6418
- **作者**: jiangli221
- **创建时间**: 2026-01-30T07:28:08Z
- **关闭时间**: 2026-01-30T07:30:09Z
- **标签**: RFC

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/6418)
