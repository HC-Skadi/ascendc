# Issue #6162: [v0.13.0]skip eagle dp allreduce

**类型**: Pull Request

## 问题背景
<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
On releases/v0.13.0 branch, we only support dense eagle head. Since these dense draft models do not actually take any communication between dp groups, we can directly skip the dp allreduce which gets `num_tokens_across_dp` to improve performance. On main branch, this will be incorporated by refactor of eagle proposer (such as #6096 ).

### Does this PR introduce _any_ user-facing change?
<!--
Note that it means *any* user-facing change including all aspects such as API, interface or other behavior changes.
Documentation-only updates are not considered user-facing changes.
-->

### How was this patch tested?
<!--
CI passed with new added/existing test.
If it was tested in a way different from regular unit tests, please clarify how you tested step by step, ideally copy and paste-able, so that other

## 基本信息
- **编号**: #6162
- **作者**: Angazenn
- **创建时间**: 2026-01-22T15:54:37Z
- **关闭时间**: 2026-01-23T15:23:37Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6162)
