# Issue #5611: Revert "[Feat] enable hierarchical mc2 ops on A2 by default (#5545)"

**类型**: Pull Request

## 问题背景
This reverts commit fb9fdcdbe4f193cddf793dfab9e5666950f3fe4b.

### What this PR does / why we need it?
this pr breaks the smoke test because of that leads the error of aclnnNeScalar:Kernel Run failed. opType: 25, NotEqual
        launch failed for NotEqual, errno:361001
<img width="1149" height="166" alt="A6C9453D-4F0B-4256-DD80-A9C181DAB2D9" src="https://github.com/user-attachments/assets/cab9c4b8-3fd1-4c6b-b424-474b46042726" />

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/7157596103666ee7ccb7008acee8bff8a8ff1731


## 基本信息
- **编号**: #5611
- **作者**: Toneymiller
- **创建时间**: 2026-01-05T09:45:15Z
- **关闭时间**: 2026-01-05T14:39:05Z
- **标签**: module:ops, module:core

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5611)
