# Issue #5901: [Attention] add gpt-oss support

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Please refer to the following link for the historical conversation https://github.com/vllm-project/vllm-ascend/pull/4467. We have made updates in light of the comments from the prior PR review. Given the refactoring of the attention_v1 component, we have carried out necessary adjustments to fit the newly revised code.

### Does this PR introduce _any_ user-facing change?

1. Modified the code in the Attention section to adapt to the SWA and Sink features required by gpt-oss.
2. Modified the code in the MoE section to add support for bias and swigluoai.

### How was this patch tested?
Please refer to the https://github.com/vllm-project/vllm-ascend/pull/4467 for performance tests, on the basis of which the accuracy tests from AIME2024 have been newly added.
![img_v3_02tu_501e88e3-2217-4565-8edf-b9acf4f43f2g](https://github.com/user-attachments/assets/024f8283-18ab-4d4d-ab12-27917b5d7d06)


- vLLM version: v0.13.0
- vLLM main: https://gi

## 基本信息
- **编号**: #5901
- **作者**: mikequan0425
- **创建时间**: 2026-01-14T09:41:12Z
- **关闭时间**: 2026-02-12T02:55:34Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5901)
