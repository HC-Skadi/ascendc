# Issue #111: Inference speed is slow

## 基本信息

- **编号**: #111
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/111
- **创建时间**: 2025-02-19T13:52:02Z
- **关闭时间**: 2025-05-14T01:50:07Z
- **更新时间**: 2025-05-14T01:50:08Z
- **提交者**: @junming-yang
- **评论数**: 7

## 标签

performance

## 问题描述

在测试 Qwen/Qwen2.5-0.5B-Instruct 时发现，3090能达到 300 token/s，910B 单卡维持在20 ～ 30 token/s，似乎慢了不少
