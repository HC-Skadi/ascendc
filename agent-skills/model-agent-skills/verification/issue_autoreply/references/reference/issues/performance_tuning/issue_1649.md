# Issue #1649: [RFC]: Support Full Graph with multiple attention kernels

## 基本信息

- **编号**: #1649
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1649
- **创建时间**: 2025-07-07T09:44:22Z
- **关闭时间**: 2025-10-16T06:23:21Z
- **更新时间**: 2025-10-16T06:23:21Z
- **提交者**: @yiz-liu
- **评论数**: 7

## 标签

RFC

## 问题描述

### Motivation

Compared to piecewise graph capture, the “full graph” approach offers three primary advantages:

* **Reduced dispatch latency:** By replaying the entire model execution graph at once, we cut overhead compared with multiple smaller replays.
* **Stabilized multi-device performance:** Captureing the whole model as one static graph also mitigates the dispatch fluctuations across devices.
* **Stream/resource savings:** Consolidating graph captures frees up streams, allowing more graphs to be captured.

<img width="2560" height="1378" alt="Image" src="https://github.com/user-attachments/assets/1c88d336-409a-4245-a491-45f30b2650d3" />

### Proposed Change

Our implementation will differ slightly from vLLM’s native mechanism for two main reasons:

1. **Divergent Attention Operator Paths**
   In vLLM‑Ascend, the attention operator path is not uniform and is selected at inference time based on the `AttentionState`. To accommodate this, we will hoist the control flow logic outside the inference graph. We will pre‑compile distinct graphs for each possible attention state, then dispatch the appropriate graph at each step.

2. **Dynamic Attention Parameter Updates**
   Parameters such as `seq_lens` and `block_table` must be updated at every decoding step to ensure correct tiling and maintain numerical accuracy. We will leverage `graph_task_update` to asynchronously re‑issue updated parameters for the attention operator on a separate stream, thereby minimizing compute bubbles caused by synchronous dispatch.

#### Implementation Plan

1. **Decode‑Stage Full Graph**
   Build the foundational framework and implement full‑graph capture for the `DecodeOnly` stage—where host dispatch latency is most critical. (See PRs #1503 and #1677.)

2. **Prefill‑Stage Full Graph**
   Extend the graph‑dispatching framework to support the Prefill stage, and refactor the implementation into its long‑term location within the codebase.

3. **Engineering Tasks**
   Address additional concerns such as memory profiling, stream management, batch sizes adjusting, and integration testing.

### Feedback Period.

2 weeks.

### CC List.

@Yikun @wangxiyuan 

### Any Other Things.

_No response_
