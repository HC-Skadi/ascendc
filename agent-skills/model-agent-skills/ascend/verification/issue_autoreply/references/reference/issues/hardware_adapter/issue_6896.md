# Issue #6896: fix: adapt to upstream vLLM changes (2026-03-02)

**类型**: Pull Request

## 问题背景
## Summary
Fixes CI failures in schedule_test_vllm_main caused by upstream vLLM changes.

**Commit range:** `15d76f74e2fdb12a95ea00f0ca283acf6219a2b7`..`6290470843c131681e3e1318ae71070a34f33225`

### Issues Fixed

**Issue 1: CudagraphDispatcher.dispatch() 'disable_full' parameter removed**
- Upstream commit: `1d532f9d8fb2` - "[DP] Only use DP padding when cudagraphs are actually used (#34102)"
- Fix: Removed `disable_full` parameter from dispatch() calls in `vllm_ascend/worker/model_runner_v1.py`

**Issue 2: NoneType comparison in compilation_time aggregation**
- Upstream commit: `7b346ba8ed54` - "[Bugfix] Propagate compilation_time from workers to main process for TP>1 (#35503)"
- Status: Requires worker implementation changes (not included in this PR - needs further investigation)

**Issue 3: MMEncoderAttention 'sequence_lengths' parameter added**
- Upstream commit: `9c3fe9936b92` - "Flashinfer cuDNN backend for Qwen3 VL ViT attention (#34580)"
- Fix: Added `sequence_lengths=None` pa

## 基本信息
- **编号**: #6896
- **作者**: Meihan-chen
- **创建时间**: 2026-03-02T02:11:20Z
- **关闭时间**: 2026-03-02T02:28:23Z
- **标签**: documentation, module:ops, module:core

## 涉及版本
- vLLM: v0.16.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6896)
