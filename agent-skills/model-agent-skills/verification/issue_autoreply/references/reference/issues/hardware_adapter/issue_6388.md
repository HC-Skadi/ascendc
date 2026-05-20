# Issue #6388: [ST]Add e2e test for Npugraphex_pass

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
We found the custom passes of NPUGraphEX have implemented fusion operator features, which still require E2E test case validation and guard. This PR implements E2E test cases for the AddRMSNormQuant and SplitQKVNormRope operator fusions under NPUGraphEX that are already in the codebase.
### Does this PR introduce _any_ user-facing change?
NO
### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6388
- **作者**: ForBetterCodeNine
- **创建时间**: 2026-01-29T07:20:48Z
- **关闭时间**: 2026-01-30T01:14:08Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6388)
