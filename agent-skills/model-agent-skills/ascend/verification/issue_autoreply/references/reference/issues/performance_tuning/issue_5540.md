# Issue #5540: [P/D] Performance enhancement of Layerwise connector in TP asymmetric scenarios

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
[P/D] Performance enhancement of Layerwise connector in TP asymmetric scenarios
1. Session fusion: For transmission tasks at each layer, aggregate transmission tasks with the same destination and merge them into a single task for assignment.
2. Alltoall aggregation: For TP asymmetric scenarios, perform all alltoall operations at once according to the block granularity for all requests.

[RFC]: CDCP Scheduling for Disaggregated Prefilling with KV Cache Layerwise Push Support https://github.com/vllm-project/vllm-ascend/issues/4842
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/45c1ca1ca1ee8fa06df263c8715e8a412ff408d4


## 基本信息
- **编号**: #5540
- **作者**: liziyu179
- **创建时间**: 2025-12-30T13:01:14Z
- **关闭时间**: 2026-01-06T12:25:36Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5540)
