# Issue #348: [Bug]: Can't run quantized DeepSeek-R1-w8a8

## 基本信息

- **编号**: #348
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/348
- **创建时间**: 2025-03-18T03:23:55Z
- **关闭时间**: 2025-05-14T02:32:13Z
- **更新时间**: 2025-05-14T02:32:13Z
- **提交者**: @zkryakgul
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

```text
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.35
Is XNNPACK available: True

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
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] transformers==4.49.0
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.6                   Version: 23.0.6                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 96.0        47                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3344 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 93.5        48                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3342 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 93.0        48                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3342 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 96.0        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3342 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 93.8        48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3343 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 93.5        47                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3342 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 92.6        49                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3343 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 93.9        51                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3341 / 65536         |
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
```

### 🐛 Describe the bug

I'm trying to run quintized version of DeepSeek-R1 Accross 2 node ray cluster with image version `vllm-ascend:v0.7.3rc1`. But it fails to run model. Here is my commands to run

```bash
############################### RAY SETUP ###############################
# Head node
export HCCL_IF_IP=192.168.0.88
export GLOO_SOCKET_IFNAME=enp67s0f5
export TP_SOCKET_IFNAME=enp67s0f5
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1
ray start --head --num-gpus=8

# Worker node
export HCCL_IF_IP=192.168.0.88
export ASCEND_PROCESS_LOG_PATH=/var/log/plog
export GLOO_SOCKET_IFNAME=enp67s0f5
export TP_SOCKET_IFNAME=enp67s0f5
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1 
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ray --logging-level=debug start --block --address='192.168.0.88:6379' --num-gpus=8 --node-ip-address=192.168.0.60 &

############################### RUN MODEL ###############################

# Head Node
export VLLM_HOST_IP=192.168.0.88
export HCCL_CONNECT_TIMEOUT=120
export ASCEND_PROCESS_LOG_PATH=/var/log/plog
export HCCL_IF_IP=192.168.0.88

if [ -d "{plog_save_path}" ]; then
    rm -rf {plog_save_path}
    echo ">>> remove {plog_save_path}"
fi

LOG_FILE="multinode_$(date +%Y%m%d_%H%M).log"
VLLM_TORCH_PROFILER_DIR=./vllm_profile
python -m vllm.entrypoints.openai.api_server  \
       --model="/home/mind/model" \
       --trust-remote-code \
       --enforce-eager \
       --max-model-len 32768 \
       --distributed_executor_backend "ray" \
       --tensor-parallel-size 8 \
       --pipeline-parallel-size 2 \
       --disable-log-requests \
       --disable-log-stats \
       --disable-frontend-multiprocessing \
       --port 8080 
```

Output Logs:
```ini
INFO 03-18 03:09:14 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-18 03:09:14 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-18 03:09:14 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-18 03:09:14 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-18 03:09:14 __init__.py:44] plugin ascend loaded.
INFO 03-18 03:09:14 __init__.py:198] Platform plugin ascend is activated
INFO 03-18 03:09:14 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 03-18 03:09:14 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 03-18 03:09:14 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 03-18 03:09:14 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-18 03:09:14 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 03-18 03:09:14 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-18 03:09:15 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 03-18 03:09:16 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
INFO 03-18 03:09:16 api_server.py:912] vLLM API server version 0.7.3
INFO 03-18 03:09:16 api_server.py:913] args: Namespace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=True, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/home/mind/model', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend='ray', pipeline_parallel_size=2, tensor_parallel_size=8, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=True, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=True, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=True, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False)
INFO 03-18 03:09:16 config.py:208] Replacing legacy 'type' key with 'rope_type'
INFO 03-18 03:09:27 config.py:549] This model supports multiple tasks: {'classify', 'generate', 'score', 'reward', 'embed'}. Defaulting to 'generate'.
WARNING 03-18 03:09:27 config.py:628] ascend quantization is not fully optimized yet. The speed can be slower than non-quantized models.
WARNING 03-18 03:09:27 config.py:676] Async output processing can not be enabled with pipeline parallel
INFO 03-18 03:09:27 config.py:3329] MLA is enabled; forcing chunked prefill and prefix caching to be disabled.
INFO 03-18 03:09:27 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/home/mind/model', speculative_config=None, tokenizer='/home/mind/model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=2, disable_custom_all_reduce=False, quantization=ascend, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/home/mind/model, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=False, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, 
2025-03-18 03:09:28,110 INFO worker.py:1654 -- Connecting to existing Ray cluster at address: 192.168.0.88:6379...
2025-03-18 03:09:28,120 INFO worker.py:1841 -- Connected to Ray cluster.
INFO 03-18 03:09:45 ray_distributed_executor.py:153] use_ray_spmd_worker: False
(pid=14508) INFO 03-18 03:09:52 __init__.py:30] Available plugins for group vllm.platform_plugins:
(pid=14508) INFO 03-18 03:09:52 __init__.py:32] name=ascend, value=vllm_ascend:register
(pid=14508) INFO 03-18 03:09:52 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
(pid=14508) INFO 03-18 03:09:52 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(pid=14508) INFO 03-18 03:09:52 __init__.py:44] plugin ascend loaded.
(pid=14508) INFO 03-18 03:09:52 __init__.py:198] Platform plugin ascend is activated
(pid=14508) INFO 03-18 03:09:52 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
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
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) INFO 03-18 03:09:56 __init__.py:30] Available plugins for group vllm.general_plugins:
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) INFO 03-18 03:09:56 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) INFO 03-18 03:09:56 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) INFO 03-18 03:09:56 __init__.py:44] plugin ascend_enhanced_model loaded.
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) WARNING 03-18 03:09:56 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) WARNING 03-18 03:09:56 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
(NPURayWorkerWrapper pid=14509) /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning: 
(NPURayWorkerWrapper pid=14509)     *************************************************************************************************************
(NPURayWorkerWrapper pid=14509)     The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now..
(NPURayWorkerWrapper pid=14509)     The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now..
(NPURayWorkerWrapper pid=14509)     The backend in torch.distributed.init_process_group set to hccl now..
(NPURayWorkerWrapper pid=14509)     The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now..
(NPURayWorkerWrapper pid=14509)     The device parameters have been replaced with npu in the function below:
(NPURayWorkerWrapper pid=14509)     torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty
(NPURayWorkerWrapper pid=14509)     *************************************************************************************************************
(NPURayWorkerWrapper pid=14509)     
(NPURayWorkerWrapper pid=14509)   warnings.warn(msg, ImportWarning)
(NPURayWorkerWrapper pid=14509) /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu.
(NPURayWorkerWrapper pid=14509)   warnings.warn(msg, RuntimeWarning)
(NPURayWorkerWrapper pid=14505)     
(NPURayWorkerWrapper pid=14504)     
(NPURayWorkerWrapper pid=14503)     
(NPURayWorkerWrapper pid=14502)     
(NPURayWorkerWrapper pid=14594)     
(NPURayWorkerWrapper pid=14703)     
WARNING 03-18 03:09:56 utils.py:2262] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd201ee1d0>
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) WARNING 03-18 03:09:56 utils.py:2262] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffa07108b50>
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2597, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2598, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2599, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2600, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2602, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2601, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) INFO 03-18 03:10:04 shm_broadcast.py:258] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_f936c8e3'), local_subscribe_port=43919, remote_subscribe_port=None)
(pid=2603, ip=192.168.0.60) INFO 03-18 03:09:54 __init__.py:30] Available plugins for group vllm.platform_plugins: [repeated 15x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(pid=2603, ip=192.168.0.60) INFO 03-18 03:09:54 __init__.py:32] name=ascend, value=vllm_ascend:register [repeated 15x across cluster]
(pid=2603, ip=192.168.0.60) INFO 03-18 03:09:54 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded. [repeated 15x across cluster]
(NPURayWorkerWrapper pid=14703) INFO 03-18 03:09:56 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. [repeated 30x across cluster]
(pid=2603, ip=192.168.0.60) INFO 03-18 03:09:54 __init__.py:44] plugin ascend loaded. [repeated 15x across cluster]
(pid=2603, ip=192.168.0.60) INFO 03-18 03:09:54 __init__.py:198] Platform plugin ascend is activated [repeated 15x across cluster]
(pid=2603, ip=192.168.0.60) INFO 03-18 03:09:54 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available. [repeated 15x across cluster]
(NPURayWorkerWrapper pid=14703) INFO 03-18 03:09:56 __init__.py:30] Available plugins for group vllm.general_plugins: [repeated 14x across cluster]
(NPURayWorkerWrapper pid=14703) INFO 03-18 03:09:56 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model [repeated 14x across cluster]
(NPURayWorkerWrapper pid=14703) INFO 03-18 03:09:56 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=14703) INFO 03-18 03:09:56 __init__.py:44] plugin ascend_enhanced_model loaded. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=14703) WARNING 03-18 03:09:56 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") [repeated 14x across cluster]
(NPURayWorkerWrapper pid=14703) WARNING 03-18 03:09:56 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=14703) WARNING 03-18 03:09:56 utils.py:2262] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffa2dc88a90> [repeated 14x across cluster]
INFO 03-18 03:10:04 shm_broadcast.py:258] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_4ac13411'), local_subscribe_port=44861, remote_subscribe_port=None)
WARNING 03-18 03:10:04 utils.py:168] The model class DeepseekV3ForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) WARNING 03-18 03:10:04 utils.py:168] The model class DeepseekV3ForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581] Error executing method 'load_model'. This might cause deadlock in distributed execution.
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581] Traceback (most recent call last):
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     return run_method(target, method, args, kwargs)
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     return func(*args, **kwargs)
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.model_runner.load_model()
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 818, in load_model
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.model = get_model(vllm_config=self.vllm_config)
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     return loader.load_model(vllm_config=vllm_config)
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     model = _initialize_model(vllm_config=vllm_config)
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     return model_class(vllm_config=vllm_config, prefix=prefix)
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.model = DeepseekV2Model(vllm_config=vllm_config,
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.start_layer, self.end_layer, self.layers = make_layers(
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     [PPMissingLayer() for _ in range(start_layer)] + [
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
ERROR 03-18 03:10:05 worker_base.py:581] Error executing method 'load_model'. This might cause deadlock in distributed execution.
ERROR 03-18 03:10:05 worker_base.py:581] Traceback (most recent call last):
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
ERROR 03-18 03:10:05 worker_base.py:581]     return run_method(target, method, args, kwargs)
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 03-18 03:10:05 worker_base.py:581]     return func(*args, **kwargs)
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
ERROR 03-18 03:10:05 worker_base.py:581]     self.model_runner.load_model()
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 818, in load_model
ERROR 03-18 03:10:05 worker_base.py:581]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 03-18 03:10:05 worker_base.py:581]     return loader.load_model(vllm_config=vllm_config)
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
ERROR 03-18 03:10:05 worker_base.py:581]     model = _initialize_model(vllm_config=vllm_config)
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
ERROR 03-18 03:10:05 worker_base.py:581]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
ERROR 03-18 03:10:05 worker_base.py:581]     self.model = DeepseekV2Model(vllm_config=vllm_config,
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
ERROR 03-18 03:10:05 worker_base.py:581]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
ERROR 03-18 03:10:05 worker_base.py:581]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
ERROR 03-18 03:10:05 worker_base.py:581]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
ERROR 03-18 03:10:05 worker_base.py:581]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
ERROR 03-18 03:10:05 worker_base.py:581]     lambda prefix: DeepseekV2DecoderLayer(
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
ERROR 03-18 03:10:05 worker_base.py:581]     self.self_attn = attn_cls(
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 374, in __init__
ERROR 03-18 03:10:05 worker_base.py:581]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 209, in __init__
ERROR 03-18 03:10:05 worker_base.py:581]     super().__init__(input_size,
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
ERROR 03-18 03:10:05 worker_base.py:581]     self.quant_method = quant_config.get_quant_method(self,
ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 89, in get_quant_method
ERROR 03-18 03:10:05 worker_base.py:581]     self.packed_modules_mapping):
ERROR 03-18 03:10:05 worker_base.py:581] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     lambda prefix: DeepseekV2DecoderLayer(
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.self_attn = attn_cls(
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 374, in __init__
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 209, in __init__
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     super().__init__(input_size,
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.quant_method = quant_config.get_quant_method(self,
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 89, in get_quant_method
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581]     self.packed_modules_mapping):
(NPURayWorkerWrapper pid=14502) ERROR 03-18 03:10:05 worker_base.py:581] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/local/python3.10/lib/python3.10/runpy.py", line 196, in _run_module_as_main
[rank0]:     return _run_code(code, main_globals, None,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/runpy.py", line 86, in _run_code
[rank0]:     exec(code, run_globals)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 991, in <module>
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
[rank0]:     return loop.run_until_complete(wrapper())
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
[rank0]:     async with build_async_engine_client(args) as engine_client:
[rank0]:   File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 163, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 644, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 594, in __init__
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 267, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 271, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 90, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 360, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 480, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 582, in execute_method
[rank0]:     raise e
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
[rank0]:     return run_method(target, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 818, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
[rank0]:     model = _initialize_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
[rank0]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
[rank0]:     self.model = DeepseekV2Model(vllm_config=vllm_config,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
[rank0]:     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
[rank0]:     self.start_layer, self.end_layer, self.layers = make_layers(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
[rank0]:     [PPMissingLayer() for _ in range(start_layer)] + [
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
[rank0]:     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
[rank0]:     lambda prefix: DeepseekV2DecoderLayer(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
[rank0]:     self.self_attn = attn_cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 374, in __init__
[rank0]:     self.q_a_proj = ReplicatedLinear(self.hidden_size,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 209, in __init__
[rank0]:     super().__init__(input_size,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
[rank0]:     self.quant_method = quant_config.get_quant_method(self,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 89, in get_quant_method
[rank0]:     self.packed_modules_mapping):
[rank0]: AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60) WARNING 03-18 03:10:04 utils.py:168] The model class DeepseekV3ForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581] Error executing method 'load_model'. This might cause deadlock in distributed execution. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581] Traceback (most recent call last): [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     return run_method(target, method, args, kwargs) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     return func(*args, **kwargs) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model [repeated 42x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.model_runner.load_model() [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.model = get_model(vllm_config=self.vllm_config) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     return loader.load_model(vllm_config=vllm_config) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     model = _initialize_model(vllm_config=vllm_config) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     return model_class(vllm_config=vllm_config, prefix=prefix) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__ [repeated 98x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.model = DeepseekV2Model(vllm_config=vllm_config, [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.start_layer, self.end_layer, self.layers = make_layers( [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     [PPMissingLayer() for _ in range(start_layer)] + [ [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp> [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda> [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     lambda prefix: DeepseekV2DecoderLayer( [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.self_attn = attn_cls( [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.q_a_proj = ReplicatedLinear(self.hidden_size, [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     super().__init__(input_size, [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.quant_method = quant_config.get_quant_method(self, [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 89, in get_quant_method [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581]     self.packed_modules_mapping): [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2596, ip=192.168.0.60) ERROR 03-18 03:10:06 worker_base.py:581] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping' [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60) /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning:  [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     ************************************************************************************************************* [repeated 28x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now.. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now.. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     The backend in torch.distributed.init_process_group set to hccl now.. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now.. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     The device parameters have been replaced with npu in the function below: [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)     torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)   warnings.warn(msg, ImportWarning) [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60) /usr/local/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu. [repeated 14x across cluster]
(NPURayWorkerWrapper pid=2603, ip=192.168.0.60)   warnings.warn(msg, RuntimeWarning) [repeated 14x across cluster]
[ERROR] 2025-03-18-03:10:08 (PID:14193, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
INFO 03-18 03:10:08 ray_distributed_executor.py:104] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
sys:1: ResourceWarning: unclosed <socket.socket fd=15, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 8080)>
root@model:/workspace# /usr/local/python3.10/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

```
