# Issue #6120: [v0.13.0][Feature] Support DSA-CP for Hybrid scenario (#5702)

**类型**: Pull Request

## 问题背景
> Extracted from PR #5513
Based on the Sharded-CP feature PR:#4702;
RFC:https://github.com/vllm-project/vllm/issues/30055

Extends DSA-CP to handle the FULL_DECODE_ONLY execution mode when running in a prefill-decode mixed (PD-mixed) serving environment, improving throughput and resource utilization for decode-intensive workloads.
**In pure prefill nodes:**
- Both q_proj and o_proj are sharded across world ranks, using **broadcast** for weights distribution.

**In PD-mixed nodes (supporting both prefill and decode):**

- q_proj is fully replicated (not sharded) to avoid communication overhead during decoding.
- o_proj Using the original TP `RowParallelLinear` method to store weights

**During prefill execution:**
- o_proj forwards through all_gather to collect weights, reconstructing the complete o_proj weights on each card.

**During decode (graph replay phase):**
- Additional all_to_all (before o_proj) and reduce_scatter (after o_proj) are introduced to enable sequen

## 基本信息
- **编号**: #6120
- **作者**: zzhx1
- **创建时间**: 2026-01-22T06:14:35Z
- **关闭时间**: 2026-01-23T01:13:36Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6120)
