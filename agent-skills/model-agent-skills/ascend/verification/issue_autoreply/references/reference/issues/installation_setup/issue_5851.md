# Issue #5851: move _process_image_input to modelrunner process for Qwen3-VL

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
-->Qwen3-VL-235B-A22B-Instruct-W8A8
  |TTFT | TPOT | TPS |
 |-- | -- | -- | -- | --
 |base | 5.50s | 94.73 | 0.4868 |
 |test | 4.65s | 94.36| 0.3036 |


### Does this PR introduce _any_ user-facing change?
<!--
Note that it means *any* user-facing change including all aspects such as API, interface or other behavior changes.
Documentation-only updates are not considered user-facing changes.
-->NO

### How was this patch tested?
<!--
CI passed with new ad

## 基本信息
- **编号**: #5851
- **作者**: leonlou33333
- **创建时间**: 2026-01-13T08:43:11Z
- **关闭时间**: 2026-01-14T03:06:18Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5851)
