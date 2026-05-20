# Issue #5857: [P/D] [cherry-pick] fix layerwise connector for decoder tp size > num kv head (#5431)

**类型**: Pull Request

## 问题背景

### What this PR does / why we need it?
Fix layerwise connector for decoder tp size > num kv heads. In this case prefiller should push kv cache to all decoder npu.

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d

### What this PR does / why we need it?

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?



## 基本信息
- **编号**: #5857
- **作者**: liziyu179
- **创建时间**: 2026-01-13T09:54:32Z
- **关闭时间**: 2026-01-13T11:27:14Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5857)
