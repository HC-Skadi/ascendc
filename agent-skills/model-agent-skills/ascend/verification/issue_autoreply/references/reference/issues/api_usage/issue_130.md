# Issue #130: Failed to infer device type

## 基本信息

- **编号**: #130
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/130
- **创建时间**: 2025-02-21T07:16:19Z
- **关闭时间**: 2025-04-10T09:13:44Z
- **更新时间**: 2025-04-10T09:13:46Z
- **提交者**: @Qukka0914
- **评论数**: 20

## 标签

question

## 问题描述

base env:
torch                             2.5.1+cpu
torch-npu                     2.5.1.dev20250218
torchaudio                    2.5.1+cpu
torchvision                    0.20.1+cpu
vllm                               0.7.1+empty
vllm_ascend                  0.7.1rc1
CANN 8.0.0.beta1
when I running the vllm server, encounter RuntimeError: Failed to infer device type

![Image](https://github.com/user-attachments/assets/0306ee9d-6bfb-4684-826c-5e3433d58d63)
