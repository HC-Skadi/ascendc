# Issue #2819: [Bug]: vllm==v0.7.3使用昇腾量化版本，vllm serve --quantization ascend没有这个选项

## 基本信息

- **编号**: #2819
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2819
- **创建时间**: 2025-09-09T05:26:57Z
- **关闭时间**: 2025-11-11T13:16:04Z
- **更新时间**: 2025-11-11T13:16:04Z
- **提交者**: @wangyinchen-hub
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

为什么pip install vllm==v0.7.3
pip install vllm-ascend==v0.7.3.post1
，这样使用vllm serve --quantization ascend，是没有这个选项的。这么修复呢


### 🐛 Describe the bug

root@autodl-container-33ab4e930e-bf8c0fa8:~/autodl-tmp# vllm serve /root/autodl-tmp/qwen72bw8a8  \     --tensor-parallel-size 1 \     --served-model-name "qwq-7b-w8a8" \     --max-model-len 4096 \     --quantization ascend
INFO 09-09 13:13:55 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 09-09 13:13:55 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 09-09 13:13:55 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 09-09 13:13:55 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 09-09 13:13:55 __init__.py:44] plugin ascend loaded.
INFO 09-09 13:13:55 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 09-09 13:13:55 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 09-09 13:13:55 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 09-09 13:13:55 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 09-09 13:13:55 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 09-09 13:13:55 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 09-09 13:13:55 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 09-09 13:13:55 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 09-09 13:13:55 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 09-09 13:13:55 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 09-09 13:13:55 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 09-09 13:13:55 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
usage: vllm serve <model_tag> [options]
vllm serve: error: argument --quantization/-q: invalid choice: 'ascend' (choose from 'aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'ptpc_fp8', 'fbgemm_fp8', 'modelopt', 'marlin', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'awq_marlin', 'gptq', 'compressed-tensors', 'bitsandbytes', 'qqq', 'hqq', 'experts_int8', 'neuron_quant', 'ipex', 'quark', 'moe_wna16', None)
