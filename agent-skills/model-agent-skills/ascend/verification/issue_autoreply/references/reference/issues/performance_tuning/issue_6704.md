# Issue #6704: [Feat.][310P] addrmsnorm for 300I DUO

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR integrates the `npu_add_rms_norm` fused kernel for RMSNorm operations with residual connections on 310P devices. This change optimizes the computation by replacing a two-step process (manual residual addition followed by RMSNorm) with a single, more efficient fused operation. This is needed to improve the performance of models utilizing RMSNorm with residual connections on the 310P architecture.

Fixes #

### Does this PR introduce _any_ user-facing change?
No, this PR introduces an internal optimization and does not change any user-facing APIs or behaviors.

### How was this patch tested?
This patch was tested with updated unit tests (`test_RMSNorm_forward_310p`) that mock the `npu_add_rms_norm` operation to verify the correctness of the fused kernel integration.

## 基本信息
- **编号**: #6704
- **作者**: Tflowers-0129
- **创建时间**: 2026-02-11T11:59:04Z
- **关闭时间**: 2026-02-13T07:40:49Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6704)
