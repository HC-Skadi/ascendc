# Issue #6254: [Tests] Fix qwen3 performance test

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Unlimited request rate, achieving high concurrency of 40, fixes https://github.com/vllm-project/vllm-ascend/actions/runs/21327913593/job/61388195448

### Does this PR introduce _any_ user-facing change?
N/A

### How was this patch tested?
CI passed with new added/existing test.

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6254
- **作者**: wxsIcey
- **创建时间**: 2026-01-26T05:02:32Z
- **关闭时间**: 2026-01-29T03:29:22Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6254)
