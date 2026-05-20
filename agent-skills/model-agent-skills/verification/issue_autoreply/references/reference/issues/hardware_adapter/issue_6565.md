# Issue #6565: [draft][feat] [Spec Decode] Unified Parallel Drafting

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Implement a unified parallelized speculative decoding in VLLM Ascend，which can simultaneously support parallel speculative inference schemes such as Pard, P-Eagle, DFlash, etc.  refer to: https://github.com/vllm-project/vllm/pull/32887  

This PR is currently under development and has not been completed yet. now the triton operate compile failed, i will fix soon，and supplement relevant tests

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/v0.15.0


## 基本信息
- **编号**: #6565
- **作者**: HF-001
- **创建时间**: 2026-02-05T08:57:56Z
- **关闭时间**: 2026-02-14T03:17:42Z
- **标签**: merge-conflicts

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6565)
