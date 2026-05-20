# Issue #5516: [Bugfix] record cos and sin cache in AscendRotaryEmbedding

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

In scenarios where models like [Moonlight](https://modelscope.cn/models/moonshotai/Moonlight-16B-A3B-Instruct) (using MLA but without `rope_scaling` in config.json) invoke `AscendRotaryEmbedding`. `_cos_cache` and `_sin_cache` are not recorded correctly.

<img width="2880" height="840" alt="image" src="https://github.com/user-attachments/assets/af8d02ba-29e2-4c7f-a662-8b9c9c513ffd" />

### Does this PR introduce _any_ user-facing change?

No

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/45c1ca1ca1ee8fa06df263c8715e8a412ff408d4


## 基本信息
- **编号**: #5516
- **作者**: Debonex
- **创建时间**: 2025-12-30T07:58:37Z
- **关闭时间**: 2026-01-05T12:12:41Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5516)
