# Issue #6898: [P/D][v0.16.0]Adapt to RecomputeScheduler in vLLM 0.16.0

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Adapt the recompute feature to vLLM 0.16.0, where the D node forwards recompute requests to the P node.
### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?
By ci
- vLLM version: v0.16.0
- vLLM main: https://github.com/vllm-project/vllm/commit/15d76f74e2fdb12a95ea00f0ca283acf6219a2b7


## 基本信息
- **编号**: #6898
- **作者**: wangxiaoteng888
- **创建时间**: 2026-03-02T02:16:24Z
- **关闭时间**: 2026-03-02T15:24:03Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.16.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6898)
