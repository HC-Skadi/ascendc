# Issue #1305: [Bug]: vLLM0.8.5.post1 + vLLM_Ascend0.8.5rc1 + TRL Qwen2.5 GRPO v1 fail back v0 engine

## 基本信息

- **编号**: #1305
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1305
- **创建时间**: 2025-06-20T02:00:46Z
- **关闭时间**: 2025-06-24T07:15:18Z
- **更新时间**: 2025-06-24T07:15:18Z
- **提交者**: @geekpanda-py
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<html>
<body>
<!--StartFragment-->
CANN | 8.1.RC1
-- | --
HDK | 24.1.rc2.2
Python | 3.10.12
TRL | 0.19
vLLM | 0.8.5.post1
vLLM-Ascend | 0.8.5rc1
Torch | 2.5.1+cpu
Torch-NPU | 2.5.1

<!--EndFragment-->
</body>
</html>


### 🐛 Describe the bug

TRL 0.18 Qwen2.5 GRPO训练中，尝试开始V1 engine时。显示npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.


![Image](https://github.com/user-attachments/assets/89f643d3-901a-42e2-ab1e-6d857a91b4b4)
