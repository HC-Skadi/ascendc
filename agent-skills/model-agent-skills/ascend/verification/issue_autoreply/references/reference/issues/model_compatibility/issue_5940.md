# Issue #5940: [Feat] Merge the multi eagle graphs to one graph

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR merge all steps of draft model in fullgraph mode, to avoid the synchronize between each graph, reduce the bubble time.

#### Key ideas:
- The "model forward" of the step 0 (first step) and remaining steps are captured together as a "Callable", rather than capturing each model individually.
- "update_attn_params" is moved outside the entire graph, meaning that all "attn_metadata" required by all steps are constructed before "replay", and the "attn_params" of all steps are updated at once.
- Remove synchronization between the main model graph and draft model graph.

#### Key params/functions:
- params: draft_attn_metadatas, attn_metadata_multi_steps, slot_mapping_group
- functions: _run_merged_draft, attn_update_stack_num_spec_norm, update_attn_params, _propose, dummy_run

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-projec

## 基本信息
- **编号**: #5940
- **作者**: anon189Ty
- **创建时间**: 2026-01-15T13:44:16Z
- **关闭时间**: 2026-01-23T00:37:03Z
- **标签**: module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5940)
