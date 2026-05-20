# Issue #1502: [Usage]:can not start vllm serve

## 基本信息

- **编号**: #1502
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1502
- **创建时间**: 2025-06-28T08:55:16Z
- **关闭时间**: 2025-06-30T21:54:27Z
- **更新时间**: 2025-06-30T21:54:27Z
- **提交者**: @waaaooo
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

```
docker run --name vllm-ascend   --device $DEVICE     --device /dev/davinci_manager     --device /dev/devmm_svm     --device /dev/hisi_hdc     -v /usr/local/dcmi:/usr/local/dcmi     -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi     -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/     -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info     -v /etc/ascend_install.info:/etc/ascend_install.info     -v /root/.cache:/root/.cache    -v /home/models:/models  -v  /root/Ascend-cann-kernels-910b_8.1.RC1_linux-aarch64.run.1:/kernels.run -v  /root/Ascend-cann-nnal_8.1.RC1_linux-aarch64.run:/nnal.run -v /root/Ascend-cann-toolkit_8.1.RC1_linux-aarch64.run:/toolkit.run -it $IMAGE bash
```

I follow the method of https://vllm-ascend.readthedocs.io/en/v0.7.3-dev/installation.html (pip install)

 ```
#vllm serve /models/Qwen2.5-7B-Instruct/
INFO 06-28 08:27:50 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 06-28 08:27:50 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 06-28 08:27:50 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 06-28 08:27:50 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 06-28 08:27:50 __init__.py:44] plugin ascend loaded.
INFO 06-28 08:27:50 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 06-28 08:27:50 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 06-28 08:27:50 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 06-28 08:27:50 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 06-28 08:27:50 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 06-28 08:27:50 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 06-28 08:27:50 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-28 08:27:50 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-28 08:27:50 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-28 08:27:50 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-28 08:27:50 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 06-28 08:27:50 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 06-28 08:27:50 api_server.py:912] vLLM API server version 0.7.3
INFO 06-28 08:27:50 api_server.py:913] args: Namespace(subparser='serve', model_tag='/models/Qwen2.5-7B-Instruct/', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/models/Qwen2.5-7B-Instruct/', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffd24732b90>)
INFO 06-28 08:27:50 api_server.py:209] Started engine process with PID 574
INFO 06-28 08:28:00 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 06-28 08:28:00 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 06-28 08:28:00 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 06-28 08:28:00 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 06-28 08:28:00 __init__.py:44] plugin ascend loaded.
INFO 06-28 08:28:00 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 06-28 08:28:00 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 06-28 08:28:00 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 06-28 08:28:00 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 06-28 08:28:00 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 06-28 08:28:00 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 06-28 08:28:00 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-28 08:28:00 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-28 08:28:00 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-28 08:28:00 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-28 08:28:00 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 06-28 08:28:00 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 06-28 08:28:01 config.py:549] This model supports multiple tasks: {'score', 'classify', 'embed', 'reward', 'generate'}. Defaulting to 'generate'.
INFO 06-28 08:28:12 config.py:549] This model supports multiple tasks: {'embed', 'generate', 'classify', 'reward', 'score'}. Defaulting to 'generate'.
INFO 06-28 08:28:12 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/models/Qwen2.5-7B-Instruct/', speculative_config=None, tokenizer='/models/Qwen2.5-7B-Instruct/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/models/Qwen2.5-7B-Instruct/, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
WARNING 06-28 08:28:13 camem.py:69] Failed to import vllm_ascend_C:No module named 'vllm_ascend.vllm_ascend_C'
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
WARNING 06-28 08:28:14 utils.py:2262] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd1daa8820>
INFO 06-28 08:28:30 model_runner.py:902] Starting to load model /models/Qwen2.5-7B-Instruct/...
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:01,  2.51it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.88it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:01<00:00,  1.79it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:02<00:00,  1.73it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:02<00:00,  1.80it/s]

INFO 06-28 08:28:37 model_runner.py:907] Loading model weights took 14.2488 GB
[rank0]:[E628 08:28:45.008203220 compiler_depend.ts:422] setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:131 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0xb8 (0xffff890dc908 in /usr/local/python3.10.17/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, char const*) + 0x70 (0xffff8908b4e0 in /usr/local/python3.10.17/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x8c (0xfffcc00446bc in /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0x34d84 (0xfffcc0044d84 in /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x1644484 (0xfffde11b4484 in /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x78d244 (0xfffde02fd244 in /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x78da58 (0xfffde02fda58 in /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0x78a1cc (0xfffde02fa1cc in /usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0x4c9e4c (0xffff89119e4c in /usr/local/python3.10.17/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #9: <unknown function> + 0x7d5b8 (0xffff93b0d5b8 in /lib/aarch64-linux-gnu/libc.so.6)
frame #10: <unknown function> + 0xe5edc (0xffff93b75edc in /lib/aarch64-linux-gnu/libc.so.6)

ERROR 06-28 08:28:45 engine.py:400] The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RopeOperation.
ERROR 06-28 08:28:45 engine.py:400] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
ERROR 06-28 08:28:45 engine.py:400] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
ERROR 06-28 08:28:45 engine.py:400] [ERROR] 2025-06-28-08:28:45 (PID:574, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 06-28 08:28:45 engine.py:400] Traceback (most recent call last):
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 06-28 08:28:45 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
ERROR 06-28 08:28:45 engine.py:400]     return cls(ipc_path=ipc_path,
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
ERROR 06-28 08:28:45 engine.py:400]     self.engine = LLMEngine(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
ERROR 06-28 08:28:45 engine.py:400]     self._initialize_kv_caches()
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
ERROR 06-28 08:28:45 engine.py:400]     self.model_executor.determine_num_available_blocks())
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
ERROR 06-28 08:28:45 engine.py:400]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 06-28 08:28:45 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 06-28 08:28:45 engine.py:400]     return func(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-28 08:28:45 engine.py:400]     return func(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 255, in determine_num_available_blocks
ERROR 06-28 08:28:45 engine.py:400]     self.model_runner.profile_run()
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-28 08:28:45 engine.py:400]     return func(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1490, in profile_run
ERROR 06-28 08:28:45 engine.py:400]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-28 08:28:45 engine.py:400]     return func(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1270, in execute_model
ERROR 06-28 08:28:45 engine.py:400]     hidden_or_intermediate_states = model_executable(
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-28 08:28:45 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-28 08:28:45 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward
ERROR 06-28 08:28:45 engine.py:400]     hidden_states = self.model(input_ids, positions, kv_caches,
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
ERROR 06-28 08:28:45 engine.py:400]     return self.forward(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward
ERROR 06-28 08:28:45 engine.py:400]     hidden_states, residual = layer(
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-28 08:28:45 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-28 08:28:45 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 257, in forward
ERROR 06-28 08:28:45 engine.py:400]     hidden_states = self.mlp(hidden_states)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-28 08:28:45 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-28 08:28:45 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 95, in forward
ERROR 06-28 08:28:45 engine.py:400]     gate_up, _ = self.gate_up_proj(x)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-28 08:28:45 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-28 08:28:45 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 388, in forward
ERROR 06-28 08:28:45 engine.py:400]     output_parallel = self.quant_method.apply(self, input_, bias)
ERROR 06-28 08:28:45 engine.py:400]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 142, in apply
ERROR 06-28 08:28:45 engine.py:400]     return F.linear(x, layer.weight, bias)
ERROR 06-28 08:28:45 engine.py:400] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RopeOperation.
ERROR 06-28 08:28:45 engine.py:400] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
ERROR 06-28 08:28:45 engine.py:400] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
ERROR 06-28 08:28:45 engine.py:400] [ERROR] 2025-06-28-08:28:45 (PID:574, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 06-28 08:28:45 engine.py:400] 
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
    return cls(ipc_path=ipc_path,
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
    self._initialize_kv_caches()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 255, in determine_num_available_blocks
    self.model_runner.profile_run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1490, in profile_run
    self.execute_model(model_input, kv_caches, intermediate_tensors)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1270, in execute_model
    hidden_or_intermediate_states = model_executable(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward
    hidden_states = self.model(input_ids, positions, kv_caches,
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
    return self.forward(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward
    hidden_states, residual = layer(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 257, in forward
    hidden_states = self.mlp(hidden_states)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 95, in forward
    gate_up, _ = self.gate_up_proj(x)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 388, in forward
    output_parallel = self.quant_method.apply(self, input_, bias)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 142, in apply
    return F.linear(x, layer.weight, bias)
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RopeOperation.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[ERROR] 2025-06-28-08:28:45 (PID:574, Device:0, RankID:-1) ERR00100 PTA call acl api failed.

Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 233, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-06-28-08:28:53 (PID:441, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

