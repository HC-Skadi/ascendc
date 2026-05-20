# Issue #6063: [Usage]: When deploying vll-ascend using Docker, regardless of how the devices are mapped, only the first NPU device is ultimately recognized.

## 基本信息

- **编号**: #6063
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6063
- **创建时间**: 2026-01-21T02:04:57Z
- **关闭时间**: 2026-02-02T09:02:32Z
- **更新时间**: 2026-02-02T09:02:32Z
- **提交者**: @Sp00n-X
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

I configured the device mappings within Compose, as shown below. I also tried mapping physical machines 4, 5, 6, and 7 to containers 1, 2, 3, and 4, as well as some other methods, but ultimately the Docker containers still use my devices 1, 2, 3, and 4.
===================
  docker-compose.yaml
===================
    environment:
      - ASCEND_VISIBLE_DEVICES=4,5
      - PYTHONUNBUFFERED=1
     
    devices:
      - /dev/davinci0:/dev/davinci0
      - /dev/davinci1:/dev/davinci1
      - /dev/davinci2:/dev/davinci2
      - /dev/davinci3:/dev/davinci3
      - /dev/davinci4:/dev/davinci4
      - /dev/davinci5:/dev/davinci5
      - /dev/davinci6:/dev/davinci6
      - /dev/davinci7:/dev/davinci7
      

```text
The output of above commands
```
**inside the docker container**

# npu-smi info
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1                                 Version: 25.3.rc1                                     |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310P3                 | OK              | NA           86                16885 / 16885         |
| 0       0                     | 0000:01:00.0    | 0            35552/ 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 0       310P3                 | OK              | NA           84                16997 / 16997         |
| 1       1                     | 0000:01:00.0    | 0            35270/ 43693                            |
+===============================+=================+======================================================+
| 96      310P3                 | OK              | NA           84                0     / 0             |
| 0       2                     | 0000:03:00.0    | 0            1705 / 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 96      310P3                 | OK              | NA           84                0     / 0             |
| 1       3                     | 0000:03:00.0    | 0            1242 / 43693                            |
+===============================+=================+======================================================+
| 32768   310P3                 | OK              | NA           79                0     / 0             |
| 0       4                     | 0000:81:00.0    | 0            1696 / 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 32768   310P3                 | OK              | NA           78                0     / 0             |
| 1       5                     | 0000:81:00.0    | 0            1246 / 43693                            |
+===============================+=================+======================================================+
| 32896   310P3                 | OK              | NA           82                0     / 0             |
| 0       6                     | 0000:84:00.0    | 0            1658 / 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 32896   310P3                 | OK              | NA           81                0     / 0             |
| 1       7                     | 0000:84:00.0    | 0            1265 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| 0       0                     | 326429          |                          | 33842                     |
| 0       0                     | 326430          |                          | 108                       |
| 0       1                     | 326430          |                          | 34086                     |
+===============================+=================+======================================================+
| No running processes found in NPU 96                                                                   |
+===============================+=================+======================================================+
| No running processes found in NPU 32768                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32896                                                                |
+===============================+=================+======================================================+

# cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux

# python collect_env.py 
Collecting environment information...
==============================
        System Info
==============================
OS                           : Ubuntu 22.04.5 LTS (aarch64)
GCC version                  : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version                : Could not collect
CMake version                : version 4.0.3
Libc version                 : glibc-2.35

==============================
       PyTorch Info
==============================
PyTorch version              : 2.7.1+cpu
Is debug build               : False
CUDA used to build PyTorch   : None
ROCM used to build PyTorch   : N/A

==============================
      Python Environment
==============================
Python version               : 3.11.13 (main, Jul 26 2025, 08:20:43) [GCC 11.4.0] (64-bit runtime)
Python platform              : Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.35

==============================
       CUDA / GPU Info
==============================
Is CUDA available            : False
CUDA runtime version         : No CUDA
CUDA_MODULE_LOADING set to   : N/A
GPU models and configuration : No CUDA
Nvidia driver version        : No CUDA
cuDNN version                : No CUDA
HIP runtime version          : N/A
MIOpen runtime version       : N/A
Is XNNPACK available         : True

==============================
          CPU Info
==============================
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             128
On-line CPU(s) list:                0-127
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 7260
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 64
Socket(s):                          2
Stepping:                           0x1
Frequency boost:                    disabled
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm
L1d cache:                          8 MiB (128 instances)
L1i cache:                          8 MiB (128 instances)
L2 cache:                           64 MiB (128 instances)
L3 cache:                           128 MiB (4 instances)
NUMA node(s):                       4
NUMA node0 CPU(s):                  0-31
NUMA node1 CPU(s):                  32-63
NUMA node2 CPU(s):                  64-95
NUMA node3 CPU(s):                  96-127
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Not affected
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

==============================
Versions of relevant libraries
==============================
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.53.3
[conda] Could not collect

==============================
         vLLM Info
==============================
ROCM Version                 : Could not collect
vLLM Version                 : 0.10.0
vLLM Build Flags:
  CUDA Archs: Not Set; ROCm: Disabled
GPU Topology:
  Could not collect

==============================
     Environment Variables
==============================
CUDA_VISIBLE_DEVICES=4,5
CUDA_VISIBLE_DEVICES=4,5
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64:/data/ai/Ascend/ascend-toolkit/latest/lib64:/data/ai/Ascend/driver/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64:/data/ai/Ascend/ascend-toolkit/latest/lib64:/data/ai/Ascend/driver/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64:/data/ai/Ascend/ascend-toolkit/latest/lib64:/data/ai/Ascend/driver/lib64:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1

### How would you like to use vllm on ascend

_No response_
