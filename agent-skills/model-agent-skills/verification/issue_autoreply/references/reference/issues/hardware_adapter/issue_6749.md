# Issue #6749: [v0.13.0][Fusion]add checks to skip fusion where split_rmsnorm_rope is not supported

**类型**: Pull Request

## 问题背景
<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
With #6602 , `npu_rotary_embedding` unifies all rope implementation in AscendRotaryEmbedding, but allows a wider range of application of fusion op `split_qkv_rmsnorm_rope`. This PR restricts the fusion of `split_qkv_rmsnorm_rope` to only cases where `head_size` == 128 && `rotary_dim` == `head_size`.  Further enhancement and generalization of this op will be accomplished by @whx-sjtu .

### Does this PR introduce _any_ user-facing change?
<!--
Note that it means *any* user-facing change including all aspects such as API, interface or other behavior changes.
Documentation-only updates are not considered user-facing changes.
-->

### How was this patch tested?
<!--
CI passed with new added/existing test.
If it was tested in a way different from regular unit tests, please clarify how you tested step 

## 基本信息
- **编号**: #6749
- **作者**: Angazenn
- **创建时间**: 2026-02-13T09:49:00Z
- **关闭时间**: 2026-02-14T10:36:38Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6749)
