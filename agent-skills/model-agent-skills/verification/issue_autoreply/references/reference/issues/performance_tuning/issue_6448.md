# Issue #6448: [MM][Perf] Use `seq_lens` CPU cache to avoid frequent d2h copy for better performance

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Currently, the performance of multi-modal encoding (i.e., `AscendMMEncoderAttention` forward) is considerably bounded by the heavy host pre-process operations.

We can see from the profiling results below, before the real computation of Attention, there are long free time in the device, which will lead to extremely low NPU utilization.

<img width="2264" height="1398" alt="iShot_2026-01-23_16 26 39" src="https://github.com/user-attachments/assets/37f21d06-e526-4f28-82fe-005746cf13bd" />

---
**To opitimize this, this PR has proposed four changes:**

1. Use `seq_lens` CPU cache to avoid frequent d2h copy. Before this PR, `AscendMMEncoderAttention` will copy the `cu_seqlens` from NPU to CPU in every forward, since the op `_npu_flash_attention_unpad()` requires CPU `cu_seqlens` (otherwise it will crash). Thus, we use `seq_lens_cpu_cache` to cache this tensor, since it's shared between all layers, but may change in different forward step.

## 基本信息
- **编号**: #6448
- **作者**: shen-shanshan
- **创建时间**: 2026-01-31T02:13:49Z
- **关闭时间**: 2026-02-26T00:49:36Z
- **标签**: module:ops, ready, ready-for-test, module:multimodal

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6448)
