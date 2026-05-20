# Issue #177: [Feature]: Add Support for Guided Decoding (Structured Output)

## 基本信息

- **编号**: #177
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/177
- **创建时间**: 2025-02-26T08:56:35Z
- **关闭时间**: 2025-06-15T07:49:47Z
- **更新时间**: 2026-01-31T07:14:26Z
- **提交者**: @shen-shanshan
- **评论数**: 12

## 标签

guide

## 问题描述

## Overview

In our roadmap, we plan to support **guided decoding** in 2025 Q1 as shown here (#71).

Feel free to feedback your issues when using guided decoding with vllm-ascend, and we will try to fix them if we can.

## Roadmap

  - [7/N] Refactor for structured output module:
    - [x] https://github.com/vllm-project/vllm/pull/16748
    - [x] https://github.com/vllm-project/vllm/pull/16578
    - [x] https://github.com/vllm-project/vllm-ascend/pull/531
    - [x] https://github.com/vllm-project/vllm-ascend/pull/475
    - [x] https://github.com/vllm-project/vllm/pull/16148
    - [x] https://github.com/vllm-project/vllm/pull/21999
    - [x] https://github.com/vllm-project/vllm-ascend/pull/2524
  - [3/N] Bugfix for xgrammar backend:
    - [x] https://github.com/vllm-project/vllm/pull/16954
    - [x] https://github.com/vllm-project/vllm-ascend/pull/555
    - [x] https://github.com/vllm-project/vllm-ascend/pull/2314
  - [2/N] Bugfix for guidance backend:
    - [x] https://github.com/vllm-project/vllm/pull/17839
    - [x] https://github.com/vllm-project/vllm-ascend/pull/2645
  - [2/N] CI & Test:
    - [x] https://github.com/vllm-project/vllm-ascend/pull/1312
    - [x] https://github.com/vllm-project/vllm-ascend/pull/2283
  - [3/N] Doc:
    - [x] https://github.com/vllm-project/vllm-ascend/pull/234
    - [x] https://github.com/vllm-project/vllm-ascend/pull/576 
    - [x] https://github.com/vllm-project/vllm-ascend/pull/1499
  - [3/N] Others:
    - [x] https://github.com/vllm-project/vllm-ascend/pull/1459
    - [x] https://github.com/vllm-project/vllm/pull/22481
 
## Learning Materials

I have written some posts for better understanding this feature:

- [vLLM Guided Decoding (V0)](https://zhuanlan.zhihu.com/p/31572085999)
- [vLLM Guided Decoding (V1)](https://zhuanlan.zhihu.com/p/1895887395691423231)



