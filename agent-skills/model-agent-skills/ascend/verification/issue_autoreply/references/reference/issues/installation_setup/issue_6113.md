# Issue #6113: [Bugfix]KV pool rank 0 consumes more HBM

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

before add_set_deivce
<img width="2354" height="674" alt="image" src="https://github.com/user-attachments/assets/8b81ab5f-b9ba-4fd2-8546-8f36ac15d32b" />
after
<img width="1044" height="156" alt="image" src="https://github.com/user-attachments/assets/996d845a-8abd-4aae-b894-4a9832b1f742" />

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6113
- **作者**: baxingpiaochong
- **创建时间**: 2026-01-22T03:12:33Z
- **关闭时间**: 2026-01-23T11:47:33Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6113)
