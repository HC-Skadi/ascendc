# Issue #6705: [Feat.][310P]: weightNZ feature with quant or unquant.

**类型**: Pull Request

## 问题背景
NZ Format Support for Linear Layers: Implemented support for the NZ (N-dimensional Z-order) format for linear layer weights on Ascend 310P, enhancing performance for both quantized and unquantized layers.
Unquantized Linear Method for Ascend 310P: Introduced AscendUnquantizedLinearMethod310 to specifically handle and apply NZ format casting to unquantized linear layer weights during the loading process.
MRotaryEmbedding Integration: Extended Rotary Embedding support by adding AscendMRotaryEmbedding310 to provide an Ascend-specific implementation for MRotaryEmbedding.
Quantization Method Updates: Updated the w8a8_static quantization method to directly transpose weights and apply NZ format casting, ensuring consistency with the new format.
- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/9562912cead1f11e8540fb91306c5cbda66f0007


## 基本信息
- **编号**: #6705
- **作者**: Tflowers-0129
- **创建时间**: 2026-02-11T12:26:11Z
- **关闭时间**: 2026-02-13T07:41:03Z
- **标签**: module:tests, module:core

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6705)
