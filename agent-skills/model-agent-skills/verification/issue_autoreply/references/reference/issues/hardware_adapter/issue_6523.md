# Issue #6523: [Ops][Refactor] Remove custom rotary_embedding operator

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR removes the custom `rotary_embedding` operator and its associated C++ kernel implementation, PyTorch bindings, and tests.

The codebase now falls back to using the native `torch_npu._npu_rotary_embedding` implementation. This change simplifies the codebase by removing custom, platform-specific kernel code and relying on the standard NPU library implementation, which is presumably more optimized and easier to maintain.

### Does this PR introduce _any_ user-facing change?
No. This is an internal refactoring and does not introduce any user-facing changes.

### How was this patch tested?
The tests for the custom `rotary_embedding` operator have been removed along with the operator itself. The correctness of the fallback to the native `torch_npu` implementation is verified by existing CI tests for attention layers and models that use rotary embeddings.

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/comm

## 基本信息
- **编号**: #6523
- **作者**: wangxiyuan
- **创建时间**: 2026-02-04T01:24:49Z
- **关闭时间**: 2026-02-07T01:24:05Z
- **标签**: module:tests, module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6523)
