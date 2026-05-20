# Issue #5528: Adapted to the minimax m2 quantization model

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR fixes Minimax model loading in vLLM Ascend backend by:
1. Adding model type check for "minimax" and "minimax_m2" to replace "mlp" prefix with "block_sparse_moe"
2. Implementing special handling for Minimax expert layer naming conventions
3. Adding Minimax configuration to `packed_modules_model_mapping` for proper qkv_proj and experts module handling

Without these changes, Minimax models fail to load on Ascend devices due to incompatible layer naming and module packing.

### Does this PR introduce _any_ user-facing change?
Yes. Users can now successfully load and run Minimax models on Ascend hardware with vLLM. This enables inference capabilities for this model family on Ascend devices.


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/45c1ca1ca1ee8fa06df263c8715e8a412ff408d4


## 基本信息
- **编号**: #5528
- **作者**: a213402010
- **创建时间**: 2025-12-30T11:38:23Z
- **关闭时间**: 2026-01-05T09:50:37Z
- **标签**: module:quantization

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5528)
