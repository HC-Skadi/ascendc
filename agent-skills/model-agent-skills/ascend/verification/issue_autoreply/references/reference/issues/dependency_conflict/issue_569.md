# Issue #569: [Bug]: 推理量化模型qwen2.5-32b-w8a8报错

## 基本信息

- **编号**: #569
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/569
- **创建时间**: 2025-04-18T06:51:16Z
- **关闭时间**: 2025-05-14T05:15:26Z
- **更新时间**: 2025-06-03T04:02:34Z
- **提交者**: @YuBYan
- **评论数**: 9

## 标签

bug

## 问题描述

### Your current environment

<details>
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.oe2203.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
Frequency boost:                 disabled
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
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
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] transformers==4.50.3
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc2

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
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
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 98.6        39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3387 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 92.6        37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3387 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 92.5        38                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 92.2        38                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3385 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 100.2       45                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3385 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 95.7        42                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3385 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 91.1        40                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3385 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 91.3        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3386 / 65536         |
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
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux

</details>


### 🐛 Describe the bug

使用昇腾官网对qwen2.5-instruct-32b模型进行w8a8量化

cd ${llm_path}
bash examples/models/qwen/convert_quant_weight.sh -src {浮点权重路径} -dst {W8A8量化权重路径} -type qwen_w8a8

我使用/usr/local/Ascend/mindie/latest/mindie-service/bin/mindieservice_daemon 验证量化后的模型是否可用，是可以推理运行的

在vllm中，使用命令 
**vllm serve /root/.cache/Qwen2.5-32B-Instruct-w8a8/  --served-model-name "qwen2.5_32b" -tp 1**
运行报错
INFO 04-18 06:28:02 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-18 06:28:02 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-18 06:28:02 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-18 06:28:02 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 06:28:02 __init__.py:44] plugin ascend loaded.
INFO 04-18 06:28:02 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 04-18 06:28:02 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-18 06:28:02 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-18 06:28:02 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-18 06:28:02 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 06:28:02 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 04-18 06:28:02 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-18 06:28:02 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-18 06:28:02 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-18 06:28:02 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 04-18 06:28:02 api_server.py:912] vLLM API server version 0.7.3
INFO 04-18 06:28:02 api_server.py:913] args: Namespace(subparser='serve', model_tag='/root/.cache/Qwen2.5-32B-Instruct-w8a8/', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/root/.cache/Qwen2.5-32B-Instruct-w8a8/', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['qwen2.5_32b'], qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffdd1e760e0>)
INFO 04-18 06:28:02 api_server.py:209] Started engine process with PID 1030
INFO 04-18 06:28:10 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-18 06:28:10 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-18 06:28:10 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-18 06:28:10 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 06:28:10 __init__.py:44] plugin ascend loaded.
INFO 04-18 06:28:10 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 04-18 06:28:10 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 04-18 06:28:10 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 04-18 06:28:10 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 04-18 06:28:10 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-18 06:28:10 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 04-18 06:28:10 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
WARNING 04-18 06:28:10 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 04-18 06:28:10 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 04-18 06:28:10 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 04-18 06:28:12 config.py:549] This model supports multiple tasks: {'embed', 'reward', 'score', 'generate', 'classify'}. Defaulting to 'generate'.
WARNING 04-18 06:28:12 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 04-18 06:28:13 config.py:628] ascend quantization is not fully optimized yet. The speed can be slower than non-quantized models.
INFO 04-18 06:28:20 config.py:549] This model supports multiple tasks: {'reward', 'classify', 'score', 'generate', 'embed'}. Defaulting to 'generate'.
WARNING 04-18 06:28:20 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 04-18 06:28:21 config.py:628] ascend quantization is not fully optimized yet. The speed can be slower than non-quantized models.
INFO 04-18 06:28:21 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/root/.cache/Qwen2.5-32B-Instruct-w8a8/', speculative_config=None, tokenizer='/root/.cache/Qwen2.5-32B-Instruct-w8a8/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=ascend, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=qwen2.5_32b, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True, 
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
WARNING 04-18 06:28:22 utils.py:2262] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd2f186b60>
ERROR 04-18 06:28:36 engine.py:400] 'model.layers.0.self_attn.q_proj.weight'
ERROR 04-18 06:28:36 engine.py:400] Traceback (most recent call last):
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 04-18 06:28:36 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
ERROR 04-18 06:28:36 engine.py:400]     return cls(ipc_path=ipc_path,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self.engine = LLMEngine(*args, **kwargs)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self.model_executor = executor_class(vllm_config=vllm_config, )
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self._init_executor()
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
ERROR 04-18 06:28:36 engine.py:400]     self.collective_rpc("load_model")
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 04-18 06:28:36 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 04-18 06:28:36 engine.py:400]     return func(*args, **kwargs)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
ERROR 04-18 06:28:36 engine.py:400]     self.model_runner.load_model()
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 824, in load_model
ERROR 04-18 06:28:36 engine.py:400]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 04-18 06:28:36 engine.py:400]     return loader.load_model(vllm_config=vllm_config)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
ERROR 04-18 06:28:36 engine.py:400]     model = _initialize_model(vllm_config=vllm_config)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
ERROR 04-18 06:28:36 engine.py:400]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 453, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self.model = Qwen2Model(vllm_config=vllm_config,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
ERROR 04-18 06:28:36 engine.py:400]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 307, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
ERROR 04-18 06:28:36 engine.py:400]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
ERROR 04-18 06:28:36 engine.py:400]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 309, in <lambda>
ERROR 04-18 06:28:36 engine.py:400]     lambda prefix: Qwen2DecoderLayer(config=config,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 208, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self.self_attn = Qwen2Attention(
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self.qkv_proj = QKVParallelLinear(
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 736, in __init__
ERROR 04-18 06:28:36 engine.py:400]     super().__init__(input_size=input_size,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 305, in __init__
ERROR 04-18 06:28:36 engine.py:400]     super().__init__(input_size, output_size, skip_bias_add, params_dtype,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
ERROR 04-18 06:28:36 engine.py:400]     self.quant_method = quant_config.get_quant_method(self,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
ERROR 04-18 06:28:36 engine.py:400]     if self.is_layer_skipped_ascend(prefix,
ERROR 04-18 06:28:36 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 124, in is_layer_skipped_ascend
ERROR 04-18 06:28:36 engine.py:400]     is_shard_skipped = self.quant_description[shard_prefix +
ERROR 04-18 06:28:36 engine.py:400] KeyError: 'model.layers.0.self_attn.q_proj.weight'
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
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
    self.collective_rpc("load_model")
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
    self.model_runner.load_model()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 824, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
    return loader.load_model(vllm_config=vllm_config)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
    model = _initialize_model(vllm_config=vllm_config)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
    return model_class(vllm_config=vllm_config, prefix=prefix)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 453, in __init__
    self.model = Qwen2Model(vllm_config=vllm_config,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
    old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 307, in __init__
    self.start_layer, self.end_layer, self.layers = make_layers(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
    [PPMissingLayer() for _ in range(start_layer)] + [
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
    maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 309, in <lambda>
    lambda prefix: Qwen2DecoderLayer(config=config,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 208, in __init__
    self.self_attn = Qwen2Attention(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
    self.qkv_proj = QKVParallelLinear(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 736, in __init__
    super().__init__(input_size=input_size,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 305, in __init__
    super().__init__(input_size, output_size, skip_bias_add, params_dtype,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
    self.quant_method = quant_config.get_quant_method(self,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
    if self.is_layer_skipped_ascend(prefix,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 124, in is_layer_skipped_ascend
    is_shard_skipped = self.quant_description[shard_prefix +
KeyError: 'model.layers.0.self_attn.q_proj.weight'
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
[ERROR] 2025-04-18-06:28:44 (PID:957, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
