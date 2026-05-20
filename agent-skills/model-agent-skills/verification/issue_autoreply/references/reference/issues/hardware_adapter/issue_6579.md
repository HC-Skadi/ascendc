# Issue #6579: [Refactor]refactor 310p attention impl and add ut

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This pull request significantly refactors the attention mechanism for the Ascend 310P hardware, enhancing its architecture by separating mask generation concerns from the core attention implementation. It introduces a dedicated mask builder class capable of handling various mask types, including causal, splitfuse, and sliding window attention masks, all optimized for the NPU's fractal data format. This change not only cleans up the codebase but also lays the groundwork for more robust and feature-rich attention operations on Ascend devices, backed by new, extensive unit tests.
### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?
E2E test with qwen3 and qwen3-moe
- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d7e17aaacd5ed1b4b4be6bcfef3a1b7cbc84fc9a


## 基本信息
- **编号**: #6579
- **作者**: pu-zhe
- **创建时间**: 2026-02-05T12:44:00Z
- **关闭时间**: 2026-02-07T01:26:26Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6579)
