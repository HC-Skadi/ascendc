# Issue #5936: [Performance] Remove index opetation when VLLM_ASCEND_FLASHCOMM2_PARALLEL_SIZE=1

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

When enable VLLM_ASCEND_FLASHCOMM2_PARALLEL_SIZE>1, we need index operation to reorganize the batch, because that we need ensure the correct batch-id for each rank after the reduce-scatter op in VLLM_ASCEND_FLASHCOMM2_PARALLEL_SIZE>1. But we do not need it when  VLLM_ASCEND_FLASHCOMM2_PARALLEL_SIZE=1, which dose not need reduce-scatter.
<img width="755" height="520" alt="image" src="https://github.com/user-attachments/assets/7180719f-822f-427b-9955-3372bb8ac105

## 基本信息
- **编号**: #5936
- **作者**: Levi-JQ
- **创建时间**: 2026-01-15T12:20:37Z
- **关闭时间**: 2026-01-19T09:12:13Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5936)
