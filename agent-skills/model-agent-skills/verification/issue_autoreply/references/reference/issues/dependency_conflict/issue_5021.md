# Issue #5021: [Bug]: bf16 lora don't work with 0.11.0rc2

## 基本信息

- **编号**: #5021
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5021
- **创建时间**: 2025-12-15T07:20:01Z
- **关闭时间**: 2025-12-29T12:25:21Z
- **更新时间**: 2025-12-29T12:25:21Z
- **提交者**: @hhd52859
- **评论数**: 3

## 标签

bug; module:lora

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

/vllm-workspace/vllm-ascend# python collect_env.py 
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-2107.6.0.0251.43.oe1.bclinux.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
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
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.1.2
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc3.dev0+ga2e4c3fe7.d20251124 (git sha: a2e4c3fe7, date: 20251124)

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
| npu-smi 25.0.rc1.1               Version: 25.0.rc1.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 95.5        43                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3414 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 95.7        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          61258/ 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 97.9        44                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          34445/ 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 96.9        45                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          52462/ 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 101.5       45                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          21100/ 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 103.3       47                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          15984/ 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 92.4        44                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          49121/ 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 96.0        45                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          32177/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| 1       0                 | 30496         |                          | 328                     |
| 1       0                 | 30336         |                          | 3790                    |
| 1       0                 | 22400         |                          | 21066                   |
| 1       0                 | 21128         |                          | 260                     |
| 1       0                 | 15704         |                          | 7859                    |
| 1       0                 | 8416          |                          | 150                     |
| 1       0                 | 20513         |                          | 160                     |
| 1       0                 | 14162         |                          | 1150                    |
+===========================+===============+====================================================+
| 2       0                 | 49984         |                          | 8971                    |
| 2       0                 | 48040         |                          | 1014                    |
| 2       0                 | 46664         |                          | 166                     |
| 2       0                 | 56929         |                          | 682                     |
| 2       0                 | 56641         |                          | 210                     |
| 2       0                 | 55233         |                          | 208                     |
| 2       0                 | 53409         |                          | 259                     |
| 2       0                 | 49841         |                          | 624                     |
+===========================+===============+====================================================+
| 3       0                 | 24456         |                          | 673                     |
| 3       0                 | 24392         |                          | 3615                    |
| 3       0                 | 24626         |                          | 3103                    |
| 3       0                 | 24521         |                          | 673                     |
| 3       0                 | 24553         |                          | 1360                    |
| 3       0                 | 24173         |                          | 666                     |
| 3       0                 | 24495         |                          | 673                     |
| 3       0                 | 31391         |                          | 38729                   |
+===========================+===============+====================================================+
| 4       0                 | 875           |                          | 17752                   |
+===========================+===============+====================================================+
| 5       0                 | 33376         |                          | 122                     |
| 5       0                 | 31176         |                          | 113                     |
| 5       0                 | 30832         |                          | 9606                    |
| 5       0                 | 32353         |                          | 264                     |
| 5       0                 | 32581         |                          | 262                     |
| 5       0                 | 31894         |                          | 396                     |
| 5       0                 | 34087         |                          | 147                     |
| 5       0                 | 33767         |                          | 328                     |
+===========================+===============+====================================================+
| 6       0                 | 52781         |                          | 45767                   |
+===========================+===============+====================================================+
| 7       0                 | 16600         |                          | 4720                    |
| 7       0                 | 16598         |                          | 5106                    |
| 7       0                 | 16599         |                          | 4419                    |
| 7       0                 | 16601         |                          | 5231                    |
| 7       0                 | 16602         |                          | 4739                    |
| 7       0                 | 16603         |                          | 4689                    |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux

</details>


### 🐛 Describe the bug

image: quay.io/ascend/vllm-ascend:v0.11.0rc2
models:
   - text: Qwen3-4B-Instruct-2507
   - VL: Qwen2.5-VL-3B-Instruct

Lora prams don't make any effect with BF16, the result is still same with the original models.  But with fp16 it works.

Located as the lora kernels were not correctly compiled. Seems that the  __CCE_AICORE__ >= 220 doesn't meet for official image. After comment out every __CCE_AICORE__ condition, re-compile with following commands, the lora take effects again:
```
FROM quay.io/ascend/vllm-ascend:v0.11.0rc2

# Copy and replace the LoRA-related files
COPY bgmv_expand.cpp /vllm-workspace/vllm-ascend/csrc/kernels/bgmv_expa
nd.cpp
COPY bgmv_shrink.cpp /vllm-workspace/vllm-ascend/csrc/kernels/bgmv_shri
nk.cpp
COPY pos_encoding_kernels.cpp /vllm-workspace/vllm-ascend/csrc/kernels/
pos_encoding_kernels.cpp
COPY sgmv_expand.cpp /vllm-workspace/vllm-ascend/csrc/kernels/sgmv_expa
nd.cpp
COPY sgmv_shrink.cpp /vllm-workspace/vllm-ascend/csrc/kernels/sgmv_shri
nk.cpp

#ascend kernel complie
RUN cd /vllm-workspace/vllm-ascend && \
TORCH_DEVICE_BACKEND_AUTOLOAD=0 \
SOC_VERSION=ASCEND910B2 \
COMPILE_CUSTOM_KERNELS=1 \
ASCEND_HOME_PATH="/usr/local/Ascend/ascend-toolkit/latest" \
python3 setup.py install --force
```

