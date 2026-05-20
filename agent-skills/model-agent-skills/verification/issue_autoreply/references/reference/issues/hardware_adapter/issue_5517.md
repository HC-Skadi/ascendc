# Issue #5517: [Feature] implement basic framework for batch invariant

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR implement the basic framework for batch invariant, please see https://github.com/vllm-project/vllm-ascend/issues/5487.
### Does this PR introduce _any_ user-facing change?
we reuse the function `vllm_is_batch_invariant` in vllm to judge if batch invariant is  enabled.

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/45c1ca1ca1ee8fa06df263c8715e8a412ff408d4


## 基本信息
- **编号**: #5517
- **作者**: Ronald1995
- **创建时间**: 2025-12-30T08:04:11Z
- **关闭时间**: 2026-01-07T01:11:27Z
- **标签**: ci/build, module:tests, module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5517)
