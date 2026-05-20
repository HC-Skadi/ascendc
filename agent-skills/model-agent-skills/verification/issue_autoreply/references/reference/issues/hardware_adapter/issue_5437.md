# Issue #5437: [Refactor][EAGLE] 2/N: load model and generate token

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. Refactor eagle and mtp function: load_model and generate_token_ids
2. Remove redundant code in mtp and eagle file
3. Refactor the UT of file

2/N of Refactor and merge mtp and eagle
Relational RFC: https://github.com/vllm-project/vllm-ascend/issues/5467

### Does this PR introduce _any_ user-facing change?
no

### How was this patch tested?
ut and tests

- vLLM version: release/v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/81786c87748b0177111dfdc07af5351d8389baa1


## 基本信息
- **编号**: #5437
- **作者**: lilinsiman
- **创建时间**: 2025-12-27T09:18:56Z
- **关闭时间**: 2026-01-05T06:07:54Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5437)
