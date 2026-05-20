# Issue #6849: [300I] support decode-only aclgraph mode

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
310p aclgraph mode, but has some problems:
- the event-id hardware limit, the num of graph will be limited.
- the cann version support this feature cannot be get from external of huawei.
### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?
local test
- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/83b47f67b1dfad505606070ae4d9f83e50ad4ebd


## 基本信息
- **编号**: #6849
- **作者**: Tflowers-0129
- **创建时间**: 2026-02-27T07:40:36Z
- **关闭时间**: 2026-03-02T06:15:15Z
- **标签**: module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6849)
