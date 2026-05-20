# Issue #5455: [RFC]: 【910B部署】希望mindie_turbo与性能采集工具可以相互适配

## 基本信息

- **编号**: #5455
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5455
- **创建时间**: 2025-12-29T01:21:16Z
- **关闭时间**: 2026-01-04T03:20:43Z
- **更新时间**: 2026-01-04T03:20:43Z
- **提交者**: @Liuzi134
- **评论数**: 1

## 标签

question

## 问题描述

### Motivation.

目前发现使能mindie_turbo后，使用torch_npu.profiler.profile采集profile，部分算子调用不能正确统计，希望mindie_turbo与性能采集工具可以相互适配。

### Proposed Change.

目前发现使能mindie_turbo后，使用torch_npu.profiler.profile采集profile，部分算子调用不能正确统计，希望mindie_turbo与性能采集工具可以相互适配。

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
