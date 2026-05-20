# Issue #6459: [ModelRunner] Revert "[Fix] Pads query_start_loc to satisfy FIA/TND constraint

**类型**: Pull Request

## 问题背景

This reverts commit 56f5d3bd49ab4275c1bf95d064b020bbf16456fe.

### What this PR does / why we need it?
The patch https://github.com/vllm-project/vllm-ascend/pull/6357 which break the functionality availability in the spec_decode scenario, let's revert and make CI happy first 
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6459
- **作者**: Potabk
- **创建时间**: 2026-01-31T07:01:13Z
- **关闭时间**: 2026-01-31T08:33:34Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6459)
