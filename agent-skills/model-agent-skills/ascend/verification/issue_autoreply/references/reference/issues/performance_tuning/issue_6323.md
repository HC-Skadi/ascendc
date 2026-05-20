# Issue #6323: [Doc] Contributing a Benchmark Tutorial for Suffix Speculative Decoding

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Suffix Decoding is a CPU-based speculative decoding optimization that accelerates inference by pattern matching and frequency-based prediction from both prompts and generated content. 

This document provides a step-by-step guide for deploying and evaluating **Suffix Speculative Decoding** on the **Ascend** platform. By analyzing performance gains across diverse datasets, it demonstrates the significant advantages of this technology in inference acceleration. Our goal is to empower developers to achieve high-efficiency model optimization using Ascend hardware.
### Does this PR introduce _any_ user-facing change?
NO
### How was this patch tested?
vLLM version: release/v0.13.0
vLLM main: https://github.com/vllm-project/vllm/commit/58996f3589434d99c320e6ee2460a231135f9641
- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6323
- **作者**: zhangguinan
- **创建时间**: 2026-01-27T12:47:43Z
- **关闭时间**: 2026-02-03T06:52:38Z
- **标签**: documentation

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6323)
