# Issue #6304: [Main2Main] Upgrade vllm commit to `v0.15.0rc0`

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

1. Fix `TypeError: MMEncoderAttention.__init__() got an unexpected keyword argument 'multimodal_config'` due to https://github.com/vllm-project/vllm/pull/31972.
2. Fix `_shared_experts: 'NoneType' object is not callable` due to https://github.com/vllm-project/vllm/pull/32082 by https://github.com/vllm-project/vllm-ascend/pull/6335.
3. Fix `ReshapeAndCacheOperation setup failed!` due to https://github.com/vllm-project/vllm/pull/25954 by registering `unified_kv_cache_update` custom op.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6304
- **作者**: shen-shanshan
- **创建时间**: 2026-01-27T07:13:27Z
- **关闭时间**: 2026-02-02T06:22:35Z
- **标签**: documentation, ci/build, module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6304)
