# Issue #5668: Add Medusa speculative decoding support for vllm_ascend

**类型**: Pull Request

## 问题背景

### What this PR does / why we need it?
`vllm_ascend` already supports several speculative decoding strategies such as MTP, EAGLE, N-gram, and suffix decoding. However, Medusa is not yet supported. Medusa is an efficient speculative decoding framework that leverages a lightweight draft model to propose multiple tokens in a single step, which can significantly improve decoding throughput and reduce latency.

To enable Medusa-based speculative decoding on Ascend hardware and provide more decoding options for users, this PR adds Medusa support into the `vllm_ascend` speculative decoding pipeline.

### Does this PR introduce _any_ user-facing change?

This PR introduces Medusa speculative decoding as an additional speculative decoding method:

✔ Adds `MedusaProposer` and integrates it into the speculative decoding registry
✔ Extends `SpecDcodeType` with a `MEDUSA` enum entry
✔ Updates `NPUModelRunner` to recognize and invoke Medusa during decoding
✔ Adds Medusa-specific handl

## 基本信息
- **编号**: #5668
- **作者**: simplzyu
- **创建时间**: 2026-01-06T13:52:31Z
- **关闭时间**: 2026-01-23T06:14:23Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5668)
