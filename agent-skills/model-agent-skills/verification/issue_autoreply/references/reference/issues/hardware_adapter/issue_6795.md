# Issue #6795: feat(310p): add MLA backend and runner support

**类型**: Pull Request

## 问题背景
## Summary
- Add MLA (Multi-Head Latent Attention) backend support for 310P devices
- Implement MLA runner with software-based attention mechanism
- Support configurable KV cache format (ND/NZ) via environment variable
- Fix typing and required modules for 310P MLA implementation

## Test Plan
- CI will run automated tests
- Manual testing on 310P hardware recommended
- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/83b47f67b1dfad505606070ae4d9f83e50ad4ebd


## 基本信息
- **编号**: #6795
- **作者**: 08mamba24
- **创建时间**: 2026-02-25T02:35:49Z
- **关闭时间**: 2026-03-01T09:46:12Z
- **标签**: module:core, merge-conflicts

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6795)
