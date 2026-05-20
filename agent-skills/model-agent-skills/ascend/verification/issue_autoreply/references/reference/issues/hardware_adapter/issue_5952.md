# Issue #5952: Default enable MLAPO for deepseek W8A8 models

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1) Default enable MLAPO for deepseek MLA Attention W8A8 models on PD disagregation D Instance, for example: DeepSeekV3-W8A8,  DeepSeek-R1-W8A8.
2) Default enable MLAPO for DeepSeek SFA Attention W8A8 models, currently is DeepSeek-V3.2-W8A8.

### Does this PR introduce _any_ user-facing change?
Don't need use manully to VLLM_ASCEND_ENABLE_MLAPO=1, to enable MLAPO feature for deepseek w8a8 model

### How was this patch tested?
<img width="1265" height="378" alt="image" src="https://github.com/user-attachments/assets/a35c7522-b31b-44f1-ac95-b52aad9c9300" />

The effect of enabling MLAPO SFA model deployed on a single A3 Node:
Test with:tests/e2e/nightly/single_node/models/test_deepseek_v3_2_exp_w8a8.py
dataset: gsm8k-lite，without set MTP, FULL GRAPH, has 19% promote：
未默认开启 MLAPO 时：
├─────────────────────────┤
│                TTFT                      │ 14055.8836 ms   │
├─────────────────────────┤
│                ITL              

## 基本信息
- **编号**: #5952
- **作者**: leo-pony
- **创建时间**: 2026-01-16T07:21:20Z
- **关闭时间**: 2026-01-22T01:26:39Z
- **标签**: documentation, module:tests, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5952)
