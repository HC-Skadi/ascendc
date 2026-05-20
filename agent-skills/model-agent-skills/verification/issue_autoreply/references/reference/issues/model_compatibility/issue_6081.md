# Issue #6081: [Feature][Cherry Pick]Enable DispatchGmmCombineDecode when eagle is moe with w8a8, or not moe

**类型**: Pull Request

## 问题背景


<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
<!--
- Please clarify what changes you are proposing. The purpose of this section is to outline the changes and how this PR fixes the issue.
If possible, please consider writing useful notes for better and faster reviews in your PR.

- Please clarify why the changes are needed. For instance, the use case and bug description.

- Fixes #
-->
This PR is cherry-picked from https://github.com/vllm-project/vllm-ascend/pull/5758.

Operator DispatchGmmCombineDecode does not support non-W8A8 scenarios and cannot share the same communication domain with Operator Dispatch/Combine.

for instance, when the draft model uses a non-W8A8 MOE architecture while the main model employs a W8A8 MOE architecture.

Therefore days ago, I implemented an interception that unconditionally disables Operator DispatchGm

## 基本信息
- **编号**: #6081
- **作者**: wangqiankun13
- **创建时间**: 2026-01-21T07:01:57Z
- **关闭时间**: 2026-01-22T02:51:29Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6081)
