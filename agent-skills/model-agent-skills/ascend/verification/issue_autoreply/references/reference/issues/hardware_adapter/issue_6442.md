# Issue #6442: [Refactor] MLP weight prefetch to consistency with MoE Model's prefetching in terms of code and usage

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Refactor MLP weight prefetch to consistency with MoE Model's prefetching in terms of code and usage. 
Environments VLLM_ASCEND_ENABLE_PREFETCH_MLP, VLLM_ASCEND_MLP_DOWN_PREFETCH_SIZE and VLLM_ASCEND_MLP_GATE_UP_PREFETCH_SIZE is removed, usage as following:

--additional-config  '{"weight_prefetch_config": { "enabled": true,  "prefetch_ratio": {"mlp": { "gate_up": 1.0,  "down": 1.0}  }}}'

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6442
- **作者**: leo-pony
- **创建时间**: 2026-01-30T12:55:54Z
- **关闭时间**: 2026-02-04T01:08:18Z
- **标签**: documentation, module:tests, module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6442)
