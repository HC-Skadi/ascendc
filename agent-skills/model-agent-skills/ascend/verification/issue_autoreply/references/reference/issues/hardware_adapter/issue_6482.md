# Issue #6482: [CI]Disable early exit to complete all tests

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. Disable the feature to exit early upon encountering an error in order to complete all tests.
2. Within each partition, tests are re-sorted by `estimated_time` in ascending order. This allows the CI to cover as many test cases as possible in the early stages.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6482
- **作者**: MrZ20
- **创建时间**: 2026-02-02T05:08:33Z
- **关闭时间**: 2026-02-03T03:25:51Z
- **标签**: ci/build, module:tests

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6482)
