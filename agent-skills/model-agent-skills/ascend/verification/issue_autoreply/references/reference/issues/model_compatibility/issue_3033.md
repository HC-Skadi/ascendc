# Issue #3033: [RFC]: Optimiztion of Qwen3-MoE series models.

## 基本信息

- **编号**: #3033
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3033
- **创建时间**: 2025-09-19T06:35:10Z
- **关闭时间**: 2025-12-15T13:42:31Z
- **更新时间**: 2025-12-15T13:42:31Z
- **提交者**: @Angazenn
- **评论数**: 1

## 标签

RFC

## 问题描述

### Motivation.

The Qwen3-MoE series models have become the most famous open-source moe LLMs. However, the performance of Qwen3-MoE in vLLM-Ascend is still under-optimized. In this RFC we aim to utilize new optimization techniques to boost the performance of Qwen3-MoE and generalize to different MoE models.

### Proposed Change.

1. MoE refactor and computation flow optimiztion.
2. Utilization of fused ops.
3. scheduling optimization.

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
