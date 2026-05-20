# Issue #1895: [Bug]: vllm v1 graph mode report errot NotImplementedError: _C::rotary_embedding

## 基本信息

- **编号**: #1895
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1895
- **创建时间**: 2025-07-21T02:38:16Z
- **关闭时间**: 2025-09-15T13:45:17Z
- **更新时间**: 2025-09-15T13:45:17Z
- **提交者**: @didongli182
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.10.17 (main, May  8 2025, 07:18:04) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.86.h1032.eulerosv2r12.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          256
On-line CPU(s) list:             0-255
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 7265
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              64
Socket(s):                       4
Stepping:                        0x1
Frequency boost:                 disabled
CPU max MHz:                     3000.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       16 MiB (256 instances)
L1i cache:                       16 MiB (256 instances)
L2 cache:                        128 MiB (256 instances)
L3 cache:                        256 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-31
NUMA node1 CPU(s):               32-63
NUMA node2 CPU(s):               64-95
NUMA node3 CPU(s):               96-127
NUMA node4 CPU(s):               128-159
NUMA node5 CPU(s):               160-191
NUMA node6 CPU(s):               192-223
NUMA node7 CPU(s):               224-255
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
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.2
vLLM Ascend Version: 0.9.2rc1

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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 23.0.7                   Version: 23.0.7                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 98.3        43                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          59985/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 96.6        44                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          59985/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 96.3        43                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          59988/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 101.8       46                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          59990/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 91.3        45                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3353 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 96.4        47                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3353 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 97.5        47                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3352 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 92.1        49                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3350 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 49943         |                          | 56681                   |
+===========================+===============+====================================================+
| 1       0                 | 49944         |                          | 56681                   |
+===========================+===============+====================================================+
| 2       0                 | 49945         |                          | 56681                   |
+===========================+===============+====================================================+
| 3       0                 | 49946         |                          | 56681                   |
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

 vllm-ascend v0.9.2rc1, use blew cmd start serve

```bash
vllm serve /opt/ddl/Qwen-2.5-32B \
    --served-model-name qwen \
    --tensor-parallel-size 4 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --no-enable-prefix-caching
```
error info:
INFO 07-18 07:29:40 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:29:40 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:29:40 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:29:40 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-18 07:29:41 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-18 07:29:44 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-18 07:29:44 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.mo
WARNING 07-18 07:29:44 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model classion.
WARNING 07-18 07:29:44 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model cllGeneration.
WARNING 07-18 07:29:44 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:29:44 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:29:44 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend
INFO 07-18 07:29:46 [api_server.py:1395] vLLM API server version 0.9.2
INFO 07-18 07:29:46 [cli_args.py:325] non-default args: {'enable_auto_tool_choice': True, 'tool_call_parser': 'hermes', 'model': '/opt/ddl/Qwen-2.5-32B', 'dtype'ze': 4, 'enable_prefix_caching': False}
INFO 07-18 07:29:56 [config.py:841] This model supports multiple tasks: {'generate', 'reward', 'embed', 'classify'}. Defaulting to 'generate'.
WARNING 07-18 07:29:56 [config.py:3371] Casting torch.bfloat16 to torch.float16.
INFO 07-18 07:29:56 [config.py:1472] Using max model len 32768
INFO 07-18 07:29:56 [config.py:2285] Chunked prefill is enabled with max_num_batched_tokens=2048.
INFO 07-18 07:29:56 [platform.py:175] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 07-18 07:29:56 [utils.py:321] Calculated maximum supported batch sizes for ACL graph: 9
INFO 07-18 07:29:56 [utils.py:336] Adjusted ACL graph batch sizes for Qwen2ForCausalLM model (layers: 64): 67 → 9 sizes
INFO 07-18 07:30:03 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:03 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:03 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:03 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-18 07:30:04 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-18 07:30:06 [core.py:526] Waiting for init message from front-end.
INFO 07-18 07:30:08 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-18 07:30:08 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.mo
WARNING 07-18 07:30:08 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model classion.
WARNING 07-18 07:30:08 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model cllGeneration.
WARNING 07-18 07:30:08 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:08 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:08 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend
INFO 07-18 07:30:08 [core.py:69] Initializing a V1 LLM engine (v0.9.2) with config: model='/opt/ddl/Qwen-2.5-32B', speculative_config=None, tokenizer='/opt/ddl/Qevision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_formate_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disableal_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_deter_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilatiod":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.unified_ascend_attention_with_output"],"use_inducuctor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,448,384,312,248,184,112,48,1],"cudagraph_copy_inputs":false,"fuull}
WARNING 07-18 07:30:08 [multiproc_worker_utils.py:307] Reducing Torch parallelism from 256 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS
INFO 07-18 07:30:08 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0, 1, 2, 3], buffer_handle=(4, 16777216, 10, 'psm_-b235-30633c9e6448', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 07-18 07:30:14 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:14 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:14 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:14 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:14 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:14 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:14 [__init__.py:235] Platform plugin ascend is activated
INFO 07-18 07:30:14 [__init__.py:235] Platform plugin ascend is activated
INFO 07-18 07:30:14 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:14 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:14 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:14 [__init__.py:235] Platform plugin ascend is activated
INFO 07-18 07:30:14 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:14 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:14 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:14 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-18 07:30:15 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-18 07:30:15 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-18 07:30:15 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-18 07:30:16 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 07-18 07:30:19 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 07-18 07:30:19 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 07-18 07:30:19 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.mo
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.mo
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model classion.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model classion.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model cllGeneration.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model cllGeneration.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend
INFO 07-18 07:30:19 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.mo
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model classion.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model cllGeneration.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.mo
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model classion.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model cllGeneration.
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_asce
WARNING 07-18 07:30:19 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend
(VllmWorker rank=1 pid=7479) INFO 07-18 07:30:19 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1,p/8f27ba2b-ceb4-4a4b-a035-2a0f25b06f40', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=3 pid=7481) INFO 07-18 07:30:19 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1,p/83b39d5e-802e-44dc-8ef4-1aff6c824d75', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=0 pid=7478) INFO 07-18 07:30:19 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1,p/6737fc65-f2ed-4ac7-8a9a-8a3e3acc2f3d', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=2 pid=7480) INFO 07-18 07:30:20 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1,p/cb83ccef-59d1-4a21-a6c9-bf9293ba28e0', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 07-18 07:30:29 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:29 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:29 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:29 [__init__.py:235] Platform plugin ascend is activated
INFO 07-18 07:30:29 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:29 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:29 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:29 [__init__.py:235] Platform plugin ascend is activated
INFO 07-18 07:30:29 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:29 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:29 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:29 [__init__.py:235] Platform plugin ascend is activated
INFO 07-18 07:30:29 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-18 07:30:29 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-18 07:30:29 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-18 07:30:29 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-18 07:30:30 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-18 07:30:30 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-18 07:30:30 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-18 07:30:31 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorker rank=0 pid=7478) INFO 07-18 07:30:35 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3], buffer_hand//tmp/3c6cc0f7-f5ae-4ddc-a5ef-985a4232a54f', remote_subscribe_addr=None, remote_addr_ipv6=False)
(VllmWorker rank=1 pid=7479) INFO 07-18 07:30:35 [parallel_state.py:1076] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
(VllmWorker rank=0 pid=7478) INFO 07-18 07:30:35 [parallel_state.py:1076] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(VllmWorker rank=2 pid=7480) INFO 07-18 07:30:35 [parallel_state.py:1076] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
(VllmWorker rank=3 pid=7481) INFO 07-18 07:30:35 [parallel_state.py:1076] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
(VllmWorker rank=0 pid=7478) INFO 07-18 07:30:36 [model_runner_v1.py:1755] Starting to load model /opt/ddl/Qwen-2.5-32B...
(VllmWorker rank=1 pid=7479) INFO 07-18 07:30:36 [model_runner_v1.py:1755] Starting to load model /opt/ddl/Qwen-2.5-32B...
(VllmWorker rank=3 pid=7481) INFO 07-18 07:30:36 [model_runner_v1.py:1755] Starting to load model /opt/ddl/Qwen-2.5-32B...
(VllmWorker rank=2 pid=7480) INFO 07-18 07:30:36 [model_runner_v1.py:1755] Starting to load model /opt/ddl/Qwen-2.5-32B...
Loading safetensors checkpoint shards:   0% Completed | 0/17 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   6% Completed | 1/17 [00:01<00:19,  1.20s/it]
Loading safetensors checkpoint shards:  12% Completed | 2/17 [00:02<00:19,  1.30s/it]
Loading safetensors checkpoint shards:  18% Completed | 3/17 [00:03<00:17,  1.29s/it]
Loading safetensors checkpoint shards:  24% Completed | 4/17 [00:05<00:16,  1.25s/it]
Loading safetensors checkpoint shards:  29% Completed | 5/17 [00:06<00:15,  1.31s/it]
Loading safetensors checkpoint shards:  35% Completed | 6/17 [00:07<00:14,  1.35s/it]
Loading safetensors checkpoint shards:  41% Completed | 7/17 [00:09<00:13,  1.35s/it]
Loading safetensors checkpoint shards:  47% Completed | 8/17 [00:10<00:12,  1.40s/it]
Loading safetensors checkpoint shards:  53% Completed | 9/17 [00:12<00:11,  1.42s/it]
Loading safetensors checkpoint shards:  59% Completed | 10/17 [00:13<00:09,  1.41s/it]
Loading safetensors checkpoint shards:  65% Completed | 11/17 [00:15<00:08,  1.47s/it]
Loading safetensors checkpoint shards:  71% Completed | 12/17 [00:16<00:07,  1.51s/it]
Loading safetensors checkpoint shards:  76% Completed | 13/17 [00:18<00:05,  1.47s/it]
Loading safetensors checkpoint shards:  82% Completed | 14/17 [00:19<00:04,  1.40s/it]
Loading safetensors checkpoint shards:  88% Completed | 15/17 [00:20<00:02,  1.41s/it]
Loading safetensors checkpoint shards:  94% Completed | 16/17 [00:22<00:01,  1.39s/it]
(VllmWorker rank=3 pid=7481) INFO 07-18 07:30:59 [default_loader.py:272] Loading weights took 22.38 seconds
(VllmWorker rank=2 pid=7480) INFO 07-18 07:30:59 [default_loader.py:272] Loading weights took 22.83 seconds
Loading safetensors checkpoint shards: 100% Completed | 17/17 [00:23<00:00,  1.27s/it]
Loading safetensors checkpoint shards: 100% Completed | 17/17 [00:23<00:00,  1.36s/it]
(VllmWorker rank=0 pid=7478)
(VllmWorker rank=0 pid=7478) INFO 07-18 07:31:00 [default_loader.py:272] Loading weights took 23.23 seconds
(VllmWorker rank=3 pid=7481) INFO 07-18 07:31:00 [model_runner_v1.py:1787] Loading model weights took 15.3924 GB
(VllmWorker rank=1 pid=7479) INFO 07-18 07:31:00 [default_loader.py:272] Loading weights took 23.79 seconds
(VllmWorker rank=0 pid=7478) INFO 07-18 07:31:01 [model_runner_v1.py:1787] Loading model weights took 15.3924 GB
(VllmWorker rank=2 pid=7480) INFO 07-18 07:31:01 [model_runner_v1.py:1787] Loading model weights took 15.3924 GB
(VllmWorker rank=1 pid=7479) INFO 07-18 07:31:02 [model_runner_v1.py:1787] Loading model weights took 15.3924 GB
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_subclasses/fak
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522]     r = func(*args, **kwargs)
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522]     return self._op(*args, **kwargs)
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522] NotImplementedError: _C::rotary_embedding: attempted to run this operator with Meta You may have run into this message while using an operator with PT2 compilation APIs (torch.compile/torch.export); in order to use this operator with those APIsext steps:  https://pytorch.org/tutorials/advanced/custom_ops_landing_page.html
(VllmWorker rank=0 pid=7478) ERROR 07-18 07:31:03 [multiproc_executor.py:522]

