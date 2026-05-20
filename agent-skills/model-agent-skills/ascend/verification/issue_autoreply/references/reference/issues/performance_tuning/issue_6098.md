# Issue #6098: [ops] support advanced apply_top_k_top_p without top_k constraint

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Implement `apply_top_k_top_p` via ascendC to eliminate the constraint of k [1,1024]. It enables high performance TopKTopP calculation and avoid D2H synchronization introduced by k validation.

### Does this PR introduce _any_ user-facing change?
No.

### How was this patch tested?
E2E serving with `k=4096` and  `p=0.95`
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6098
- **作者**: linfeng-yuan
- **创建时间**: 2026-01-21T10:32:19Z
- **关闭时间**: 2026-01-26T01:08:43Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6098)
