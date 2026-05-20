# Issue #6536: [CI] Add long and short prompt tests for DeepSeek-V3.2

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This version has no divisibility constraint between tp and mtp+1. However, cudagraph_capture_sizes must be a common multiple of tp and mtp+1, with a maximum of tp * (mtp+1). Therefore, we fixed cudagraph_capture_sizes.

We added a long-sequence test (64k input, 3k output) for the two-node mixed deployment scenario. Due to the excessive time required for performance benchmarking, we are only verifying functionality. The single-node scenario is skipped because VRAM limitations prevent launching the model with a max-model-len of 68,000.

and we also add aime2025 test for dual-node deepseek 3.2 nightly test.

### Does this PR introduce _any_ user-facing change?

no.

### How was this patch tested?

test at nightly environment.

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/v0.15.0


## 基本信息
- **编号**: #6536
- **作者**: starmountain1997
- **创建时间**: 2026-02-04T07:29:35Z
- **关闭时间**: 2026-02-26T02:58:51Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6536)
