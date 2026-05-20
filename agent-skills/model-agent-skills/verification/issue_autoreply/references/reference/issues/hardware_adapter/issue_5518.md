# Issue #5518: [Triton][Config] Add muls_add triton kernel and refactor AscendCompilationConfig

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Add muls_add triton kernel with related fusion pass. What's more, this PR refactors `AscendCompilationConfig` and delete `NpugraphExConfig`.

### Does this PR introduce _any_ user-facing change?
None

### How was this patch tested?
CI passed with new added test.


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/45c1ca1ca1ee8fa06df263c8715e8a412ff408d4


## 基本信息
- **编号**: #5518
- **作者**: whx-sjtu
- **创建时间**: 2025-12-30T08:28:09Z
- **关闭时间**: 2026-03-02T09:54:25Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5518)
