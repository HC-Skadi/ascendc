# Issue #829: [Bug]: modelscope.hub.errors.NotExistError: The model: Qwen/Qwen2.5-VL-7B-Instruct has no revision: main !

## 基本信息

- **编号**: #829
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/829
- **创建时间**: 2025-05-12T16:02:46Z
- **关闭时间**: 2026-01-04T03:38:28Z
- **更新时间**: 2026-01-04T03:38:28Z
- **提交者**: @nutriver
- **评论数**: 17

## 标签

bug

## 问题描述

### Your current environment

docker：quay.io/ascend/vllm-ascend:v0.7.3
Machine：Atlas 800I A2

### 🐛 Describe the bug


<details>
<summary>Running the command `vllm serve Qwen/Qwen2.5-VL-7B-Instruct --dtype bfloat16 --max_model_len 32768 --max-num-batched-tokens 32768` results in an error.</summary>

```text
INFO 05-12 15:39:24 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-12 15:39:24 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-12 15:39:24 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-12 15:39:24 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 15:39:24 __init__.py:44] plugin ascend loaded.
INFO 05-12 15:39:24 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 05-12 15:39:25 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-12 15:39:25 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-12 15:39:25 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-12 15:39:25 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 15:39:25 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-12 15:39:25 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-12 15:39:25 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-12 15:39:25 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-12 15:39:25 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 05-12 15:39:25 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 05-12 15:39:25 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 05-12 15:39:25 api_server.py:912] vLLM API server version 0.7.3
INFO 05-12 15:39:25 api_server.py:913] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2.5-VL-7B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen2.5-VL-7B-Instruct', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='bfloat16', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=32768, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffd1d6f95a0>)
INFO 05-12 15:39:25 api_server.py:209] Started engine process with PID 2319
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:39:26,273 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:39:26,861 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 05-12 15:39:34 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-12 15:39:34 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-12 15:39:34 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-12 15:39:34 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 15:39:34 __init__.py:44] plugin ascend loaded.
INFO 05-12 15:39:34 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 05-12 15:39:34 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-12 15:39:34 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-12 15:39:34 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-12 15:39:34 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 15:39:34 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-12 15:39:34 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-12 15:39:34 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-12 15:39:34 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-12 15:39:34 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 05-12 15:39:34 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 05-12 15:39:34 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:39:35,651 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:39:36,238 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 05-12 15:39:38 config.py:549] This model supports multiple tasks: {'generate', 'reward', 'embed', 'classify', 'score'}. Defaulting to 'generate'.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:39:38,819 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 05-12 15:39:47 config.py:549] This model supports multiple tasks: {'generate', 'embed', 'classify', 'score', 'reward'}. Defaulting to 'generate'.
INFO 05-12 15:39:47 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='Qwen/Qwen2.5-VL-7B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-VL-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=Qwen/Qwen2.5-VL-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:39:48,066 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:40:00,895 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:40:01,566 - modelscope - INFO - Target directory already exists, skipping creation.
ERROR 05-12 15:40:01 camem.py:69] Failed to import vllm_ascend_C:No module named 'vllm_ascend.vllm_ascend_C'
/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning: 
    *************************************************************************************************************
    The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now..
    The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now..
    The backend in torch.distributed.init_process_group set to hccl now..
    The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now..
    The device parameters have been replaced with npu in the function below:
    torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty
    *************************************************************************************************************
    
  warnings.warn(msg, ImportWarning)
/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu.
  warnings.warn(msg, RuntimeWarning)
WARNING 05-12 15:40:01 utils.py:2262] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd3eef8ca0>
[rank0]:[W512 15:40:16.289563062 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
INFO 05-12 15:40:16 model_runner.py:902] Starting to load model Qwen/Qwen2.5-VL-7B-Instruct...
WARNING 05-12 15:40:16 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-12 15:40:16 config.py:3054] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:40:17,650 - modelscope - INFO - Target directory already exists, skipping creation.
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:00<00:01,  3.05it/s]
Loading safetensors checkpoint shards:  40% Completed | 2/5 [00:00<00:01,  2.37it/s]
Loading safetensors checkpoint shards:  60% Completed | 3/5 [00:01<00:00,  2.21it/s]
Loading safetensors checkpoint shards:  80% Completed | 4/5 [00:01<00:00,  2.68it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:02<00:00,  2.25it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:02<00:00,  2.35it/s]

INFO 05-12 15:40:20 model_runner.py:907] Loading model weights took 18.4429 GB
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:40:21,086 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
2025-05-12 15:40:22,190 - modelscope - INFO - Target directory already exists, skipping creation.
Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
Downloading Model to directory: /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-7B-Instruct
ERROR 05-12 15:40:22 engine.py:400] The model: Qwen/Qwen2.5-VL-7B-Instruct has no revision: main !
ERROR 05-12 15:40:22 engine.py:400] Traceback (most recent call last):
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 05-12 15:40:22 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
ERROR 05-12 15:40:22 engine.py:400]     return cls(ipc_path=ipc_path,
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 76, in __init__
ERROR 05-12 15:40:22 engine.py:400]     self.engine = LLMEngine(*args, **kwargs)
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 276, in __init__
ERROR 05-12 15:40:22 engine.py:400]     self._initialize_kv_caches()
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
ERROR 05-12 15:40:22 engine.py:400]     self.model_executor.determine_num_available_blocks())
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
ERROR 05-12 15:40:22 engine.py:400]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 05-12 15:40:22 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/utils.py", line 2196, in run_method
ERROR 05-12 15:40:22 engine.py:400]     return func(*args, **kwargs)
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 05-12 15:40:22 engine.py:400]     return func(*args, **kwargs)
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 255, in determine_num_available_blocks
ERROR 05-12 15:40:22 engine.py:400]     self.model_runner.profile_run()
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 05-12 15:40:22 engine.py:400]     return func(*args, **kwargs)
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1452, in profile_run
ERROR 05-12 15:40:22 engine.py:400]     .dummy_data_for_profiling(self.model_config,
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 336, in dummy_data_for_profiling
ERROR 05-12 15:40:22 engine.py:400]     dummy_data = profiler.get_dummy_data(
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/multimodal/profiling.py", line 168, in get_dummy_data
ERROR 05-12 15:40:22 engine.py:400]     mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/multimodal/profiling.py", line 138, in _get_dummy_mm_inputs
ERROR 05-12 15:40:22 engine.py:400]     processor_inputs = factory.get_dummy_processor_inputs(
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_vl.py", line 944, in get_dummy_processor_inputs
ERROR 05-12 15:40:22 engine.py:400]     hf_processor = self.info.get_hf_processor()
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 698, in get_hf_processor
ERROR 05-12 15:40:22 engine.py:400]     return self.ctx.get_hf_processor(
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 136, in get_hf_processor
ERROR 05-12 15:40:22 engine.py:400]     return super().get_hf_processor(
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 100, in get_hf_processor
ERROR 05-12 15:40:22 engine.py:400]     return cached_processor_from_config(
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/transformers_utils/processor.py", line 106, in cached_processor_from_config
ERROR 05-12 15:40:22 engine.py:400]     return cached_get_processor(
ERROR 05-12 15:40:22 engine.py:400]   File "/vllm-workspace/vllm/vllm/transformers_utils/processor.py", line 69, in get_processor
ERROR 05-12 15:40:22 engine.py:400]     processor = processor_factory.from_pretrained(
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1079, in from_pretrained
ERROR 05-12 15:40:22 engine.py:400]     args = cls._get_arguments_from_pretrained(pretrained_model_name_or_path, **kwargs)
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1143, in _get_arguments_from_pretrained
ERROR 05-12 15:40:22 engine.py:400]     args.append(attribute_class.from_pretrained(pretrained_model_name_or_path, **kwargs))
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/hf_util.py", line 247, in from_pretrained
ERROR 05-12 15:40:22 engine.py:400]     model_dir = get_model_dir(pretrained_model_name_or_path, None,
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/hf_util.py", line 172, in get_model_dir
ERROR 05-12 15:40:22 engine.py:400]     model_dir = snapshot_download(
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/hub/snapshot_download.py", line 109, in snapshot_download
ERROR 05-12 15:40:22 engine.py:400]     return _snapshot_download(
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/hub/snapshot_download.py", line 257, in _snapshot_download
ERROR 05-12 15:40:22 engine.py:400]     revision_detail = _api.get_valid_revision_detail(
ERROR 05-12 15:40:22 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/hub/api.py", line 600, in get_valid_revision_detail
ERROR 05-12 15:40:22 engine.py:400]     raise NotExistError('The model: %s has no revision: %s !' % (model_id, revision))
ERROR 05-12 15:40:22 engine.py:400] modelscope.hub.errors.NotExistError: The model: Qwen/Qwen2.5-VL-7B-Instruct has no revision: main !
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
    return cls(ipc_path=ipc_path,
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 76, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 276, in __init__
    self._initialize_kv_caches()
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/vllm-workspace/vllm/vllm/utils.py", line 2196, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 255, in determine_num_available_blocks
    self.model_runner.profile_run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1452, in profile_run
    .dummy_data_for_profiling(self.model_config,
  File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 336, in dummy_data_for_profiling
    dummy_data = profiler.get_dummy_data(
  File "/vllm-workspace/vllm/vllm/multimodal/profiling.py", line 168, in get_dummy_data
    mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
  File "/vllm-workspace/vllm/vllm/multimodal/profiling.py", line 138, in _get_dummy_mm_inputs
    processor_inputs = factory.get_dummy_processor_inputs(
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_vl.py", line 944, in get_dummy_processor_inputs
    hf_processor = self.info.get_hf_processor()
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 698, in get_hf_processor
    return self.ctx.get_hf_processor(
  File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 136, in get_hf_processor
    return super().get_hf_processor(
  File "/vllm-workspace/vllm/vllm/inputs/registry.py", line 100, in get_hf_processor
    return cached_processor_from_config(
  File "/vllm-workspace/vllm/vllm/transformers_utils/processor.py", line 106, in cached_processor_from_config
    return cached_get_processor(
  File "/vllm-workspace/vllm/vllm/transformers_utils/processor.py", line 69, in get_processor
    processor = processor_factory.from_pretrained(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1079, in from_pretrained
    args = cls._get_arguments_from_pretrained(pretrained_model_name_or_path, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1143, in _get_arguments_from_pretrained
    args.append(attribute_class.from_pretrained(pretrained_model_name_or_path, **kwargs))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/hf_util.py", line 247, in from_pretrained
    model_dir = get_model_dir(pretrained_model_name_or_path, None,
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/hf_util.py", line 172, in get_model_dir
    model_dir = snapshot_download(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/hub/snapshot_download.py", line 109, in snapshot_download
    return _snapshot_download(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/hub/snapshot_download.py", line 257, in _snapshot_download
    revision_detail = _api.get_valid_revision_detail(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/hub/api.py", line 600, in get_valid_revision_detail
    raise NotExistError('The model: %s has no revision: %s !' % (model_id, revision))
modelscope.hub.errors.NotExistError: The model: Qwen/Qwen2.5-VL-7B-Instruct has no revision: main !
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 34, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 947, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 233, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-05-12-15:40:29 (PID:2183, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

</details>

