# Issue #5869: [Refactor][EAGLE] 5/N Update attn_metadata by common_attn_metadata

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
4/N EAGLE refactor plan devided into many parts, this PR is the first change, which modifies the attn_metadata update method by modifying common_metadata and then rebuilding the code.

### Does this PR introduce _any_ user-facing change?
ut

### How was this patch tested?
no
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/bde38c11df0ea066a740efe9b77fff5418be45df


## 基本信息
- **编号**: #5869
- **作者**: lilinsiman
- **创建时间**: 2026-01-13T12:59:34Z
- **关闭时间**: 2026-01-20T02:06:00Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5869)
