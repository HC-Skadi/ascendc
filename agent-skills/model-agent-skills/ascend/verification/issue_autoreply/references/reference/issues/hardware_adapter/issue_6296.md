# Issue #6296: [Refact.]: refactoring 310p ops ut

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Refactor swiglu and rms_norm unittest case for 310P and 910B.
Apply attention_v1 get_kv_cache_shape and build metadata on all of platforms
### Does this PR introduce _any_ user-facing change?
NA
### How was this patch tested?
CI UT test
- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6296
- **作者**: pu-zhe
- **创建时间**: 2026-01-27T02:30:37Z
- **关闭时间**: 2026-01-27T08:31:51Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6296)
