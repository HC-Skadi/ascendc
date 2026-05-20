# Issue #5502: [CI]Add Disaggregated PD Nightly Test for  Qwen3-235B and Qwen3-VL-235B

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR adds online **Disaggregated Prefill/Decode** performance and accuracy tests for the **Qwen3-235B-A22B** and **Qwen3-VL-235B-A22B-Instruct** models to the Nightly test suite.

These test configurations simulate the deployment of massive MoE and Vision-Language models in **a dual-node (32 NPU)** environment, utilizing Mooncake (KVCache Transfer) technology to achieve efficient KV cache transfer between the Prefill node and the Decode node.

#### Test Configuration
**Qwen3-235B-A22B**
- Model: Qwen/Qwen3-235B-A22B
- Hardware: A3, 2 Nodes (32 NPUs total, 16 NPUs per node)
- Architecture: Disaggregated Prefill & Decode
  - Node 0 (Producer/Prefill): **DP2 + TP8 + EP + FLASHCOMM1 + FUSED_MC2**.
  - Node 1 (Consumer/Decode): **DP4 + TP4 + EP + FLASHCOMM1 + FUSED_MC2 + FULL_DECODE_ONLY**.
- Benchmarks:
  - Performance: vllm-ascend/GSM8K-in3500-bs2800.
  - Accuracy: vllm-ascend/gsm8k-lite.

**Qwen3-VL-235B-A22B-Instruct**
- Model:

## 基本信息
- **编号**: #5502
- **作者**: MrZ20
- **创建时间**: 2025-12-30T02:45:23Z
- **关闭时间**: 2026-01-09T08:25:21Z
- **标签**: ci/build, module:tests

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5502)
