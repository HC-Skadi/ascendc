# Issue #441: [Bug]: TypeError is raised for ProcessGroup when runing data parallel

## 基本信息

- **编号**: #441
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/441
- **创建时间**: 2025-03-31T06:36:28Z
- **关闭时间**: 2025-06-11T06:21:17Z
- **更新时间**: 2025-06-11T06:21:17Z
- **提交者**: @yangqinj
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 03-31 06:25:19 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-31 06:25:19 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-31 06:25:19 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-31 06:25:19 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-31 06:25:19 [__init__.py:44] plugin ascend loaded.
INFO 03-31 06:25:19 [__init__.py:230] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-91-generic-aarch64-with-glibc2.35

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
Core(s) per socket:                 48
Socket(s):                          4
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
[pip3] transformers==4.50.2
[conda] Could not collect
vLLM Version: 0.8.3.dev80+gb2dde038 (git sha: b2dde038)
vLLM Ascend Version: 0.1.dev132+g2237453 (git sha: 2237453)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
VLLM_WORKER_MULTIPROC_METHOD=spawn
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
VLLM_HOST_IP=7.193.130.36
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.6                   Version: 23.0.6                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 86.3        37                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2791 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 88.0        39                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2792 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 88.3        39                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2791 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 87.4        39                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2791 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 94.0        41                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2787 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 85.1        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2787 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 91.4        50                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2787 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 91.4        41                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2787 / 32768         |
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

</details>


### 🐛 Describe the bug

TypeError is raised for ProcessGroup when runing data parallel:
```bash
INFO 03-31 03:07:52 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-31 03:07:52 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-31 03:07:52 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-31 03:07:52 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-31 03:07:52 [__init__.py:44] plugin ascend loaded.
INFO 03-31 03:07:52 [__init__.py:230] Platform plugin ascend is activated
INFO 03-31 03:07:55 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 03-31 03:07:55 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 03-31 03:07:55 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 03-31 03:07:55 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-31 03:07:55 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 03-31 03:07:55 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-31 03:07:55 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 03-31 03:07:55 [registry.py:366] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
INFO 03-31 03:07:55 [api_server.py:1018] vLLM API server version 0.8.3.dev80+gb2dde038
INFO 03-31 03:07:55 [api_server.py:1019] args: Namespace(subparser='serve', model_tag='/home/models/Qwen1.5-MoE-A2.7B-Chat', config='', host='7.193.130.36', port=8080, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=True, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/home/models/Qwen1.5-MoE-A2.7B-Chat', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=4096, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=4, data_parallel_size=2, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=128, enable_prefix_caching=None, prefix_caching_hash_algo='builtin', disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.8, num_gpu_blocks_override=None, max_num_batched_tokens=16384, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=4, max_logprobs=20, disable_log_stats=True, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=True, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, use_tqdm_on_load=True, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_config=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['Qwen1.5-MoE-A2.7B-Chat'], qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, enable_reasoning=False, reasoning_parser=None, disable_cascade_attn=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, enable_server_load_tracking=False, dispatch_function=<function ServeSubcommand.cmd at 0xfffdb7369000>)
INFO 03-31 03:08:05 [config.py:593] This model supports multiple tasks: {'generate', 'reward', 'score', 'classify', 'embed'}. Defaulting to 'generate'.
WARNING 03-31 03:08:05 [arg_utils.py:1888] Detected VLLM_USE_V1=1 with npu. Usage should be considered experimental. Please report any issues on Github.
INFO 03-31 03:08:05 [config.py:1563] Defaulting to use mp for distributed inference
INFO 03-31 03:08:05 [config.py:1742] Chunked prefill is enabled with max_num_batched_tokens=16384.
Prefix caching is not supported for V1 now, disable prefix caching
WARNING 03-31 03:08:05 [api_server.py:170] V1 is enabled, but got --disable-frontend-multiprocessing. To disable frontend multiprocessing, set VLLM_USE_V1=0.
INFO 03-31 03:08:12 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-31 03:08:12 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-31 03:08:12 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-31 03:08:12 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-31 03:08:12 [__init__.py:44] plugin ascend loaded.
INFO 03-31 03:08:12 [__init__.py:230] Platform plugin ascend is activated
INFO 03-31 03:08:12 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-31 03:08:12 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-31 03:08:12 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-31 03:08:12 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-31 03:08:12 [__init__.py:44] plugin ascend loaded.
INFO 03-31 03:08:12 [__init__.py:230] Platform plugin ascend is activated
[1;36m(EngineCore_1 pid=27550)[0;0m INFO 03-31 03:08:15 [utils.py:303] +++ prefix_store: <class 'torch.distributed.distributed_c10d.PrefixStore'>
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367] EngineCore hit an exception: Traceback (most recent call last):
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 353, in run_engine_core
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]     engine_core = DPEngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 533, in __init__
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]     self.dp_group = vllm_config.parallel_config.stateless_init_dp_group()
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/config.py", line 1465, in stateless_init_dp_group
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]     dp_group = stateless_init_torch_distributed_process_group(
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/distributed/utils.py", line 304, in stateless_init_torch_distributed_process_group
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]     pg: ProcessGroup = ProcessGroup(
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367] TypeError: __init__(): incompatible constructor arguments. The following argument types are supported:
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]     1. torch._C._distributed_c10d.ProcessGroup(arg0: int, arg1: int)
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367]     2. torch._C._distributed_c10d.ProcessGroup(arg0: torch._C._distributed_c10d.Store, arg1: int, arg2: int, arg3: c10d::ProcessGroup::Options)
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367] 
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367] Invoked with: <torch.distributed.distributed_c10d.PrefixStore object at 0xfffdce37fcb0>, 1, 2
[1;36m(EngineCore_1 pid=27550)[0;0m ERROR 03-31 03:08:15 [core.py:367] 
CRITICAL 03-31 03:08:15 [core_client.py:319] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
[1;36m(EngineCore_0 pid=27549)[0;0m INFO 03-31 03:08:15 [utils.py:303] +++ prefix_store: <class 'torch.distributed.distributed_c10d.PrefixStore'>

```

Version of main package:
 - vllm: main branch with commit 726efc6a320ad9a4ef0b0378b40abbd0561ea394 with extra modification for ascend 
 - vllm-ascend: main branch with commit b1557abab6534af830f1555f262332aba2bf6e51 with extra modification to adapt to vllm main branch
 -  torch：2.5.1
 - torch-npu: 2.5.1.dev20250320

Deploy on single node with 8 devices with TP+DP with command:
```bash
export VLLM_HOST_IP=$(/home/models/packages/hostname -I | awk '{print $1}')
export HCCL_CONNECT_TIMEOUT=120
export HCCL_IF_IP=$(/home/models/packages/hostname -I | awk '{print $1}')
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
export VLLM_USE_V1=1
export VLLM_WORKER_MULTIPROC_METHOD=spawn

vllm serve /home/models/Qwen1.5-MoE-A2.7B-Chat \
  --served-model-name Qwen1.5-MoE-A2.7B-Chat \
  --enforce-eager \
  --max-num-seqs=4 \
  --max-model-len=4096 \
  --max-num-batched-tokens=16384 \
  --tensor-parallel-size=4 \
  --data-parallel-size=2 \
  --block-size=128 \
  --host=$(/home/models/packages/hostname -I | awk '{print $1}') \
  --port=8080 \
  --gpu-memory-utilization=0.8 \
  --trust-remote-code \
  --disable-log-stats \
  --disable-frontend-multiprocessing 2>&1 | tee log_service_tp_ep_dp

```

You can reproduce with error with this simple snippet:
```bash
from torch.distributed.rendezvous import rendezvous
from torch.distributed.distributed_c10d import PrefixStore
from torch.distributed import ProcessGroup



host = "127.0.0.1"
port = 29500
init_method = f"tcp://{host}:{port}"

rank = 0
world_size = 1
store, rank, world_size = next(
        rendezvous(init_method, rank, world_size))
print(type(store))


prefix_store = PrefixStore(init_method, store)
print(type(prefix_store))

pg: ProcessGroup = ProcessGroup(
        prefix_store,
        rank,
        world_size,
    )

```

