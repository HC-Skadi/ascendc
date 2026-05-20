# Issue #1579: [Bug]: 310P单机多卡运行Qwen3-32B, Ran out of input

## 基本信息

- **编号**: #1579
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1579
- **创建时间**: 2025-07-02T06:04:32Z
- **关闭时间**: 2025-07-03T04:32:11Z
- **更新时间**: 2025-07-17T14:42:43Z
- **提交者**: @hmxdemoney
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

310P单机多卡运行Qwen3-32B

### 🐛 Describe the bug

使用的镜像是quay.io/ascend/vllm-ascend:v0.9.1rc1-310p
日志在文件里面，首先进行了hccl_test，然后再拉起的模型

[docker_log.txt](https://github.com/user-attachments/files/21012196/docker_log.txt)
