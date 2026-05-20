# Issue #4284: [Bug]: npu init 失败

## 基本信息

- **编号**: #4284
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4284
- **创建时间**: 2025-11-19T11:23:00Z
- **关闭时间**: 2025-12-29T09:05:53Z
- **更新时间**: 2025-12-29T09:05:53Z
- **提交者**: @jc7ctzphbf-dotcom
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```
 Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov  2 2025, 08:46:33) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-119-generic-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               192
On-line CPU(s) list:                  0-191
Vendor ID:                            HiSilicon
Model name:                           Kunpeng-920
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   48
Socket(s):                            4
Stepping:                             0x1
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
[pip3] onnxruntime==1.23.2
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ASCEND_DEVICE_NAME=davinci0,davinci1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
ASCEND_DEVICE_ID=0,1
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 98.1        32                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 86.6        30                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 88.7        30                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 89.9        30                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 93.6        36                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 91.4        34                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 88.4        34                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 89.9        34                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3381 / 65536         |
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
version=8.0.RC3.alpha001
innerversion=V100R001C77B220SPC008
compatible_version=[V100R001C80,V100R001C84],[V100R001C77,V100R001C79],[V100R001C29],[V100R001C11,V100R001C50]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.RC3.alpha001/aarch64-linux
</details>


### 🐛 Describe the bug

```python
import torch_npu
if torch_npu.npu.is_available():
    total_memory = torch_npu.npu.get_device_properties('npu').total_memory / (1024 ** 3)  # 转为 GB
```

mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/mineru/utils/model_utils.py", line 446, in get_vram
mineru-npu-model-server   |     total_memory = torch_npu.npu.get_device_properties(device).total_memory / (1024 ** 3)  # 转为 GB
mineru-npu-model-server   |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/__init__.py", line 462, in get_device_properties
mineru-npu-model-server   |     device_id = _get_device_index(device_name, optional=True)
mineru-npu-model-server   |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 155, in _get_device_index
mineru-npu-model-server   |     return _torch_get_device_index(device, optional, allow_cpu)
mineru-npu-model-server   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_utils.py", line 851, in _get_device_index
mineru-npu-model-server   |     device_idx = _get_current_device_index()
mineru-npu-model-server   |                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_utils.py", line 788, in _get_current_device_index
mineru-npu-model-server   |     return _get_device_attr(lambda m: m.current_device())
mineru-npu-model-server   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_utils.py", line 781, in _get_device_attr
mineru-npu-model-server   |     return get_member(getattr(torch, device_type))
mineru-npu-model-server   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_utils.py", line 788, in <lambda>
mineru-npu-model-server   |     return _get_device_attr(lambda m: m.current_device())
mineru-npu-model-server   |                                       ^^^^^^^^^^^^^^^^^^
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/utils.py", line 95, in current_device
mineru-npu-model-server   |     torch_npu.npu._lazy_init()
mineru-npu-model-server   |   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/__init__.py", line 251, in _lazy_init
mineru-npu-model-server   |     torch_npu._C._npu_init()
mineru-npu-model-server   | RuntimeError: Initialize:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:152 NPU function error: c10_npu::SetDevice(device_id_), error code is 507033
mineru-npu-model-server   | [ERROR] 2025-11-19-11:14:58 (PID:356, Device:0, RankID:-1) ERR00100 PTA call acl api failed
mineru-npu-model-server   | [Error]: Failed to start the device. 
mineru-npu-model-server   |         Rectify the fault based on the error information in the ascend log.
mineru-npu-model-server   | E30006: 2025-11-19-11:14:58.516.606 Failed to verify the OPP
mineru-npu-model-server   |         Possible Cause: 1.The OPP is incorrect.
mineru-npu-model-server   |         Solution: 1. Use a correct OPP.
mineru-npu-model-server   |         TraceBack (most recent call last):
mineru-npu-model-server   |         tsd client wait response fail, hostpid:1944202, device response code[1]. unknown device error.[FUNC:WaitRsp][FILE:process_mode_manager.cpp][LINE:332]
mineru-npu-model-server   |         Start aicpu executor failed, retCode=0x7020009 devId=0[FUNC:DeviceRetain][FILE:runtime.cc][LINE:3810]
mineru-npu-model-server   |         Check param failed, dev can not be NULL![FUNC:PrimaryContextRetain][FILE:runtime.cc][LINE:3576]
mineru-npu-model-server   |         Check param failed, ctx can not be NULL![FUNC:PrimaryContextRetain][FILE:runtime.cc][LINE:3603]
mineru-npu-model-server   |         Check param failed, context can not be null.[FUNC:NewDevice][FILE:api_impl.cc][LINE:2375]
mineru-npu-model-server   |         New device failed, retCode=0x7010006[FUNC:SetDevice][FILE:api_impl.cc][LINE:2398]
mineru-npu-model-server   |         rtSetDevice execute failed, reason=[device retain error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
mineru-npu-model-server   |         open device 0 failed, runtime result = 507033.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
mineru-npu-model-server   |         ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5196]
mineru-npu-model-server   |         The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
mineru-npu-model-server   | 
mineru-npu-model-server   | 
mineru-npu-model-server   | INFO:     127.0.0.1:47070 - "POST /infer HTTP/1.1" 500 Internal Server Error
mineru-npu-model-server   | 2025-11-19 11:14:59.028 | ERROR    | __main__:doc_parse:95 | Dispatch error to http://127.0.0.1:8100/infer: 500: {"detail":"Initialize:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:152 NPU function error: c10_npu::SetDevice(device_id_), error code is 507033\n[ERROR] 2025-11-19-11:14:58 (PID:356, Device:0, RankID:-1) ERR00100 PTA call acl api failed\n[Error]: Failed to start the device. \n        Rectify the fault based on the error information in the ascend log.\nE30006: 2025-11-19-11:14:58.516.606 Failed to verify the OPP\n        Possible Cause: 1.The OPP is incorrect.\n        Solution: 1. Use a correct OPP.\n        TraceBack (most recent call last):\n        tsd client wait response fail, hostpid:1944202, device response code[1]. unknown device error.[FUNC:WaitRsp][FILE:process_mode_manager.cpp][LINE:332]\n        Start aicpu executor failed, retCode=0x7020009 devId=0[FUNC:DeviceRetain][FILE:runtime.cc][LINE:3810]\n        Check param failed, dev can not be NULL![FUNC:PrimaryContextRetain][FILE:runtime.cc][LINE:3576]\n        Check param failed, ctx can not be NULL![FUNC:PrimaryContextRetain][FILE:runtime.cc][LINE:3603]\n        Check param failed, context can not be null.[FUNC:NewDevice][FILE:api_impl.cc][LINE:2375]\n        New device failed, retCode=0x7010006[FUNC:SetDevice][FILE:api_impl.cc][LINE:2398]\n        rtSetDevice execute failed, reason=[device retain error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]\n        open device 0 failed, runtime result = 507033.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]\n        ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5196]\n        The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]\n"}


