# Issue #622: [Bug]: v0.8.4rc2运行qwen-vl-72B-instruct会导致机器重启

## 基本信息

- **编号**: #622
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/622
- **创建时间**: 2025-04-22T11:28:58Z
- **关闭时间**: 2025-07-12T17:26:29Z
- **更新时间**: 2025-07-12T17:26:29Z
- **提交者**: @15626471095
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

```text
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 91.1        49                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 91.6        50                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3373 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 88.1        48                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 92.4        50                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3375 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 91.7        50                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 92.1        52                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3374 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 90.9        49                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3373 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 87.8        50                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3375 / 65536         |
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


package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux


Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.86.r1526_92.hce2.aarch64-aarch64-with-glibc2.35
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] transformers==4.50.3
[conda] Could not collect
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.7.3
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
```



###  Describe the bug

运行qwen2.5-vl-72B-instruct稳定重启。运行qwen2.5-72B-instruct没有问题

![Image](https://github.com/user-attachments/assets/38a3c187-7568-4e29-a370-5ae86d4b72bd)

vllm日志
```text
INFO 04-22 11:23:52 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:23:52 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:23:52 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:23:52 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:23:52 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:23:52 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:23:55 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-22 11:23:55 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-22 11:23:55 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-22 11:23:55 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:23:55 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 04-22 11:23:55 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 04-22 11:23:55 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 04-22 11:23:55 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-22 11:23:55 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-22 11:23:55 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-22 11:23:56 [api_server.py:1034] vLLM API server version 0.8.4
INFO 04-22 11:23:56 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='/share/model/Qwen/Qwen2.5-VL-72B-Instruct', config='', host='0.0.0.0', port=8085, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=True, tool_call_parser='hermes', tool_parser_plugin='', model='/share/model/Qwen/Qwen2.5-VL-72B-Instruct', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, load_format='auto', download_dir=None, model_loader_extra_config=None, use_tqdm_on_load=True, config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=8, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, disable_custom_all_reduce=False, block_size=None, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.95, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_token=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt={'image': 10}, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['Qwen2.5-VL-72B-Instruct'], qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, enable_reasoning=False, reasoning_parser=None, disable_cascade_attn=False, disable_chunked_mm_input=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffdba699c60>)
INFO 04-22 11:24:07 [config.py:689] This model supports multiple tasks: {'reward', 'score', 'classify', 'embed', 'generate'}. Defaulting to 'generate'.
INFO 04-22 11:24:07 [arg_utils.py:1742] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
INFO 04-22 11:24:07 [config.py:1713] Defaulting to use mp for distributed inference
INFO 04-22 11:24:07 [config.py:1747] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 04-22 11:24:07 [api_server.py:246] Started engine process with PID 3684
INFO 04-22 11:24:13 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:13 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:13 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:13 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:13 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:13 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:16 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-22 11:24:16 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-22 11:24:16 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-22 11:24:16 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:16 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 04-22 11:24:16 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 04-22 11:24:16 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 04-22 11:24:16 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-22 11:24:16 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-22 11:24:16 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-22 11:24:16 [llm_engine.py:243] Initializing a V0 LLM engine (v0.8.4) with config: model='/share/model/Qwen/Qwen2.5-VL-72B-Instruct', speculative_config=None, tokenizer='/share/model/Qwen/Qwen2.5-VL-72B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=Qwen2.5-VL-72B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
WARNING 04-22 11:24:17 [multiproc_worker_utils.py:306] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
WARNING 04-22 11:24:17 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffdbcffa410>
INFO 04-22 11:24:23 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:23 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:23 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:23 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:23 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:23 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:24 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:24 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:24 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:24 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:24 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:24 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:24 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:24 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:24 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:24 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:24 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:24 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:24 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:24 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:24 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:24 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:24 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:24 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:24 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:24 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:24 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:24 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:24 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:24 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:24 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:24 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:24 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:24 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:24 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:24 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:24 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:24 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:24 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:24 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:24 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:24 [__init__.py:230] Platform plugin ascend is activated
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:26 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:26 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:26 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:26 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:26 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:26 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=3821) WARNING 04-22 11:24:26 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:26 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:26 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:26 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:26 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:26 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:26 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=3826) WARNING 04-22 11:24:26 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:26 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:26 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:26 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:26 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:26 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:26 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:26 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:27 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=3827) WARNING 04-22 11:24:27 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=3821) WARNING 04-22 11:24:27 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=3821) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=3821) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:27 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:27 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:27 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:27 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:27 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:27 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:27 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=3826) WARNING 04-22 11:24:27 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=3826) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=3826) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=3822) WARNING 04-22 11:24:27 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:27 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=3821) WARNING 04-22 11:24:27 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff56112800>
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:27 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=3827) WARNING 04-22 11:24:27 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=3827) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=3827) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:27 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:27 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:27 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:27 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:27 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=3824) WARNING 04-22 11:24:27 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=3826) WARNING 04-22 11:24:27 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff8e1a27a0>
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:27 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:27 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=3822) WARNING 04-22 11:24:27 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=3822) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=3822) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:27 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:27 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:27 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:27 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:27 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=3827) WARNING 04-22 11:24:27 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff68fb2830>
(VllmWorkerProcess pid=3823) WARNING 04-22 11:24:27 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:27 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:27 [__init__.py:30] Available plugins for group vllm.general_plugins:
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:27 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:27 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:27 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:27 [__init__.py:44] plugin ascend_enhanced_model loaded.
(VllmWorkerProcess pid=3824) WARNING 04-22 11:24:27 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=3824) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=3824) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:27 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=3825) WARNING 04-22 11:24:27 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=3822) WARNING 04-22 11:24:27 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff69702800>
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:27 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(VllmWorkerProcess pid=3823) WARNING 04-22 11:24:27 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=3823) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=3823) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=3824) WARNING 04-22 11:24:27 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff5d1127a0>
(VllmWorkerProcess pid=3825) WARNING 04-22 11:24:27 [registry.py:380] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=3825) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=3825) WARNING 04-22 11:24:27 [registry.py:380] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=3823) WARNING 04-22 11:24:27 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff7b4b2830>
(VllmWorkerProcess pid=3825) WARNING 04-22 11:24:27 [utils.py:2444] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff5c7127a0>
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
INFO 04-22 11:24:38 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 11:24:38 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 11:24:38 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 11:24:38 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 11:24:38 [__init__.py:44] plugin ascend loaded.
INFO 04-22 11:24:38 [__init__.py:230] Platform plugin ascend is activated
[rank3]:[W422 11:24:43.878198894 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank1]:[W422 11:24:43.878277644 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank2]:[W422 11:24:43.878920745 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank5]:[W422 11:24:43.895239367 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank7]:[W422 11:24:43.945343934 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank4]:[W422 11:24:43.990094205 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank0]:[W422 11:24:43.011589464 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
[rank6]:[W422 11:24:43.013449237 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
INFO 04-22 11:24:43 [shm_broadcast.py:264] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_cadf330f'), local_subscribe_addr='ipc:///tmp/6fb0858e-817a-4ada-a9e5-aba891eca35d', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 04-22 11:24:43 [parallel_state.py:959] rank 0 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 0
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:44 [parallel_state.py:959] rank 7 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 7
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:44 [parallel_state.py:959] rank 3 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 3
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:44 [parallel_state.py:959] rank 5 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 5
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:44 [parallel_state.py:959] rank 1 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 1
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:44 [parallel_state.py:959] rank 2 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 2
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:44 [parallel_state.py:959] rank 4 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 4
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:44 [parallel_state.py:959] rank 6 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 6
INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:44 [model_runner.py:899] Starting to load model /share/model/Qwen/Qwen2.5-VL-72B-Instruct...
INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=3822) INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=3827) INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=3824) INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=3821) INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=3825) INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=3823) INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=3826) INFO 04-22 11:24:44 [config.py:3466] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
Loading safetensors checkpoint shards:   0% Completed | 0/38 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   3% Completed | 1/38 [00:00<00:18,  1.96it/s]
Loading safetensors checkpoint shards:   5% Completed | 2/38 [00:00<00:17,  2.05it/s]
Loading safetensors checkpoint shards:   8% Completed | 3/38 [00:01<00:18,  1.91it/s]
Loading safetensors checkpoint shards:  11% Completed | 4/38 [00:02<00:18,  1.86it/s]
Loading safetensors checkpoint shards:  13% Completed | 5/38 [00:02<00:18,  1.80it/s]
Loading safetensors checkpoint shards:  16% Completed | 6/38 [00:03<00:19,  1.67it/s]
Loading safetensors checkpoint shards:  18% Completed | 7/38 [00:03<00:18,  1.67it/s]
Loading safetensors checkpoint shards:  21% Completed | 8/38 [00:04<00:17,  1.69it/s]
Loading safetensors checkpoint shards:  24% Completed | 9/38 [00:05<00:18,  1.60it/s]
Loading safetensors checkpoint shards:  26% Completed | 10/38 [00:05<00:17,  1.61it/s]
Loading safetensors checkpoint shards:  29% Completed | 11/38 [00:06<00:17,  1.55it/s]
Loading safetensors checkpoint shards:  32% Completed | 12/38 [00:07<00:15,  1.63it/s]
Loading safetensors checkpoint shards:  34% Completed | 13/38 [00:07<00:14,  1.68it/s]
Loading safetensors checkpoint shards:  37% Completed | 14/38 [00:08<00:14,  1.69it/s]
Loading safetensors checkpoint shards:  39% Completed | 15/38 [00:08<00:13,  1.66it/s]
Loading safetensors checkpoint shards:  42% Completed | 16/38 [00:09<00:13,  1.64it/s]
Loading safetensors checkpoint shards:  45% Completed | 17/38 [00:10<00:12,  1.65it/s]
Loading safetensors checkpoint shards:  47% Completed | 18/38 [00:10<00:11,  1.67it/s]
Loading safetensors checkpoint shards:  50% Completed | 19/38 [00:11<00:11,  1.68it/s]
Loading safetensors checkpoint shards:  53% Completed | 20/38 [00:11<00:10,  1.69it/s]
Loading safetensors checkpoint shards:  55% Completed | 21/38 [00:12<00:10,  1.69it/s]
Loading safetensors checkpoint shards:  58% Completed | 22/38 [00:13<00:09,  1.69it/s]
Loading safetensors checkpoint shards:  61% Completed | 23/38 [00:13<00:09,  1.66it/s]
Loading safetensors checkpoint shards:  63% Completed | 24/38 [00:14<00:08,  1.63it/s]
Loading safetensors checkpoint shards:  66% Completed | 25/38 [00:14<00:06,  2.05it/s]
Loading safetensors checkpoint shards:  68% Completed | 26/38 [00:15<00:06,  1.89it/s]
Loading safetensors checkpoint shards:  71% Completed | 27/38 [00:15<00:06,  1.70it/s]
Loading safetensors checkpoint shards:  74% Completed | 28/38 [00:16<00:06,  1.59it/s]
(VllmWorkerProcess pid=3823) INFO 04-22 11:25:02 [loader.py:458] Loading weights took 16.90 seconds
Loading safetensors checkpoint shards:  76% Completed | 29/38 [00:17<00:05,  1.61it/s]
(VllmWorkerProcess pid=3823) INFO 04-22 11:25:02 [model_runner.py:904] Loading model weights took 17.2832 GB
(VllmWorkerProcess pid=3825) INFO 04-22 11:25:02 [loader.py:458] Loading weights took 17.43 seconds
Loading safetensors checkpoint shards:  79% Completed | 30/38 [00:17<00:04,  1.63it/s]
(VllmWorkerProcess pid=3825) INFO 04-22 11:25:03 [model_runner.py:904] Loading model weights took 17.2832 GB
(VllmWorkerProcess pid=3827) INFO 04-22 11:25:03 [loader.py:458] Loading weights took 17.90 seconds
Loading safetensors checkpoint shards:  82% Completed | 31/38 [00:18<00:04,  1.61it/s]
Loading safetensors checkpoint shards:  84% Completed | 32/38 [00:19<00:03,  1.61it/s]
(VllmWorkerProcess pid=3827) INFO 04-22 11:25:04 [model_runner.py:904] Loading model weights took 17.2832 GB
Loading safetensors checkpoint shards:  87% Completed | 33/38 [00:19<00:03,  1.51it/s]
Loading safetensors checkpoint shards:  89% Completed | 34/38 [00:20<00:02,  1.48it/s]
Loading safetensors checkpoint shards:  92% Completed | 35/38 [00:21<00:01,  1.52it/s]
Loading safetensors checkpoint shards:  95% Completed | 36/38 [00:21<00:01,  1.58it/s]
Loading safetensors checkpoint shards:  97% Completed | 37/38 [00:22<00:00,  1.65it/s]
Loading safetensors checkpoint shards: 100% Completed | 38/38 [00:22<00:00,  1.69it/s]
Loading safetensors checkpoint shards: 100% Completed | 38/38 [00:22<00:00,  1.67it/s]

INFO 04-22 11:25:08 [loader.py:458] Loading weights took 22.90 seconds
INFO 04-22 11:25:08 [model_runner.py:904] Loading model weights took 17.2832 GB
(VllmWorkerProcess pid=3822) INFO 04-22 11:25:09 [loader.py:458] Loading weights took 22.96 seconds
(VllmWorkerProcess pid=3822) INFO 04-22 11:25:09 [model_runner.py:904] Loading model weights took 17.2832 GB
(VllmWorkerProcess pid=3826) INFO 04-22 11:25:09 [loader.py:458] Loading weights took 24.04 seconds
(VllmWorkerProcess pid=3821) INFO 04-22 11:25:09 [loader.py:458] Loading weights took 23.59 seconds
(VllmWorkerProcess pid=3826) INFO 04-22 11:25:10 [model_runner.py:904] Loading model weights took 17.2832 GB
(VllmWorkerProcess pid=3821) INFO 04-22 11:25:10 [model_runner.py:904] Loading model weights took 17.2832 GB
(VllmWorkerProcess pid=3824) INFO 04-22 11:25:11 [loader.py:458] Loading weights took 24.47 seconds
(VllmWorkerProcess pid=3824) INFO 04-22 11:25:11 [model_runner.py:904] Loading model weights took 17.2832 GB
(VllmWorkerProcess pid=3825) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=3824) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=3823) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=3827) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=3821) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=3822) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=3826) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=3825) WARNING 04-22 11:25:23 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=3824) WARNING 04-22 11:25:24 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=3827) WARNING 04-22 11:25:24 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=3826) WARNING 04-22 11:25:24 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=3823) WARNING 04-22 11:25:24 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=3822) WARNING 04-22 11:25:24 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=3821) WARNING 04-22 11:25:25 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
WARNING 04-22 11:25:25 [model_runner.py:1024] Computed max_num_seqs (min(256, 32768 // 180224)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=3825) Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=3824) Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=3825) WARNING 04-22 11:25:48 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=3826) Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=3824) WARNING 04-22 11:25:50 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=3826) WARNING 04-22 11:25:50 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=3822) Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=3823) Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=3821) Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=3822) WARNING 04-22 11:25:51 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=3823) WARNING 04-22 11:25:51 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=3827) Token indices sequence length is longer than the specified maximum sequence length for this model (180224 > 131072). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=3821) WARNING 04-22 11:25:52 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
WARNING 04-22 11:25:53 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=3827) WARNING 04-22 11:25:53 [profiling.py:245] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 32768) is too short to hold the multi-modal embeddings in the worst case (180224 tokens in total, out of which {'image': 163840, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.

Socket error Event: 32 Error: 10053.
Connection closing...Socket close.

Connection closed by foreign host.
```
