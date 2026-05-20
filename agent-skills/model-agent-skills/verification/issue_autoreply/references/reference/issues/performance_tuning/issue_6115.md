# Issue #6115: [CI] Enable FLASHCOMM1 with layer_sharding and FULL_DECODE_ONLY in ds32 testing

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

  This PR enables FLASHCOMM1 communication optimization with layer sharding for DeepSeek-V3.2 W8A8 model testing to
  validate PR #5702. The changes include:

  1. Enable FLASHCOMM1: Set VLLM_ASCEND_ENABLE_FLASHCOMM1=1
  improves performance for distributed inference
  2. Add layer sharding: Configure layer_sharding: ["q_b_proj", "o_proj"] 
  4. Update baselines: Adjust performance baselines to reflect the improvements from FLASHCOMM1 and layer sharding

### Does this PR introduce _any_ user-facing change?

  No. This is a CI/test-only change that enables new communication optimization features for testing purposes. 

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6115
- **作者**: starmountain1997
- **创建时间**: 2026-01-22T03:19:19Z
- **关闭时间**: 2026-01-23T11:48:38Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6115)
