# Issue #800: [Bug]: vllm can't run deepseek 70b with Huawei ascend 910b npu card

## 基本信息

- **编号**: #800
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/800
- **创建时间**: 2025-05-09T09:07:53Z
- **关闭时间**: 2026-01-04T02:15:23Z
- **更新时间**: 2026-01-04T02:15:23Z
- **提交者**: @huazq
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
```

</details>


### 🐛 Describe the bug

[root@cetccloud-custom-vllm-predictor-ffb4b55bc-gvmv5 code]# vllm serve  /mnt/models --served-model-name "deepseek-70B" --host 0.0.0.0 --port 80 --dtype bfloat16 -tp 4 --gpu-memory-utilization 0.9
INFO 05-09 08:05:50 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-09 08:05:50 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-09 08:05:50 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-09 08:05:52 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-09 08:05:52 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-09 08:05:52 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-09 08:05:52 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-09 08:05:52 [__init__.py:44] plugin ascend loaded.
INFO 05-09 08:05:52 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-09 08:05:53 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-09 08:05:56 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-09 08:05:56 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-09 08:05:56 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-09 08:05:56 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-09 08:05:56 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-09 08:05:56 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-09 08:05:56 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-09 08:05:56 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-09 08:05:56 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-09 08:05:56 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-09 08:06:00 [api_server.py:1043] vLLM API server version 0.8.5.post1
INFO 05-09 08:06:00 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/mnt/models', config='', host='0.0.0.0', port=80, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/mnt/models', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, load_format='auto', download_dir=None, model_loader_extra_config={}, use_tqdm_on_load=True, config_format=<ConfigFormat.AUTO: 'auto'>, dtype='bfloat16', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=4, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, disable_custom_all_reduce=False, block_size=None, gpu_memory_utilization=0.9, swap_space=4, kv_cache_dtype='auto', num_gpu_blocks_override=None, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', cpu_offload_gb=0, calculate_kv_scales=False, disable_sliding_window=False, use_v2_block_manager=True, seed=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_token=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config={}, limit_mm_per_prompt={}, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=None, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=None, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', speculative_config=None, ignore_patterns=[], served_model_name=['deepseek-70B'], qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, max_num_batched_tokens=None, max_num_seqs=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, num_lookahead_slots=0, scheduler_delay_factor=0.0, preemption_mode=None, num_scheduler_steps=1, multi_step_stream_outputs=True, scheduling_policy='fcfs', enable_chunked_prefill=None, disable_chunked_mm_input=False, scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, additional_config=None, enable_reasoning=False, disable_cascade_attn=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffdb8fab010>)
INFO 05-09 08:06:11 [config.py:717] This model supports multiple tasks: {'classify', 'score', 'embed', 'reward', 'generate'}. Defaulting to 'generate'.
INFO 05-09 08:06:11 [arg_utils.py:1669] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
WARNING 05-09 08:06:11 [arg_utils.py:1536] The model has a long context length (131072). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value.
INFO 05-09 08:06:11 [config.py:1770] Defaulting to use mp for distributed inference
INFO 05-09 08:06:11 [config.py:1804] Disabled the custom all-reduce kernel because it is not supported on current platform.
WARNING 05-09 08:06:11 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
INFO 05-09 08:06:11 [platform.py:133] Compilation disabled, using eager mode by default
INFO 05-09 08:06:11 [api_server.py:246] Started engine process with PID 207
INFO 05-09 08:06:16 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-09 08:06:16 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-09 08:06:16 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-09 08:06:17 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-09 08:06:17 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-09 08:06:17 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-09 08:06:17 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-09 08:06:17 [__init__.py:44] plugin ascend loaded.
INFO 05-09 08:06:17 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-09 08:06:19 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-09 08:06:21 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-09 08:06:21 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-09 08:06:21 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-09 08:06:21 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-09 08:06:21 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-09 08:06:21 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-09 08:06:21 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-09 08:06:21 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-09 08:06:21 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-09 08:06:21 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-09 08:06:21 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='/mnt/models', speculative_config=None, tokenizer='/mnt/models', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=deepseek-70B, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
WARNING 05-09 08:06:22 [multiproc_worker_utils.py:306] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
WARNING 05-09 08:06:23 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffdc3814bb0>
INFO 05-09 08:06:27 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 05-09 08:06:27 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 05-09 08:06:27 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-09 08:06:27 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
WARNING 05-09 08:06:27 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
WARNING 05-09 08:06:27 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-09 08:06:27 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-09 08:06:27 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-09 08:06:27 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-09 08:06:28 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-09 08:06:28 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-09 08:06:28 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-09 08:06:28 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-09 08:06:28 [__init__.py:44] plugin ascend loaded.
INFO 05-09 08:06:28 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-09 08:06:28 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-09 08:06:28 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-09 08:06:28 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-09 08:06:28 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-09 08:06:28 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-09 08:06:28 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-09 08:06:28 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-09 08:06:28 [__init__.py:44] plugin ascend loaded.
INFO 05-09 08:06:28 [__init__.py:44] plugin ascend loaded.
INFO 05-09 08:06:28 [__init__.py:230] Platform plugin ascend is activated
INFO 05-09 08:06:28 [__init__.py:230] Platform plugin ascend is activated
INFO 05-09 08:06:28 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-09 08:06:30 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 05-09 08:06:30 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 05-09 08:06:30 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=343) INFO 05-09 08:06:32 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=345) INFO 05-09 08:06:32 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=343) INFO 05-09 08:06:32 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=343) INFO 05-09 08:06:32 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=343) INFO 05-09 08:06:32 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=343) INFO 05-09 08:06:32 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=343) INFO 05-09 08:06:32 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=344) INFO 05-09 08:06:32 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=345) INFO 05-09 08:06:32 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=345) INFO 05-09 08:06:32 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=345) INFO 05-09 08:06:32 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=345) INFO 05-09 08:06:32 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=345) INFO 05-09 08:06:32 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=344) INFO 05-09 08:06:32 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=344) INFO 05-09 08:06:32 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=344) INFO 05-09 08:06:32 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=344) INFO 05-09 08:06:32 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=344) INFO 05-09 08:06:32 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=343) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(VllmWorkerProcess pid=343) WARNING 05-09 08:06:32 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=343) WARNING 05-09 08:06:32 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(VllmWorkerProcess pid=343) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=343) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=345) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(VllmWorkerProcess pid=345) WARNING 05-09 08:06:32 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=345) WARNING 05-09 08:06:32 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(VllmWorkerProcess pid=345) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=345) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=344) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(VllmWorkerProcess pid=344) WARNING 05-09 08:06:32 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=344) WARNING 05-09 08:06:32 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(VllmWorkerProcess pid=344) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=344) WARNING 05-09 08:06:32 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=345) WARNING 05-09 08:06:33 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff91292cb0>
(VllmWorkerProcess pid=343) WARNING 05-09 08:06:33 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff7ac62cb0>
(VllmWorkerProcess pid=344) WARNING 05-09 08:06:33 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff80102cb0>
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method init_device.
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 604, in init_device
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     self.worker.init_device()  # type: ignore
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 211, in init_device
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     NPUPlatform.set_device(self.device)
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 95, in set_device
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     torch.npu.set_device(device)
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 83, in set_device
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     torch_npu._C._npu_setDevice(device_id)
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] RuntimeError: GetDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:60 NPU function error: aclrtGetCurrentContext(&used_devices[local_device]), error code is 107002
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method init_device.
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] [ERROR] 2025-05-09-08:06:34 (PID:345, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] [Error]: The context is empty.
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         Check whether acl.rt.set_context or acl.rt.set_device is called.
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] EE1001: [PID: 345] 2025-05-09-08:06:34.182.045 The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         TraceBack (most recent call last):
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 604, in init_device
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     self.worker.init_device()  # type: ignore
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 211, in init_device
(VllmWorkerProcess pid=345) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] 
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     NPUPlatform.set_device(self.device)
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 95, in set_device
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     torch.npu.set_device(device)
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 83, in set_device
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]     torch_npu._C._npu_setDevice(device_id)
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] RuntimeError: GetDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:60 NPU function error: aclrtGetCurrentContext(&used_devices[local_device]), error code is 107002
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] [ERROR] 2025-05-09-08:06:34 (PID:343, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] [Error]: The context is empty.
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         Check whether acl.rt.set_context or acl.rt.set_device is called.
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] EE1001: [PID: 343] 2025-05-09-08:06:34.182.218 The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         TraceBack (most recent call last):
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
(VllmWorkerProcess pid=343) ERROR 05-09 08:06:34 [multiproc_worker_utils.py:238] 
ERROR 05-09 08:06:34 [engine.py:448] GetDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:60 NPU function error: aclrtGetCurrentContext(&used_devices[local_device]), error code is 107002
ERROR 05-09 08:06:34 [engine.py:448] [ERROR] 2025-05-09-08:06:34 (PID:207, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 05-09 08:06:34 [engine.py:448] [Error]: The context is empty.
ERROR 05-09 08:06:34 [engine.py:448]         Check whether acl.rt.set_context or acl.rt.set_device is called.
ERROR 05-09 08:06:34 [engine.py:448] EE1001: [PID: 207] 2025-05-09-08:06:34.181.090 The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
ERROR 05-09 08:06:34 [engine.py:448]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
ERROR 05-09 08:06:34 [engine.py:448]         TraceBack (most recent call last):
ERROR 05-09 08:06:34 [engine.py:448]         [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-09 08:06:34 [engine.py:448]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]
ERROR 05-09 08:06:34 [engine.py:448]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
ERROR 05-09 08:06:34 [engine.py:448] Traceback (most recent call last):
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 05-09 08:06:34 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 05-09 08:06:34 [engine.py:448]     return cls(
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 05-09 08:06:34 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
ERROR 05-09 08:06:34 [engine.py:448]     self.model_executor = executor_class(vllm_config=vllm_config)
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 286, in __init__
ERROR 05-09 08:06:34 [engine.py:448]     super().__init__(*args, **kwargs)
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 05-09 08:06:34 [engine.py:448]     self._init_executor()
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 124, in _init_executor
ERROR 05-09 08:06:34 [engine.py:448]     self._run_workers("init_device")
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
ERROR 05-09 08:06:34 [engine.py:448]     driver_worker_output = run_method(self.driver_worker, sent_method,
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-09 08:06:34 [engine.py:448]     return func(*args, **kwargs)
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 604, in init_device
ERROR 05-09 08:06:34 [engine.py:448]     self.worker.init_device()  # type: ignore
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 211, in init_device
ERROR 05-09 08:06:34 [engine.py:448]     NPUPlatform.set_device(self.device)
ERROR 05-09 08:06:34 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 95, in set_device
ERROR 05-09 08:06:34 [engine.py:448]     torch.npu.set_device(device)
ERROR 05-09 08:06:34 [engine.py:448]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 83, in set_device
ERROR 05-09 08:06:34 [engine.py:448]     torch_npu._C._npu_setDevice(device_id)
ERROR 05-09 08:06:34 [engine.py:448] RuntimeError: GetDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:60 NPU function error: aclrtGetCurrentContext(&used_devices[local_device]), error code is 107002
ERROR 05-09 08:06:34 [engine.py:448] [ERROR] 2025-05-09-08:06:34 (PID:207, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 05-09 08:06:34 [engine.py:448] [Error]: The context is empty.
ERROR 05-09 08:06:34 [engine.py:448]         Check whether acl.rt.set_context or acl.rt.set_device is called.
ERROR 05-09 08:06:34 [engine.py:448] EE1001: [PID: 207] 2025-05-09-08:06:34.181.090 The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
ERROR 05-09 08:06:34 [engine.py:448]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
ERROR 05-09 08:06:34 [engine.py:448]         TraceBack (most recent call last):
ERROR 05-09 08:06:34 [engine.py:448]         [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-09 08:06:34 [engine.py:448]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]
ERROR 05-09 08:06:34 [engine.py:448]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
ERROR 05-09 08:06:34 [engine.py:448] 
INFO 05-09 08:06:34 [multiproc_worker_utils.py:124] Killing local vLLM worker processes
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 450, in run_mp_engine
    raise e
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
    engine = MQLLMEngine.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 82, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 286, in __init__
    super().__init__(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 124, in _init_executor
    self._run_workers("init_device")
  File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
    driver_worker_output = run_method(self.driver_worker, sent_method,
  File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 604, in init_device
    self.worker.init_device()  # type: ignore
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 211, in init_device
    NPUPlatform.set_device(self.device)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 95, in set_device
    torch.npu.set_device(device)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 83, in set_device
    torch_npu._C._npu_setDevice(device_id)
RuntimeError: GetDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:60 NPU function error: aclrtGetCurrentContext(&used_devices[local_device]), error code is 107002
[ERROR] 2025-05-09-08:06:34 (PID:207, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The context is empty.
        Check whether acl.rt.set_context or acl.rt.set_device is called.
EE1001: [PID: 207] 2025-05-09-08:06:34.181.090 The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
        Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
        TraceBack (most recent call last):
        [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]
        The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]

Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 53, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1078, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 269, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
