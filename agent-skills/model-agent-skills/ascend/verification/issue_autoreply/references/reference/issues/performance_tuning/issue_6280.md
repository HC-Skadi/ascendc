# Issue #6280: [Misc] Removes unnecessary graph size re-initialization

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR removes `update_default_aclgraph_sizes`. In earlier versions, we add this function to change default `cudagraph_capture_sizes`  because `_npu_paged_attention` degrades significantly on certain shapes (which is included in default `cudagraph_capture_sizes` of VLLM). Now since we use FIA as default attention op (which does not contain such performance degradation), there is no need to add this default change. Otherwise, it could cause some conflicts if we set a small `cudagraph_capture_sizes` that  < 20 now.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6280
- **作者**: Angazenn
- **创建时间**: 2026-01-26T12:59:39Z
- **关闭时间**: 2026-01-27T06:38:07Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6280)
