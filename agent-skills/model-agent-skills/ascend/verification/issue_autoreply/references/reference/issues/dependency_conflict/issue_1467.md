# Issue #1467: [Bug]: RuntimeError: shape '[-1, 3, 80, 1280]' is invalid for input size xxxxx |

## 基本信息

- **编号**: #1467
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1467
- **创建时间**: 2025-06-26T13:25:57Z
- **关闭时间**: 2025-06-30T02:04:23Z
- **更新时间**: 2025-06-30T02:04:23Z
- **提交者**: @geekpanda-py
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

vllm:0.8.5.post1
vllm-ascend:0.8.5

### 🐛 Describe the bug

使用trl框架对Qwen2.5-vl-7b模型进行GRPO训练，第二个step会出现RuntimeError: shape '[-1, 3, 80, 1280]' is invalid for input size xxxxxxx

在085rc1上遇到073上已经修复的bug：https://github.com/vllm-project/vllm-ascend/issues/809
