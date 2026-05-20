# Issue #6454: [Feat.]: support 310p w8a8

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Introduced 310P W8A8 Quantization Support: New modules and methods have been added to enable W8A8 static quantization specifically for the Ascend 310P platform.
Platform-Specific Quantization Configuration Loading: The system now dynamically loads the appropriate quantization configurations (AscendCompressedTensorsConfig, AscendModelSlimConfig) based on whether the current hardware is an Ascend 310P device.
Implemented AscendW8A8LinearMethod310P: A dedicated linear quantization method for 310P is provided, handling the specifics of weight and activation quantization, including input parameter broadcasting and weight data manipulation.
Extended AscendModelSlimConfig for 310P: A specialized configuration class for 310P integrates the new W8A8 linear method for both standard linear layers and vocabulary parallel embeddings, ensuring proper quantization application.
### Does this PR introduce _any_ user-facing change?

### How was this patch t

## 基本信息
- **编号**: #6454
- **作者**: Tflowers-0129
- **创建时间**: 2026-01-31T03:53:38Z
- **关闭时间**: 2026-02-03T06:13:07Z
- **标签**: module:core

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6454)
