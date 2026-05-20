# Issue #6648: [main][Quant] Remove unused rotation functions and parameters from W4A4 LAOS quantization

**类型**: Pull Request

## 问题背景
## Summary
- Remove unused `set_rotation_config` and `apply_rotation` methods from `AscendW4A4LaosDynamicLinearMethod`
- Remove unused `rotation_type` field and associated conditional quantization parameters (`heads_rotation`, `kronecker_rotation_n`, `kronecker_rotation_m`)

These rotation-related functions and parameters are never called in the current W4A4 LAOS dynamic quantization workflow. 

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d7e17aaacd5ed1b4b4be6bcfef3a1b7cbc84fc9a


## 基本信息
- **编号**: #6648
- **作者**: SlightwindSec
- **创建时间**: 2026-02-10T01:50:28Z
- **关闭时间**: 2026-02-11T08:38:46Z
- **标签**: module:quantization, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6648)
