# Issue #6807: [DOC] enable both flashcomm1 and cudagraph

**类型**: Pull Request

## 问题背景
## What this PR does / why we need it?

This PR updates the DeepSeek-V3.2 documentation to include the latest performance optimizations and configuration improvements.

### Changes

- **Enable FlashComm1**: Added `VLLM_ASCEND_ENABLE_FLASHCOMM1=1` environment variable across all deployment scenarios to enable FlashComm1 for improved communication performance
- **Layer Sharding**: Added `--additional-config '{"layer_sharding": ["q_b_proj", "o_proj"]}'` configuration to enable layer sharding for better memory distribution
- **CUDA Graph Optimization**: Updated cudagraph capture sizes from `[3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48]` to `[8, 16, 24, 32, 40, 48]`
- **Speculative Decoding**: Increased `num_speculative_tokens` from 2 to 3
- **Documentation Links**: Fixed request forwarding documentation to use proper GitHub repository links

## Does this PR introduce _any_ user-facing change?

Yes, users can now follow the updated documentation to enable FlashComm1 and layer

## 基本信息
- **编号**: #6807
- **作者**: starmountain1997
- **创建时间**: 2026-02-25T09:12:49Z
- **关闭时间**: 2026-02-27T06:52:55Z
- **标签**: documentation

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6807)
