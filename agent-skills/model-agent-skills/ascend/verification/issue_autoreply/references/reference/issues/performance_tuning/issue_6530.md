# Issue #6530: [Feat.]: 310p support MOE models

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This pull request integrates comprehensive support for Mixture of Experts (MoE) models on the Ascend 310P device within the vllm-ascend framework. It achieves this by introducing specialized modules for expert selection, fused MoE layers, and optimized all-gather communication. The changes also refine existing NPU operations, making them more consistent and efficient for 310P, ultimately enhancing the performance and compatibility of MoE models on this hardware.

Highlights
310P MoE Support: Introduces dedicated implementations for Mixture of Experts (MoE) models on Ascend 310P devices, including new modules for expert selection, fused MoE layers, and communication.
All-Gather Communication: Enforces the use of ALLGATHER communication for MoE operations on 310P, optimizing data transfer and leveraging NPU-specific token dispatching.
Simplified NPU Operations: Removes conditional type casting for npu_swiglu and enables custom rotary embeddin

## 基本信息
- **编号**: #6530
- **作者**: pu-zhe
- **创建时间**: 2026-02-04T04:04:49Z
- **关闭时间**: 2026-02-06T02:30:57Z
- **标签**: module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6530)
