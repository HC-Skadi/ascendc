# Issue #4661: [Bug]:  Qwen3-235B-A22B-Instruct-2507  index 0 is out of bounds for dimension 0 with size 0

## 基本信息

- **编号**: #4661
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4661
- **创建时间**: 2025-12-03T06:49:00Z
- **关闭时间**: 2025-12-09T01:30:32Z
- **更新时间**: 2025-12-09T01:30:32Z
- **提交者**: @ZRJ026
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.88.4.ctl3.aarch64-aarch64-with-glibc2.35

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
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc2

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.1               Version: 24.1.rc2.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 92.0        38                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          33429/ 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 96.0        38                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          33427/ 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 93.5        37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          33427/ 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 95.8        38                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          33428/ 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 92.6        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          33427/ 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 97.3        38                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          33427/ 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 92.3        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          33426/ 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 92.4        37                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          33426/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 784778        | VLLMWorker_DP            | 30112                   |
+===========================+===============+====================================================+
| 1       0                 | 784779        | VLLMWorker_DP            | 30112                   |
+===========================+===============+====================================================+
| 2       0                 | 784780        | VLLMWorker_DP            | 30112                   |
+===========================+===============+====================================================+
| 3       0                 | 784784        | VLLMWorker_DP            | 30112                   |
+===========================+===============+====================================================+
| 4       0                 | 784785        | VLLMWorker_DP            | 30112                   |
+===========================+===============+====================================================+
| 5       0                 | 784786        | VLLMWorker_DP            | 30112                   |
+===========================+===============+====================================================+
| 6       0                 | 784787        | VLLMWorker_DP            | 30113                   |
+===========================+===============+====================================================+
| 7       0                 | 784788        | VLLMWorker_DP            | 30112                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

I am starting two pods with a total of 16 Ascend 910B GPUs, using the image vllm ascend 0.11.0.rc2   @sha256:79629abfd563615a7b14d18252fb5e6759ecd983f13517bd9ee8bbbd08b90aaf.

Startup commands for **pod0** :
```shell
 vllm serve /data/models --host 0.0.0.0 --port 8000 --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-address ${MASTER_IP} --data-parallel-rpc-port 13389 --tensor-parallel-size 8 --seed 1024 --served-model-name inference-qwen3-235b-a22b-instruct-2507 --enable-expert-parallel --max-num-seqs  8 --max-model-len 2048  --max-num-batched-tokens 2048 --trust-remote-code --no-enable-prefix-caching --gpu-memory-utilization 0.95 --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'
```

Startup commands for **pod1** :
```shell
 vllm serve /data/models --host 0.0.0.0 --port 8000 --headless --data-parallel-size 2 --data-parallel-size-local 1 --data-parallel-start-rank 1 --data-parallel-address ${MASTER_IP}   --data-parallel-rpc-port 13389 --tensor-parallel-size 8 --seed 1024  --served-model-name inference-qwen3-235b-a22b-instruct-2507 --max-num-seqs 8 --max-model-len 2048 --max-num-batched-tokens 2048 --enable-expert-parallel --trust-remote-code --no-enable-prefix-caching --gpu-memory-utilization 0.95 --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}''
```
<details>
<summary>And the output from pod0</summary>

```text
INFO 12-03 06:06:04 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-03 06:06:04 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-03 06:06:04 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-03 06:06:05 [__init__.py:207] Platform plugin ascend is activated
WARNING 12-03 06:06:10 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 12-03 06:06:11 [registry.py:582] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-03 06:06:11 [registry.py:582] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-03 06:06:11 [registry.py:582] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-03 06:06:11 [registry.py:582] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-03 06:06:11 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
WARNING 12-03 06:06:11 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
WARNING 12-03 06:06:11 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
INFO 12-03 06:06:11 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
[1;36m(APIServer pid=654162)[0;0m INFO 12-03 06:06:12 [api_server.py:1839] vLLM API server version 0.11.0
[1;36m(APIServer pid=654162)[0;0m INFO 12-03 06:06:12 [utils.py:233] non-default args: {'model_tag': '/data/models', 'host': '0.0.0.0', 'port': 8004, 'model': '/data/models', 'trust_remote_code': True, 'seed': 1024, 'max_model_len': 2048, 'served_model_name': ['inference-qwen3-235b-a22b-instruct-2507'], 'tensor_parallel_size': 8, 'data_parallel_size': 2, 'data_parallel_size_local': 1, 'data_parallel_address': 'inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default', 'data_parallel_rpc_port': 13389, 'enable_expert_parallel': True, 'gpu_memory_utilization': 0.95, 'enable_prefix_caching': False, 'max_num_batched_tokens': 2048, 'max_num_seqs': 8, 'additional_config': {'ascend_scheduler_config': {'enabled': True}, 'torchair_graph_config': {'enabled': True}}}
[1;36m(APIServer pid=654162)[0;0m The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
[1;36m(APIServer pid=654162)[0;0m INFO 12-03 06:06:25 [model.py:547] Resolved architecture: Qwen3MoeForCausalLM
[1;36m(APIServer pid=654162)[0;0m `torch_dtype` is deprecated! Use `dtype` instead!
[1;36m(APIServer pid=654162)[0;0m INFO 12-03 06:06:25 [model.py:1510] Using max model len 2048
[1;36m(APIServer pid=654162)[0;0m INFO 12-03 06:06:25 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048.
[1;36m(APIServer pid=654162)[0;0m INFO 12-03 06:06:25 [platform.py:167] Torchair compilation enabled on NPU. Setting CUDAGraphMode to NONE
[1;36m(APIServer pid=654162)[0;0m INFO 12-03 06:06:26 [utils.py:651] Started DP Coordinator process (PID: 657845)
INFO 12-03 06:06:34 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-03 06:06:34 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-03 06:06:34 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-03 06:06:34 [__init__.py:207] Platform plugin ascend is activated
INFO 12-03 06:06:34 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-03 06:06:34 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-03 06:06:34 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-03 06:06:34 [__init__.py:207] Platform plugin ascend is activated
vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
[1;36m(EngineCore_DP0 pid=657851)[0;0m WARNING 12-03 06:06:41 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
[1;36m(EngineCore_DP0 pid=657851)[0;0m WARNING 12-03 06:06:41 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
[1;36m(EngineCore_DP0 pid=657851)[0;0m WARNING 12-03 06:06:41 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
[1;36m(EngineCore_DP0 pid=657851)[0;0m INFO 12-03 06:06:41 [core.py:77] Initializing a V1 LLM engine (v0.11.0) with config: model='/data/models', speculative_config=None, tokenizer='/data/models', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, data_parallel_size=2, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=1024, served_model_name=inference-qwen3-235b-a22b-instruct-2507, enable_prefix_caching=False, chunked_prefill_enabled=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":16,"local_cache_dir":null}
[1;36m(EngineCore_DP0 pid=657851)[0;0m WARNING 12-03 06:06:41 [multiproc_executor.py:720] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
[1;36m(EngineCore_DP0 pid=657851)[0;0m INFO 12-03 06:06:41 [shm_broadcast.py:289] vLLM message queue communication handle:

INFO 12-03 06:06:57 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_0c5612f2'), local_subscribe_addr='ipc:///tmp/f43fd868-144c-4104-a10d-9fc95e148d6d', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:57 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_6db738eb'), local_subscribe_addr='ipc:///tmp/2a5d363d-8f8b-4ae7-8fdb-9ef053d5378d', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:57 [parallel_state.py:1047] Adjusting world_size=16 rank=4 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:57 [parallel_state.py:1047] Adjusting world_size=16 rank=7 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:57 [parallel_state.py:1047] Adjusting world_size=16 rank=6 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:57 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_6840c4d1'), local_subscribe_addr='ipc:///tmp/7be4c656-5380-4974-894c-55db3eb08d0b', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:57 [parallel_state.py:1047] Adjusting world_size=16 rank=2 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:57 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_2422932a'), local_subscribe_addr='ipc:///tmp/0ef3e00d-7880-4a75-b34f-73bc8c9c929e', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:57 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_452b0c46'), local_subscribe_addr='ipc:///tmp/f0162d6c-6760-4b43-98d6-c44497a3b059', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:57 [parallel_state.py:1047] Adjusting world_size=16 rank=0 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:58 [parallel_state.py:1047] Adjusting world_size=16 rank=1 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:58 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_e622c42b'), local_subscribe_addr='ipc:///tmp/396ba1e2-83e8-4adf-abd1-5ac26f0eb917', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:58 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_218ea84b'), local_subscribe_addr='ipc:///tmp/1faa00f6-42f0-4e54-9a2c-c2b0170a2112', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:58 [parallel_state.py:1047] Adjusting world_size=16 rank=3 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:58 [parallel_state.py:1047] Adjusting world_size=16 rank=5 distributed_init_method=tcp://inference-qwen3-235b-a22b-instruct-2507-inference-0.inference-qwen3-235b-a22b-instruct-2507-inference.default:36251 for DP
INFO 12-03 06:06:58 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_b000af7a'), local_subscribe_addr='ipc:///tmp/518c2a61-5944-4ddf-8aa2-cc0c6925bf3c', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 0 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 1 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 2 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 3 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 4 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 4, EP rank 4
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 6 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 6, EP rank 6
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 5 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 5, EP rank 5
INFO 12-03 06:06:59 [parallel_state.py:1208] rank 7 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 7, EP rank 7
WARNING 12-03 06:06:59 [registry.py:582] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.torchair.models.torchair_deepseek_mtp:TorchairDeepSeekMTP.
ill be overwritten by the new model class vllm_ascend.torchair.models.torchair_deepseek_mtp:TorchairDeepSeekMTP.
[1;36m(Worker_DP0_TP2_EP2 pid=659282)[0;0m INFO 12-03 06:06:59 [model_runner_v1.py:2641] Starting to load model /data/models...
[1;36m(Worker_DP0_TP6_EP6 pid=659292)[0;0m INFO 12-03 06:06:59 [model_runner_v1.py:2641] Starting to load model /data/models...
[1;36m(Worker_DP0_TP3_EP3 pid=659289)[0;0m INFO 12-03 06:06:59 [model_runner_v1.py:2641] Starting to load model /data/models...
[1;36m(Worker_DP0_TP1_EP1 pid=659281)[0;0m INFO 12-03 06:06:59 [model_runner_v1.py:2641] Starting to load model /data/models...
[1;36m(Worker_DP0_TP4_EP4 pid=659290)[0;0m INFO 12-03 06:06:59 [model_runner_v1.py:2641] Starting to load model /data/models...
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m INFO 12-03 06:06:59 [model_runner_v1.py:2641] Starting to load model /data/models...
[1;36m(Worker_DP0_TP2_EP2 pid=659282)[0;0m INFO 12-03 06:06:59 [layer.py:1052] [EP Rank 2/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->16, 1->17, 2->18, 3->19, 4->20, 5->21, 6->22, 7->23.
[1;36m(Worker_DP0_TP2_EP2 pid=659282)[0;0m INFO 12-03 06:06:59 [layer.py:332] FlashInfer CUTLASS MoE is currently not available for DP.
[1;36m(Worker_DP0_TP2_EP2 pid=659282)[0;0m INFO 12-03 06:06:59 [torchair_fused_moe.py:1086] [EP Rank 2/16] Expert parallelism is enabled. Local/global number of experts: 8/128. Experts local to global index map: 0->16, 1->17, 2->18, 3->19, 4->20, 5->21, 6->22, 7->23.
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m INFO 12-03 06:06:59 [layer.py:1052] [EP Rank 0/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->0, 1->1, 2->2, 3->3, 4->4, 5->5, 6->6, 7->7.
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m INFO 12-03 06:06:59 [layer.py:332] FlashInfer CUTLASS MoE is currently not available for DP.
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m INFO 12-03 06:06:59 [torchair_fused_moe.py:1086] [EP Rank 0/16] Expert parallelism is enabled. Local/global number of experts: 8/128. Experts local to global index map: 0->0, 1->1, 2->2, 3->3, 4->4, 5->5, 6->6, 7->7.
[1;36m(Worker_DP0_TP7_EP7 pid=659293)[0;0m INFO 12-03 06:06:59 [layer.py:1052] [EP Rank 7/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->56, 1->57, 2->58, 3->59, 4->60, 5->61, 6->62, 7->63.
[1;36m(Worker_DP0_TP7_EP7 pid=659293)[0;0m INFO 12-03 06:06:59 [layer.py:332] FlashInfer CUTLASS MoE is currently not available for DP.
[1;36m(Worker_DP0_TP7_EP7 pid=659293)[0;0m INFO 12-03 06:06:59 [torchair_fused_moe.py:1086] [EP Rank 7/16] Expert parallelism is enabled. Local/global number of experts: 8/128. Experts local to global index map: 0->56, 1->57, 2->58, 3->59, 4->60, 5->61, 6->62, 7->63.
[1;36m(Worker_DP0_TP4_EP4 pid=659290)[0;0m INFO 12-03 06:06:59 [layer.py:1052] [EP Rank 4/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->32, 1->33, 2->34, 3->35, 4->36, 5->37, 6->38, 7->39.
[1;36m(Worker_DP0_TP4_EP4 pid=659290)[0;0m INFO 12-03 06:06:59 [layer.py:332] FlashInfer CUTLASS MoE is currently not available for DP.
[1;36m(Worker_DP0_TP4_EP4 pid=659290)[0;0m INFO 12-03 06:06:59 [torchair_fused_moe.py:1086] [EP Rank 4/16] Expert parallelism is enabled. Local/global number of experts: 8/128. Experts local to global index map: 0->32, 1->33, 2->34, 3->35, 4->36, 5->37, 6->38, 7->39.
[1;36m(Worker_DP0_TP6_EP6 pid=659292)[0;0m INFO 12-03 06:06:59 [layer.py:1052] [EP Rank 6/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->48, 1->49, 2->50, 3->51, 4->52, 5->53, 6->54, 7->55.
[1;36m(Worker_DP0_TP6_EP6 pid=659292)[0;0m INFO 12-03 06:06:59 [layer.py:332] FlashInfer CUTLASS MoE is currently not available for DP.
[1;36m(Worker_DP0_TP6_EP6 pid=659292)[0;0m INFO 12-03 06:06:59 [torchair_fused_moe.py:1086] [EP Rank 6/16] Expert parallelism is enabled. Local/global number of experts: 8/128. Experts local to global index map: 0->48, 1->49, 2->50, 3->51, 4->52, 5->53, 6->54, 7->55.
[1;36m(Worker_DP0_TP3_EP3 pid=659289)[0;0m INFO 12-03 06:07:00 [layer.py:1052] [EP Rank 3/16] Expert parallelism is enabled. Expert placement strategy: linear. Local/global number of experts: 8/128. Experts local to global index map: 0->24, 1->25, 2->26, 3->27, 4->28, 5->29, 6->30, 7->31.
[1;36m(Worker_DP0_TP5_EP5 pid=659291)[0;0m INFO 12-03 06:07:00 [layer.py:332] FlashInfer CUTLASS MoE is currently not available for DP.
[1;36m(Worker_DP0_TP5_EP5 pid=659291)[0;0m INFO 12-03 06:07:00 [torchair_fused_moe.py:1086] [EP Rank 5/16] Expert parallelism is enabled. Local/global number of experts: 8/128. Experts local to global index map: 0->40, 1->41, 2->42, 3->43, 4->44, 5->45, 6->46, 7->47.
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m 
Loading safetensors checkpoint shards:   0% Completed | 0/118 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 118/118 [00:49<00:00,  2.41it/s]
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m 
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m INFO 12-03 06:07:52 [default_loader.py:267] Loading weights took 49.06 seconds
INFO 12-03 06:07:53 [__init__.py:207] Platform plugin ascend is activated
[1;36m(Worker_DP0_TP6_EP6 pid=659292)[0;0m INFO 12-03 06:07:55 [model_runner_v1.py:2667] Loading model weights took 28.7522 GB
[1;36m(Worker_DP0_TP3_EP3 pid=659289)[0;0m INFO 12-03 06:08:00 [model_runner_v1.py:2667] Loading model weights took 28.7522 GB

[1;36m(Worker_DP0_TP2_EP2 pid=659282)[0;0m WARNING 12-03 06:08:13 [cudagraph_dispatcher.py:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
[1;36m(Worker_DP0_TP6_EP6 pid=659292)[0;0m WARNING 12-03 06:08:14 [cudagraph_dispatcher.py:106] cudagraph dispatching keys are not initialized. No cudagraph will be used.
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671] WorkerProc hit an exception.
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_worker.py", line 34, in determine_available_memory
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     available_kv_cache_memory = super().determine_available_memory()
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 227, in determine_available_memory
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     self.model_runner.profile_run()
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2530, in profile_run
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self._dummy_run(self.max_num_tokens,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2493, in _dummy_run
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 195, in _generate_dummy_run_hidden_states
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = super()._generate_dummy_run_hidden_states(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2314, in _generate_dummy_run_hidden_states
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 534, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, kv_caches,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 225, in __call__
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 442, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states, residual = layer(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                               ^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 362, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self.self_attn(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 260, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     attn_output = self.attn(q, k, v)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                   ^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/worker/patch_attention_layer.py", line 67, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     self.impl.forward(self,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_attention.py", line 365, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     if kv_cache is not None and kv_cache[0].numel() > 0:
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                                 ~~~~~~~~^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671] IndexError: index 0 is out of bounds for dimension 0 with size 0
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_worker.py", line 34, in determine_available_memory
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     available_kv_cache_memory = super().determine_available_memory()
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 227, in determine_available_memory
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     self.model_runner.profile_run()
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2530, in profile_run
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self._dummy_run(self.max_num_tokens,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return func(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2493, in _dummy_run
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self._generate_dummy_run_hidden_states(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 195, in _generate_dummy_run_hidden_states
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = super()._generate_dummy_run_hidden_states(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2314, in _generate_dummy_run_hidden_states
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self.model(input_ids=input_ids,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 534, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self.model(input_ids, positions, kv_caches,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 225, in __call__
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self.forward(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 442, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states, residual = layer(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                               ^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 362, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     hidden_states = self.self_attn(
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                     ^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/models/qwen3_moe.py", line 260, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     attn_output = self.attn(q, k, v)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                   ^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return self._call_impl(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     return forward_call(*args, **kwargs)
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/worker/patch_attention_layer.py", line 67, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     self.impl.forward(self,
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/torchair/torchair_attention.py", line 365, in forward
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]     if kv_cache is not None and kv_cache[0].numel() > 0:
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671]                                 ~~~~~~~~^^^
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671] IndexError: index 0 is out of bounds for dimension 0 with size 0
[1;36m(Worker_DP0_TP0_EP0 pid=659280)[0;0m ERROR 12-03 06:08:15 [multiproc_executor.py:671] 
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708] EngineCore failed to start.
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708] Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 695, in run_engine_core
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     engine_core = DPEngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 965, in __init__
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     super().__init__(vllm_config, local_client, handshake_address,
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     self._initialize_kv_caches(vllm_config)
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     self.model_executor.determine_available_memory())
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 85, in determine_available_memory
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     return self.collective_rpc("determine_available_memory")
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     result = get_response(w, dequeue_timeout,
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708]     raise RuntimeError(
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:15 [core.py:708] RuntimeError: Worker failed with error 'index 0 is out of bounds for dimension 0 with size 0', please check the stack trace above for the root cause
[1;36m(EngineCore_DP0 pid=657851)[0;0m ERROR 12-03 06:08:29 [multiproc_executor.py:154] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
[1;36m(EngineCore_DP0 pid=657851)[0;0m Process EngineCore_DP0:
[1;36m(EngineCore_DP0 pid=657851)[0;0m Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
[1;36m(EngineCore_DP0 pid=657851)[0;0m     self.run()
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
[1;36m(EngineCore_DP0 pid=657851)[0;0m     self._target(*self._args, **self._kwargs)
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
[1;36m(EngineCore_DP0 pid=657851)[0;0m     raise e
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 695, in run_engine_core
[1;36m(EngineCore_DP0 pid=657851)[0;0m     engine_core = DPEngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=657851)[0;0m                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 965, in __init__
[1;36m(EngineCore_DP0 pid=657851)[0;0m     super().__init__(vllm_config, local_client, handshake_address,
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
[1;36m(EngineCore_DP0 pid=657851)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
[1;36m(EngineCore_DP0 pid=657851)[0;0m     self._initialize_kv_caches(vllm_config)
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 190, in _initialize_kv_caches
[1;36m(EngineCore_DP0 pid=657851)[0;0m     self.model_executor.determine_available_memory())
[1;36m(EngineCore_DP0 pid=657851)[0;0m     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 85, in determine_available_memory
[1;36m(EngineCore_DP0 pid=657851)[0;0m     return self.collective_rpc("determine_available_memory")
[1;36m(EngineCore_DP0 pid=657851)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
[1;36m(EngineCore_DP0 pid=657851)[0;0m     result = get_response(w, dequeue_timeout,
[1;36m(EngineCore_DP0 pid=657851)[0;0m              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=657851)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
[1;36m(EngineCore_DP0 pid=657851)[0;0m     raise RuntimeError(
[1;36m(EngineCore_DP0 pid=657851)[0;0m RuntimeError: Worker failed with error 'index 0 is out of bounds for dimension 0 with size 0', please check the stack trace above for the root cause
[1;36m(APIServer pid=654162)[0;0m Traceback (most recent call last):
[1;36m(APIServer pid=654162)[0;0m   File "/usr/local/python3.11.13/bin/vllm", line 7, in <module>
[1;36m(APIServer pid=654162)[0;0m     sys.exit(main())
[1;36m(APIServer pid=654162)[0;0m              ^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
[1;36m(APIServer pid=654162)[0;0m     args.dispatch_function(args)
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
[1;36m(APIServer pid=654162)[0;0m     uvloop.run(run_server(args))
[1;36m(APIServer pid=654162)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
[1;36m(APIServer pid=654162)[0;0m     return runner.run(wrapper())
[1;36m(APIServer pid=654162)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
[1;36m(APIServer pid=654162)[0;0m     return self._loop.run_until_complete(task)
[1;36m(APIServer pid=654162)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[1;36m(APIServer pid=654162)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
[1;36m(APIServer pid=654162)[0;0m     return await main
[1;36m(APIServer pid=654162)[0;0m            ^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
[1;36m(APIServer pid=654162)[0;0m     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
[1;36m(APIServer pid=654162)[0;0m     async with build_async_engine_client(
[1;36m(APIServer pid=654162)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
[1;36m(APIServer pid=654162)[0;0m     return await anext(self.gen)
[1;36m(APIServer pid=654162)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
[1;36m(APIServer pid=654162)[0;0m     async with build_async_engine_client_from_engine_args(
[1;36m(APIServer pid=654162)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
[1;36m(APIServer pid=654162)[0;0m     return await anext(self.gen)
[1;36m(APIServer pid=654162)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
[1;36m(APIServer pid=654162)[0;0m     async_llm = AsyncLLM.from_vllm_config(
[1;36m(APIServer pid=654162)[0;0m                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1572, in inner
[1;36m(APIServer pid=654162)[0;0m     return fn(*args, **kwargs)
[1;36m(APIServer pid=654162)[0;0m            ^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
[1;36m(APIServer pid=654162)[0;0m     return cls(
[1;36m(APIServer pid=654162)[0;0m            ^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
[1;36m(APIServer pid=654162)[0;0m     self.engine_core = EngineCoreClient.make_async_mp_client(
[1;36m(APIServer pid=654162)[0;0m                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 101, in make_async_mp_client
[1;36m(APIServer pid=654162)[0;0m     return DPLBAsyncMPClient(*client_args)
[1;36m(APIServer pid=654162)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1125, in __init__
[1;36m(APIServer pid=654162)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 975, in __init__
[1;36m(APIServer pid=654162)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
[1;36m(APIServer pid=654162)[0;0m     super().__init__(
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
[1;36m(APIServer pid=654162)[0;0m     with launch_core_engines(vllm_config, executor_class,
[1;36m(APIServer pid=654162)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
[1;36m(APIServer pid=654162)[0;0m     next(self.gen)
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
[1;36m(APIServer pid=654162)[0;0m     wait_for_engine_startup(
[1;36m(APIServer pid=654162)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
[1;36m(APIServer pid=654162)[0;0m     raise RuntimeError("Engine core initialization failed. "
[1;36m(APIServer pid=654162)[0;0m RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore_DP0': 1}
[1;36m(APIServer pid=654162)[0;0m [ERROR] 2025-12-03-06:08:32 (PID:654162, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
</details>
