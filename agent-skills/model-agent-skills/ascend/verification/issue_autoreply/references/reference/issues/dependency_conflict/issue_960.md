# Issue #960: [Bug]: When use v1_engine func "execute_model", return None

## 基本信息

- **编号**: #960
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/960
- **创建时间**: 2025-05-26T09:56:56Z
- **关闭时间**: 2025-12-30T01:59:39Z
- **更新时间**: 2025-12-30T01:59:39Z
- **提交者**: @zzyyanggu
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

INFO 05-26 17:39:01 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-26 17:39:01 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-26 17:39:01 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-26 17:39:03 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-26 17:39:03 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-26 17:39:03 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-26 17:39:03 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-26 17:39:03 [__init__.py:44] plugin ascend loaded.
INFO 05-26 17:39:03 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-26 17:39:04 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.34

Python version: 3.10.6 | packaged by conda-forge | (main, Aug 22 2022, 20:27:42) [GCC 10.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
BIOS Model name:                      Kunpeng 920 7285Z
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   80
Socket(s):                            4
Stepping:                             0x0
Frequency boost:                      disabled
CPU max MHz:                          3000.0000
CPU min MHz:                          400.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                            20 MiB (320 instances)
L1i cache:                            20 MiB (320 instances)
L2 cache:                             400 MiB (320 instances)
L3 cache:                             560 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-39
NUMA node1 CPU(s):                    40-79
NUMA node2 CPU(s):                    80-119
NUMA node3 CPU(s):                    120-159
NUMA node4 CPU(s):                    160-199
NUMA node5 CPU(s):                    200-239
NUMA node6 CPU(s):                    240-279
NUMA node7 CPU(s):                    280-319
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
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchdata==0.11.0
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.0
[conda] numpy                     1.26.4                    <pip>
[conda] pyzmq                     26.4.0                    <pip>
[conda] torch                     2.5.1                     <pip>
[conda] torch-npu                 2.5.1                     <pip>
[conda] torchdata                 0.11.0                    <pip>
[conda] torchvision               0.20.1                    <pip>
[conda] transformers              4.51.0                    <pip>
[conda] transformers              4.52.3                    <pip>
vLLM Version: 0.8.5.post2.dev0+g3015d5634.d20250524 (git sha: 3015d5634, date: 20250524)
vLLM Ascend Version: 0.8.5rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
VLLM_TARGET_DEVICE=empty
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/::/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3.5               Version: 24.1.rc3.5                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 180.2       38                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3430 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           37                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3188 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 185.9       39                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3430 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3188 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 173.4       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3427 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3187 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 176.2       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3425 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           36                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3191 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 178.3       36                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3414 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           36                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 178.4       37                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3415 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           37                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3203 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 176.0       36                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3413 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           37                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 181.1       38                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3427 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           36                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          3187 / 65536         |
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
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
</details>


### 🐛 Describe the bug

When task arrive func step (in vllm/v1/engine/core.py), it will execute func execute_model:
![Image](https://github.com/user-attachments/assets/244aa9af-56e9-4a78-b0e3-74ab582e84f4)
This function will use a rpc func and return output[0]:
![Image](https://github.com/user-attachments/assets/3bb374b3-4794-42eb-a434-4da106dbcc96)
And in vllm_ascend/worker/worker_v1.py, execute_model will return output if rank==0 else None:
![Image](https://github.com/user-attachments/assets/7df096e8-65d1-4127-8cbc-7ad579499c03)
Theoretically, it should be executed when rank==0, but in fact it return None, and then the error appeared:

![Image](https://github.com/user-attachments/assets/1c521493-9a34-4699-8c4b-688bb3c275f5)
so how to solve this problem
