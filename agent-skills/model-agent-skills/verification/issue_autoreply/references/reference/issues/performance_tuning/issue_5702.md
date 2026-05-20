# Issue #5702: [Feature] Support DSA-CP for Hybrid scenario

**类型**: Pull Request

## 问题背景
Signed-off-by: zzhx1 <zzh_201018@outlook.com>

### What this PR does / why we need it?
> Extracted from PR #5513
Based on the Sharded-CP feature PR:#4702; RFC:https://github.com/vllm-project/vllm/issues/30055

### Support FULL_DECODE_ONLY Mode under PD-Mixed Scenario:
Extends DSA-CP to handle the FULL_DECODE_ONLY execution mode when running in a prefill-decode mixed (PD-mixed) serving environment, improving throughput and resource utilization for decode-intensive workloads.
**In pure prefill nodes:**
- Both q_proj and o_proj are sharded across world ranks, using **broadcast** for weights distribution.

**In PD-mixed nodes (supporting both prefill and decode):**

- q_proj is fully replicated (not sharded) to avoid communication overhead during decoding.
- o_proj Using the original TP `RowParallelLinear` method to store weights

**During prefill execution:**
- o_proj forwards through all_gather to collect weights, reconstructing the complete o_proj weights on each card.

## 基本信息
- **编号**: #5702
- **作者**: zzhx1
- **创建时间**: 2026-01-07T17:46:42Z
- **关闭时间**: 2026-01-22T02:12:09Z
- **标签**: documentation, module:tests, module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5702)
