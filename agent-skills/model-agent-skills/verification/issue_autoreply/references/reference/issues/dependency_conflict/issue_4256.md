# Issue #4256: [Bug]: DeepSeek-v3.2-EXP-W8A8 Deployment Fails on 2 x A2 Nodes.

## 基本信息

- **编号**: #4256
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4256
- **创建时间**: 2025-11-18T10:51:15Z
- **关闭时间**: 2025-11-18T14:22:33Z
- **更新时间**: 2025-11-18T14:22:33Z
- **提交者**: @zkryakgul
- **评论数**: 1

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
CMake version: version 4.1.2
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov  2 2025, 08:46:33) [GCC 11.4.0] (64-bit runtime)
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
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc1

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
ASCEND_DOCKER_RUNTIME=True
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
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 91.1        32                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 88.6        34                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3396 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 89.4        32                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3396 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 90.6        33                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3393 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 86.8        36                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3396 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 89.4        39                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3396 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 92.9        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 90.0        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3396 / 65536         |
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
version=8.3.RC1
innerversion=V100R001C23SPC001B235
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

I'm trying to run DeepSeek-v3.2-EXP-w8a8 model on 2 x A2 Nodes. I followed the wiki in the official documentation. Create a one new image with the necessary extensions as described. Here is the Dockerfile:

```Dockerfile
FROM quay.io/ascend/vllm-ascend:v0.11.0rc1


RUN wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a2/CANN-custom_ops-sfa-linux.aarch64.run
RUN chmod +x ./CANN-custom_ops-sfa-linux.aarch64.run
RUN ./CANN-custom_ops-sfa-linux.aarch64.run --quiet
ENV ASCEND_CUSTOM_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize:${ASCEND_CUSTOM_OPP_PATH}
ENV LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api/lib/:${LD_LIBRARY_PATH}
RUN wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a2/custom_ops-1.0-cp311-cp311-linux_aarch64.whl
RUN pip install custom_ops-1.0-cp311-cp311-linux_aarch64.whl
```

After that I run the image on both of the nodes and run the exact same vllm serve commands in the guide (of course changing the `nic_name`, `local_ip` and `node0_ip`). Model weight files has been successfully loading but after load vllm process crashes with the following error log:

- Full Log file: https://turkey-llm-models.obs.cn-north-4.myhuaweicloud.com/tmp/ds-v3_2-deployment-node-0.log?AccessKeyId=DZ8HMRYG5ADNBICEL8GX&Expires=1764672859&Signature=ym51MUdpQ/jn5A5U5qi4qjY3Jmg%3D

- **Node-0 vllm process Log**
```
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:27[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:33[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m Process EngineCore_DP0:
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m Traceback (most recent call last):
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     self.run()
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     self._target(*self._args, **self._kwargs)
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     raise e
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 695, in run_engine_core
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     engine_core = DPEngineCoreProc(*args, **kwargs)
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 965, in __init__
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     super().__init__(vllm_config, local_client, handshake_address,
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     self._initialize_kv_caches(vllm_config)
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     self.model_executor.initialize_from_config(kv_cache_configs)
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 75, in initialize_from_config
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     self.collective_rpc("compile_or_warm_up_model")
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     result = get_response(w, dequeue_timeout,
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m     raise RuntimeError(
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m RuntimeError: Worker failed with error 'operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 507011
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m [ERROR] 2025-11-18-10:35:31 (PID:833, Device:0, RankID:-1) ERR00100 PTA call acl api failed
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m [Error]: Model execution failed. 
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m         Rectify the fault based on the error information in the ascend log.
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m E39999: Inner Error!
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m E39999[PID: 833] 2025-11-18-10:35:31.222.032 (E39999):  The error from device(chipId:0, dieId:0), serial number is 3, an exception occurred during AICPU execution, stream_id:45, task_id:1, errcode:135175, msg:aicpu execute failed.[FUNC:ProcessStarsAicpuErrorInfo][FILE:device_error_proc.cc][LINE:1483]
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m         TraceBack (most recent call last):
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m        Aicpu kernel execute failed, device_id=0, stream_id=45, task_id=1, soName=, funcName=, kernelName=, errorCode=0x91.[FUNC:PrintAicpuErrorInfo][FILE:davinci_kernel_task.cc][LINE:1308]
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m        Aicpu kernel execute failed, device_id=0,stream_id=45,task_id=1, soName=, funcName=, kernelName=[FUNC:PrintAicpuErrorInfo][FILE:davinci_kernel_task.cc][LINE:1333]
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m        Op execute failed. origin_op_name [MoeDistributeDispatchV2], op_name [MoeDistributeDispatchV2], error_info: task_id 1, stream_id 45, tid 833, device_id 0, retcode 0x7bc83[FUNC:ErrorTrackingCallback][FILE:error_tracking.cc][LINE:117]
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m        Aicpu kernel execute failed, device_id=0, stream_id=45, task_id=1, flip_num=0, kernel_type=5, fault op_name=, extend_info=.[FUNC:GetError][FILE:stream.cc][LINE:1191]
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m        rtStreamSynchronizeWithTimeout execute failed, reason=[the model stream execute failed][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m        synchronize stream with timeout failed, runtime result = 507011[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:162]
deepseek-v3_2-exp  | [1;36m(EngineCore_DP0 pid=414)[0;0m ', please check the stack trace above for the root cause
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:27[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:22[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:26[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:30[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:23[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:26[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:33[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:33[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:32[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:26[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:38[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:29[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [[32m2025-11-18 10:24:28[0m] [[93mWARNING[0m] [ascend910b] Not found tiling so file, use default api soc verison
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m Traceback (most recent call last):
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/usr/local/python3.11.13/bin/vllm", line 7, in <module>
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     sys.exit(main())
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m              ^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     args.dispatch_function(args)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     uvloop.run(run_server(args))
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return runner.run(wrapper())
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return self._loop.run_until_complete(task)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return await main
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     async with build_async_engine_client(
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return await anext(self.gen)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     async with build_async_engine_client_from_engine_args(
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return await anext(self.gen)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     async_llm = AsyncLLM.from_vllm_config(
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1572, in inner
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return fn(*args, **kwargs)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return cls(
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     self.engine_core = EngineCoreClient.make_async_mp_client(
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 101, in make_async_mp_client
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     return DPLBAsyncMPClient(*client_args)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1125, in __init__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 975, in __init__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     super().__init__(
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     with launch_core_engines(vllm_config, executor_class,
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     next(self.gen)
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     wait_for_engine_startup(
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m     raise RuntimeError("Engine core initialization failed. "
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
deepseek-v3_2-exp  | [1;36m(APIServer pid=145)[0;0m [ERROR] 2025-11-18-10:35:37 (PID:145, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

```
