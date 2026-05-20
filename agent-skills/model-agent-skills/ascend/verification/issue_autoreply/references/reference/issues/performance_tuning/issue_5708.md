# Issue #5708: [RFC]: Building an Event Callback Mechanism to Achieve Fine-Grained Overlap of Shared Experts

## 基本信息

- **编号**: #5708
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5708
- **创建时间**: 2026-01-08T03:00:25Z
- **关闭时间**: 2026-01-17T03:53:24Z
- **更新时间**: 2026-01-17T03:53:24Z
- **提交者**: @jianzs
- **评论数**: 0

## 标签

RFC

## 问题描述

### Motivation.

In the current repository, the implementation of overlap for shared experts is relatively coarse. After entering `SharedFusedMoE`, all shared-expert compute operations are first enqueued on the shared-expert stream; then non-shared expert compute operations are enqueued on the main stream; finally, the main stream waits for the shared-expert stream to finish.

This approach can cause the shared-expert compute to run in parallel with non-shared expert compute, leading to resource contention and degraded overall performance.

The best practice we aim for is to overlap the shared-expert compute with the non-shared expert communication (e.g., dispatch/combine/all-reduce), thereby maximizing resource utilization and improving performance.

<img width="1285" height="244" alt="Image" src="https://github.com/user-attachments/assets/015a7ad3-7de2-443f-8ce3-2ec7b56469d5" />

### Proposed Change.

Previously, to achieve fine-grained overlap, we passed shared experts directly into FusedMoE for computation. While effective, this increased code complexity and hurt maintainability.

We propose a new event callback mechanism to enable fine-grained overlap while simplifying the structure:

1. Enqueue all FusedMoE operators on the main stream and record events such as `before_dispatch` and `before_combine`.
2. Return these event handles to `SharedFusedMoE`.
3. On the shared-expert stream, use wait-on-event synchronization to achieve fine-grained overlap.

Example: when launching the shared experts’ down-projection (the “down” op), first wait on the main stream’s `before_combine` event so that the down-projection executes concurrently with the main stream’s combine operation. This aligns compute/communication overlap with best practices and reduces contention.

<img width="492" height="576" alt="Image" src="https://github.com/user-attachments/assets/06d192fe-57eb-4279-a2b6-705a9bdaab23" />

<img width="867" height="203" alt="Image" src="https://github.com/user-attachments/assets/9c3d5003-dd38-46f8-9590-e0cee30ea005" />

### Feedback Period.

_No response_

### CC List.

@realliujiaxu @dragondream-chen 

### Any Other Things.

_No response_
