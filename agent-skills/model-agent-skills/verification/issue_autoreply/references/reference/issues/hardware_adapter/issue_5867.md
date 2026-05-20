# Issue #5867: add restrictions on the fusion parameter

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Add an enablement restriction for the fused operator gmmswigluquant: only enable this operator when the number of devices is greater than 16.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/bde38c11df0ea066a740efe9b77fff5418be45df


## 基本信息
- **编号**: #5867
- **作者**: aipaes
- **创建时间**: 2026-01-13T12:38:46Z
- **关闭时间**: 2026-01-27T01:54:58Z
- **标签**: module:ops, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5867)
