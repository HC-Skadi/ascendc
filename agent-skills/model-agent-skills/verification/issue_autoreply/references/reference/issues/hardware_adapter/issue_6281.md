# Issue #6281: [Misc][v0.13.0]Removes unnecessary graph size re-initialization

**类型**: Pull Request

## 问题背景
<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
Cherry-pick from #6280 .
This PR removes `update_default_aclgraph_sizes`. In earlier versions, we add this function to change default `cudagraph_capture_sizes`  because `_npu_paged_attention` degrades significantly on certain shapes (which is included in default `cudagraph_capture_sizes` of VLLM). Now since we use FIA as default attention op (which does not contain such performance degradation), there is no need to add this default change. Otherwise, it could cause some conflicts if we set a small `cudagraph_capture_sizes` that  < 20 now.

### Does this PR introduce _any_ user-facing change?
<!--
Note that it means *any* user-facing change including all aspects such as API, interface or other behavior changes.
Documentation-only updates are not considered user-facing changes.
-->

### How was this 

## 基本信息
- **编号**: #6281
- **作者**: Angazenn
- **创建时间**: 2026-01-26T13:01:06Z
- **关闭时间**: 2026-01-27T06:38:16Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6281)
