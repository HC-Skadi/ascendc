# Issue #1768: [Usage]: 是否支持ZhipuAI/GLM-4.1V-9B-Thinking

## 基本信息

- **编号**: #1768
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1768
- **创建时间**: 2025-07-14T03:09:05Z
- **关闭时间**: 2025-07-16T08:24:57Z
- **更新时间**: 2025-10-11T09:48:19Z
- **提交者**: @Chenhb123
- **评论数**: 4

## 标签

无

## 问题描述

### Your current environment

```text
您好，跟您确认下现在是否支持在910B上运行ZhipuAI/GLM-4.1V-9B-Thinking模型。
我使用最新镜像：quay.nju.edu.cn/ascend/vllm-ascend:v0.9.2rc1
运行命令如下：
```
```bash
export IMAGE=quay.nju.edu.cn/ascend/vllm-ascend:v0.9.2rc1
docker run --rm \
--name vllm-ascend \
--device /dev/davinci2 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /data/ZhipuAI:/data/ZhipuAI \
-p 8000:8000 \
-e VLLM_USE_MODELSCOPE=True \
-e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 \
-it $IMAGE bash

npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 85.1        62                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2843 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+

pip install --upgrade transformers

MODEL_NAME="/data/ZhipuAI/GLM-4___1V-9B-Thinking"
vllm serve $MODEL_NAME --limit-mm-per-prompt '{"image":32}'   --allowed-local-media-path /
```

输出报错信息：
```bash
INFO 07-14 02:51:15 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-14 02:51:15 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-14 02:51:15 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-14 02:51:15 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-14 02:51:16 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-14 02:51:19 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-14 02:51:20 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-14 02:51:20 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-14 02:51:20 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-14 02:51:20 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-14 02:51:20 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-14 02:51:20 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-14 02:51:21 [api_server.py:1395] vLLM API server version 0.9.2
INFO 07-14 02:51:21 [cli_args.py:325] non-default args: {'model': '/data/ZhipuAI/GLM-4___1V-9B-Thinking', 'allowed_local_media_path': '/', 'limit_mm_per_prompt': {'image': 32}}
INFO 07-14 02:51:33 [config.py:841] This model supports multiple tasks: {'generate', 'embed', 'classify', 'reward'}. Defaulting to 'generate'.
INFO 07-14 02:51:33 [config.py:1472] Using max model len 65536
INFO 07-14 02:51:33 [config.py:2285] Chunked prefill is enabled with max_num_batched_tokens=2048.
WARNING 07-14 02:51:33 [ascend_config.py:168] ACL Graph is currently experimental. Please raise an issue on https://github.com/vllm-project/vllm-ascend/issues if you encourage any Error
INFO 07-14 02:51:33 [platform.py:174] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 07-14 02:51:33 [utils.py:321] Calculated maximum supported batch sizes for ACL graph: 46
INFO 07-14 02:51:33 [utils.py:336] Adjusted ACL graph batch sizes for Glm4vForConditionalGeneration model (layers: 40): 67 → 46 sizes
INFO 07-14 02:51:41 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-14 02:51:41 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-14 02:51:41 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-14 02:51:41 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-14 02:51:43 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-14 02:51:45 [core.py:526] Waiting for init message from front-end.
INFO 07-14 02:51:46 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-14 02:51:46 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-14 02:51:46 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-14 02:51:46 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-14 02:51:46 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-14 02:51:46 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-14 02:51:46 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-14 02:51:46 [core.py:69] Initializing a V1 LLM engine (v0.9.2) with config: model='/data/ZhipuAI/GLM-4___1V-9B-Thinking', speculative_config=None, tokenizer='/data/ZhipuAI/GLM-4___1V-9B-Thinking', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=65536, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/data/ZhipuAI/GLM-4___1V-9B-Thinking, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,488,480,464,456,440,432,416,408,392,384,368,360,344,336,328,312,304,288,280,264,256,240,232,216,208,192,184,168,160,152,136,128,112,104,88,80,64,56,40,32,16,8,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":512,"local_cache_dir":null}
INFO 07-14 02:51:57 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-14 02:51:57 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-14 02:51:57 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-14 02:51:57 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-14 02:51:58 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-14 02:52:02 [parallel_state.py:1076] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
ERROR 07-14 02:52:07 [core.py:586] EngineCore failed to start.
ERROR 07-14 02:52:07 [core.py:586] Traceback (most recent call last):
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core
ERROR 07-14 02:52:07 [core.py:586]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 404, in __init__
ERROR 07-14 02:52:07 [core.py:586]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 75, in __init__
ERROR 07-14 02:52:07 [core.py:586]     self.model_executor = executor_class(vllm_config)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
ERROR 07-14 02:52:07 [core.py:586]     self._init_executor()
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 47, in _init_executor
ERROR 07-14 02:52:07 [core.py:586]     self.collective_rpc("init_device")
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 07-14 02:52:07 [core.py:586]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2736, in run_method
ERROR 07-14 02:52:07 [core.py:586]     return func(*args, **kwargs)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 606, in init_device
ERROR 07-14 02:52:07 [core.py:586]     self.worker.init_device()  # type: ignore
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 142, in init_device
ERROR 07-14 02:52:07 [core.py:586]     self.model_runner = NPUModelRunner(self.vllm_config, device)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 166, in __init__
ERROR 07-14 02:52:07 [core.py:586]     self.max_num_encoder_input_tokens, self.encoder_cache_size = compute_encoder_budget(
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/core/encoder_cache_manager.py", line 199, in compute_encoder_budget
ERROR 07-14 02:52:07 [core.py:586]     ) = _compute_encoder_budget_multimodal(
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/core/encoder_cache_manager.py", line 229, in _compute_encoder_budget_multimodal
ERROR 07-14 02:52:07 [core.py:586]     .get_max_tokens_per_item_by_nonzero_modality(model_config)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/multimodal/registry.py", line 158, in get_max_tokens_per_item_by_nonzero_modality
ERROR 07-14 02:52:07 [core.py:586]     self.get_max_tokens_per_item_by_modality(model_config).items()
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/multimodal/registry.py", line 132, in get_max_tokens_per_item_by_modality
ERROR 07-14 02:52:07 [core.py:586]     return profiler.get_mm_max_tokens(
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/multimodal/profiling.py", line 282, in get_mm_max_tokens
ERROR 07-14 02:52:07 [core.py:586]     mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/multimodal/profiling.py", line 170, in _get_dummy_mm_inputs
ERROR 07-14 02:52:07 [core.py:586]     processor_inputs = factory.get_dummy_processor_inputs(
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/multimodal/profiling.py", line 92, in get_dummy_processor_inputs
ERROR 07-14 02:52:07 [core.py:586]     dummy_text = self.get_dummy_text(mm_counts)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/glm4_1v.py", line 1005, in get_dummy_text
ERROR 07-14 02:52:07 [core.py:586]     hf_processor = self.info.get_hf_processor()
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/multimodal/processing.py", line 1075, in get_hf_processor
ERROR 07-14 02:52:07 [core.py:586]     return self.ctx.get_hf_processor(**kwargs)
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 138, in get_hf_processor
ERROR 07-14 02:52:07 [core.py:586]     return super().get_hf_processor(
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 96, in get_hf_processor
ERROR 07-14 02:52:07 [core.py:586]     return cached_processor_from_config(
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/transformers_utils/processor.py", line 110, in cached_processor_from_config
ERROR 07-14 02:52:07 [core.py:586]     return cached_get_processor(
ERROR 07-14 02:52:07 [core.py:586]   File "/vllm-workspace/vllm/vllm/transformers_utils/processor.py", line 72, in get_processor
ERROR 07-14 02:52:07 [core.py:586]     processor = processor_factory.from_pretrained(
ERROR 07-14 02:52:07 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/hf_util/patcher.py", line 177, in patch_pretrained_model_name_or_path
ERROR 07-14 02:52:07 [core.py:586]     return cls._from_pretrained_origin.__func__(cls, model_dir,
ERROR 07-14 02:52:07 [core.py:586]   File "/workspace/transformers/src/transformers/models/auto/processing_auto.py", line 379, in from_pretrained
ERROR 07-14 02:52:07 [core.py:586]     return processor_class.from_pretrained(
ERROR 07-14 02:52:07 [core.py:586]   File "/workspace/transformers/src/transformers/processing_utils.py", line 1304, in from_pretrained
ERROR 07-14 02:52:07 [core.py:586]     return cls.from_args_and_dict(args, processor_dict, **kwargs)
ERROR 07-14 02:52:07 [core.py:586]   File "/workspace/transformers/src/transformers/processing_utils.py", line 1105, in from_args_and_dict
ERROR 07-14 02:52:07 [core.py:586]     processor = cls(*args, **valid_kwargs)
ERROR 07-14 02:52:07 [core.py:586] TypeError: Glm4vProcessor.__init__() got multiple values for argument 'tokenizer'
Process EngineCore_0:

```

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

