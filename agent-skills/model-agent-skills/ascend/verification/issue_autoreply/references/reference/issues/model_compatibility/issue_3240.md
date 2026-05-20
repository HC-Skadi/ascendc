# Issue #3240: [Misc]: e2e CI missing comprehensive LoRA tests about `LogitsProcessorWithLoRA`

## 基本信息

- **编号**: #3240
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3240
- **创建时间**: 2025-09-28T09:23:08Z
- **关闭时间**: 2025-10-31T06:12:07Z
- **更新时间**: 2025-10-31T06:12:07Z
- **提交者**: @slippersss
- **评论数**: 0

## 标签

无

## 问题描述

### e2e CI missing comprehensive LoRA tests about `LogitsProcessorWithLoRA`

The LoRA-related tests, e.g., test_ilama_lora.py and test_ilama_lora_tp2.py, use ilama-3.2-1B, and this model is regarded as `TransformersForCausalLM`, where `embedding_modules` attribute lacks `lm_head`. However, `LlamaForCausalLM` and most other models include both `embed_tokens` and `lm_head` in `embedding_modules`. This attribute contributes to `supported_lora_modules` when using LoRA in vllm. Therefore, without `lm_head` in `embedding_modules`, current tests using ilama-3.2-1B are unable to find the abve errors since `LogitsProcessorWithLoRA` replacing `lm_head` is skipped. It's necessary to add more comprehensive tests for LoRA.

