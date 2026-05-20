# Issue #813: [Bug]: fail to start W8A8 deepseek-R1 with TP=8,PP=2

## 基本信息

- **编号**: #813
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/813
- **创建时间**: 2025-05-12T06:51:40Z
- **关闭时间**: 2025-05-15T05:51:13Z
- **更新时间**: 2025-06-09T08:48:11Z
- **提交者**: @gao12312
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

env:
```text
INFO 05-12 06:49:47 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-12 06:49:47 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-12 06:49:47 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-12 06:49:48 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-12 06:49:48 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-12 06:49:48 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-12 06:49:48 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 06:49:48 [__init__.py:44] plugin ascend loaded.
INFO 05-12 06:49:48 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-12 06:49:49 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.17 (main, Apr 30 2025, 16:00:31) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-2107.6.0.0192.8.oe1.bclinux.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 5250
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.5.post1
vLLM Ascend Version: 0.1.dev1+gd6bfae8 (git sha: d6bfae8)

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
| npu-smi 23.0.3                   Version: 23.0.3                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 97.1        40                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3332 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 96.6        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3330 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 90.4        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3337 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 93.1        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3338 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 96.5        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 94.0        44                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 94.5        42                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3333 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 90.5        44                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3331 / 65536         |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```
start command:
```text
python -m vllm.entrypoints.openai.api_server \
       --model="/root/models/deepseek_r1_w8a8" \
       --trust-remote-code \
       --enforce-eager \
       --distributed_executor_backend "ray" \
       --tensor-parallel-size 8 \
       --pipeline-parallel-size 2 \
       --disable-frontend-multiprocessing 
```


### 🐛 Describe the bug

```python
root@test:/vllm-workspace/vllm# python -m vllm.entrypoints.openai.api_server \
       --model="/root/models/deepseek_r1_w8a8" \
       --trust-remote-code \
       --enforce-eager \
       --distributed_executor_backend "ray" \
       --tensor-parallel-size 8 \
       --pipeline-parallel-size 2 \
       --disable-frontend-multiprocessing 
INFO 05-12 06:34:01 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-12 06:34:01 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-12 06:34:01 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-12 06:34:02 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-12 06:34:02 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-12 06:34:02 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-12 06:34:02 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 06:34:02 [__init__.py:44] plugin ascend loaded.
INFO 05-12 06:34:02 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-12 06:34:03 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-12 06:34:06 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-12 06:34:06 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-12 06:34:06 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-12 06:34:06 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 06:34:06 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-12 06:34:06 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-12 06:34:06 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-12 06:34:06 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-12 06:34:06 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-12 06:34:06 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-12 06:34:07 [api_server.py:1043] vLLM API server version 0.8.5.post1
INFO 05-12 06:34:07 [api_server.py:1044] args: Namespace(host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=True, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/root/models/deepseek_r1_w8a8_zhw', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, load_format='auto', download_dir=None, model_loader_extra_config={}, use_tqdm_on_load=True, config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend='ray', pipeline_parallel_size=2, tensor_parallel_size=8, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, disable_custom_all_reduce=False, block_size=None, gpu_memory_utilization=0.9, swap_space=4, kv_cache_dtype='auto', num_gpu_blocks_override=None, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', cpu_offload_gb=0, calculate_kv_scales=False, disable_sliding_window=False, use_v2_block_manager=True, seed=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_token=None, hf_overrides=None, enforce_eager=True, max_seq_len_to_capture=8192, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config={}, limit_mm_per_prompt={}, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=None, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=None, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', speculative_config=None, ignore_patterns=[], served_model_name=None, qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, max_num_batched_tokens=None, max_num_seqs=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, num_lookahead_slots=0, scheduler_delay_factor=0.0, preemption_mode=None, num_scheduler_steps=1, multi_step_stream_outputs=True, scheduling_policy='fcfs', enable_chunked_prefill=None, disable_chunked_mm_input=False, scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, additional_config=None, enable_reasoning=False, disable_cascade_attn=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False)
You are using a model of type deepseekv2 to instantiate a model of type deepseek_v3. This is not supported for all configurations of models and can yield errors.
INFO 05-12 06:34:07 [config.py:209] Replacing legacy 'type' key with 'rope_type'
INFO 05-12 06:34:19 [config.py:717] This model supports multiple tasks: {'classify', 'reward', 'generate', 'embed', 'score'}. Defaulting to 'generate'.
WARNING 05-12 06:34:19 [config.py:830] ascend quantization is not fully optimized yet. The speed can be slower than non-quantized models.
INFO 05-12 06:34:19 [arg_utils.py:1669] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
WARNING 05-12 06:34:19 [arg_utils.py:1536] The model has a long context length (163840). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value.
INFO 05-12 06:34:19 [config.py:1804] Disabled the custom all-reduce kernel because it is not supported on current platform.
WARNING 05-12 06:34:19 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine. 
INFO 05-12 06:34:19 [platform.py:133] Compilation disabled, using eager mode by default
INFO 05-12 06:34:19 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='/root/models/deepseek_r1_w8a8_zhw', speculative_config=None, tokenizer='/root/models/deepseek_r1_w8a8_zhw', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=163840, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=2, disable_custom_all_reduce=True, quantization=ascend, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=/root/models/deepseek_r1_w8a8_zhw, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=False, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, 
You are using a model of type deepseekv2 to instantiate a model of type deepseek_v3. This is not supported for all configurations of models and can yield errors.
INFO 05-12 06:34:20 [config.py:209] Replacing legacy 'type' key with 'rope_type'
2025-05-12 06:34:20,462 INFO worker.py:1694 -- Connecting to existing Ray cluster at address: 192.168.1.10:6379...
2025-05-12 06:34:20,473 INFO worker.py:1888 -- Connected to Ray cluster.
INFO 05-12 06:34:20 [ray_utils.py:335] No current placement group found. Creating a new placement group.
INFO 05-12 06:34:21 [ray_distributed_executor.py:176] use_ray_spmd_worker: False
(pid=342995) INFO 05-12 06:34:26 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
(pid=342995) WARNING 05-12 06:34:26 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
(pid=342995) INFO 05-12 06:34:26 [importing.py:53] Triton module has been replaced with a placeholder.
(pid=342995) INFO 05-12 06:34:27 [__init__.py:30] Available plugins for group vllm.platform_plugins:
(pid=342995) INFO 05-12 06:34:27 [__init__.py:32] name=ascend, value=vllm_ascend:register
(pid=342995) INFO 05-12 06:34:27 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
(pid=342995) INFO 05-12 06:34:27 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(pid=342995) INFO 05-12 06:34:27 [__init__.py:44] plugin ascend loaded.
(pid=342995) INFO 05-12 06:34:27 [__init__.py:230] Platform plugin ascend is activated
(pid=342995) WARNING 05-12 06:34:29 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-12 06:34:33 [ray_distributed_executor.py:352] non_carry_over_env_vars from config: set()
INFO 05-12 06:34:33 [ray_distributed_executor.py:354] Copying the following environment variables to workers: ['LD_LIBRARY_PATH', 'VLLM_WORKER_MULTIPROC_METHOD', 'VLLM_USE_V1']
INFO 05-12 06:34:33 [ray_distributed_executor.py:357] If certain env vars should NOT be copied to workers, add them to /root/.config/vllm/ray_non_carry_over_env_vars.json file
(RayWorkerWrapper pid=343188) INFO 05-12 06:34:33 [__init__.py:30] Available plugins for group vllm.general_plugins:
(RayWorkerWrapper pid=343188) INFO 05-12 06:34:33 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(RayWorkerWrapper pid=343188) INFO 05-12 06:34:33 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(RayWorkerWrapper pid=343188) INFO 05-12 06:34:33 [__init__.py:44] plugin ascend_enhanced_model loaded.
(pid=169575, ip=10.151.18.104) INFO 05-12 06:34:28 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available. [repeated 15x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(pid=169575, ip=10.151.18.104) WARNING 05-12 06:34:28 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation. [repeated 15x across cluster]
(pid=169575, ip=10.151.18.104) INFO 05-12 06:34:28 [importing.py:53] Triton module has been replaced with a placeholder. [repeated 15x across cluster]
(pid=169575, ip=10.151.18.104) INFO 05-12 06:34:29 [__init__.py:30] Available plugins for group vllm.platform_plugins: [repeated 15x across cluster]
(pid=169575, ip=10.151.18.104) INFO 05-12 06:34:29 [__init__.py:32] name=ascend, value=vllm_ascend:register [repeated 15x across cluster]
(pid=169575, ip=10.151.18.104) INFO 05-12 06:34:29 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded. [repeated 15x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) INFO 05-12 06:34:33 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. [repeated 23x across cluster]
(pid=169575, ip=10.151.18.104) INFO 05-12 06:34:29 [__init__.py:44] plugin ascend loaded. [repeated 15x across cluster]
(pid=169575, ip=10.151.18.104) INFO 05-12 06:34:29 [__init__.py:230] Platform plugin ascend is activated [repeated 15x across cluster]
(RayWorkerWrapper pid=343188) WARNING 05-12 06:34:33 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(RayWorkerWrapper pid=343188) WARNING 05-12 06:34:33 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(RayWorkerWrapper pid=343188) WARNING 05-12 06:34:33 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(RayWorkerWrapper pid=343188) WARNING 05-12 06:34:33 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(RayWorkerWrapper pid=343188) WARNING 05-12 06:34:33 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 05-12 06:34:34 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffdc16b15d0>
(RayWorkerWrapper pid=169573, ip=10.151.18.104) WARNING 05-12 06:34:34 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffc3f556680>
[rank0]:[W512 06:35:02.820115420 ProcessGroupGloo.cpp:715] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
(RayWorkerWrapper pid=169568, ip=10.151.18.104) INFO 05-12 06:35:02 [shm_broadcast.py:266] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_020d5bdf'), local_subscribe_addr='ipc:///tmp/20219a29-c213-47ab-86d2-a5ea2b4d7936', remote_subscribe_addr=None, remote_addr_ipv6=False)
(pid=169575, ip=10.151.18.104) WARNING 05-12 06:34:31 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") [repeated 15x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) INFO 05-12 06:34:33 [__init__.py:30] Available plugins for group vllm.general_plugins: [repeated 14x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) INFO 05-12 06:34:33 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model [repeated 14x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) INFO 05-12 06:34:33 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded. [repeated 14x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) INFO 05-12 06:34:33 [__init__.py:44] plugin ascend_enhanced_model loaded. [repeated 14x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) INFO 05-12 06:34:33 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. [repeated 7x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) WARNING 05-12 06:34:33 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP. [repeated 14x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) WARNING 05-12 06:34:33 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM. [repeated 56x across cluster]
(RayWorkerWrapper pid=169575, ip=10.151.18.104) WARNING 05-12 06:34:34 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffc3b3de680> [repeated 14x across cluster]
INFO 05-12 06:35:12 [shm_broadcast.py:266] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_f7274dea'), local_subscribe_addr='ipc:///tmp/b8bfe53f-18a3-4843-a295-6f82ebde01e3', remote_subscribe_addr=None, remote_addr_ipv6=False)
(RayWorkerWrapper pid=343190) INFO 05-12 06:35:12 [parallel_state.py:1004] rank 3 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 3
(RayWorkerWrapper pid=169568, ip=10.151.18.104) INFO 05-12 06:35:22 [parallel_state.py:1004] rank 8 in world size 16 is assigned as DP rank 0, PP rank 1, TP rank 0 [repeated 14x across cluster]
INFO 05-12 06:35:32 [parallel_state.py:1004] rank 0 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 0
INFO 05-12 06:35:52 [model_runner.py:943] Starting to load model /root/models/deepseek_r1_w8a8_zhw...
INFO 05-12 06:35:52 [utils.py:106] Hidden layers were unevenly partitioned: [31,30]. This can be manually overridden using the VLLM_PP_LAYER_PARTITION environment variable
(RayWorkerWrapper pid=169573, ip=10.151.18.104) INFO 05-12 06:35:52 [model_runner.py:943] Starting to load model /root/models/deepseek_r1_w8a8_zhw...
(RayWorkerWrapper pid=169573, ip=10.151.18.104) INFO 05-12 06:35:52 [utils.py:106] Hidden layers were unevenly partitioned: [31,30]. This can be manually overridden using the VLLM_PP_LAYER_PARTITION environment variable
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution.
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620] Traceback (most recent call last):
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     return run_method(self, method, args, kwargs)
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     return func(*args, **kwargs)
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     self.model_runner.load_model()
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     self.model = get_model(vllm_config=self.vllm_config)
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     return loader.load_model(vllm_config=vllm_config)
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     model = _initialize_model(vllm_config=vllm_config)
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     return model_class(vllm_config=vllm_config, prefix=prefix)
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 629, in __init__
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 555, in __init__
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     self.start_layer, self.end_layer, self.layers = make_layers(
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     [PPMissingLayer() for _ in range(start_layer)] + [
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 557, in <lambda>
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     lambda prefix: CustomDeepseekV2DecoderLayer(
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 441, in __init__
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     self.self_attn = attn_cls(
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 224, in __init__
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 278, in __init__
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     super().__init__(input_size,
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     self.quant_method = quant_config.get_quant_method(self,
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 87, in get_quant_method
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     if self.is_layer_skipped_ascend(prefix,
ERROR 05-12 06:35:53 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution.
ERROR 05-12 06:35:53 [worker_base.py:620] Traceback (most recent call last):
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
ERROR 05-12 06:35:53 [worker_base.py:620]     return run_method(self, method, args, kwargs)
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-12 06:35:53 [worker_base.py:620]     return func(*args, **kwargs)
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
ERROR 05-12 06:35:53 [worker_base.py:620]     self.model_runner.load_model()
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
ERROR 05-12 06:35:53 [worker_base.py:620]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 05-12 06:35:53 [worker_base.py:620]     return loader.load_model(vllm_config=vllm_config)
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
ERROR 05-12 06:35:53 [worker_base.py:620]     model = _initialize_model(vllm_config=vllm_config)
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
ERROR 05-12 06:35:53 [worker_base.py:620]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 629, in __init__
ERROR 05-12 06:35:53 [worker_base.py:620]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 555, in __init__
ERROR 05-12 06:35:53 [worker_base.py:620]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
ERROR 05-12 06:35:53 [worker_base.py:620]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
ERROR 05-12 06:35:53 [worker_base.py:620]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 557, in <lambda>
ERROR 05-12 06:35:53 [worker_base.py:620]     lambda prefix: CustomDeepseekV2DecoderLayer(
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 441, in __init__
ERROR 05-12 06:35:53 [worker_base.py:620]     self.self_attn = attn_cls(
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 224, in __init__
ERROR 05-12 06:35:53 [worker_base.py:620]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 278, in __init__
ERROR 05-12 06:35:53 [worker_base.py:620]     super().__init__(input_size,
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
ERROR 05-12 06:35:53 [worker_base.py:620]     self.quant_method = quant_config.get_quant_method(self,
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 87, in get_quant_method
ERROR 05-12 06:35:53 [worker_base.py:620]     if self.is_layer_skipped_ascend(prefix,
ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 129, in is_layer_skipped_ascend
ERROR 05-12 06:35:53 [worker_base.py:620]     is_skipped = self.quant_description[prefix + '.weight'] == "W8A8"  #"FLOAT"
ERROR 05-12 06:35:53 [worker_base.py:620] KeyError: 'model.layers.0.self_attn.q_a_proj.weight'
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 129, in is_layer_skipped_ascend
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620]     is_skipped = self.quant_description[prefix + '.weight'] == "W8A8"  #"FLOAT"
(RayWorkerWrapper pid=343190) ERROR 05-12 06:35:53 [worker_base.py:620] KeyError: 'model.layers.0.self_attn.q_a_proj.weight'
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/runpy.py", line 196, in _run_module_as_main
[rank0]:     return _run_code(code, main_globals, None,
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/runpy.py", line 86, in _run_code
[rank0]:     exec(code, run_globals)
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1130, in <module>
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
[rank0]:     return loop.run_until_complete(wrapper())
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1078, in run_server
[rank0]:     async with build_async_engine_client(args) as engine_client:
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_vllm_config(
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/async_llm_engine.py", line 657, in from_vllm_config
[rank0]:     return cls(
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/async_llm_engine.py", line 612, in __init__
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/async_llm_engine.py", line 267, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config)
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 286, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 114, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 396, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 516, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 621, in execute_method
[rank0]:     raise e
[rank0]:   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
[rank0]:     return run_method(self, method, args, kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
[rank0]:     model = _initialize_model(vllm_config=vllm_config)
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
[rank0]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 629, in __init__
[rank0]:     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 555, in __init__
[rank0]:     self.start_layer, self.end_layer, self.layers = make_layers(
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
[rank0]:     [PPMissingLayer() for _ in range(start_layer)] + [
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
[rank0]:     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 557, in <lambda>
[rank0]:     lambda prefix: CustomDeepseekV2DecoderLayer(
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 441, in __init__
[rank0]:     self.self_attn = attn_cls(
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 224, in __init__
[rank0]:     self.q_a_proj = ReplicatedLinear(self.hidden_size,
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 278, in __init__
[rank0]:     super().__init__(input_size,
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
[rank0]:     self.quant_method = quant_config.get_quant_method(self,
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 87, in get_quant_method
[rank0]:     if self.is_layer_skipped_ascend(prefix,
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 129, in is_layer_skipped_ascend
[rank0]:     is_skipped = self.quant_description[prefix + '.weight'] == "W8A8"  #"FLOAT"
[rank0]: KeyError: 'model.layers.0.self_attn.q_a_proj.weight'
(RayWorkerWrapper pid=169570, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
(RayWorkerWrapper pid=343199) INFO 05-12 06:35:52 [model_runner.py:943] Starting to load model /root/models/deepseek_r1_w8a8_zhw... [repeated 14x across cluster]
(RayWorkerWrapper pid=343199) INFO 05-12 06:35:52 [utils.py:106] Hidden layers were unevenly partitioned: [31,30]. This can be manually overridden using the VLLM_PP_LAYER_PARTITION environment variable [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution. [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620] Traceback (most recent call last): [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     return run_method(self, method, args, kwargs) [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     return func(*args, **kwargs) [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     self.model_runner.load_model() [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     self.model = get_model(vllm_config=self.vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     return loader.load_model(vllm_config=vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     model = _initialize_model(vllm_config=vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     return model_class(vllm_config=vllm_config, prefix=prefix) [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 224, in __init__ [repeated 56x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config, [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     self.start_layer, self.end_layer, self.layers = make_layers( [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     [PPMissingLayer() for _ in range(start_layer)] + [ [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp> [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 557, in <lambda> [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     lambda prefix: CustomDeepseekV2DecoderLayer( [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     self.self_attn = attn_cls( [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     self.q_a_proj = ReplicatedLinear(self.hidden_size, [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__ [repeated 28x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     super().__init__(input_size, [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     self.quant_method = quant_config.get_quant_method(self, [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 87, in get_quant_method [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     if self.is_layer_skipped_ascend(prefix, [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 129, in is_layer_skipped_ascend [repeated 14x across cluster]
(RayWorkerWrapper pid=343199) ERROR 05-12 06:35:53 [worker_base.py:620]     is_skipped = self.quant_description[prefix + '.weight'] == "W8A8"  #"FLOAT" [repeated 6x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620] KeyError: 'model.layers.31.self_attn.q_a_proj.weight' [repeated 14x across cluster]
(RayWorkerWrapper pid=169568, ip=10.151.18.104) ERROR 05-12 06:35:53 [worker_base.py:620]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT" [repeated 7x across cluster]
[ERROR] 2025-05-12-06:35:55 (PID:342365, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
INFO 05-12 06:35:55 [ray_distributed_executor.py:127] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
root@wz-training-tianchi-2:/vllm-workspace/vllm# /usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```
