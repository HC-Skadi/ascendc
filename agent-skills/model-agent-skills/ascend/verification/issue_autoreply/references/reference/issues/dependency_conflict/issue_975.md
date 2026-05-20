# Issue #975: [Bug]: Atlas 800T A2 8*910B(64G)无法推理Qwen-235B-A22B

## 基本信息

- **编号**: #975
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/975
- **创建时间**: 2025-05-27T10:01:46Z
- **关闭时间**: 2025-11-11T06:26:44Z
- **更新时间**: 2025-11-11T06:26:44Z
- **提交者**: @shiyunalex
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 05-27 09:33:12 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-27 09:33:12 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-27 09:33:12 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-27 09:33:14 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-27 09:33:14 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-27 09:33:14 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-27 09:33:14 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-27 09:33:14 [__init__.py:44] plugin ascend loaded.
INFO 05-27 09:33:14 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-27 09:33:16 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: openEuler 22.03 (LTS-SP4) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.34

Python version: 3.10.17 (main, Apr 30 2025, 11:54:22) [GCC 10.3.1] (64-bit runtime)
Python platform: Linux-4.19.90-2107.6.0.0192.8.oe1.bclinux.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              0
Core(s) per cluster:             0
Socket(s):                       -
Cluster(s):                      0
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
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
VLLM_USE_MODELSCOPE=true
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 105.8       39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3385 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 94.1        37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3197 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 97.6        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3197 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 97.8        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3197 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 98.5        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3366 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 96.8        43                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3196 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 97.4        43                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3197 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 95.3        42                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3376 / 65536         |
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

</details>


### 🐛 Describe the bug

我是用的是```quay.io/ascend/vllm-ascend:v0.8.5rc1-openeuler```镜像，
启动容器代码：
```text
docker run --rm \
--name vllm-ascend \
--device=/dev/davinci0 \
--device=/dev/davinci1 \
--device=/dev/davinci2 \
--device=/dev/davinci3 \
--device=/dev/davinci4 \
--device=/dev/davinci5 \
--device=/dev/davinci6 \
--device=/dev/davinci7 \
--device=/dev/davinci_manager \
--device=/dev/devmm_svm \
--device=/dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /root/alex/qwen235b:/home/mindie-volume \
-p 8000:8000 \
-e VLLM_USE_MODELSCOPE=true \
-it  quay.io/ascend/vllm-ascend:v0.8.5rc1-openeuler bash
```

进入容器后，运行```vllm serve qwen3/qwen3-235b-a22b  --tensor-parallel-size 8```,
报错：
```text
INFO 05-27 09:52:25 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-27 09:52:25 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-27 09:52:25 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-27 09:52:27 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-27 09:52:27 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-27 09:52:27 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-27 09:52:27 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-27 09:52:27 [__init__.py:44] plugin ascend loaded.
INFO 05-27 09:52:27 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-27 09:52:29 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-27 09:52:32 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-27 09:52:32 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-27 09:52:32 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-27 09:52:32 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-27 09:52:32 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-27 09:52:32 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-27 09:52:32 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-27 09:52:32 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-27 09:52:32 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-27 09:52:32 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-27 09:52:36 [api_server.py:1043] vLLM API server version 0.8.5.post1
INFO 05-27 09:52:36 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/home/mindie-volume', config='', host=None, port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/home/mindie-volume', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, load_format='auto', download_dir=None, model_loader_extra_config={}, use_tqdm_on_load=True, config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', max_model_len=None, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, data_parallel_size=1, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, disable_custom_all_reduce=False, block_size=None, gpu_memory_utilization=0.9, swap_space=4, kv_cache_dtype='auto', num_gpu_blocks_override=None, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', cpu_offload_gb=0, calculate_kv_scales=False, disable_sliding_window=False, use_v2_block_manager=True, seed=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_token=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config={}, limit_mm_per_prompt={}, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=None, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=None, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', speculative_config=None, ignore_patterns=[], served_model_name=None, qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, max_num_batched_tokens=None, max_num_seqs=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, num_lookahead_slots=0, scheduler_delay_factor=0.0, preemption_mode=None, num_scheduler_steps=1, multi_step_stream_outputs=True, scheduling_policy='fcfs', enable_chunked_prefill=None, disable_chunked_mm_input=False, scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, additional_config=None, enable_reasoning=False, disable_cascade_attn=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffd2801e170>)
INFO 05-27 09:52:49 [config.py:717] This model supports multiple tasks: {'generate', 'classify', 'embed', 'score', 'reward'}. Defaulting to 'generate'.
INFO 05-27 09:52:49 [arg_utils.py:1669] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
WARNING 05-27 09:52:49 [arg_utils.py:1536] The model has a long context length (40960). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value.
INFO 05-27 09:52:49 [config.py:1804] Disabled the custom all-reduce kernel because it is not supported on current platform.
WARNING 05-27 09:52:49 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine.
INFO 05-27 09:52:49 [platform.py:133] Compilation disabled, using eager mode by default
INFO 05-27 09:52:49 [api_server.py:246] Started engine process with PID 854
INFO 05-27 09:52:54 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-27 09:52:54 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-27 09:52:54 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-27 09:52:56 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-27 09:52:56 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-27 09:52:56 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-27 09:52:56 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-27 09:52:56 [__init__.py:44] plugin ascend loaded.
INFO 05-27 09:52:56 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-27 09:52:57 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-27 09:53:00 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-27 09:53:00 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-27 09:53:00 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-27 09:53:00 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-27 09:53:00 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-27 09:53:00 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-27 09:53:00 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-27 09:53:00 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-27 09:53:00 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-27 09:53:00 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-27 09:53:00 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='/home/mindie-volume', speculative_config=None, tokenizer='/home/mindie-volume', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=/home/mindie-volume, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True,
WARNING 05-27 09:53:02 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd45e0db10>
ERROR 05-27 09:53:02 [engine.py:448] SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
ERROR 05-27 09:53:02 [engine.py:448] [ERROR] 2025-05-27-09:53:02 (PID:854, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 05-27 09:53:02 [engine.py:448] [Error]: The internal ACL of the system is incorrect.
ERROR 05-27 09:53:02 [engine.py:448]         Rectify the fault based on the error information in the ascend log.
ERROR 05-27 09:53:02 [engine.py:448] EH9999: Inner Error!
ERROR 05-27 09:53:02 [engine.py:448] EH9999: [PID: 854] 2025-05-27-09:53:02.440.058 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-27 09:53:02 [engine.py:448]         TraceBack (most recent call last):
ERROR 05-27 09:53:02 [engine.py:448]        GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:184]
ERROR 05-27 09:53:02 [engine.py:448]        GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:371]
ERROR 05-27 09:53:02 [engine.py:448]        [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 05-27 09:53:02 [engine.py:448]        [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-27 09:53:02 [engine.py:448]        [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-27 09:53:02 [engine.py:448] Traceback (most recent call last):
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 05-27 09:53:02 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 05-27 09:53:02 [engine.py:448]     return cls(
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 05-27 09:53:02 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
ERROR 05-27 09:53:02 [engine.py:448]     self.model_executor = executor_class(vllm_config=vllm_config)
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 05-27 09:53:02 [engine.py:448]     self._init_executor()
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 46, in _init_executor
ERROR 05-27 09:53:02 [engine.py:448]     self.collective_rpc("init_device")
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 05-27 09:53:02 [engine.py:448]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-27 09:53:02 [engine.py:448]     return func(*args, **kwargs)
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 604, in init_device
ERROR 05-27 09:53:02 [engine.py:448]     self.worker.init_device()  # type: ignore
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 211, in init_device
ERROR 05-27 09:53:02 [engine.py:448]     NPUPlatform.set_device(self.device)
ERROR 05-27 09:53:02 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 95, in set_device
ERROR 05-27 09:53:02 [engine.py:448]     torch.npu.set_device(device)
ERROR 05-27 09:53:02 [engine.py:448]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 83, in set_device
ERROR 05-27 09:53:02 [engine.py:448]     torch_npu._C._npu_setDevice(device_id)
ERROR 05-27 09:53:02 [engine.py:448] RuntimeError: SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
ERROR 05-27 09:53:02 [engine.py:448] [ERROR] 2025-05-27-09:53:02 (PID:854, Device:0, RankID:-1) ERR00100 PTA call acl api failed
ERROR 05-27 09:53:02 [engine.py:448] [Error]: The internal ACL of the system is incorrect.
ERROR 05-27 09:53:02 [engine.py:448]         Rectify the fault based on the error information in the ascend log.
ERROR 05-27 09:53:02 [engine.py:448] EH9999: Inner Error!
ERROR 05-27 09:53:02 [engine.py:448] EH9999: [PID: 854] 2025-05-27-09:53:02.440.058 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-27 09:53:02 [engine.py:448]         TraceBack (most recent call last):
ERROR 05-27 09:53:02 [engine.py:448]        GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:184]
ERROR 05-27 09:53:02 [engine.py:448]        GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:371]
ERROR 05-27 09:53:02 [engine.py:448]        [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
ERROR 05-27 09:53:02 [engine.py:448]        [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-27 09:53:02 [engine.py:448]        [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 05-27 09:53:02 [engine.py:448]
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
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 46, in _init_executor
    self.collective_rpc("init_device")
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
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
RuntimeError: SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
[ERROR] 2025-05-27-09:53:02 (PID:854, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The internal ACL of the system is incorrect.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
EH9999: [PID: 854] 2025-05-27-09:53:02.440.058 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
       GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:184]
       GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:371]
       [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
       [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
       [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

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
[ERROR] 2025-05-27-09:53:10 (PID:585, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

```
尝试运行更小的模型，也出现报错：
复现代码
```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# Create an LLM.
llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

报错信息
```text
INFO 05-27 09:41:10 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-27 09:41:10 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-27 09:41:10 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-27 09:41:12 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-27 09:41:12 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-27 09:41:12 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-27 09:41:12 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-27 09:41:12 [__init__.py:44] plugin ascend loaded.
INFO 05-27 09:41:12 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-27 09:41:14 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-27 09:41:16 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-27 09:41:16 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-27 09:41:16 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-27 09:41:16 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-27 09:41:16 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-27 09:41:16 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-27 09:41:16 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-27 09:41:16 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-27 09:41:16 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-27 09:41:16 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-05-27 09:41:17,488 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-05-27 09:41:17,741 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-05-27 09:41:18,088 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-05-27 09:41:18,380 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 05-27 09:41:31 [config.py:717] This model supports multiple tasks: {'classify', 'score', 'embed', 'reward', 'generate'}. Defaulting to 'generate'.
INFO 05-27 09:41:31 [arg_utils.py:1669] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
INFO 05-27 09:41:31 [config.py:1804] Disabled the custom all-reduce kernel because it is not supported on current platform.
WARNING 05-27 09:41:31 [platform.py:125] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine.
INFO 05-27 09:41:31 [platform.py:133] Compilation disabled, using eager mode by default
INFO 05-27 09:41:31 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='Qwen/Qwen2.5-0.5B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-0.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=Qwen/Qwen2.5-0.5B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False,
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-05-27 09:41:31,740 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-0.5B-Instruct
2025-05-27 09:41:32,600 - modelscope - WARNING - Using branch: master as version is unstable, use with caution
2025-05-27 09:41:32,807 - modelscope - INFO - Target directory already exists, skipping creation.
WARNING 05-27 09:41:33 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd1191cf10>
Traceback (most recent call last):
  File "/workspace/test1.py", line 13, in <module>
    llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")
  File "/vllm-workspace/vllm/vllm/utils.py", line 1161, in inner
    return fn(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/llm.py", line 247, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 510, in from_engine_args
    return engine_cls.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 486, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 46, in _init_executor
    self.collective_rpc("init_device")
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
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
RuntimeError: SetPrecisionMode:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:155 NPU function error: at_npu::native::AclSetCompileopt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
[ERROR] 2025-05-27-09:41:38 (PID:307, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The internal ACL of the system is incorrect.
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
EH9999: [PID: 307] 2025-05-27-09:41:38.250.050 [Init][PlatformInfo]init runtime platform info failed, SocVersion = Ascend910B2[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
       GELib::InnerInitialize failed.[FUNC:Initialize][FILE:gelib.cc][LINE:184]
       GEInitialize failed.[FUNC:GEInitialize][FILE:ge_api.cc][LINE:371]
       [Initialize][Ge]GEInitialize failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
       [Init][Compiler]Init compiler failed[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
       [Set][Options]OpCompileProcessor init failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

```
