# Issue #5722: [P/D] layerwise connector supports DeepSeek-V3.2 sparse attention && Distribute transfer tasks to redundant kv_head cards

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Add new function to mooncake layerwise connector, including:
1. supports sparse attention, for DeepSeek-V3.2
2. Distribute transfer tasks to redundant kv_head cards

This PR is related to [[RFC]: CDCP Scheduling for Disaggregated Prefilling with KV Cache Layerwise Push Support](https://github.com/vllm-project/vllm-ascend/issues/4842)

### Does this PR introduce _any_ user-facing change?
No.

### How was this patch tested?
By CI.

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5722
- **作者**: nwpu-zxr
- **创建时间**: 2026-01-08T08:06:42Z
- **关闭时间**: 2026-01-10T15:04:17Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5722)
