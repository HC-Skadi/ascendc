# Issue #6418: [RFC]: vllm-ascend supports MXFP8 quantization

## 基本信息

- **编号**: #6418
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6418
- **创建时间**: 2026-01-30T07:28:08Z
- **关闭时间**: 2026-01-30T07:30:09Z
- **更新时间**: 2026-01-30T07:30:09Z
- **提交者**: @jiangli221
- **评论数**: 0

## 标签

RFC

## 问题描述

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
