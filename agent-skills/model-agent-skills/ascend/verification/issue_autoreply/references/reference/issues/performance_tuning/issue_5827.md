# Issue #5827: [Performance]use triton mrope for Qwen3-VL

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
The performance can be optimized by use triton mrope for Qwen3-VL.

1. Qwen3-VL-235B-A22B-Instruct-W8A8

  | accuracy | TTFT | TPOT | TPS
-- | -- | -- | -- | --
base | 83.76 | 4.8771s | 0.1472 | 49
test | 83.59 | 4.3273 | 0.0615 | 105

2. Qwen3-VL-8B-Instruct

  | accuracy | TTFT | TPOT | TPS
-- | -- | -- | -- | --
base | 80.65 | 4.1744 | 0.0499 | 125
test | 80.86 | 3.1858 | 0.0245 | 227

### Does this PR introduce _any_ user-facing change?
<!--


## 基本信息
- **编号**: #5827
- **作者**: ichaoren
- **创建时间**: 2026-01-13T01:43:06Z
- **关闭时间**: 2026-01-17T02:08:39Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5827)
