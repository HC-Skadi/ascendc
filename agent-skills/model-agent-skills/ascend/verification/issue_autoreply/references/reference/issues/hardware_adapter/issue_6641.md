# Issue #6641: [Feat] 310p support MoE W8A8 quantizaition

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR introduces support for W8A8 dynamic quantization for Mixture-of-Experts (MoE) models on Ascend 310P devices. This is achieved by:
- Implementing a new quantization scheme `AscendW8A8DynamicFusedMoEMethod310`.
- Adding a unified MLP implementation (`unified_apply_mlp`) for 310P that handles both quantized and unquantized paths.
- Refactoring the MoE and quantization configuration logic to correctly route to the new 310P-specific implementations.
- Adding new e2e and unit tests to verify the functionality of MoE W8A8 quantization.

### Does this PR introduce _any_ user-facing change?
No

### How was this patch tested?
- Added a new e2e test `test_qwen3_moe_tp2_w8a8` to test MoE W8A8 quantization in a multi-card setup.
- Added several new unit tests for the 310P-specific MoE components, including `experts_selector`, `fused_moe`, `moe_comm_method`, `moe_mlp`, and the new `w8a8_dynamic` quantization method.

- vLLM version: v0.15

## 基本信息
- **编号**: #6641
- **作者**: pu-zhe
- **创建时间**: 2026-02-09T12:29:25Z
- **关闭时间**: 2026-02-10T09:17:44Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6641)
