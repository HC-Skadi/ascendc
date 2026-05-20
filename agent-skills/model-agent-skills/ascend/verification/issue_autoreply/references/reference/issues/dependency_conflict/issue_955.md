# Issue #955: [Bug]: ascend/vllm-ascend:v0.8.4rc2 running Qwen2.5-VL-7B-Instruct Failed with  HeaderTooLarge Error

## 基本信息

- **编号**: #955
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/955
- **创建时间**: 2025-05-26T05:48:26Z
- **关闭时间**: 2025-05-26T06:44:29Z
- **更新时间**: 2025-05-26T06:44:29Z
- **提交者**: @BenjaminP-Runner
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.5.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.17 (main, Apr 30 2025, 15:23:17) [GCC 11.4.0] (64-bit runtime)

CPU:
Architecture:                       x86_64
CPU op-mode(s):                     32-bit, 64-bit
Address sizes:                      46 bits physical, 57 bits virtual
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          GenuineIntel
Model name:                         Intel(R) Xeon(R) Platinum 8468
CPU family:                         6
Model:                              143
Thread(s) per core:                 2
Core(s) per socket:                 48
Socket(s):                          2
Stepping:                           8
CPU max MHz:                        3800.0000
CPU min MHz:                        800.0000
BogoMIPS:                           4200.00
Flags:                              fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cat_l2 cdp_l3 invpcid_single intel_ppin cdp_l2 ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid bus_lock_detect cldemote movdiri movdir64b enqcmd fsrm uintr md_clear serialize tsxldtrk pconfig arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 flush_l1d arch_capabilities
Virtualization:                     VT-x
L1d cache:                          4.5 MiB (96 instances)
L1i cache:                          3 MiB (96 instances)
L2 cache:                           192 MiB (96 instances)
L3 cache:                           210 MiB (2 instances)
NUMA node(s):                       2
NUMA node0 CPU(s):                  0-47,96-143
NUMA node1 CPU(s):                  48-95,144-191
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:           Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:           Mitigation; Enhanced / Automatic IBRS, IBPB conditional, RSB filling, PBRSB-eIBRS SW sequence
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1+cpu
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.5.post1
vLLM Ascend Version: 0.8.5rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_DOCKER_RUNTIME=True
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc1                 Version: 24.1.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 94.8        60                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3345 / 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 99.9        59                0    / 0             |
| 0                         | 0000:19:00.0  | 0           0    / 0          3339 / 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 94.0        59                0    / 0             |
| 0                         | 0000:49:00.0  | 0           0    / 0          3339 / 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 97.3        60                0    / 0             |
| 0                         | 0000:39:00.0  | 0           0    / 0          3340 / 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 96.6        59                0    / 0             |
| 0                         | 0000:DA:00.0  | 0           0    / 0          3341 / 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 106.0       60                0    / 0             |
| 0                         | 0000:99:00.0  | 0           0    / 0          3340 / 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 95.1        59                0    / 0             |
| 0                         | 0000:B8:00.0  | 0           0    / 0          3339 / 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 105.2       59                0    / 0             |
| 0                         | 0000:C8:00.0  | 0           0    / 0          3338 / 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 91.0        57                0    / 0             |
| 0                         | 0000:59:00.0  | 0           0    / 0          3339 / 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 107.6       61                0    / 0             |
| 0                         | 0000:18:00.0  | 0           0    / 0          3339 / 65536         |
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
| No running processes found in NPU 8                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 9                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/x86_64-linux
```

</details>

### 🐛 Describe the bug

just start as `vllm serve ` and set tp as 4,it shows  HeadTooLarge

<details>
<summary>The Error Info </summary>

```text
INFO 05-26 03:28:24 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-26 03:28:24 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-26 03:28:24 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-26 03:28:25 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-26 03:28:25 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-26 03:28:25 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-26 03:28:25 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-26 03:28:25 [__init__.py:44] plugin ascend loaded.
INFO 05-26 03:28:25 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-26 03:28:26 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO:root:user set. pp is None, tp is 4
INFO 05-26 03:28:27 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-26 03:28:27 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-26 03:28:27 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-26 03:28:27 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-26 03:28:27 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-26 03:28:27 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-26 03:28:27 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-26 03:28:27 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-26 03:28:27 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-26 03:28:27 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-26 03:28:27 [api_server.py:111] vLLM API server version 0.8.5.post1
INFO 05-26 03:28:27 [api_server.py:112] args: Namespace(host='0.0.0.0', port=8001, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/Qwen2.5-VL-7B-Instruct/', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, load_format='auto', download_dir=None, model_loader_extra_config={}, use_tqdm_on_load=True, config_format=<ConfigFormat.AUTO: 'auto'>, dtype='bfloat16', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=4, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, disable_custom_all_reduce=False, block_size=None, gpu_memory_utilization=0.9, swap_space=4, kv_cache_dtype='auto', num_gpu_blocks_override=None, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', cpu_offload_gb=0, calculate_kv_scales=False, disable_sliding_window=False, use_v2_block_manager=True, seed=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_token=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config={}, limit_mm_per_prompt={}, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=None, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=None, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', speculative_config=None, ignore_patterns=[], served_model_name=['Qwen2.5-VL-7B-Instruct'], qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, max_num_batched_tokens=None, max_num_seqs=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, num_lookahead_slots=0, scheduler_delay_factor=0.0, preemption_mode=None, num_scheduler_steps=1, multi_step_stream_outputs=True, scheduling_policy='fcfs', enable_chunked_prefill=None, disable_chunked_mm_input=False, scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, additional_config=None, enable_reasoning=False, disable_cascade_attn=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False)
INFO 05-26 03:28:34 [config.py:717] This model supports multiple tasks: {'generate', 'embed', 'classify', 'reward', 'score'}. Defaulting to 'generate'.
INFO 05-26 03:28:34 [arg_utils.py:1669] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
WARNING 05-26 03:28:34 [arg_utils.py:1536] The model has a long context length (128000). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value.
INFO 05-26 03:28:34 [config.py:1770] Defaulting to use mp for distributed inference
INFO 05-26 03:28:34 [config.py:1804] Disabled the custom all-reduce kernel because it is not supported on current platform.
WARNING 05-26 03:28:34 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
INFO 05-26 03:28:34 [platform.py:133] Compilation disabled, using eager mode by default
INFO 05-26 03:28:34 [api_server.py:246] Started engine process with PID 157
INFO 05-26 03:28:37 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-26 03:28:37 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-26 03:28:37 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-26 03:28:37 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-26 03:28:37 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-26 03:28:37 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-26 03:28:37 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-26 03:28:37 [__init__.py:44] plugin ascend loaded.
INFO 05-26 03:28:37 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-26 03:28:38 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-26 03:28:39 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-26 03:28:39 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-26 03:28:39 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-26 03:28:39 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-26 03:28:39 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-26 03:28:39 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-26 03:28:39 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-26 03:28:39 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-26 03:28:39 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-26 03:28:39 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-26 03:28:39 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='/data/Qwen2.5-VL-7B-Instruct/', speculative_config=None, tokenizer='/data/Qwen2.5-VL-7B-Instruct/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=128000, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=Qwen2.5-VL-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
WARNING 05-26 03:28:39 [multiproc_worker_utils.py:306] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
(VllmWorkerProcess pid=294) INFO 05-26 03:28:39 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=296) INFO 05-26 03:28:39 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=298) INFO 05-26 03:28:39 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
(VllmWorkerProcess pid=298) WARNING 05-26 03:28:40 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x7f6b36b6a740>
(VllmWorkerProcess pid=294) WARNING 05-26 03:28:40 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x7f6b36b6a800>
(VllmWorkerProcess pid=296) WARNING 05-26 03:28:40 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x7f6b36b2d090>
WARNING 05-26 03:28:40 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x7f6b36b2cbb0>
INFO 05-26 03:28:45 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-26 03:28:45 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-26 03:28:45 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-26 03:28:46 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-26 03:28:46 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-26 03:28:46 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-26 03:28:46 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-26 03:28:46 [__init__.py:44] plugin ascend loaded.
INFO 05-26 03:28:46 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-26 03:28:46 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-26 03:28:51 [shm_broadcast.py:266] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3], buffer_handle=(3, 4194304, 6, 'psm_ee4ae581'), local_subscribe_addr='ipc:///tmp/50691b78-a8ce-42c4-953d-04e4cae05d16', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 05-26 03:28:51 [parallel_state.py:1004] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0
(VllmWorkerProcess pid=294) INFO 05-26 03:28:51 [parallel_state.py:1004] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1
(VllmWorkerProcess pid=298) INFO 05-26 03:28:51 [parallel_state.py:1004] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3
(VllmWorkerProcess pid=296) INFO 05-26 03:28:51 [parallel_state.py:1004] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2
INFO 05-26 03:28:51 [model_runner.py:943] Starting to load model /data/Qwen2.5-VL-7B-Instruct/...
(VllmWorkerProcess pid=294) INFO 05-26 03:28:51 [model_runner.py:943] Starting to load model /data/Qwen2.5-VL-7B-Instruct/...
(VllmWorkerProcess pid=296) INFO 05-26 03:28:51 [model_runner.py:943] Starting to load model /data/Qwen2.5-VL-7B-Instruct/...
(VllmWorkerProcess pid=298) INFO 05-26 03:28:51 [model_runner.py:943] Starting to load model /data/Qwen2.5-VL-7B-Instruct/...
(VllmWorkerProcess pid=298) INFO 05-26 03:28:51 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=294) INFO 05-26 03:28:51 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=298) WARNING 05-26 03:28:51 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
(VllmWorkerProcess pid=298) INFO 05-26 03:28:51 [platform.py:133] Compilation disabled, using eager mode by default
(VllmWorkerProcess pid=294) WARNING 05-26 03:28:51 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
(VllmWorkerProcess pid=294) INFO 05-26 03:28:51 [platform.py:133] Compilation disabled, using eager mode by default
(VllmWorkerProcess pid=296) INFO 05-26 03:28:51 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=296) WARNING 05-26 03:28:51 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
(VllmWorkerProcess pid=296) INFO 05-26 03:28:51 [platform.py:133] Compilation disabled, using eager mode by default
INFO 05-26 03:28:51 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
WARNING 05-26 03:28:51 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
INFO 05-26 03:28:51 [platform.py:133] Compilation disabled, using eager mode by default
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]

ERROR 05-26 03:28:51 [engine.py:448] Error while deserializing header: HeaderTooLarge
ERROR 05-26 03:28:51 [engine.py:448] Traceback (most recent call last):
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 05-26 03:28:51 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 05-26 03:28:51 [engine.py:448]     return cls(
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 05-26 03:28:51 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
ERROR 05-26 03:28:51 [engine.py:448]     self.model_executor = executor_class(vllm_config=vllm_config)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 286, in __init__
ERROR 05-26 03:28:51 [engine.py:448]     super().__init__(*args, **kwargs)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 05-26 03:28:51 [engine.py:448]     self._init_executor()
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 125, in _init_executor
ERROR 05-26 03:28:51 [engine.py:448]     self._run_workers("load_model",
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
ERROR 05-26 03:28:51 [engine.py:448]     driver_worker_output = run_method(self.driver_worker, sent_method,
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-26 03:28:51 [engine.py:448]     return func(*args, **kwargs)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
ERROR 05-26 03:28:51 [engine.py:448]     self.model_runner.load_model()
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
ERROR 05-26 03:28:51 [engine.py:448]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 05-26 03:28:51 [engine.py:448]     return loader.load_model(vllm_config=vllm_config)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
ERROR 05-26 03:28:51 [engine.py:448]     loaded_weights = model.load_weights(
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1126, in load_weights
ERROR 05-26 03:28:51 [engine.py:448]     return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights
ERROR 05-26 03:28:51 [engine.py:448]     autoloaded_weights = set(self._load_module("", self.module, weights))
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 213, in _load_module
ERROR 05-26 03:28:51 [engine.py:448]     for child_prefix, child_weights in self._groupby_prefix(weights):
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 103, in _groupby_prefix
ERROR 05-26 03:28:51 [engine.py:448]     for prefix, group in itertools.groupby(weights_by_parts,
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 100, in <genexpr>
ERROR 05-26 03:28:51 [engine.py:448]     weights_by_parts = ((weight_name.split(".", 1), weight_data)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 63, in <genexpr>
ERROR 05-26 03:28:51 [engine.py:448]     return ((out_name, data) for name, data in weights
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 431, in get_all_weights
ERROR 05-26 03:28:51 [engine.py:448]     yield from self._get_weights_iterator(primary_weights)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 414, in <genexpr>
ERROR 05-26 03:28:51 [engine.py:448]     return ((source.prefix + name, tensor)
ERROR 05-26 03:28:51 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/weight_utils.py", line 441, in safetensors_weights_iterator
ERROR 05-26 03:28:51 [engine.py:448]     with safe_open(st_file, framework="pt") as f:
ERROR 05-26 03:28:51 [engine.py:448] safetensors_rust.SafetensorError: Error while deserializing header: HeaderTooLarge
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     loaded_weights = model.load_weights(
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1126, in load_weights
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     autoloaded_weights = set(self._load_module("", self.module, weights))
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 213, in _load_module
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     for child_prefix, child_weights in self._groupby_prefix(weights):
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 103, in _groupby_prefix
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     for prefix, group in itertools.groupby(weights_by_parts,
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 100, in <genexpr>
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     weights_by_parts = ((weight_name.split(".", 1), weight_data)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 63, in <genexpr>
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return ((out_name, data) for name, data in weights
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 431, in get_all_weights
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     yield from self._get_weights_iterator(primary_weights)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 414, in <genexpr>
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return ((source.prefix + name, tensor)
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/weight_utils.py", line 441, in safetensors_weights_iterator
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     with safe_open(st_file, framework="pt") as f:
(VllmWorkerProcess pid=298) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] safetensors_rust.SafetensorError: Error while deserializing header: HeaderTooLarge
(VllmWorkerProcess pid=298) Traceback (most recent call last):
(VllmWorkerProcess pid=298)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/queues.py", line 244, in _feed
(VllmWorkerProcess pid=298)     obj = _ForkingPickler.dumps(obj)
(VllmWorkerProcess pid=298)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/reduction.py", line 51, in dumps
(VllmWorkerProcess pid=298)     cls(buf, protocol).dump(obj)
(VllmWorkerProcess pid=298) _pickle.PicklingError: Can't pickle <class 'safetensors_rust.SafetensorError'>: import of module 'safetensors_rust' failed
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     loaded_weights = model.load_weights(
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1126, in load_weights
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     autoloaded_weights = set(self._load_module("", self.module, weights))
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 213, in _load_module
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     for child_prefix, child_weights in self._groupby_prefix(weights):
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 103, in _groupby_prefix
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     for prefix, group in itertools.groupby(weights_by_parts,
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 100, in <genexpr>
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     weights_by_parts = ((weight_name.split(".", 1), weight_data)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 63, in <genexpr>
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return ((out_name, data) for name, data in weights
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 431, in get_all_weights
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     yield from self._get_weights_iterator(primary_weights)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 414, in <genexpr>
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return ((source.prefix + name, tensor)
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/weight_utils.py", line 441, in safetensors_weights_iterator
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     with safe_open(st_file, framework="pt") as f:
(VllmWorkerProcess pid=296) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] safetensors_rust.SafetensorError: Error while deserializing header: HeaderTooLarge
(VllmWorkerProcess pid=296) Traceback (most recent call last):
(VllmWorkerProcess pid=296)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/queues.py", line 244, in _feed
(VllmWorkerProcess pid=296)     obj = _ForkingPickler.dumps(obj)
(VllmWorkerProcess pid=296)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/reduction.py", line 51, in dumps
(VllmWorkerProcess pid=296)     cls(buf, protocol).dump(obj)
(VllmWorkerProcess pid=296) _pickle.PicklingError: Can't pickle <class 'safetensors_rust.SafetensorError'>: import of module 'safetensors_rust' failed
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     loaded_weights = model.load_weights(
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1126, in load_weights
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     autoloaded_weights = set(self._load_module("", self.module, weights))
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 213, in _load_module
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     for child_prefix, child_weights in self._groupby_prefix(weights):
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 103, in _groupby_prefix
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     for prefix, group in itertools.groupby(weights_by_parts,
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 100, in <genexpr>
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     weights_by_parts = ((weight_name.split(".", 1), weight_data)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 63, in <genexpr>
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return ((out_name, data) for name, data in weights
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 431, in get_all_weights
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     yield from self._get_weights_iterator(primary_weights)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 414, in <genexpr>
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     return ((source.prefix + name, tensor)
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/weight_utils.py", line 441, in safetensors_weights_iterator
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238]     with safe_open(st_file, framework="pt") as f:
(VllmWorkerProcess pid=294) ERROR 05-26 03:28:51 [multiproc_worker_utils.py:238] safetensors_rust.SafetensorError: Error while deserializing header: HeaderTooLarge
(VllmWorkerProcess pid=294) Traceback (most recent call last):
(VllmWorkerProcess pid=294)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/queues.py", line 244, in _feed
(VllmWorkerProcess pid=294)     obj = _ForkingPickler.dumps(obj)
(VllmWorkerProcess pid=294)   File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/reduction.py", line 51, in dumps
(VllmWorkerProcess pid=294)     cls(buf, protocol).dump(obj)
(VllmWorkerProcess pid=294) _pickle.PicklingError: Can't pickle <class 'safetensors_rust.SafetensorError'>: import of module 'safetensors_rust' failed
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
  File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 125, in _init_executor
    self._run_workers("load_model",
  File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
    driver_worker_output = run_method(self.driver_worker, sent_method,
  File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
    self.model_runner.load_model()
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
    return loader.load_model(vllm_config=vllm_config)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
    loaded_weights = model.load_weights(
  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1126, in load_weights
    return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights
    autoloaded_weights = set(self._load_module("", self.module, weights))
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 213, in _load_module
    for child_prefix, child_weights in self._groupby_prefix(weights):
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 103, in _groupby_prefix
    for prefix, group in itertools.groupby(weights_by_parts,
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 100, in <genexpr>
    weights_by_parts = ((weight_name.split(".", 1), weight_data)
  File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 63, in <genexpr>
    return ((out_name, data) for name, data in weights
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 431, in get_all_weights
    yield from self._get_weights_iterator(primary_weights)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 414, in <genexpr>
    return ((source.prefix + name, tensor)
  File "/vllm-workspace/vllm/vllm/model_executor/model_loader/weight_utils.py", line 441, in safetensors_weights_iterator
    with safe_open(st_file, framework="pt") as f:
safetensors_rust.SafetensorError: Error while deserializing header: HeaderTooLarge
INFO 05-26 03:28:54 [multiproc_worker_utils.py:137] Terminating local vLLM worker processes
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
Traceback (most recent call last):
  File "/app/api_server.py", line 252, in main
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/app/api_server.py", line 140, in run_server
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
[ERROR] 2025-05-26-03:28:55 (PID:10, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

</details>

