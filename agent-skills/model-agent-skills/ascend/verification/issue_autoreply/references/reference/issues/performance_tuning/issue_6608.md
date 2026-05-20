# Issue #6608: [feat]310P accesses the add_rms_nrom fusion operator

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR updates the `AscendRMSNorm310` layer to use the `npu_add_rms_norm` fused operator from `torch_npu`. This operator combines the residual addition and RMS normalization into a single kernel, which improves compute efficiency for models running on Ascend 310P hardware.

### Does this PR introduce _any_ user-facing change?
No, this is a performance optimization and does not introduce any user-facing changes.

### How was this patch tested?
CI tests should be sufficient to verify the correctness of this change.

## 基本信息
- **编号**: #6608
- **作者**: csoulndai
- **创建时间**: 2026-02-07T02:56:17Z
- **关闭时间**: 2026-02-07T03:15:48Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6608)
