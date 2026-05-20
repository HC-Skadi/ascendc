# Issue #564: [Usage]: ACL error when running Qwen2.5-7B on 910B2

## 基本信息

- **编号**: #564
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/564
- **创建时间**: 2025-04-18T02:34:22Z
- **关闭时间**: 2025-04-18T05:13:28Z
- **更新时间**: 2025-04-18T05:13:28Z
- **提交者**: @zhaoning1987
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

```text
npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 96.0        27                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3367 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 89.3        26                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 92.3        26                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 91.2        27                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 89.4        29                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 95.2        32                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 91.2        30                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 89.6        30                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
```

```text
cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=7.0.1
innerversion=V100R001C15SPC004B220
compatible_version=[V100R001C15],[V100R001C29],[V100R001C30],[V100R001C13],[V100R003C10],[V100R003C11]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/7.0.1/aarch64-linux

```


### How would you like to use vllm on ascend

I want to run inference of Qwen2.5-7B on device above with quay.io/ascend/vllm-ascend:v0.7.3rc2 image. And i got the following error.
```text
root@ea451a232c03:/workspace# export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
root@ea451a232c03:/workspace# vllm serve Qwen/Qwen2.5-7B-Instruct --max_mod^C_len 26240
root@ea451a232c03:/workspace# VLLM_USE_MODELSCOPE=True
root@ea451a232c03:/workspace# vllm serve /models/Qwen2.5-7B-Instruct --max_model_len 26240
Qwen2.5-7B-Instruct/     Qwen2.5-7B-Instruct.zip  
root@ea451a232c03:/workspace# vllm serve /models/Qwen2.5-7B-Instruct/ --max_model_len 26240
config.json                       merges.txt                        model-00002-of-00004.safetensors  model-00004-of-00004.safetensors  tokenizer.json                    vocab.json
generation_config.json            model-00001-of-00004.safetensors  model-00003-of-00004.safetensors  model.safetensors.index.json      tokenizer_config.json             
root@ea451a232c03:/workspace# vllm serve /models/Qwen2.5-7B-Instruct/ --max_model_len 26240
INFO 04-18 01:55:25 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-18 01:55:25 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-18 01:55:25 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-18 01:55:25 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 01:55:25 __init__.py:44] plugin ascend loaded.
INFO 04-18 01:55:25 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 04-18 01:55:25 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-18 01:55:25 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-18 01:55:25 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-18 01:55:25 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 01:55:25 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 04-18 01:55:25 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-18 01:55:25 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-18 01:55:25 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-18 01:55:25 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 04-18 01:55:25 api_server.py:912] vLLM API server version 0.7.3
INFO 04-18 01:55:25 api_server.py:913] args: Namespace(subparser='serve', model_tag='/models/Qwen2.5-7B-Instruct/', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/models/Qwen2.5-7B-Instruct/', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=26240, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffdc50320e0>)
INFO 04-18 01:55:25 api_server.py:209] Started engine process with PID 352
INFO 04-18 01:55:34 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-18 01:55:34 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-18 01:55:34 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-18 01:55:34 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 01:55:34 __init__.py:44] plugin ascend loaded.
INFO 04-18 01:55:34 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 04-18 01:55:34 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-18 01:55:34 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-18 01:55:34 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-18 01:55:34 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 01:55:34 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 04-18 01:55:34 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-18 01:55:34 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-18 01:55:34 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-18 01:55:34 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 04-18 01:55:35 config.py:549] This model supports multiple tasks: {'reward', 'generate', 'score', 'embed', 'classify'}. Defaulting to 'generate'.
INFO 04-18 01:55:43 config.py:549] This model supports multiple tasks: {'classify', 'embed', 'reward', 'generate', 'score'}. Defaulting to 'generate'.
INFO 04-18 01:55:44 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/models/Qwen2.5-7B-Instruct/', speculative_config=None, tokenizer='/models/Qwen2.5-7B-Instruct/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=26240, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/models/Qwen2.5-7B-Instruct/, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning: 
    *************************************************************************************************************
    The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now..
    The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now..
    The backend in torch.distributed.init_process_group set to hccl now..
    The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now..
    The device parameters have been replaced with npu in the function below:
    torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty
    *************************************************************************************************************
    
  warnings.warn(msg, ImportWarning)
/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu.
  warnings.warn(msg, RuntimeWarning)
WARNING 04-18 01:55:44 utils.py:2262] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd42217880>
ERROR 04-18 01:55:45 engine.py:400] SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
ERROR 04-18 01:55:45 engine.py:400] [ERROR] 2025-04-18-01:55:45 (PID:352, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 04-18 01:55:45 engine.py:400] [Error]: The internal ACL of the system is incorrect.
ERROR 04-18 01:55:45 engine.py:400]         Rectify the fault based on the error information in the ascend log.
ERROR 04-18 01:55:45 engine.py:400] EH9999: Inner Error!
ERROR 04-18 01:55:45 engine.py:400] EH9999: [PID: 352] 2025-04-18-01:55:45.332.619 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 04-18 01:55:45 engine.py:400]         TraceBack (most recent call last):
ERROR 04-18 01:55:45 engine.py:400]        GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
ERROR 04-18 01:55:45 engine.py:400]        GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
ERROR 04-18 01:55:45 engine.py:400]        [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 04-18 01:55:45 engine.py:400]        [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 04-18 01:55:45 engine.py:400]        [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 04-18 01:55:45 engine.py:400] Traceback (most recent call last):
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 04-18 01:55:45 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
ERROR 04-18 01:55:45 engine.py:400]     return cls(ipc_path=ipc_path,
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
ERROR 04-18 01:55:45 engine.py:400]     self.engine = LLMEngine(*args, **kwargs)
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
ERROR 04-18 01:55:45 engine.py:400]     self.model_executor = executor_class(vllm_config=vllm_config, )
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
ERROR 04-18 01:55:45 engine.py:400]     self._init_executor()
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 46, in _init_executor
ERROR 04-18 01:55:45 engine.py:400]     self.collective_rpc("init_device")
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 04-18 01:55:45 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 04-18 01:55:45 engine.py:400]     return func(*args, **kwargs)
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 164, in init_device
ERROR 04-18 01:55:45 engine.py:400]     NPUPlatform.set_device(self.device)
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/platform.py", line 103, in set_device
ERROR 04-18 01:55:45 engine.py:400]     torch.npu.set_device(device)
ERROR 04-18 01:55:45 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 83, in set_device
ERROR 04-18 01:55:45 engine.py:400]     torch_npu._C._npu_setDevice(device_id)
ERROR 04-18 01:55:45 engine.py:400] RuntimeError: SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
ERROR 04-18 01:55:45 engine.py:400] [ERROR] 2025-04-18-01:55:45 (PID:352, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 04-18 01:55:45 engine.py:400] [Error]: The internal ACL of the system is incorrect.
ERROR 04-18 01:55:45 engine.py:400]         Rectify the fault based on the error information in the ascend log.
ERROR 04-18 01:55:45 engine.py:400] EH9999: Inner Error!
ERROR 04-18 01:55:45 engine.py:400] EH9999: [PID: 352] 2025-04-18-01:55:45.332.619 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 04-18 01:55:45 engine.py:400]         TraceBack (most recent call last):
ERROR 04-18 01:55:45 engine.py:400]        GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
ERROR 04-18 01:55:45 engine.py:400]        GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
ERROR 04-18 01:55:45 engine.py:400]        [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 04-18 01:55:45 engine.py:400]        [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 04-18 01:55:45 engine.py:400]        [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 04-18 01:55:45 engine.py:400] 
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
    return cls(ipc_path=ipc_path,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config, )
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 46, in _init_executor
    self.collective_rpc("init_device")
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 164, in init_device
    NPUPlatform.set_device(self.device)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/platform.py", line 103, in set_device
    torch.npu.set_device(device)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 83, in set_device
    torch_npu._C._npu_setDevice(device_id)
RuntimeError: SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
[ERROR] 2025-04-18-01:55:45 (PID:352, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The internal ACL of the system is incorrect.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
EH9999: [PID: 352] 2025-04-18-01:55:45.332.619 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
       GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
       GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
       [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
       [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
       [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

/usr/local/python3.10/lib/python3.10/tempfile.py:869: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/tmp/tmppo6xwne6'>
  _warnings.warn(warn_message, ResourceWarning)
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 233, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-04-18-01:55:47 (PID:280, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
root@ea451a232c03:/workspace# 
root@ea451a232c03:/workspace# 
root@ea451a232c03:/workspace# 
```

Is there any problem of installation of driver or cann? what should I do to make it running correctly? Thanks
