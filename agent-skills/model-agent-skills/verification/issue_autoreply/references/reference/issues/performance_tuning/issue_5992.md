# Issue #5992: 【feat】switch for fusion ops gmmswigluquant

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Set a additional config parameter to control whether the gmmswigluequant fuseion operator is enabled; it is enabled by True. / When enabled with a small number of GPUs, the gmmswigluquant fused operator can cause some performance degradation.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060

#### Perf

test model: GLM 4.6(w8a8)
- single A3 node(ep16, tp16),  async-scheduling, mtp, FULL_DECODE_ONLY
- bs=1, input_lens=32000, ouput_lens=1024

Without this PR: TPOT 32.22.ms
With this PR: TPOT 30.23ms


## 基本信息
- **编号**: #5992
- **作者**: aipaes
- **创建时间**: 2026-01-19T05:02:50Z
- **关闭时间**: 2026-01-19T13:19:25Z
- **标签**: module:tests, module:ops, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5992)
