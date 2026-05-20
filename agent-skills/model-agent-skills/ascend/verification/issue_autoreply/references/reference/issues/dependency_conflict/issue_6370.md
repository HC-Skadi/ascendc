# Issue #6370: The x86 image of vllm-ascend v0.14.0rc1 contains a bug that causes the error "zeros_like.json is invalid or does not exist".

## 基本信息

- **编号**: #6370
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6370
- **创建时间**: 2026-01-28T17:10:08Z
- **关闭时间**: 2026-01-28T17:11:16Z
- **更新时间**: 2026-01-28T17:11:16Z
- **提交者**: @qiudepei
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

 The x86 image of vllm-ascend version 0.14.0rc1



### 🐛 Describe the bug

When starting the service with the x86 image of vllm-ascend version 0.14.0rc1, the console log will throw the error code EI9999 for the operator aclnnInplaceZero_1_ZerosLikeAiCore, and the plog log will record the detailed error message: "[xxx//zeros_like.json] is invalid or does not exist".
