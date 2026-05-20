# Issue #5624: adapt to minimax_m2

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR fixes Minimax model loading in vLLM Ascend backend by:

Adding model type check for "minimax" and "minimax_m2" to replace "mlp" prefix with "block_sparse_moe"
Implementing special handling for Minimax expert layer naming conventions
Adding Minimax configuration to packed_modules_model_mapping for proper qkv_proj and experts module handling
Without these changes, Minimax models fail to load on Ascend devices due to incompatible layer naming and module packing.

### Does this PR introduce _any_ user-facing change?
Yes. Users can now successfully load and run Minimax models on Ascend hardware with vLLM. This enables inference capabilities for this model family on Ascend devices.

### How was this patch tested?
Local Testing:
Verified model loading for minimax-xxx and minimax_m2-xxx model variants on Atlas 800I A2 hardware
Tested inference with sample prompts using vLLM's OpenAI-compatible API server

Benchmark Validation:
Co

## 基本信息
- **编号**: #5624
- **作者**: Feng-xiaosuo
- **创建时间**: 2026-01-06T02:50:30Z
- **关闭时间**: 2026-01-10T15:01:35Z
- **标签**: module:quantization

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5624)
