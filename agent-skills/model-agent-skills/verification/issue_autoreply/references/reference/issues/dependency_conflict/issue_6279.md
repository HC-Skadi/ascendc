# Issue #6279: [Bug]: 910b入图使用多lora起Qwen3-32B模型，发送推理请求时选择基础模型推理，进程直接挂掉。

## 基本信息

- **编号**: #6279
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6279
- **创建时间**: 2026-01-26T12:01:35Z
- **关闭时间**: 2026-02-03T02:31:17Z
- **更新时间**: 2026-02-03T02:31:17Z
- **提交者**: @liaoqingqing677
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

quay.io/ascend/vllm-ascend:v0.13.0rc2

### 🐛 Describe the bug

910b入图使用多lora起Qwen3-32B模型，发送推理请求时选择基础模型推理，进程直接挂掉。报错如下：
(EngineCore_DP0 pid=480) ERROR 01-26 08:19:45 [patch_core.py:70] RuntimeError: Worker failed with error 'CUDA graph capturing detected at an inappropriate time. This operation is currently disabled.', please check the stack trace above for the root cause
