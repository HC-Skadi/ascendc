# Issue #6635: [main][Quantization][DFX] Add friendly error checks for quantization and weight dtype mismatch

**类型**: Pull Request

## 问题背景
**Description**
This PR introduces input validation to detect mismatches between the `--quantization ascend` flag and the actual model weight data type.
**Motivation**
Currently, if users misconfigure the quantization settings (e.g., using `--quantization ascend` with FP16 weights, or vice versa), the backend throws obscure errors that are difficult to debug.
**Changes**
* Added a check to ensure quantized weights are loaded when quantization is enabled.
* Added a check to ensure floating-point weights are used when quantization is disabled.
* Raise a helpful `ValueError` with clear instructions instead of letting the process crash with internal errors.
- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d7e17aaacd5ed1b4b4be6bcfef3a1b7cbc84fc9a


## 基本信息
- **编号**: #6635
- **作者**: SlightwindSec
- **创建时间**: 2026-02-09T08:45:57Z
- **关闭时间**: 2026-02-09T14:14:19Z
- **标签**: module:tests, module:quantization

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6635)
