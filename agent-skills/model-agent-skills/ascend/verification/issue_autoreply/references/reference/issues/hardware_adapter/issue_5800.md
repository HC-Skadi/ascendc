# Issue #5800: [0.13.0][Patch] AscendLoRAModelManager.__init__ 

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
 Adapted for vLLM v0.13.0, added lora_config parameter to the 'get_punica_wrapper' function. Add a conditional check: use a custom operator when rank < 128, otherwise use the vllm operator.
### Does this PR introduce _any_ user-facing change?
<!--
Note that it means *any* user-facing change including all aspects such as API, interface or other behavior changes.
Documentation-only updates are not considered user-facing changes.
-->
No
### How was this patch 

## 基本信息
- **编号**: #5800
- **作者**: ZT-AIA
- **创建时间**: 2026-01-12T07:55:25Z
- **关闭时间**: 2026-01-13T00:45:37Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5800)
