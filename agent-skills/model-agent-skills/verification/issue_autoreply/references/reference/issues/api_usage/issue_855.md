# Issue #855: [Bug]:  pip's dependency conflict about torch

## 基本信息

- **编号**: #855
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/855
- **创建时间**: 2025-05-14T07:17:45Z
- **关闭时间**: 2026-01-04T03:39:41Z
- **更新时间**: 2026-01-04T03:39:41Z
- **提交者**: @mingMelody
- **评论数**: 5

## 标签

question

## 问题描述

### Your current environment

ARMv8 CPUs + Ascend NPUs + openEuler

### 🐛 Describe the bug

## pip's dependency conflict about torch

![Image](https://github.com/user-attachments/assets/afc2907f-285c-4688-b94a-e797bb5ed333)

The depicted conflict is as follow:
- vllm-ascend==0.8.5rc1 depends on torch-npu==2.5.1, vllm==0.8.5, torch>=2.5.1
- vllm==0.8.5 depends on torch==2.6.0 
- torch-npu==2.5.1 depends on torch==2.5.1

How can I fix this issue?

