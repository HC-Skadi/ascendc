# Issue #5664: support triton of mrope

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
this pr support use triton mrope like cuda_forward, which performance is equal to ascendc ops
this triton ops should use cann 8.5.0
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?
test in qwen3-vl-235b acc textvqa
native 81.82
npu triton 81.58
cuda triton 81.52
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5664
- **作者**: shiyuan680
- **创建时间**: 2026-01-06T12:44:58Z
- **关闭时间**: 2026-01-13T01:13:52Z
- **标签**: module:tests, module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5664)
