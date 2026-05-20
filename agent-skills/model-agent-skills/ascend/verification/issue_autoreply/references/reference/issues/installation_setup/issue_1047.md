# Issue #1047: [Usage]: 部署vllm-ascend报错

## 基本信息

- **编号**: #1047
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1047
- **创建时间**: 2025-06-03T07:14:43Z
- **关闭时间**: 2025-07-13T09:47:25Z
- **更新时间**: 2025-07-13T09:47:25Z
- **提交者**: @bottleofwater11
- **评论数**: 2

## 标签

module:mindie-turbo

## 问题描述

### Your current environment

[root@51442de2b6e3 LLMs]# npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910ProB             | OK            | 78.0        38                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           2387 / 13553      18   / 32768         |
+===========================+===============+====================================================+
| 1     910ProB             | OK            | 75.8        38                0    / 0             |
| 0                         | 0000:81:00.0  | 0           1840 / 15665      8    / 32768         |
+===========================+===============+====================================================+
| 2     910ProB             | OK            | 78.2        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           2512 / 15665      5    / 32768         |
+===========================+===============+====================================================+
| 3     910ProB             | OK            | 76.5        39                0    / 0             |
| 0                         | 0000:01:00.0  | 0           1645 / 15567      4    / 32768         |
+===========================+===============+====================================================+
| 4     910ProB             | OK            | 78.8        38                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           1520 / 13553      10   / 32768         |
+===========================+===============+====================================================+
| 5     910ProB             | OK            | 77.0        38                0    / 0             |
| 0                         | 0000:82:00.0  | 0           2639 / 15665      14   / 32768         |
+===========================+===============+====================================================+
| 6     910ProB             | OK            | 83.0        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           2143 / 15665      3    / 32768         |
+===========================+===============+====================================================+
| 7     910ProB             | OK            | 77.3        38                0    / 0             |
| 0                         | 0000:02:00.0  | 0           2088 / 15567      2    / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
[root@51442de2b6e3 LLMs]# cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux


### How would you like to use vllm on ascend

操作步骤：按mindie turbo文档构建镜像，修改dockerfile（容器git失败，下载到本地进行的）

################################################## 4. Install vLLM  && vLLM_Ascned ##################################################

FROM cann AS vllm

COPY ./vllm /tmp/vllm

RUN cd /tmp/vllm && \

    git init -q && \

    git config user.email "builder@example.com" && \

    git config user.name  "Builder" && \

    git add -A && \

    git commit -qm "init for build" && \

    git tag -a v0.7.3 -m "v0.7.3"

RUN pip install --no-cache-dir numpy==1.26.4

WORKDIR /tmp/vllm

RUN pip install -r requirements-common.txt \

    -r requirements-build.txt && \

    VLLM_TARGET_DEVICE=empty pip install .

COPY ./vllm-ascend /tmp/vllm-ascend

RUN pip install /tmp/vllm-ascend

2、镜像构建完成后把DeepSeek-R1-Distill-Qwen-32B 及 Qwen2.5-1.5B-Instruct放到/data/LLMs中运行vllm指令
vllm serve /data/LLMs/Qwen2.5-1.5B-Instruct --dtype auto --port 8000 因为运行DS模型会报错OOM，好像是单卡执行的，想跑起来因此先找了一个小模型
日志报错如下：
 

[root@51442de2b6e3 opp_kernel]# vllm serve /data/LLMs/Qwen2.5-1.5B-Instruct --dtype auto --port 8000 

INFO 06-03 14:53:47 __init__.py:30] Available plugins for group vllm.platform_plugins: 

INFO 06-03 14:53:47 __init__.py:32] name=ascend, value=vllm_ascend:register 

INFO 06-03 14:53:47 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded. 

INFO 06-03 14:53:47 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. 

INFO 06-03 14:53:47 __init__.py:44] plugin ascend loaded. 

INFO 06-03 14:53:47 __init__.py:198] Platform plugin ascend is activated 

WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled 

INFO 06-03 14:53:47 __init__.py:30] Available plugins for group vllm.general_plugins: 

INFO 06-03 14:53:47 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model 

INFO 06-03 14:53:47 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded. 

INFO 06-03 14:53:47 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. 

INFO 06-03 14:53:47 __init__.py:44] plugin ascend_enhanced_model loaded. 

WARNING 06-03 14:53:47 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration. 

WARNING 06-03 14:53:47 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration. 

WARNING 06-03 14:53:47 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM. 

WARNING 06-03 14:53:47 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM. 

WARNING 06-03 14:53:47 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP. 

INFO 06-03 14:53:47 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available. 

INFO 06-03 14:53:47 api_server.py:912] vLLM API server version 0.7.3 

INFO 06-03 14:53:47 api_server.py:913] args: Namespace(subparser='serve', model_tag='/data/LLMs/Qwen2.5-1.5B-Instruct', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/data/LLMs/Qwen2.5-1.5B-Instruct', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffebe43ff60>) 

INFO 06-03 14:53:47 api_server.py:209] Started engine process with PID 8648 

INFO 06-03 14:53:54 __init__.py:30] Available plugins for group vllm.platform_plugins: 

INFO 06-03 14:53:54 __init__.py:32] name=ascend, value=vllm_ascend:register 

INFO 06-03 14:53:54 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded. 

INFO 06-03 14:53:54 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. 

INFO 06-03 14:53:54 __init__.py:44] plugin ascend loaded. 

INFO 06-03 14:53:54 __init__.py:198] Platform plugin ascend is activated 

WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled 

INFO 06-03 14:53:54 __init__.py:30] Available plugins for group vllm.general_plugins: 

INFO 06-03 14:53:54 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model 

INFO 06-03 14:53:54 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded. 

INFO 06-03 14:53:54 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. 

INFO 06-03 14:53:54 __init__.py:44] plugin ascend_enhanced_model loaded. 

WARNING 06-03 14:53:54 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration. 

WARNING 06-03 14:53:54 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration. 

WARNING 06-03 14:53:54 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM. 

WARNING 06-03 14:53:54 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM. 

WARNING 06-03 14:53:54 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP. 

INFO 06-03 14:53:54 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available. 

INFO 06-03 14:53:56 config.py:549] This model supports multiple tasks: {'classify', 'embed', 'reward', 'generate', 'score'}. Defaulting to 'generate'. 

INFO 06-03 14:54:03 config.py:549] This model supports multiple tasks: {'embed', 'classify', 'generate', 'score', 'reward'}. Defaulting to 'generate'. 

INFO 06-03 14:54:03 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/data/LLMs/Qwen2.5-1.5B-Instruct', speculative_config=None, tokenizer='/data/LLMs/Qwen2.5-1.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/data/LLMs/Qwen2.5-1.5B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True,  

ERROR 06-03 14:54:04 camem.py:69] Failed to import vllm_ascend_C:No module named 'vllm_ascend.vllm_ascend_C' 

/usr/local/python/lib/python3.11/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning:  

    ************************************************************************************************************* 

    The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now.. 

    The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now.. 

    The backend in torch.distributed.init_process_group set to hccl now.. 

    The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now.. 

    The device parameters have been replaced with npu in the function below: 

    torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty 

    ************************************************************************************************************* 

     

  warnings.warn(msg, ImportWarning) 

/usr/local/python/lib/python3.11/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu. 

  warnings.warn(msg, RuntimeWarning) 

WARNING 06-03 14:54:04 utils.py:2262] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffe3074c6d0> 

WARNING 06-03 14:54:04 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") 

INFO 06-03 14:54:04 utils.py:33] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo. 

INFO 06-03 14:54:16 model_runner.py:902] Starting to load model /data/LLMs/Qwen2.5-1.5B-Instruct... 

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s] 

Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:04<00:00,  4.46s/it] 

Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:04<00:00,  4.46s/it] 

 
INFO 06-03 14:54:22 model_runner.py:907] Loading model weights took 2.8866 GB 

ERROR 06-03 14:54:23 engine.py:400] The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RMSNormOperation. 

ERROR 06-03 14:54:23 engine.py:400] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1. 

ERROR 06-03 14:54:23 engine.py:400] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging. 

ERROR 06-03 14:54:23 engine.py:400] [ERROR] 2025-06-03-14:54:23 (PID:8648, Device:0, RankID:-1) ERR00100 PTA call acl api failed. 

ERROR 06-03 14:54:23 engine.py:400] Traceback (most recent call last): 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine 

ERROR 06-03 14:54:23 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args, 

ERROR 06-03 14:54:23 engine.py:400]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args 

ERROR 06-03 14:54:23 engine.py:400]     return cls(ipc_path=ipc_path, 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__ 

ERROR 06-03 14:54:23 engine.py:400]     self.engine = LLMEngine(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 276, in __init__ 

ERROR 06-03 14:54:23 engine.py:400]     self._initialize_kv_caches() 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches 

ERROR 06-03 14:54:23 engine.py:400]     self.model_executor.determine_num_available_blocks()) 

ERROR 06-03 14:54:23 engine.py:400]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks 

ERROR 06-03 14:54:23 engine.py:400]     results = self.collective_rpc("determine_num_available_blocks") 

ERROR 06-03 14:54:23 engine.py:400]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc 

ERROR 06-03 14:54:23 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs) 

ERROR 06-03 14:54:23 engine.py:400]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/utils.py", line 2196, in run_method 

ERROR 06-03 14:54:23 engine.py:400]     return func(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context 

ERROR 06-03 14:54:23 engine.py:400]     return func(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm_ascend/worker/worker.py", line 255, in determine_num_available_blocks 

ERROR 06-03 14:54:23 engine.py:400]     self.model_runner.profile_run() 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context 

ERROR 06-03 14:54:23 engine.py:400]     return func(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm_ascend/worker/model_runner.py", line 1490, in profile_run 

ERROR 06-03 14:54:23 engine.py:400]     self.execute_model(model_input, kv_caches, intermediate_tensors) 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context 

ERROR 06-03 14:54:23 engine.py:400]     return func(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm_ascend/worker/model_runner.py", line 1270, in execute_model 

ERROR 06-03 14:54:23 engine.py:400]     hidden_or_intermediate_states = model_executable( 

ERROR 06-03 14:54:23 engine.py:400]                                     ^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return self._call_impl(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return forward_call(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward 

ERROR 06-03 14:54:23 engine.py:400]     hidden_states = self.model(input_ids, positions, kv_caches, 

ERROR 06-03 14:54:23 engine.py:400]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/compilation/decorators.py", line 172, in __call__ 

ERROR 06-03 14:54:23 engine.py:400]     return self.forward(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward 

ERROR 06-03 14:54:23 engine.py:400]     hidden_states, residual = layer( 

ERROR 06-03 14:54:23 engine.py:400]                               ^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return self._call_impl(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return forward_call(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 247, in forward 

ERROR 06-03 14:54:23 engine.py:400]     hidden_states = self.self_attn( 

ERROR 06-03 14:54:23 engine.py:400]                     ^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return self._call_impl(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return forward_call(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 178, in forward 

ERROR 06-03 14:54:23 engine.py:400]     q, k = self.rotary_emb(positions, q, k) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return self._call_impl(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

ERROR 06-03 14:54:23 engine.py:400]     return forward_call(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/custom_op.py", line 25, in forward 

ERROR 06-03 14:54:23 engine.py:400]     return self._forward_method(*args, **kwargs) 

ERROR 06-03 14:54:23 engine.py:400]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400]   File "/usr/local/python/lib/python3.11/site-packages/mindie_turbo/adaptor/vllm/ops.py", line 35, in rope_forward_oot 

ERROR 06-03 14:54:23 engine.py:400]     query, key = turbo_torch.rotary_embedding( 

ERROR 06-03 14:54:23 engine.py:400]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

ERROR 06-03 14:54:23 engine.py:400] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RMSNormOperation. 

ERROR 06-03 14:54:23 engine.py:400] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1. 

ERROR 06-03 14:54:23 engine.py:400] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging. 

ERROR 06-03 14:54:23 engine.py:400] [ERROR] 2025-06-03-14:54:23 (PID:8648, Device:0, RankID:-1) ERR00100 PTA call acl api failed. 

ERROR 06-03 14:54:23 engine.py:400]  

Process SpawnProcess-1: 

Traceback (most recent call last): 

  File "/usr/local/python/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap 

    self.run() 

  File "/usr/local/python/lib/python3.11/multiprocessing/process.py", line 108, in run 

    self._target(*self._args, **self._kwargs) 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine 

    raise e 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine 

    engine = MQLLMEngine.from_engine_args(engine_args=engine_args, 

             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args 

    return cls(ipc_path=ipc_path, 

           ^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__ 

    self.engine = LLMEngine(*args, **kwargs) 

                  ^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 276, in __init__ 

    self._initialize_kv_caches() 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches 

    self.model_executor.determine_num_available_blocks()) 

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks 

    results = self.collective_rpc("determine_num_available_blocks") 

              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc 

    answer = run_method(self.driver_worker, method, args, kwargs) 

             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/utils.py", line 2196, in run_method 

    return func(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context 

    return func(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm_ascend/worker/worker.py", line 255, in determine_num_available_blocks 

    self.model_runner.profile_run() 

  File "/usr/local/python/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context 

    return func(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm_ascend/worker/model_runner.py", line 1490, in profile_run 

    self.execute_model(model_input, kv_caches, intermediate_tensors) 

  File "/usr/local/python/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context 

    return func(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm_ascend/worker/model_runner.py", line 1270, in execute_model 

    hidden_or_intermediate_states = model_executable( 

                                    ^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

    return self._call_impl(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

    return forward_call(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward 

    hidden_states = self.model(input_ids, positions, kv_caches, 

                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/compilation/decorators.py", line 172, in __call__ 

    return self.forward(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward 

    hidden_states, residual = layer( 

                              ^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

    return self._call_impl(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

    return forward_call(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 247, in forward 

    hidden_states = self.self_attn( 

                    ^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

    return self._call_impl(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

    return forward_call(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/models/qwen2.py", line 178, in forward 

    q, k = self.rotary_emb(positions, q, k) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl 

    return self._call_impl(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl 

    return forward_call(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/model_executor/custom_op.py", line 25, in forward 

    return self._forward_method(*args, **kwargs) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/mindie_turbo/adaptor/vllm/ops.py", line 35, in rope_forward_oot 

    query, key = turbo_torch.rotary_embedding( 

                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is RMSNormOperation. 

Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1. 

Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging. 

[ERROR] 2025-06-03-14:54:23 (PID:8648, Device:0, RankID:-1) ERR00100 PTA call acl api failed. 

 
Traceback (most recent call last): 

  File "/usr/local/python/bin/vllm", line 8, in <module> 

    sys.exit(main()) 

             ^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 73, in main 

    args.dispatch_function(args) 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd 

    uvloop.run(run_server(args)) 

  File "/usr/local/python/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run 

    return runner.run(wrapper()) 

           ^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/asyncio/runners.py", line 118, in run 

    return self._loop.run_until_complete(task) 

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete 

  File "/usr/local/python/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper 

    return await main 

           ^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server 

    async with build_async_engine_client(args) as engine_client: 

  File "/usr/local/python/lib/python3.11/contextlib.py", line 210, in __aenter__ 

    return await anext(self.gen) 

           ^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client 

    async with build_async_engine_client_from_engine_args( 

  File "/usr/local/python/lib/python3.11/contextlib.py", line 210, in __aenter__ 

    return await anext(self.gen) 

           ^^^^^^^^^^^^^^^^^^^^^ 

  File "/usr/local/python/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 233, in build_async_engine_client_from_engine_args 

    raise RuntimeError( 

RuntimeError: Engine process failed to start. See stack trace for the root cause. 

[ERROR] 2025-06-03-14:54:28 (PID:8578, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception 

