# Issue #6416: fix: resolve sync bug in DispathFFNCombine when expert num per card is 32

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Fix the synchronization deadlock issue in DispathFFNCombine module that occurs on NPU cards when the number of experts per card exceeds 16 (the bug manifests prominently when set to 32/128).

### Does this PR introduce _any_ user-facing change?
No, this is a bug fix for internal synchronization logic specific to NPU expert dispatch, with no impact on external APIs, interfaces, or end-user behaviors.


- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6416
- **作者**: serlar
- **创建时间**: 2026-01-30T07:24:41Z
- **关闭时间**: 2026-01-30T13:21:21Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6416)
