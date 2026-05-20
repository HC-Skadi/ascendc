# Issue #5990: 【feat】switch gmmswigluquant fusion ops

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Set a additional config parameter to control whether the gmmswigluequant fuseion operator is enabled; it is enabled by True. / When enabled with a small number of GPUs, the gmmswigluquant fused operator can cause some performance degradation.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060


## 基本信息
- **编号**: #5990
- **作者**: aipaes
- **创建时间**: 2026-01-19T03:58:41Z
- **关闭时间**: 2026-01-19T05:06:08Z
- **标签**: module:tests, module:ops, module:core

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5990)
