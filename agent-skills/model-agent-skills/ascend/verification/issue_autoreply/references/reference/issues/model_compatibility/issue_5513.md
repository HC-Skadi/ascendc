# Issue #5513: [Feature][official] Support DSA-CP for Deepseek V3.2

**类型**: Pull Request

## 问题背景
# Description:

This PR officially integrates Deepseek V3.2's DSA-CP support on the basis of #4702, improving inference efficiency and scalability under mixed prefill-decode workloads. The main improvements include:

### 1. Officialize DSA-CP Implementation: 
- Promotes the existing DSA-CP logic to an officially supported feature, ensuring compatibility, maintainability, and alignment with Deepseek V3.2’s architecture.
- Replace the implementations of `o_proj`, `q_b_proj`, and `kv_b_proj` with `custom_op` for TP=1.

### 2.  All-gather KV Cache for Communication Overlap: 
- Overlap the all-gather of the KV cache (including nope, rope and index-k) with the computation of q_up_proj to hide communication latency.

### 3. Support FULL_DECODE_ONLY Mode under PD-Mixed Scenario: 
Extends DSA-CP to handle the FULL_DECODE_ONLY execution mode when running in a prefill-decode mixed (PD-mixed) serving environment, improving throughput and resource utilization for decode-intensive worklo

## 基本信息
- **编号**: #5513
- **作者**: zzhx1
- **创建时间**: 2025-12-30T07:31:10Z
- **关闭时间**: 2026-01-26T05:38:31Z
- **标签**: module:ops, module:core, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5513)
