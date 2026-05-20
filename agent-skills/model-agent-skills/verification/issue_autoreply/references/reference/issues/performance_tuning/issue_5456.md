# Issue #5456: [Performance] MLA prefill preformance optimization

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Since the _npu_ring_mla operator deteriorates in long-sequencescenarios, the long sequence is split into shorter sequences for input to improve performance.
Related RFC：https://github.com/vllm-project/vllm-ascend/issues/5449
This proposal is a modification based on the aforementioned RFC
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/5326c89803566a131c928f7fdd2100b75c981a42


## 基本信息
- **编号**: #5456
- **作者**: pichangping
- **创建时间**: 2025-12-29T01:49:55Z
- **关闭时间**: 2026-01-05T03:41:59Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5456)
