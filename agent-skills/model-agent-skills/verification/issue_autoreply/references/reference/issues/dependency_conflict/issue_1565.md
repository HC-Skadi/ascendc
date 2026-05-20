# Issue #1565: [Bug]: vllm serve with tp=2 on 310P crashes

## 基本信息

- **编号**: #1565
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1565
- **创建时间**: 2025-07-01T11:23:58Z
- **关闭时间**: 2025-12-23T11:26:18Z
- **更新时间**: 2025-12-23T11:26:18Z
- **提交者**: @SorryMaker2022
- **评论数**: 1

## 标签

bug; 310p

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
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.10.17 (main, May 27 2025, 01:34:13) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-6.8.0-60-generic-x86_64-with-glibc2.35

CPU:
Architecture:                         x86_64
CPU op-mode(s):                       32-bit, 64-bit
Address sizes:                        46 bits physical, 48 bits virtual
Byte Order:                           Little Endian
CPU(s):                               20
On-line CPU(s) list:                  0-19
Vendor ID:                            GenuineIntel
Model name:                           Intel(R) Core(TM) i5-14500
CPU family:                           6
Model:                                191
Thread(s) per core:                   2
Core(s) per socket:                   14
Socket(s):                            1
Stepping:                             2
CPU max MHz:                          5000.0000
CPU min MHz:                          800.0000
BogoMIPS:                             5222.40
Flags:                                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap clflushopt clwb intel_pt sha_ni xsaveopt xsavec xgetbv1 xsaves split_lock_detect user_shstk avx_vnni dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku ospke waitpkg gfni vaes vpclmulqdq tme rdpid movdiri movdir64b fsrm md_clear serialize pconfig arch_lbr ibt flush_l1d arch_capabilities
Virtualization:                       VT-x
L1d cache:                            544 KiB (14 instances)
L1i cache:                            704 KiB (14 instances)
L2 cache:                             11.5 MiB (8 instances)
L3 cache:                             24 MiB (1 instance)
NUMA node(s):                         1
NUMA node0 CPU(s):                    0-19
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Mitigation; Clear Register File
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:             Mitigation; Enhanced / Automatic IBRS; IBPB conditional; RSB filling; PBRSB-eIBRS SW sequence; BHI BHI_DIS_S
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1+cpu
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.20.1+cpu
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1rc2.dev45+gb308a7a (git sha: b308a7a)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ASCEND_LAUNCH_BLOCKING=1
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1                               Version: 25.0.rc1.1                                   |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 8       310P3                 | OK              | NA           47                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1475 / 44280                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 8       310P3                 | OK              | NA           45                0     / 0             |
| 1       1                     | 0000:01:00.0    | 0            1462 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 8                                                                    |
+===============================+=================+======================================================+

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

I am trying to run mistral-7B on ascend 310P with TP=2 (for tp test), with offline inference (using vllm.LLM, tensor_patallel_size=2) everything is fine:
```
python test.py 
INFO 06-30 09:36:06 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-30 09:36:06 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-30 09:36:07 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-30 09:36:07 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-30 09:36:07 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-30 09:36:07 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-30 09:36:08 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 06-30 09:36:09 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-30 09:36:09 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-30 09:36:09 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-30 09:36:09 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-30 09:36:09 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-30 09:36:09 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-30 09:36:14 [config.py:823] This model supports multiple tasks: {'generate', 'embed', 'classify', 'reward', 'score'}. Defaulting to 'generate'.
INFO 06-30 09:36:14 [arg_utils.py:1653] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
reach here
INFO 06-30 09:36:14 [config.py:1946] Defaulting to use mp for distributed inference
INFO 06-30 09:36:14 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-30 09:36:14 [platform.py:168] Compilation disabled, using eager mode by default
INFO 06-30 09:36:14 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: ...
WARNING 06-30 09:36:14 [multiproc_worker_utils.py:307] Reducing Torch parallelism from 14 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
(VllmWorkerProcess pid=224682) INFO 06-30 09:36:14 [multiproc_worker_utils.py:226] Worker ready; awaiting tasks
(VllmWorkerProcess pid=224682) WARNING 06-30 09:36:14 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x798c54bc60e0>
WARNING 06-30 09:36:14 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x798c54bc6200>
INFO 06-30 09:36:19 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_a666b14f'), local_subscribe_addr='ipc:///tmp/ef5d6b01-5739-4be2-9d05-c0b6649b7054', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 06-30 09:36:19 [parallel_state.py:1065] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(VllmWorkerProcess pid=224682) INFO 06-30 09:36:19 [parallel_state.py:1065] rank 1 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 06-30 09:36:19 [model_runner.py:995] Starting to load model ...

INFO 06-30 09:37:02 [default_loader.py:273] Loading weights took 38.71 seconds
(VllmWorkerProcess pid=224682) INFO 06-30 09:37:02 [default_loader.py:273] Loading weights took 38.53 seconds
[rank0]:[W630 09:37:03.359572320 AddKernelNpu.cpp:82] Warning: The oprator of add is executed, Currently High Accuracy but Low Performance OP with 64-bit has been used, Please Do Some Cast at Python Functions with 32-bit for Better Performance! (function operator())
[rank1]:[W630 09:37:03.360115442 AddKernelNpu.cpp:82] Warning: The oprator of add is executed, Currently High Accuracy but Low Performance OP with 64-bit has been used, Please Do Some Cast at Python Functions with 32-bit for Better Performance! (function operator())
..../usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py:124: UserWarning: HCCL doesn't support gather at the moment. Implemented with allgather instead.
  warnings.warn("HCCL doesn't support gather at the moment. Implemented with allgather instead.")
[rank0]:[W630 09:37:14.215883568 OpCommand.cpp:79] Warning: [Check][offset] Check input storage_offset[%ld] = 0 failed, result is untrustworthy151935 (function operator())
INFO 06-30 09:37:17 [executor_base.py:113] # npu blocks: 2209, # CPU blocks: 819
INFO 06-30 09:37:17 [executor_base.py:118] Maximum concurrency for 4096 tokens per request: 69.03x

INFO 06-30 09:37:18 [llm_engine.py:428] init engine (profile, create kv cache, warmup model) took 15.21 seconds
Adding requests: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 442.94it/s]
Processed prompts:   0%|                                                                                                                                                                                                                       | 0/4 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]Processed prompts: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [05:56<00:00, 89.12s/it, est. speed input: 0.06 toks/s, output: 0.18 toks/s]
Prompt: 'Hello, my name is', Generated text: ' Shin-yei" (Sorry for my spelling errors, it\'s not the'
Prompt: 'The president of the United States is', Generated text: ' elected every four years. Next year, we will be electing our new president'
Prompt: 'The capital of France is', Generated text: ' Paris." This sentence uses the is to refer to the capital of a country.\n'
Prompt: 'The future of AI is', Generated text: ' not bright when you think of the, of course you will be thinking about the'
```

But with 

`export ASCEND_RT_VISIBLE_DEVICES=0,1 && vllm serve --tensor-parallel-size 2 --trust-remote-code /path/to/Mistral-7B`

the inference engine reports an error on HcclAllgather: errcode 6:

```
INFO 07-01 00:37:05 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-01 00:37:05 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-01 00:37:05 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-01 00:37:05 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-01 00:37:05 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-01 00:37:05 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-01 00:37:06 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-01 00:37:08 [registry.py:402] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-01 00:37:08 [registry.py:402] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-01 00:37:08 [registry.py:402] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-01 00:37:08 [registry.py:402] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-01 00:37:08 [registry.py:402] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-01 00:37:08 [registry.py:402] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-01 00:37:08 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 00:37:09 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 00:37:09 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 00:37:10 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 00:37:10 [api_server.py:1287] vLLM API server version 0.9.1
INFO 07-01 00:37:10 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 00:37:10 [cli_args.py:309] non-default args: {'model': '/home/gjx/model/Mistral-7B-Instruct-v0.3', 'trust_remote_code': True, 'tensor_parallel_size': 2}
INFO 07-01 00:37:15 [config.py:823] This model supports multiple tasks: {'reward', 'score', 'generate', 'embed', 'classify'}. Defaulting to 'generate'.
INFO 07-01 00:37:15 [arg_utils.py:1653] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
reach here
INFO 07-01 00:37:15 [config.py:1946] Defaulting to use mp for distributed inference
INFO 07-01 00:37:15 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 00:37:15 [platform.py:168] Compilation disabled, using eager mode by default
INFO 07-01 00:37:15 [api_server.py:265] Started engine process with PID 176930
WARNING 07-01 00:37:17 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 07-01 00:37:17 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-01 00:37:17 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-01 00:37:17 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-01 00:37:17 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-01 00:37:17 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-01 00:37:17 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-01 00:37:18 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-01 00:37:20 [registry.py:402] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-01 00:37:20 [registry.py:402] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-01 00:37:20 [registry.py:402] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-01 00:37:20 [registry.py:402] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-01 00:37:20 [registry.py:402] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-01 00:37:20 [registry.py:402] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-01 00:37:20 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='/home/gjx/model/Mistral-7B-Instruct-v0.3', speculative_config=None, tokenizer='/home/gjx/model/Mistral-7B-Instruct-v0.3', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/home/gjx/model/Mistral-7B-Instruct-v0.3, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":256,"local_cache_dir":null}, use_cached_outputs=True, 
WARNING 07-01 00:37:20 [multiproc_worker_utils.py:307] Reducing Torch parallelism from 14 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
WARNING 07-01 00:37:20 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x75b3e4460f10>
WARNING 07-01 00:37:21 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 07-01 00:37:22 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-01 00:37:22 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-01 00:37:22 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-01 00:37:22 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-01 00:37:22 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-01 00:37:22 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-01 00:37:23 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
[1;36m(VllmWorkerProcess pid=176981)[0;0m INFO 07-01 00:37:24 [multiproc_worker_utils.py:226] Worker ready; awaiting tasks
[1;36m(VllmWorkerProcess pid=176981)[0;0m WARNING 07-01 00:37:25 [registry.py:402] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
[1;36m(VllmWorkerProcess pid=176981)[0;0m WARNING 07-01 00:37:25 [registry.py:402] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
[1;36m(VllmWorkerProcess pid=176981)[0;0m WARNING 07-01 00:37:25 [registry.py:402] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
[1;36m(VllmWorkerProcess pid=176981)[0;0m WARNING 07-01 00:37:25 [registry.py:402] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
[1;36m(VllmWorkerProcess pid=176981)[0;0m WARNING 07-01 00:37:25 [registry.py:402] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
[1;36m(VllmWorkerProcess pid=176981)[0;0m WARNING 07-01 00:37:25 [registry.py:402] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
[1;36m(VllmWorkerProcess pid=176981)[0;0m WARNING 07-01 00:37:25 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0x737f673f3f70>
WARNING 07-01 00:37:28 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
WARNING 07-01 00:37:28 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 07-01 00:37:28 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-01 00:37:28 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-01 00:37:28 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-01 00:37:28 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-01 00:37:28 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-01 00:37:28 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-01 00:37:28 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-01 00:37:28 [__init__.py:235] Platform plugin ascend is activated
INFO 07-01 00:37:29 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-01 00:37:29 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-01 00:37:29 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-01 00:37:29 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-01 00:37:30 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-01 00:37:30 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-01 00:37:33 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_556fb4ff'), local_subscribe_addr='ipc:///tmp/768b5183-2993-4cb5-b337-0bbd0f630941', remote_subscribe_addr=None, remote_addr_ipv6=False)
[1;36m(VllmWorkerProcess pid=176981)[0;0m INFO 07-01 00:37:33 [parallel_state.py:1065] rank 1 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 07-01 00:37:33 [parallel_state.py:1065] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 07-01 00:37:33 [model_runner.py:995] Starting to load model /home/gjx/model/Mistral-7B-Instruct-v0.3...
[1;36m(VllmWorkerProcess pid=176981)[0;0m INFO 07-01 00:37:33 [model_runner.py:995] Starting to load model /home/gjx/model/Mistral-7B-Instruct-v0.3...

Loading safetensors checkpoint shards:   0% Completed | 0/3 [00:00<?, ?it/s]

Loading safetensors checkpoint shards:  33% Completed | 1/3 [00:01<00:02,  1.23s/it]

Loading safetensors checkpoint shards:  67% Completed | 2/3 [00:02<00:01,  1.30s/it]

Loading safetensors checkpoint shards: 100% Completed | 3/3 [00:03<00:00,  1.32s/it]

Loading safetensors checkpoint shards: 100% Completed | 3/3 [00:03<00:00,  1.31s/it]

INFO 07-01 00:37:41 [default_loader.py:273] Loading weights took 3.97 seconds
[1;36m(VllmWorkerProcess pid=176981)[0;0m INFO 07-01 00:37:41 [default_loader.py:273] Loading weights took 3.97 seconds
INFO 07-01 00:37:41 [model_runner.py:1000] Loading model weights took 6.7585 GB
[1;36m(VllmWorkerProcess pid=176981)[0;0m INFO 07-01 00:37:41 [model_runner.py:1000] Loading model weights took 6.7585 GB
[rank1]:[W701 00:37:42.443843562 AddKernelNpu.cpp:82] Warning: The oprator of add is executed, Currently High Accuracy but Low Performance OP with 64-bit has been used, Please Do Some Cast at Python Functions with 32-bit for Better Performance! (function operator())
[rank0]:[W701 00:37:42.444075980 AddKernelNpu.cpp:82] Warning: The oprator of add is executed, Currently High Accuracy but Low Performance OP with 64-bit has been used, Please Do Some Cast at Python Functions with 32-bit for Better Performance! (function operator())
..../usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py:124: UserWarning: HCCL doesn't support gather at the moment. Implemented with allgather instead.
  warnings.warn("HCCL doesn't support gather at the moment. Implemented with allgather instead.")
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks.
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239] Traceback (most recent call last):
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 233, in _run_worker_process
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     output = run_method(worker, method, args, kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return func(*args, **kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return func(*args, **kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 288, in determine_num_available_blocks
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     self.model_runner.profile_run()
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return func(*args, **kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1205, in profile_run
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     self.execute_model(model_input, kv_caches, intermediate_tensors)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return func(*args, **kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1472, in execute_model
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     logits = self.model.compute_logits(hidden_or_intermediate_states,
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 590, in compute_logits
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     logits = self.logits_processor(self.lm_head, hidden_states,
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return forward_call(*args, **kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 71, in forward
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     logits = self._get_logits(hidden_states, lm_head, embedding_bias)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 114, in _get_logits
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     logits = self._gather_logits(logits)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 99, in _gather_logits
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     logits = tensor_model_parallel_gather(logits)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/distributed/communication_op.py", line 33, in tensor_model_parallel_gather
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return get_tp_group().gather(input_, dst, dim)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 419, in gather
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return self.device_communicator.gather(input_, dst, dim)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/distributed/device_communicators/base_device_communicator.py", line 197, in gather
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     torch.distributed.gather(input_,
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py", line 126, in _gather
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     dist.broadcast_object_list(recv_size_list, dst, group)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return func(*args, **kwargs)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 3154, in broadcast_object_list
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     object_list[i] = _tensor_to_object(obj_view, obj_size, group)
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2649, in _tensor_to_object
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239]     return _unpickler(io.BytesIO(buf)).load()
[1;36m(VllmWorkerProcess pid=176981)[0;0m ERROR 07-01 00:38:05 [multiproc_worker_utils.py:239] _pickle.UnpicklingError: invalid load key, '\x00'.
ERROR 07-01 00:40:04 [engine.py:458] InnerRunOpApi:torch_npu/csrc/framework/OpParamMaker.cpp:281 OPS function error: HcclAllgather, error code is 6
ERROR 07-01 00:40:04 [engine.py:458] [ERROR] 2025-07-01-00:40:04 (PID:176930, Device:0, RankID:-1) ERR01100 OPS call acl api failed.
ERROR 07-01 00:40:04 [engine.py:458] EI0006: [PID: 176930] 2025-07-01-00:40:04.135.732 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
ERROR 07-01 00:40:04 [engine.py:458]         Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
ERROR 07-01 00:40:04 [engine.py:458]         TraceBack (most recent call last):
ERROR 07-01 00:40:04 [engine.py:458]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[0]-localUserrank[0]-localIpAddr[172.17.0.2], dst_rank[1]-remoteUserrank[1]-remote_ip_addr[172.17.0.2]
ERROR 07-01 00:40:04 [engine.py:458] Traceback (most recent call last):
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 446, in run_mp_engine
ERROR 07-01 00:40:04 [engine.py:458]     engine = MQLLMEngine.from_vllm_config(
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 133, in from_vllm_config
ERROR 07-01 00:40:04 [engine.py:458]     return cls(
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 87, in __init__
ERROR 07-01 00:40:04 [engine.py:458]     self.engine = LLMEngine(*args, **kwargs)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 268, in __init__
ERROR 07-01 00:40:04 [engine.py:458]     self._initialize_kv_caches()
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 413, in _initialize_kv_caches
ERROR 07-01 00:40:04 [engine.py:458]     self.model_executor.determine_num_available_blocks())
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 104, in determine_num_available_blocks
ERROR 07-01 00:40:04 [engine.py:458]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 332, in collective_rpc
ERROR 07-01 00:40:04 [engine.py:458]     return self._run_workers(method, *args, **(kwargs or {}))
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 186, in _run_workers
ERROR 07-01 00:40:04 [engine.py:458]     driver_worker_output = run_method(self.driver_worker, sent_method,
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
ERROR 07-01 00:40:04 [engine.py:458]     return func(*args, **kwargs)
ERROR 07-01 00:40:04 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 07-01 00:40:04 [engine.py:458]     return func(*args, **kwargs)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 288, in determine_num_available_blocks
ERROR 07-01 00:40:04 [engine.py:458]     self.model_runner.profile_run()
ERROR 07-01 00:40:04 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 07-01 00:40:04 [engine.py:458]     return func(*args, **kwargs)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1205, in profile_run
ERROR 07-01 00:40:04 [engine.py:458]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 07-01 00:40:04 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 07-01 00:40:04 [engine.py:458]     return func(*args, **kwargs)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1472, in execute_model
ERROR 07-01 00:40:04 [engine.py:458]     logits = self.model.compute_logits(hidden_or_intermediate_states,
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 590, in compute_logits
ERROR 07-01 00:40:04 [engine.py:458]     logits = self.logits_processor(self.lm_head, hidden_states,
ERROR 07-01 00:40:04 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 07-01 00:40:04 [engine.py:458]     return self._call_impl(*args, **kwargs)
ERROR 07-01 00:40:04 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 07-01 00:40:04 [engine.py:458]     return forward_call(*args, **kwargs)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 71, in forward
ERROR 07-01 00:40:04 [engine.py:458]     logits = self._get_logits(hidden_states, lm_head, embedding_bias)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 114, in _get_logits
ERROR 07-01 00:40:04 [engine.py:458]     logits = self._gather_logits(logits)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 99, in _gather_logits
ERROR 07-01 00:40:04 [engine.py:458]     logits = tensor_model_parallel_gather(logits)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/distributed/communication_op.py", line 33, in tensor_model_parallel_gather
ERROR 07-01 00:40:04 [engine.py:458]     return get_tp_group().gather(input_, dst, dim)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 419, in gather
ERROR 07-01 00:40:04 [engine.py:458]     return self.device_communicator.gather(input_, dst, dim)
ERROR 07-01 00:40:04 [engine.py:458]   File "/vllm-workspace/vllm/vllm/distributed/device_communicators/base_device_communicator.py", line 197, in gather
ERROR 07-01 00:40:04 [engine.py:458]     torch.distributed.gather(input_,
ERROR 07-01 00:40:04 [engine.py:458]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py", line 132, in _gather
ERROR 07-01 00:40:04 [engine.py:458]     work = _group.allgather(output_tensors, input_tensors)
ERROR 07-01 00:40:04 [engine.py:458] RuntimeError: InnerRunOpApi:torch_npu/csrc/framework/OpParamMaker.cpp:281 OPS function error: HcclAllgather, error code is 6
ERROR 07-01 00:40:04 [engine.py:458] [ERROR] 2025-07-01-00:40:04 (PID:176930, Device:0, RankID:-1) ERR01100 OPS call acl api failed.
ERROR 07-01 00:40:04 [engine.py:458] EI0006: [PID: 176930] 2025-07-01-00:40:04.135.732 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
ERROR 07-01 00:40:04 [engine.py:458]         Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
ERROR 07-01 00:40:04 [engine.py:458]         TraceBack (most recent call last):
ERROR 07-01 00:40:04 [engine.py:458]         Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[0]-localUserrank[0]-localIpAddr[172.17.0.2], dst_rank[1]-remoteUserrank[1]-remote_ip_addr[172.17.0.2]
ERROR 07-01 00:40:04 [engine.py:458] 
ERROR 07-01 00:40:05 [multiproc_worker_utils.py:121] Worker VllmWorkerProcess pid 176981 died, exit code: -15
INFO 07-01 00:40:05 [multiproc_worker_utils.py:125] Killing local vLLM worker processes
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 460, in run_mp_engine
    raise e from None
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 446, in run_mp_engine
    engine = MQLLMEngine.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 133, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 87, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 268, in __init__
    self._initialize_kv_caches()
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 413, in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 104, in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 332, in collective_rpc
    return self._run_workers(method, *args, **(kwargs or {}))
  File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 186, in _run_workers
    driver_worker_output = run_method(self.driver_worker, sent_method,
  File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 288, in determine_num_available_blocks
    self.model_runner.profile_run()
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1205, in profile_run
    self.execute_model(model_input, kv_caches, intermediate_tensors)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1472, in execute_model
    logits = self.model.compute_logits(hidden_or_intermediate_states,
  File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 590, in compute_logits
    logits = self.logits_processor(self.lm_head, hidden_states,
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 71, in forward
    logits = self._get_logits(hidden_states, lm_head, embedding_bias)
  File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 114, in _get_logits
    logits = self._gather_logits(logits)
  File "/vllm-workspace/vllm/vllm/model_executor/layers/logits_processor.py", line 99, in _gather_logits
    logits = tensor_model_parallel_gather(logits)
  File "/vllm-workspace/vllm/vllm/distributed/communication_op.py", line 33, in tensor_model_parallel_gather
    return get_tp_group().gather(input_, dst, dim)
  File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 419, in gather
    return self.device_communicator.gather(input_, dst, dim)
  File "/vllm-workspace/vllm/vllm/distributed/device_communicators/base_device_communicator.py", line 197, in gather
    torch.distributed.gather(input_,
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py", line 132, in _gather
    work = _group.allgather(output_tensors, input_tensors)
RuntimeError: InnerRunOpApi:torch_npu/csrc/framework/OpParamMaker.cpp:281 OPS function error: HcclAllgather, error code is 6
[ERROR] 2025-07-01-00:40:04 (PID:176930, Device:0, RankID:-1) ERR01100 OPS call acl api failed.
EI0006: [PID: 176930] 2025-07-01-00:40:04.135.732 Getting socket times out. Reason: Remote Rank did not send the data in time. Please check the reason for the rank being stuck
        Solution: 1. Check the rank service processes with other errors or no errors in the cluster.2. If this error is reported for all NPUs, check whether the time difference between the earliest and latest errors is greater than the connect timeout interval (120s by default). If so, adjust the timeout interval by using the HCCL_CONNECT_TIMEOUT environment variable.3. Check the connectivity of the communication link between nodes. (For example, run the 'hccn_tool -i $devid -tls -g' command to check the TLS status of each NPU).
        TraceBack (most recent call last):
        Transport init error. Reason: [Create][DestLink]Create Dest error! createLink para:rank[0]-localUserrank[0]-localIpAddr[172.17.0.2], dst_rank[1]-remoteUserrank[1]-remote_ip_addr[172.17.0.2]

[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 59, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 58, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1323, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1343, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 155, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 288, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-07-01-00:40:06 (PID:176872, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
/usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 31 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```

Do anyone have idea on how to solve this? Thanks a lot!
