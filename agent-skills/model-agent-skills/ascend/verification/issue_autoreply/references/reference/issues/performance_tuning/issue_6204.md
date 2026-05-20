# Issue #6204: [MM][Perf] Parallelize Q/K/V padding in AscendMMEncoderAttention for better performance

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Currently, we pad the last dim of qkv to 128 before flash attention (in `AscendMMEncoderAttention`) to get better performance on Ascend NPU. However, the qkv padding is executed serially, which may lead to more overhead when launching `aclnnConstantPadNd` (launch 3 times).

Since the three operations are mutually independent, we stack qkv first and then pad them in one kernel launch. With this optimization, **TTFT** has been reduced by **3.15%**, **peak throughput** has been increased by **4.20%**.

---
**Before this PR:**

<img width="2328" height="842" alt="before_1" src="https://github.com/user-attachments/assets/b9de56b7-7489-4523-a21f-d9ec2f441e17" />

<img width="2326" height="726" alt="before_2" src="https://github.com/user-attachments/assets/046896ab-c60c-42ed-a4cb-8a6cb2c57ae7" />

---
**After this PR:**

<img width="2266" height="725" alt="after" src="https://github.com/user-attachments/assets/a0cc5d28-05d9-40f0-a95f-0e

## 基本信息
- **编号**: #6204
- **作者**: shen-shanshan
- **创建时间**: 2026-01-23T09:32:19Z
- **关闭时间**: 2026-01-26T02:20:24Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6204)
