# Issue #6645: [Feature][Quant] Auto-detect quantization format from model files

**类型**: Pull Request

## 问题背景
## Summary

- Add automatic quantization format detection, eliminating the need to manually specify `--quantization` when serving quantized models.
- The detection inspects only lightweight JSON files (`quant_model_description.json` and `config.json`) at engine initialization time, with no `.safetensors` reads.
- User-explicit `--quantization` flags are always respected; auto-detection only applies when the flag is omitted.

## Details

**Detection priority:**
1. `quant_model_description.json` exists → `quantization="ascend"` (ModelSlim)
2. `config.json` contains `"quant_method": "compressed-tensors"` → `quantization="compressed-tensors"` (LLM-Compressor)
3. Neither → default float behavior

**Technical approach:**
Hooked into `NPUPlatform.check_and_update_config()` to run detection after `VllmConfig.__post_init__`. Since `quant_config` is already `None` at that point, we explicitly recreate it via `VllmConfig._get_quantization_config()` to trigger the full quantization i

## 基本信息
- **编号**: #6645
- **作者**: SlightwindSec
- **创建时间**: 2026-02-09T14:28:24Z
- **关闭时间**: 2026-02-26T02:59:25Z
- **标签**: module:tests, module:core, module:quantization, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6645)
