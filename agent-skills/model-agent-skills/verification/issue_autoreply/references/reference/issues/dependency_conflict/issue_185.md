# Issue #185: [Usage]: v0.7.3-dev分支镜像无法使用

## 基本信息

- **编号**: #185
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/185
- **创建时间**: 2025-02-27T02:41:31Z
- **关闭时间**: 2025-03-04T06:44:39Z
- **更新时间**: 2025-03-04T06:44:41Z
- **提交者**: @myliangchengyu
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

拉取quay.io/ascend/vllm-ascend:v0.7.3-dev镜像后，运行发现内部torch版本2.6.0，无torch-npu安装，无法运行vllm-ascend

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

