# Issue #3114: [Bug]: 参考手册Multi-Node-Ray，把ray拉起来了，但是启动vllm serve的时候，依然报找不到NPU

## 基本信息

- **编号**: #3114
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3114
- **创建时间**: 2025-09-23T03:05:46Z
- **关闭时间**: 2025-11-14T01:36:17Z
- **更新时间**: 2025-11-14T01:36:17Z
- **提交者**: @MaoJianwei
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

```
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-98.oe2403sp2)
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.38

Python version: 3.11.13 (main, Aug 29 2025, 04:31:33) [GCC 12.3.1 (openEuler 12.3.1-97.oe2403sp2)] (64-bit runtime)
Python platform: Linux-6.6.0-28.0.0.34.oe2403.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               192
On-line CPU(s) list:                  0-191
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
Model name:                           Kunpeng-920
BIOS Model name:                      HUAWEI Kunpeng 920 5250 To be filled by O.E.M. CPU @ 2.6GHz
BIOS CPU family:                      280
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   48
Socket(s):                            4
Stepping:                             0x1
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asi
mdfhm ssbs
L1d cache:                            12 MiB (192 instances)
L1i cache:                            12 MiB (192 instances)
L2 cache:                             96 MiB (192 instances)
L3 cache:                             192 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-23
NUMA node1 CPU(s):                    24-47
NUMA node2 CPU(s):                    48-71
NUMA node3 CPU(s):                    72-95
NUMA node4 CPU(s):                    96-119
NUMA node5 CPU(s):                    120-143
NUMA node6 CPU(s):                    144-167
NUMA node7 CPU(s):                    168-191
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; __user pointer sanitization
Vulnerability Spectre v2:             Not affected
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[conda] Could not collect
vLLM Version: 0.10.2
vLLM Ascend Version: 0.10.2rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nn
al/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tool
s/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend
/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64
:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/a
tb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plu
gin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit
/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Asc
end/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/te
sts/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/
Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/p
lugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/loc
al/Ascend/driver/lib64/driver/:
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 99.3        41                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 101.8       38                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 91.0        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 99.4        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 94.8        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 100.8       42                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 99.8        43                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 92.0        45                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3378 / 65536         |
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
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux
```

### 🐛 Describe the bug

按照官网手册把ray拉起来了，但是启动vllm serve的时候，依然报找不到NPU，想问下该怎么解决呢？

服务器是两台A2推理服务器，使用的是v0.10.2rc1-openeuler容器镜像
vllm启动过程中有提示Connected to Ray cluster.

https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi_node_ray.html

@Potabk @Yikun 

```
[root@xxx 2node]# ray status
======== Autoscaler status: 2025-09-23 03:00:18.401662 ========
Node status
---------------------------------------------------------------
Active:
 1 node_f2e99af987618864161970a2b891f4e31f4edf2236deb98329cc5a17
 1 node_a7769d9548f5020b5ea9a593d89761b6adc5b4cee107d72c71e21d8e
Pending:
 (no pending nodes)
Recent failures:
 (no failures)

Resources
---------------------------------------------------------------
Total Usage:
 0.0/384.0 CPU
 0.0/16.0 GPU
 0B/3.91TiB memory
 0B/18.63GiB object_store_memory

Total Constraints:
 (no request_resources() constraints)
Total Demands:
 (no resource demands)

```

```
vllm serve /llm/Qwen3-235B-A22B-Instruct-2507/Qwen3-235B-A22B-Instruct-2507/ --distributed-executor-backend ray --pipeline-parallel-size 2 --tensor-parallel-size 8 --enable-expert-parallel --seed 1024 --max-model-len 8192 --max-num-seqs 25 --served-model-name Qwen3-235B-A22B-Instruct-2507 --trust-remote-code --gpu-memory-utilization 0.9
```

```
(EngineCore_DP0 pid=14400) INFO 09-23 03:01:22 [core.py:76] Initializing a V1 LLM engine (v0.10.2) with config: model='/llm/Qwen3-235B-A22B-Instr
uct-2507/Qwen3-235B-A22B-Instruct-2507/', speculative_config=None, tokenizer='/llm/Qwen3-235B-A22B-Instruct-2507/Qwen3-235B-A22B-Instruct-2507/',
 skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_le
n=8192, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=2, data_parallel_size=1, disable_custom_all_reduce=Tr
ue, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallba
ck=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show
_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=1024, served_model_name=Qwen3-235B-A22B-Instruct
-2507, enable_prefix_caching=True, chunked_prefill_enabled=False, use_async_output_proc=False, pooler_config=None, compilation_config={"level":3,
"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_outp
ut","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.unified
_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"induct
or_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[48,32,24,8,4,1],"cudagraph_copy_inp
uts":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":48,"local_cache_dir":null}
(EngineCore_DP0 pid=14400) 2025-09-23 03:01:22,064      INFO worker.py:1771 -- Connecting to existing Ray cluster at address: x.x.x.201:6379..
.
(EngineCore_DP0 pid=14400) 2025-09-23 03:01:22,076      INFO worker.py:1951 -- Connected to Ray cluster.
(EngineCore_DP0 pid=14400) INFO 09-23 03:01:22 [ray_utils.py:345] No current placement group found. Creating a new placement group.
(EngineCore_DP0 pid=14400) WARNING 09-23 03:01:22 [ray_utils.py:352] The number of required NPUs exceeds the total number of available NPUs in th
e placement group.
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718] EngineCore failed to start.
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718] Traceback (most recent call last):
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 82, in __init__
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 264, in __init__
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     super().__init__(*args, **kwargs)
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     self._init_executor()
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/v1/executor/ray_distributed_executor.py", line 50
, in _init_executor
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     super()._init_executor()
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 98, i
n _init_executor
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     initialize_ray_cluster(self.parallel_config)
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]   File "/vllm-workspace/vllm/vllm/executor/ray_utils.py", line 368, in initialize_r
ay_cluster
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718]     raise ValueError(
(EngineCore_DP0 pid=14400) ERROR 09-23 03:01:22 [core.py:718] ValueError: Current node has no NPU available. current_node_resource={'memory': 215
1287372800.0, 'object_store_memory': 10000000000.0, 'node:x.x.x.201': 1.0, 'CPU': 192.0, 'node:__internal_head__': 1.0, 'GPU': 8.0}. vLLM engi
ne cannot start without NPU. Make sure you have at least 1 NPU available in a node current_node_id='a7769d9548f5020b5ea9a593d89761b6adc5b4cee107d
72c71e21d8e' current_ip='x.x.x.201'.
(EngineCore_DP0 pid=14400) Process EngineCore_DP0:
(EngineCore_DP0 pid=14400) Traceback (most recent call last):
(EngineCore_DP0 pid=14400)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=14400)     self.run()
(EngineCore_DP0 pid=14400)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=14400)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 722, in run_engine_core
(EngineCore_DP0 pid=14400)     raise e
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 709, in run_engine_core
(EngineCore_DP0 pid=14400)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=14400)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 505, in __init__
(EngineCore_DP0 pid=14400)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 82, in __init__
(EngineCore_DP0 pid=14400)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=14400)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 264, in __init__
(EngineCore_DP0 pid=14400)     super().__init__(*args, **kwargs)
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=14400)     self._init_executor()
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/v1/executor/ray_distributed_executor.py", line 50, in _init_executor
(EngineCore_DP0 pid=14400)     super()._init_executor()
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 98, in _init_executor
(EngineCore_DP0 pid=14400)     initialize_ray_cluster(self.parallel_config)
(EngineCore_DP0 pid=14400)   File "/vllm-workspace/vllm/vllm/executor/ray_utils.py", line 368, in initialize_ray_cluster
(EngineCore_DP0 pid=14400)     raise ValueError(
(EngineCore_DP0 pid=14400) ValueError: Current node has no NPU available. current_node_resource={'memory': 2151287372800.0, 'object_store_memory'
: 10000000000.0, 'node:x.x.x.201': 1.0, 'CPU': 192.0, 'node:__internal_head__': 1.0, 'GPU': 8.0}. vLLM engine cannot start without NPU. Make s
ure you have at least 1 NPU available in a node current_node_id='a7769d9548f5020b5ea9a593d89761b6adc5b4cee107d72c71e21d8e' current_ip='x.x.x.2
01'.
(EngineCore_DP0 pid=14400) INFO 09-23 03:01:22 [ray_distributed_executor.py:122] Shutting down Ray distributed executor. If you see error log fro
m logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
```
