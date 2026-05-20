# Issue #6553: [CI][npugraph_ex]Fix npugraph ex e2e test

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
When running the Qwen3-0.6B model using the npugraph_ex backend, the last few characters of the generated results changed. We have modified the relevant test cases to ensure the CI runs smoothly.
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/v0.15.0


## 基本信息
- **编号**: #6553
- **作者**: ChenCangtao
- **创建时间**: 2026-02-05T03:32:41Z
- **关闭时间**: 2026-02-05T06:03:10Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6553)
