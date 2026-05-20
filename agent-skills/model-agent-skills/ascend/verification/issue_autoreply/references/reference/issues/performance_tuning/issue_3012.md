# Issue #3012: [RFC]: Prefill Performance Optimization for DeepSeek Large Scale EP

## 基本信息

- **编号**: #3012
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3012
- **创建时间**: 2025-09-18T09:07:55Z
- **关闭时间**: 2025-12-09T06:28:58Z
- **更新时间**: 2025-12-09T06:28:58Z
- **提交者**: @SlightwindSec
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

The primary motivation for this proposal is to significantly improve the prefill performance of the DeepSeek Large Scale Expert Parallelism (EP) model. Our analysis identified several bottlenecks in the existing implementation, particularly in communication overhead and inefficient operational ordering within the attention and Mixture of Experts (MoE) layers. By optimizing parallelism strategies, reducing communication volumes, and reordering key operations, we can achieve substantial performance gains during the prefill stage.

### Proposed Change.

We propose the following four changes to optimize prefill performance:

1.  **Modified Parallelism Strategy for Shared Experts:** The parallelism strategy for shared experts will be changed from following the attention's Tensor Parallelism (TP) to full Data Parallelism (DP). This involves replicating the shared expert weights on each card, eliminating cross-device communication for this component during the forward pass.
2.  **Optimized Communication for Attention Output:** In the attention mechanism, the `AllReduce` operation currently used for the output projection will be replaced with `ReduceScatter`. This change reduces the overall data transferred between devices, leading to a direct improvement in communication efficiency.
3.  **Delayed `AllGather` in MoE Layers:** The `AllGather` operation that follows the Mixture of Experts (MoE) layer will be moved to after the QKV down-projection. Because activations are partitioned along the token dimension, this move reduces the computational workload of the down-projection and also decreases the volume of data that needs to be communicated afterward.
4.  **Optimized W8A8 Quantization Order for MoE:** For W8A8 quantized MoE layers, the order of operations will be reversed. We propose to quantize the activations *before* the `All2All` communication, rather than after. This simple change reduces the communication payload by nearly 50%, yielding a significant performance enhancement.

**Implementation Details:**
* The changes described in points 1, 2, and 3 are implemented in **PR #2198**.
* The change described in point 4 is implemented in **PR #2195**.

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
