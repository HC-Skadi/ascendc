# Issue #524: [Feature]: Supporting W8A16 and W4A16 weight-only quantization

## 基本信息

- **编号**: #524
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/524
- **创建时间**: 2025-04-14T14:48:09Z
- **关闭时间**: 2026-01-04T02:13:45Z
- **更新时间**: 2026-01-04T02:13:45Z
- **提交者**: @learning-chip
- **评论数**: 4

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch

**Purpose**: Int8 weight-only quant can squeeze `DeepSeek-V2-Lite-chat` to just 16 GB, fitting into one 910B4 device, very useful for daily development. Because MoE inference is too memory-bound, W8A16 can be as efficient as W8A8 in theory, as proved by the [MARLIN paper](https://dl.acm.org/doi/10.1145/3710848.3710871).

**GPU equivalent**: Corresponding to vLLM GPU's [GPTQModel backend](https://docs.vllm.ai/en/latest/features/quantization/gptqmodel.html) or [AutoAWQ backend](https://docs.vllm.ai/en/latest/features/quantization/auto_awq.html).

## Code changes needed

The [`torch_npu.npu_grouped_matmul`](https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/apilist/ptaoplist_000504.html) takes torch.int8 weights and additional `antiquant_scale` parameter for fused dequant + matmul. 

The MoE adaptor already uses `npu_grouped_matmul`, just need to take the extra `antiquant_scale`:

https://github.com/vllm-project/vllm-ascend/blob/5fa70b63939062e5f2656eda356d4dff9a3be30b/vllm_ascend/ops/fused_moe.py#L124-L131

On GPU the equivalent kernel is the fused dequant + matmul Marlin kernel, but still a bug for v2-lite's shape: https://github.com/vllm-project/vllm/issues/7075

## Obtain model weights

DeepSeek-V2 w8a16 script available [in msmodelslim](https://gitee.com/ascend/msit/blob/master/msmodelslim/example/DeepSeek/README.md#deepseek-v2-w8a16%E9%87%8F%E5%8C%96) (runs on CPU)

Or using [GPTQModel package on DeepSeek](https://github.com/ModelCloud/GPTQModel?tab=readme-ov-file#model-support) (runs on GPU)
