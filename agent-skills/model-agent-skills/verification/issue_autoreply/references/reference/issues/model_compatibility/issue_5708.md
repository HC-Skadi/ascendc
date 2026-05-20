# Issue #5708: [RFC]: Building an Event Callback Mechanism to Achieve Fine-Grained Overlap of Shared Experts

**类型**: Issue

## 问题背景
### Motivation.

In the current repository, the implementation of overlap for shared experts is relatively coarse. After entering `SharedFusedMoE`, all shared-expert compute operations are first enqueued on the shared-expert stream; then non-shared expert compute operations are enqueued on the main stream; finally, the main stream waits for the shared-expert stream to finish.

This approach can cause the shared-expert compute to run in parallel with non-shared expert compute, leading to resource contention and degraded overall performance.

The best practice we aim for is to overlap the shared-expert compute with the non-shared expert communication (e.g., dispatch/combine/all-reduce), thereby maximizing resource utilization and improving performance.

<img width="1285" height="244" alt="Image" src="https://github.com/user-attachments/assets/015a7ad3-7de2-443f-8ce3-2ec7b56469d5" />

### Proposed Change.

Previously, to achieve fine-grained overlap, we passed shared experts directly into

## 基本信息
- **编号**: #5708
- **作者**: jianzs
- **创建时间**: 2026-01-08T03:00:25Z
- **关闭时间**: 2026-01-17T03:53:24Z
- **标签**: RFC

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5708)
