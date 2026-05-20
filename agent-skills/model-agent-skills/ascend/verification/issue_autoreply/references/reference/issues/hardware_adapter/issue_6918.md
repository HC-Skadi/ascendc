# Issue #6918: [misc] move mxfp_compat into device to decouple from quantization init chain

**类型**: Pull Request

## 问题背景

### What this PR does / why we need it?
`mxfp_compat` only provides dtype/symbol compatibility helpers for different `torch_npu` versions, but it was placed under `vllm_ascend.quantization`.   Importing it from device/ops paths could trigger `quantization/__init__.py` and pull in heavy quantization method dependencies, increasing startup coupling and causing import-cycle risk (especially on 310P paths).

### Does this PR introduce _any_ user-facing change?
No functional behavior change intended.

### How was this patch tested?
CI passed.

- vLLM version: v0.16.0
- vLLM main: https://github.com/vllm-project/vllm/commit/15d76f74e2fdb12a95ea00f0ca283acf6219a2b7


## 基本信息
- **编号**: #6918
- **作者**: linfeng-yuan
- **创建时间**: 2026-03-02T08:20:08Z
- **关闭时间**: 2026-03-02T10:17:01Z
- **标签**: module:ops, module:quantization

## 涉及版本
- vLLM: v0.16.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6918)
