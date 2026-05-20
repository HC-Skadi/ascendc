# Issue #5973: [Refactor] Separate `_prepare_inputs` to `_prepare_inputs` and `_preprocess`

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Part of RFC #5449.

Align with upstream vLLM. This PR will help downstream vLLM-Omni reduce the cost for maintaining the `_prepare_inputs`. Besides, it helps vLLM-Ascend code more readable. In the future, we can follow closer to vLLM.

- Moved the multimodal, prompt-embed, positions, PP handling and `update_cos_sin` into _preprocess, and trimmed `_prepare_input`s to return only metadata plus logits and spec-decode inputs.
- Updated `execute_model` to call `_prepare_inputs` then `_preprocess`, preserving the original ordering while separating concerns.
- Reuse `_prepare_mm_inputs` in vLLM and add `model_kwargs`.

NOTE: This PR includes #5971 changes. We need to wait it merged(if it would be approved). Then rebase this PR. 

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060


## 基本信息
- **编号**: #5973
- **作者**: gcanlin
- **创建时间**: 2026-01-17T12:58:25Z
- **关闭时间**: 2026-01-24T03:49:50Z
- **标签**: ready, ready-for-test, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5973)
