# Issue #4891: [Bug]: cpu_offload_connector not work

## 基本信息

- **编号**: #4891
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4891
- **创建时间**: 2025-12-10T12:18:56Z
- **关闭时间**: 2026-01-29T02:32:29Z
- **更新时间**: 2026-01-29T02:33:05Z
- **提交者**: @richard4fan
- **评论数**: 4

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
Python platform: Linux-5.10.0-136.12.0.86.h2374.eulerosv2r12.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               192
On-line CPU(s) list:                  0-191
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
Model name:                           Kunpeng-920
BIOS Model name:                      HUAWEI Kunpeng 920 5250
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   48
Socket(s):                            4
Stepping:                             0x1
Frequency boost:                      disabled
CPU max MHz:                          2600.0000
CPU min MHz:                          200.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
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
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc3

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 25.3.rc1.b061            Version: 25.3.rc1.b061                                        |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 98.2        52                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3434 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 91.1        50                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 93.3        49                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 95.4        51                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3436 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 95.4        54                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3425 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 93.6        53                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3228 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 97.2        53                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3226 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 100.8       53                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3224 / 65536         |
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
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

when i tried to start the vllm-ascend instance with cpu_offload_connector and i faced the following error 

startup command
```
ASCEND_RT_VISIBLE_DEVICES="0,1,2,3" vllm serve /models/Qwen3-32B --served-model-name qwen  --tensor-parallel 4 --port 8199 --enable-prefix-caching     --kv-transfer-config '{"kv_connector":"CPUOffloadingConnector","kv_connector_module_path": "vllm_ascend.distributed.cpu_offload_connector","kv_role":"kv_both", "kv_connector_extra_config": {"swap_in_threshold": 0, "cpu_swap_space_gb": 200}}'
```
error log
```
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 358, in initialize_from_config
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]     self.model_runner.initialize_kv_cache(kv_cache_config)
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2754, in initialize_kv_cache
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]     get_kv_transfer_group().register_kv_caches(kv_caches)
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/cpu_offload_connector.py", line 92, in register_kv_caches
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58] EngineCore failed to start.
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]     self.connector_worker.register_kv_caches(kv_caches)
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/cpu_offload_connector.py", line 333, in register_kv_caches
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58] Traceback (most recent call last):
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]     get_kv_cache_spec(self.vllm_config),
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 49, in run_engine_core
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]     engine_core = EngineCoreProc(*args, **kwargs)
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/distributed/cpu_offload_connector.py", line 440, in get_kv_cache_spec
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]     use_sfa = ascend_config.use_sfa
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671]               ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]     super().__init__(vllm_config, executor_class, log_stats,
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671] AttributeError: 'AscendConfig' object has no attribute 'use_sfa'
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
(Worker_TP2 pid=5094) ERROR 12-10 11:56:52 [multiproc_executor.py:671] 
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]     self._initialize_kv_caches(vllm_config)
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 73, in initialize_from_config
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]     self.collective_rpc("initialize_from_config",
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58]     raise RuntimeError(
(EngineCore_DP0 pid=4956) ERROR 12-10 11:56:52 [patch_core.py:58] RuntimeError: Worker failed with error ''AscendConfig' object has no attribute 'use_sfa'', please check the stack trace above for the root cause

```
