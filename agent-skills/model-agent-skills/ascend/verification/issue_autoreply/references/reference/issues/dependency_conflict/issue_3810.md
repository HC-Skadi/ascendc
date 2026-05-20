# Issue #3810: [Bug]: Qwen3-VL-8B在910B4推理调用超过上下文长度的图片报错

## 基本信息

- **编号**: #3810
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3810
- **创建时间**: 2025-10-28T02:47:45Z
- **关闭时间**: 2025-12-29T06:23:21Z
- **更新时间**: 2025-12-29T06:23:21Z
- **提交者**: @1579890249
- **评论数**: 17

## 标签

bug; module:multimodal; qwen3-vl

## 问题描述

### Your current environment

root@gxai-infer-3:/# python collect_env.py
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.31.6
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-282.0.0.185.oe2203sp4.aarch64-aarch64-with-glibc2.35

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
Frequency boost:                    disabled
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
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
Vulnerability Spec store bypass:    Not affected
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] onnx==1.17.0
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchaudio==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc0

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=16
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ATB_CONTEXT_HOSTTILING_RING=1
ATB_OPERATION_EXECUTE_ASYNC=1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_CONTEXT_HOSTTILING_SIZE=102400
PYTORCH_INSTALL_PATH=/usr/local/python3.11.13/lib/python3.11/site-packages/torch
PYTORCH_NPU_INSTALL_PATH=/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu
ATB_SPEED_HOME_PATH=/usr/local/Ascend/atb-models
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib:/usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib:/usr/local/Ascend/atb-models/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/lib:/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux/lib64:/usr/local/python3.11.13/lib:/usr/local/python3.11.13/lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_USE_TILING_COPY_STREAM=0
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
| 0     910B4-1             | OK            | 92.3        31                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          12566/ 65536         |
+===========================+===============+====================================================+
| 1     910B4-1             | OK            | 86.7        30                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          59719/ 65536         |
+===========================+===============+====================================================+
| 2     910B4-1             | OK            | 87.5        29                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3448 / 65536         |
+===========================+===============+====================================================+
| 3     910B4-1             | OK            | 90.2        32                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3447 / 65536         |
+===========================+===============+====================================================+
| 4     910B4-1             | OK            | 92.4        39                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3444 / 65536         |
+===========================+===============+====================================================+
| 5     910B4-1             | OK            | 92.3        40                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3445 / 65536         |
+===========================+===============+====================================================+
| 6     910B4-1             | OK            | 97.0        37                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          7952 / 65536         |
+===========================+===============+====================================================+
| 7     910B4-1             | OK            | 87.3        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          17937/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 2340          | llama-box-rpc-s          | 111                     |
+===========================+===============+====================================================+
| 1       0                 | 2357          | llama-box-rpc-s          | 111                     |
| 1       0                 | 2394858       | VLLMEngineCor            | 56313                   |
+===========================+===============+====================================================+
| 2       0                 | 2339          | llama-box-rpc-s          | 111                     |
+===========================+===============+====================================================+
| 3       0                 | 2337          | llama-box-rpc-s          | 111                     |
+===========================+===============+====================================================+
| 4       0                 | 2362          | llama-box-rpc-s          | 111                     |
+===========================+===============+====================================================+
| 5       0                 | 2367          | llama-box-rpc-s          | 112                     |
+===========================+===============+====================================================+
| 6       0                 | 2343          | llama-box-rpc-s          | 111                     |
+===========================+===============+====================================================+
| 7       0                 | 5284          | llama-box-rpc-s          | 111                     |
| 7       0                 | 2395206       | python                   | 13162                   |
| 7       0                 | 2395167       | python                   | 1429                    |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux



### 🐛 Describe the bug

export NPU_MEMORY_FRACTION=0.96 
ASCEND_RT_VISIBLE_DEVICES=2 vllm serve /data/model-cache/Qwen3-VL-8B-Instruct/ --served_model_name Qwen3-vl-8b \
	--max_model_len 128000 --port 50000 --gpu-memory-utilization 0.75

<img width="2244" height="1426" alt="Image" src="https://github.com/user-attachments/assets/30d772be-2080-48e3-8a52-c8139c0a18b3" />

具体报错如文件所示

[910B4推理错误-4.txt](https://github.com/user-attachments/files/23178095/910B4.-4.txt)
