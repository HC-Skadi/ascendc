# Issue #5626: [Fix] Fixes speculative decode indexing and unpad condition for attention metadata

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This addresses the issue brought up by #5356 and #4963, and we believe the unnecessary conditions are the root cause.

Change the unpad trigger to be driven by actual size mismatches (num_reqs vs base_num_reqs or scheduled vs input token counts) rather than specific speculative-method flags. Then remove brittle workarounds that forced request counts and sliced query start locations.

This prevents incorrect indexing and length mismatches during speculative decoding and makes metadata unpadding more robust across scheduling modes.

### Does this PR introduce _any_ user-facing change?
None.

### How was this patch tested?
Tested by existing cases.

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/8be6432bdaf6275664d857b1e5e9bf8ed1ce299e


## 基本信息
- **编号**: #5626
- **作者**: yiz-liu
- **创建时间**: 2026-01-06T03:16:48Z
- **关闭时间**: 2026-01-08T11:41:09Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5626)
