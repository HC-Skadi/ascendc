# Issue #1629: [Bug]: 0.9.1 version Lora/MultiLora 推理速度慢 2、3 tokens\s

## 基本信息

- **编号**: #1629
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1629
- **创建时间**: 2025-07-04T09:53:08Z
- **关闭时间**: 2025-08-19T02:33:36Z
- **更新时间**: 2025-08-19T02:33:36Z
- **提交者**: @zhz292
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.10.17 (main, May  8 2025, 07:18:04) [GCC 11.4.0] (64-bit runtime)
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
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250528
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=2,3
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
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
| npu-smi 24.1.rc2                 Version: 24.1.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 100.2       43                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          56363/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 96.7        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          56362/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 96.4        41                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 97.0        42                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 102.5       48                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          64748/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 101.2       45                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          64751/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 99.5        45                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          64749/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 94.5        44                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          64749/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 1271095       |                          | 52899                   |
+===========================+===============+====================================================+
| 1       0                 | 1271097       |                          | 52899                   |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| 4       0                 | 1976542       |                          | 61430                   |
+===========================+===============+====================================================+
| 5       0                 | 1976544       |                          | 61429                   |
+===========================+===============+====================================================+
| 6       0                 | 1976548       |                          | 61430                   |
+===========================+===============+====================================================+
| 7       0                 | 1976558       |                          | 61430                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
</summary>

</details>


### 🐛 Describe the bug

# 问题描述：
   使用镜像 IMAGE=quay.io/ascend/vllm-ascend:v0.9.1rc1 部署带lora的模型服务推理速度过慢。
# 操作步骤：
## 直接部署模型服务，推理速度2~3tokens/s
vllm serve /data/models/DeepSeek-R1-Distill-Qwen-32B/ --served-model-name DeepSeek-R1-Distill-Qwen-32B --trust-remote-code --tensor-parallel-size 2 --max-model-len 8000 --port 18461  --enable-lora --max-loras 3 --lora-modules '{"name": "nothink-lora", "path": "/data/models/loras/saves/deepseek-32b-nothink/lora/sft/", "base_model_name": "DeepSeek-R1-Distill-Qwen-32B"}'

![Image](https://github.com/user-attachments/assets/7fc7ac39-d961-480d-83dc-3c01cc5649b6)

## VLLM_USE_V1=1 部署模型服务，服务无法正常启动

![Image](https://github.com/user-attachments/assets/fd934596-3469-4987-ba88-50101bbd392f)

[errorlog.txt](https://github.com/user-attachments/files/21054885/errorlog.txt)

![Image](https://github.com/user-attachments/assets/97ac9cb2-a6b0-4ed0-859c-8344394bbc7e)

![Image](https://github.com/user-attachments/assets/95cbe343-c35f-4641-9e35-f3f0d4b9a410)
