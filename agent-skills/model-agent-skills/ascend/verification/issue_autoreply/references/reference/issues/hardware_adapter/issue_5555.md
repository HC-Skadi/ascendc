# Issue #5555: [Refactor] Modify the binding logic to allocate CPU cores for each NPU card

**类型**: Pull Request

## 问题背景
[Refactor] Modify the binding logic to allocate CPU cores for each NPU card

### What this PR does / why we need it?
Modify the binding logic to allocate CPU cores for each NPU card based on NUMA affinity, while isolating acl_thread/release_thread and other processes to prevent mutual interference.

### Does this PR introduce _any_ user-facing change?
No

### How was this patch tested?
https://github.com/Rozwel-dx/vllm-ascend/commit/c85cc045f893293e3b44e24d2e1f01ddc5849ea8

Signed-off-by: rowzwel_dx <1392851715@qq.com>
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/7157596103666ee7ccb7008acee8bff8a8ff1731


## 基本信息
- **编号**: #5555
- **作者**: Rozwel-dx
- **创建时间**: 2025-12-31T07:17:17Z
- **关闭时间**: 2026-01-13T01:21:28Z
- **标签**: module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5555)
