# Issue #5545: [Feat] enable hierarchical mc2 ops on A2 by default

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Previously, it was necessary to set the environment variables HCCL_INTRA_PCIE_ENABLE=1 and HCCL_INTRA_ROCE_ENABLE=0. This PR enables hierarchical MC2 operations on A2 by default.
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/7157596103666ee7ccb7008acee8bff8a8ff1731


## 基本信息
- **编号**: #5545
- **作者**: hwhaokun
- **创建时间**: 2025-12-31T02:21:33Z
- **关闭时间**: 2026-01-04T06:44:21Z
- **标签**: module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5545)
