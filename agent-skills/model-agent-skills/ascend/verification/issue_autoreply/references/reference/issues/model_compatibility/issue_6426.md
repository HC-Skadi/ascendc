# Issue #6426: [RFC]: 310P adapts to Qwen series models.

## 基本信息

- **编号**: #6426
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6426
- **创建时间**: 2026-01-30T08:27:07Z
- **关闭时间**: 2026-01-30T08:30:47Z
- **更新时间**: 2026-01-30T08:30:47Z
- **提交者**: @wanghengkang
- **评论数**: 0

## 标签

RFC

## 问题描述

### Motivation.

Currently, the vllm inference framework does not support the Ascend 310P chip. In Q1, the framework will support the Qwen series models to meet customer requirements.

### Proposed Change.

The Atlas 300I Duo card adapts to the VLLM inference engine and supports the following models and operators: Qwen3-8B, Qwen3-14B, and Qwen3-32B.
Specific scenarios:
1. Single-core Atlas 300I Duo: 4K/1K sequence, bs=1, Qwen3-8B, Qwen3-14B;
2. 2 x Atlas 300I Duo: 4K/1K sequence, bs=8, Qwen3-32B;

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
