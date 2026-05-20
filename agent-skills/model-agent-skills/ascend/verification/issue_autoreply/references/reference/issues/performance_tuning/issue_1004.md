# Issue #1004: [Feature]: Implement Eagle3 Acceleration on vllm-ascend

## 基本信息

- **编号**: #1004
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1004
- **创建时间**: 2025-05-29T03:37:42Z
- **关闭时间**: 2025-06-20T09:19:55Z
- **更新时间**: 2025-06-20T09:19:55Z
- **提交者**: @umeiko
- **评论数**: 1

## 标签

feature request; RFC

## 问题描述

### 🚀 The feature, motivation and pitch

## Description
The Eagle3 acceleration for GPU has been successfully implemented and merged in [this PR]((https://github.com/vllm-project/vllm/pull/16937). However, the NPU implementation is still missing. Eagle3 is currently the state-of-the-art (SOTA) acceleration technique, and its implementation on NPU would significantly enhance the performance and efficiency of our models running on NPU devices.


### Alternatives

Proposed Solution:
- Finish the draft model and forward on npu.
- Ensure draft model implementation is functional and meets the basic requirements.
- Ensure paged attention for draft model is optimized for NPU and performs efficiently.

### Additional context

- GPU Implementation: Completed and merged in [PR #16937](https://github.com/vllm-project/vllm/pull/16937).
- NPU Implementation: Not yet implemented.
