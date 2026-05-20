# Issue #6163: Eliminate H2D copy bubbles by leveraging asynchronous stream scheduling.

**类型**: Pull Request

## 问题背景
<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
When updating experts, it is necessary to update the expert_map and log2phy on the device side, which will result in long-duration H2D operations. These operations can be hidden via asynchronous streams.

<!--
- Please clarify what changes you are proposing. The purpose of this section is to outline the changes and how this PR fixes the issue.
If possible, please consider writing useful notes for better and faster reviews in your PR.

- Please clarify why the changes are needed. For instance, the use case and bug description.

- Fixes #
-->

### Does this PR introduce _any_ user-facing change?
<!--
Note that it means *any* user-facing change including all aspects such as API, interface or other behavior changes.
Documentation-only updates are not considered user-facing changes.
-->

### How

## 基本信息
- **编号**: #6163
- **作者**: njuyuan
- **创建时间**: 2026-01-23T01:18:29Z
- **关闭时间**: 2026-01-26T06:58:17Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6163)
