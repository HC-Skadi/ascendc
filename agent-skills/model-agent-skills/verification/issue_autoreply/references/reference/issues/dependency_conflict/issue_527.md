# Issue #527: [Bug]: cannot import name 'PoolingParams' from 'vllm' (unknown location)

## 基本信息

- **编号**: #527
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/527
- **创建时间**: 2025-04-15T03:27:07Z
- **关闭时间**: 2025-04-16T05:54:55Z
- **更新时间**: 2025-07-28T07:31:59Z
- **提交者**: @RyanOvO
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

Name: vllm_ascend
Version: 0.7.3rc1

Name: vllm
Version: 0.7.3+empty

模型是基于MindSpeed-LLM训练后，在转成hf格式，然后调用vllm做推理，报错如下：

![Image](https://github.com/user-attachments/assets/cac122a9-6b63-487d-8695-a0d57d1f9910)

脚本如下：

![Image](https://github.com/user-attachments/assets/1d20536d-42e0-4805-9307-aead91530409)

### 🐛 Describe the bug

None
