# Issue #6468: [Kernel]: Optimize DispatchFFNCombine performance

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR focuses on performance optimization for the DispatchFFNCombine operator. The key optimizations include:

1. Improving communication efficiency by merging the transmission of tokens and scales;
2. Decoupling multi-core dependencies and reducing waiting bubbles in the combine process through tile-granularity communication;
3. Optimizing the full-card synchronization overhead before the umpermute operation.

These optimizations aim to reduce the overall execution latency of the DispatchFFNCombine operator and enhance the runtime performance of the model inference process on Ascend devices.

### Does this PR introduce _any_ user-facing change?

No. This PR only involves internal performance optimization of the DispatchFFNCombine operator and does not introduce any changes to user-facing APIs, interfaces, or behaviors.

### How was this patch tested?

1. Enable the DispatchFFNCombine operator by setting the environment variabl

## 基本信息
- **编号**: #6468
- **作者**: serlar
- **创建时间**: 2026-02-01T10:14:41Z
- **关闭时间**: 2026-02-09T08:30:35Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6468)
