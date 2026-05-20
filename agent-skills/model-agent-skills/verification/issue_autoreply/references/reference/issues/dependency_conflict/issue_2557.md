# Issue #2557: [Bug]: Compatibility Issue about Using torch_npu and ASCEND_RT_VISIBLE_DEVICES for Mooncake Connector in K8s Environment

## 基本信息

- **编号**: #2557
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2557
- **创建时间**: 2025-08-26T12:29:04Z
- **关闭时间**: 2025-12-18T02:42:24Z
- **更新时间**: 2025-12-18T02:42:24Z
- **提交者**: @Shichang-Zhang
- **评论数**: 3

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
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.oe2203sp3.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             256
On-line CPU(s) list:                0-255
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                64
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
Frequency boost:                    disabled
CPU max MHz:                        3000.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          16 MiB (256 instances)
L1i cache:                          16 MiB (256 instances)
L2 cache:                           128 MiB (256 instances)
L3 cache:                           256 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-31
NUMA node1 CPU(s):                  32-63
NUMA node2 CPU(s):                  64-95
NUMA node3 CPU(s):                  96-127
NUMA node4 CPU(s):                  128-159
NUMA node5 CPU(s):                  160-191
NUMA node6 CPU(s):                  192-223
NUMA node7 CPU(s):                  224-255
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
[pip3] pyzmq==27.0.1
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1
[pip3] torchvision==0.20.1
[pip3] transformers==4.53.3
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1rc3.dev13+gf6a0e1629.d20250818 (git sha: f6a0e1629, date: 20250818)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,3,4,7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/mooncake:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/::/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib
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
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 93.7        52                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2843 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 94.3        51                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2842 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 89.9        57                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2833 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 88.2        55                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2833 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
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

</details>


### 🐛 Describe the bug

I tried to deploy vllm-ascend with v1 mooncake connector [#1568 ](https://github.com/vllm-project/vllm-ascend/pull/1568) in the K8s environment. 
I started the vllm-prefill pod with the command `sleep infinity` and mount 4 of 8 NPU (physical machine has 8 NPU) devices on the prefill Pod. 
```
        resources:
          limits:
            huawei.com/Ascend910: "4"
          requests:
            huawei.com/Ascend910: "4"
```
Then I entered the container of the vllm-prefill pod (environment of the container is shown above), and executed the command shown below to start the vllm. 
```bash
export ASCEND_RT_VISIBLE_DEVICES=$(ls /dev/davinci* 2>/dev/null | grep -o '[0-9]\+' | sort -n | paste -sd',' -)
JSON_CONTENT="{\"local_hostname\": \"$POD_IP\",\"device_name\": \"\",\"protocol\":\"ascend\"}"
          echo "$JSON_CONTENT" > /app/mooncake.json
          MOONCAKE_CONFIG_PATH=/app/mooncake.json VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-7B-Instruct --port 8100 --tensor-parallel-size 2 --seed 1024 --max-model-len 10000 --max-num-batched-tokens 2000 --data-parallel-size 2 --data-parallel-address localhost --data-parallel-rpc-port 9100 --gpu-memory-utilization 0.8 --kv-transfer-config '{"kv_connector":"MooncakeConnectorV1","kv_role":"kv_producer","kv_buffer_device":"npu","kv_connector_module_path":"vllm_ascend.distributed.mooncake_connector","kv_parallel_size": 1,"kv_port": "20001","engine_id": "0","kv_rank": 0,"kv_connector_extra_config":{"prefill":{"tp_size":2,"dp_size":2},"decode":{"tp_size":2,"dp_size":2}}}'
```
I encountered the problem from torch_npu:
```
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492] WorkerProc failed to start.
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492] Traceback (most recent call last):
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]   File "/workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 466, in worker_main
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]     worker = WorkerProc(*args, **kwargs)
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]   File "/workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 362, in __init__
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]     self.worker.init_device()
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]   File "/workspace/vllm/vllm/worker/worker_base.py", line 606, in init_device
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]     self.worker.init_device()  # type: ignore
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]     ^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]   File "/workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 140, in init_device
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]     NPUPlatform.set_device(self.device)
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]   File "/workspace/vllm-ascend/vllm_ascend/platform.py", line 99, in set_device
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]     torch.npu.set_device(device)
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 80, in set_device
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]     torch_npu._C._npu_setDevice(device_id)
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492] RuntimeError: init:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:292 NPU function error: aclrtGetDeviceCount(&device_count), error code is 207004
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492] [ERROR] 2025-08-26-12:16:15 (PID:1110, Device:-1, RankID:-1) ERR00100 PTA call acl api failed
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492] [Error]: The device is unavailable.
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         Check whether the device is running properly.
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492] EE1001: [PID: 1110] 2025-08-26-12:16:15.529.940 The argument is invalid.Reason: set ASCEND_RT_VISIBLE_DEVICES:4,7 error, input data rang[0-4)
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         TraceBack (most recent call last):
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         rtGetDeviceCount execute failed, reason=[driver error:no valid device][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         get device count failed, runtime result = 207004.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         The argument is invalid.Reason: Set visible device failed, invalid device=0, input visible devices:4,7
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         rtSetDevice execute failed, reason=[device id error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         open device 0 failed, runtime result = 107001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:6147]
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
(VllmWorker rank=0 pid=1110) ERROR 08-26 12:16:15 [multiproc_executor.py:492]
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515] EngineCore failed to start.
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515] Traceback (most recent call last):
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]   File "/workspace/vllm/vllm/v1/engine/core.py", line 504, in run_engine_core
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]   File "/workspace/vllm/vllm/v1/engine/core.py", line 764, in __init__
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]     super().__init__(vllm_config, on_head_node, handshake_address,
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]   File "/workspace/vllm/vllm/v1/engine/core.py", line 390, in __init__
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]   File "/workspace/vllm/vllm/v1/engine/core.py", line 76, in __init__
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]     self.model_executor = executor_class(vllm_config)
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]   File "/workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]     self._init_executor()
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]   File "/workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 98, in _init_executor
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]   File "/workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 427, in wait_for_ready
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515]     raise e from None
(EngineCore_1 pid=630) ERROR 08-26 12:16:18 [core.py:515] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
```
I think in the containter torch_npu could only see the assigned NPU device with logicId ranged [0-4), but the possible physical Id in ENV variables `ASCEND_RT_VISIBLE_DEVICES` ranged [0,8). 
But if the ENV variable `ASCEND_RT_VISIBLE_DEVICES ` is not assigend, in the mooncake connector initialization stage, the NPU device Id will automatically start from 0, i.e. 0,1,2,3. But the real device Id is 0,3,4,7.
So I think unlike running on the physical machine where torch_npu is able to observe all NPU device, in the condition of running on K8s, torch_npu is limitted by the resource allocated to the container. Directly using the ENV variable `ASCEND_RT_VISIBLE_DEVICES ` will cause this incompatibility. 
