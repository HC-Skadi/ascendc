# Issue #6023: [Lint]Style: Convert `vllm-ascend/` to ruff format(Batch #7)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
**Scope of Changes**:
| File Path |
| :--- |
|` vllm_ascend/quantization/compressed_tensors/compressed_tensors.py`|
|` vllm_ascend/quantization/quant_config.py`|
|` vllm_ascend/quantization/utils.py`|
|` vllm_ascend/quantization/w4a16.py`|
|` vllm_ascend/quantization/w4a4_flatquant_dynamic.py`|
|` vllm_ascend/quantization/w4a8_dynamic.py`|
|` vllm_ascend/quantization/w8a16.py`|
|` vllm_ascend/quantization/w8a8.py`|
|` vllm_ascend/quantization/w8a8_dynamic.py`|
|` vllm_ascend/quantization/w8a8_pdmix.py`|
|` vllm_ascend/quantization/w8a8mxfp8.py`|
|` vllm_ascend/sample/rejection_sampler.py`|
|` vllm_ascend/sample/sampler.py`|
|` vllm_ascend/worker/block_table.py`|

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2c24bc6996cb165fce92f780b388a5e39b3f4060


## 基本信息
- **编号**: #6023
- **作者**: MrZ20
- **创建时间**: 2026-01-20T03:19:45Z
- **关闭时间**: 2026-02-06T06:56:53Z
- **标签**: module:quantization

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6023)
