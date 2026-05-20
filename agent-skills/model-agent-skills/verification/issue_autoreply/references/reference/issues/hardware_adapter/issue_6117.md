# Issue #6117: [Refact.]: refactoring for 310p kvcache and some ops class

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
* Refactor the LayerNorm and activation operator classes to decouple the 310P device implementation from the main branch.
* Refactor `mm_encoder_attention` on 310P to use the `torch_npu._npu_flash_attention_unpad` operator.
* Refactor the QKV inputs in the prefill stage of `attention_v1` on 310P so they are no longer padded to 16× alignment.
* Refactor `model_runner` on 310P to align the KV-cache initialization logic with the mainline implementation.

### Does this PR introduce _any_ user-facing change?
NO

### How was this patch tested?
use the e2e tests.

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d68209402ddab3f54a09bc1f4de9a9495a283b60


## 基本信息
- **编号**: #6117
- **作者**: Tflowers-0129
- **创建时间**: 2026-01-22T03:48:30Z
- **关闭时间**: 2026-01-24T12:34:29Z
- **标签**: module:ops, module:core

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6117)
