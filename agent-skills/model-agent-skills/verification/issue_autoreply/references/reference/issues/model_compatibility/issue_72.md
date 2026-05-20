# Issue #72: [New Model]: DeepSeek V3 / R1

## 基本信息

- **编号**: #72
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/72
- **创建时间**: 2025-02-17T07:48:09Z
- **关闭时间**: 2025-03-31T06:54:43Z
- **更新时间**: 2025-03-31T06:54:54Z
- **提交者**: @Yikun
- **评论数**: 14

## 标签

new model

## 问题描述

This issue tracks initial support for the Deepseek V3 model with vllm-ascend:

https://huggingface.co/deepseek-ai/DeepSeek-R1
https://huggingface.co/deepseek-ai/DeepSeek-V3

Support Progress
------

**update (2025.03.07):  the DeepSeek V3 / R1 supported!** DeepSeek V3 / R1现已支持：
Please try v0.7.3-dev 请参考文档:
https://vllm-ascend.readthedocs.io/en/v0.7.3-dev/tutorials.html#online-serving-on-multi-machine

CANN version dependency resolved by https://github.com/vllm-project/vllm-ascend/pull/242

------

**update (2025.03.05) we are still waiting for  CANN 8.1.RC1.alpha001 release.**: https://www.hiascend.com/zh/developer/download/community/result?module=cann

------

 **update (2025.02.22) DeepSeek V3 / R1 support will be ready in next RC release of vLLM Ascend (v0.7.3rc1) in the early of 2025.03**

Known issue will be fixed in vllm-ascend v0.7.3rc1 (March. 2025) with CANN 8.1.RC1.alpha001 (March. 2025): 
- `AssertionError: Torch not compiled with CUDA enabled` 

  Issue link: https://github.com/vllm-project/vllm-ascend/issues/122#issuecomment-2673250779 

  Workaround: This is because in the code of the vllm community, specifically in the file vllm/vllm/model_executor/layers/rotary_embedding.py, the device is hard-coded as 'cuda'. We can choose to manually replace these occurrences of 'cuda' with 'npu' or add "from torch_npu.contrib import transfer_to_npu" at the beginning of the script.
  Fixed by:
  - vLLM PR (work in v0.7.4): https://github.com/vllm-project/vllm/pull/13658
  - vLLM Ascend workarouind PR (work in v0.7.3-dev): https://github.com/vllm-project/vllm-ascend/pull/228

- w8a8 quantization is unspported yet
  `ValueError: Unknown quantization method: ascend. Must be one of ['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'fbgemm_fp8', 'modelopt', 'marlin', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'awq_marlin', 'gptq', 'compressed-tensors', 'bitsandbytes', 'qqq', 'hqq', 'experts_int8', 'neuron_quant', 'ipex', 'quark', 'moe_wna16'].`

  Issue Link: https://github.com/vllm-project/vllm-ascend/issues/119

  Workaround:  don't use quantization, and wait for next final release (late of 2025.03)

- Quantization is unspported yet
  `KeyError: 'model.layers.0.self_attn.q_a_proj.weight'`
  issue: https://github.com/vllm-project/vllm-ascend/issues/122#issuecomment-2671040954
  Wrokaround: Remove https://huggingface.co/deepseek-ai/DeepSeek-R1/blob/main/config.json#L39-L47

- `RuntimeError: GroupTopkOperation CreateOperation failed`

  Workaround: This is caused by the inner ops in CANN, will fixed in next RC release of vLLM Ascend (v0.7.3rc1) in the early of 2025.03. Need bump CANN version to CANN 8.1.RC1.alpha001 (will public publish at the ~end of Feb. 2025~ March.2025)
  
  Will be fixed by: https://github.com/vllm-project/vllm-ascend/issues/142

  Workaround: https://github.com/vllm-project/vllm-ascend/pull/242

------

update (2025.02.19): https://github.com/vllm-project/vllm-ascend/pull/88 merged to v0.7.1-dev, DeepSeek test passed (via DeepSeek-V2-Lite),  V3 arch same as V2 should also work, will backport to main soon.

For v0.7.1-dev: https://github.com/vllm-project/vllm-ascend/pull/68 https://github.com/vllm-project/vllm-ascend/pull/88

Here is the note for DeepSeek-V2-Lite deploy: https://vllm-ascend.readthedocs.io/en/latest/tutorials.html#online-serving-on-multi-machine
