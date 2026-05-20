# Issue #302: [Bug]: docker运行报错

## 基本信息

- **编号**: #302
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/302
- **创建时间**: 2025-03-11T15:01:19Z
- **关闭时间**: 2025-03-12T01:51:40Z
- **更新时间**: 2025-03-12T01:51:40Z
- **提交者**: @wang-benqiang
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment


显卡：910B2*8

驱动：24.1.rc3

CPU: Kunpeng-920

### 🐛 Describe the bug

<details>
<summary>docker run --name vllm-ascend --device /dev/davinci0 --device /dev/davinci_manager --device /dev/devmm_svm --device /dev/hisi_hdc -v /usr/local/dcmi:/usr/local/dcmi -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info -v /etc/ascend_install.info:/etc/ascend_install.info -v /root/.cache:/root/.cache -p 8000:8000 -e VLLM_USE_MODELSCOPE=True -e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 -it quay.io/ascend/vllm-ascend:v0.7.1rc1 vllm serve Qwen/Qwen2.5-7B-Instruct --max_model_len 26240</summary>

```text
INFO 03-11 14:47:26 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-11 14:47:26 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-11 14:47:26 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-11 14:47:26 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-11 14:47:26 __init__.py:42] plugin ascend loaded.
INFO 03-11 14:47:27 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-11 14:47:27 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-11 14:47:27 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-11 14:47:27 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-11 14:47:27 __init__.py:42] plugin ascend loaded.
INFO 03-11 14:47:27 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-11 14:47:27 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-11 14:47:27 __init__.py:174] Platform plugin ascend is activated
INFO 03-11 14:47:29 api_server.py:838] vLLM API server version 0.7.1
INFO 03-11 14:47:29 api_server.py:839] args: Namespace(subparser='serve', model_tag='Qwen/Qwen2.5-7B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='Qwen/Qwen2.5-7B-Instruct', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=26240, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function serve at 0xfffd3590d750>)
INFO 03-11 14:47:29 api_server.py:204] Started engine process with PID 270
2025-03-11 14:47:30,009 - modelscope - INFO - Legacy cache dir exists: /root/.cache/modelscope/hub/Qwen/Qwen2___5-7B-Instruct, move to /root/.cache/modelscope/hub/models/Qwen/Qwen2___5-7B-Instruct
Downloading Model to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct
2025-03-11 14:47:30,375 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-11 14:47:30,773 - modelscope - INFO - Creating symbolic link [/root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct].
Downloading Model to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct
2025-03-11 14:47:31,182 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-11 14:47:31,468 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 03-11 14:47:36 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-11 14:47:36 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-11 14:47:36 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-11 14:47:36 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-11 14:47:36 __init__.py:42] plugin ascend loaded.
INFO 03-11 14:47:37 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-11 14:47:37 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-11 14:47:37 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-11 14:47:37 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-11 14:47:37 __init__.py:42] plugin ascend loaded.
INFO 03-11 14:47:37 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-11 14:47:37 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-11 14:47:37 __init__.py:174] Platform plugin ascend is activated
Downloading Model to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct
2025-03-11 14:47:39,900 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-11 14:47:40,230 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct
2025-03-11 14:47:40,550 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-11 14:47:40,844 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 03-11 14:47:46 config.py:526] This model supports multiple tasks: {'score', 'classify', 'generate', 'embed', 'reward'}. Defaulting to 'generate'.
INFO 03-11 14:47:46 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
Downloading Model to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct
2025-03-11 14:47:47,041 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 03-11 14:47:56 config.py:526] This model supports multiple tasks: {'embed', 'reward', 'generate', 'score', 'classify'}. Defaulting to 'generate'.
INFO 03-11 14:47:56 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 03-11 14:47:56 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='Qwen/Qwen2.5-7B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=26240, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=Qwen/Qwen2.5-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True,
Downloading Model to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct
2025-03-11 14:47:57,573 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-7B-Instruct
2025-03-11 14:47:58,558 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-03-11 14:47:58,868 - modelscope - INFO - Target directory already exists, skipping creation.
ERROR 03-11 14:48:04 engine.py:387] Initialize:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:251 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
ERROR 03-11 14:48:04 engine.py:387] [ERROR] 2025-03-11-14:48:04 (PID:270, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 03-11 14:48:04 engine.py:387] [Error]: The internal ACL of the system is incorrect.
ERROR 03-11 14:48:04 engine.py:387]         Rectify the fault based on the error information in the ascend log.
ERROR 03-11 14:48:04 engine.py:387] EH9999: Inner Error!
ERROR 03-11 14:48:04 engine.py:387] EH9999: [PID: 270] 2025-03-11-14:48:04.576.431 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-11 14:48:04 engine.py:387]         TraceBack (most recent call last):
ERROR 03-11 14:48:04 engine.py:387]        GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
ERROR 03-11 14:48:04 engine.py:387]        GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
ERROR 03-11 14:48:04 engine.py:387]        [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 03-11 14:48:04 engine.py:387]        [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-11 14:48:04 engine.py:387]        [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-11 14:48:04 engine.py:387] Traceback (most recent call last):
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine
ERROR 03-11 14:48:04 engine.py:387]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 121, in from_engine_args
ERROR 03-11 14:48:04 engine.py:387]     return cls(ipc_path=ipc_path,
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 73, in __init__
ERROR 03-11 14:48:04 engine.py:387]     self.engine = LLMEngine(*args, **kwargs)
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 271, in __init__
ERROR 03-11 14:48:04 engine.py:387]     self.model_executor = executor_class(vllm_config=vllm_config, )
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 49, in __init__
ERROR 03-11 14:48:04 engine.py:387]     self._init_executor()
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 39, in _init_executor
ERROR 03-11 14:48:04 engine.py:387]     self.collective_rpc("init_device")
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 49, in collective_rpc
ERROR 03-11 14:48:04 engine.py:387]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
ERROR 03-11 14:48:04 engine.py:387]     return func(*args, **kwargs)
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker.py", line 173, in init_device
ERROR 03-11 14:48:04 engine.py:387]     current_platform.set_device(self.device)
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/platform.py", line 83, in set_device
ERROR 03-11 14:48:04 engine.py:387]     torch.npu.set_device(device)
ERROR 03-11 14:48:04 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 58, in set_device
ERROR 03-11 14:48:04 engine.py:387]     torch_npu._C._npu_setDevice(device_id)
ERROR 03-11 14:48:04 engine.py:387] RuntimeError: Initialize:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:251 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
ERROR 03-11 14:48:04 engine.py:387] [ERROR] 2025-03-11-14:48:04 (PID:270, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 03-11 14:48:04 engine.py:387] [Error]: The internal ACL of the system is incorrect.
ERROR 03-11 14:48:04 engine.py:387]         Rectify the fault based on the error information in the ascend log.
ERROR 03-11 14:48:04 engine.py:387] EH9999: Inner Error!
ERROR 03-11 14:48:04 engine.py:387] EH9999: [PID: 270] 2025-03-11-14:48:04.576.431 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-11 14:48:04 engine.py:387]         TraceBack (most recent call last):
ERROR 03-11 14:48:04 engine.py:387]        GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
ERROR 03-11 14:48:04 engine.py:387]        GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
ERROR 03-11 14:48:04 engine.py:387]        [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 03-11 14:48:04 engine.py:387]        [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-11 14:48:04 engine.py:387]        [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 03-11 14:48:04 engine.py:387]
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 389, in run_mp_engine
    raise e
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 121, in from_engine_args
    return cls(ipc_path=ipc_path,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 73, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 271, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config, )
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 49, in __init__
    self._init_executor()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 39, in _init_executor
    self.collective_rpc("init_device")
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 49, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker.py", line 173, in init_device
    current_platform.set_device(self.device)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/platform.py", line 83, in set_device
    torch.npu.set_device(device)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 58, in set_device
    torch_npu._C._npu_setDevice(device_id)
RuntimeError: Initialize:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:251 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
[ERROR] 2025-03-11-14:48:04 (PID:270, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The internal ACL of the system is incorrect.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
EH9999: [PID: 270] 2025-03-11-14:48:04.576.431 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
       GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:177]
       GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:337]
       [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
       [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
       [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/scripts.py", line 202, in main
    args.dispatch_function(args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/scripts.py", line 42, in serve
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 873, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 134, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 228, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-03-11-14:48:07 (PID:1, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

</details>
