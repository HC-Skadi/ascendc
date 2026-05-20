# Issue #5765: [Ops] Add layernorm for qwen3Next

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Add layernormFn triton op for qwen3Next model for better performance.

<img width="248" height="526" alt="image" src="https://github.com/user-attachments/assets/27b47157-5df5-4db1-aa88-1dae799b2bf6" />

### Does this PR introduce _any_ user-facing change?

No

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5765
- **作者**: SunnyLee151064
- **创建时间**: 2026-01-09T07:58:04Z
- **关闭时间**: 2026-01-20T06:43:14Z
- **标签**: module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5765)
