# Issue #562: [Bug]: qwen2.5vl-7b 经过llamafactorySFT后，使用vllm-ascend推理回复全是感叹号

## 基本信息

- **编号**: #562
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/562
- **创建时间**: 2025-04-18T01:53:27Z
- **关闭时间**: 2025-04-23T02:11:01Z
- **更新时间**: 2025-04-23T02:11:01Z
- **提交者**: @w1051868626
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

pyTorch version: 2.5.1
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: Could not collect
CMake version: version 3.22.0
Libc version: glibc-2.34

Python version: 3.9.10 | packaged by conda-forge | (main, Feb  1 2022, 21:53:27)  [GCC 9.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.2.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0
[conda] numpy                     1.26.4                    <pip>
[conda] pyzmq                     26.2.0                    <pip>
[conda] torch                     2.5.1                     <pip>
[conda] torch-npu                 2.5.1.dev20250320           <pip>
[conda] torchaudio                2.5.1                     <pip>
[conda] torchvision               0.20.1                    <pip>
[conda] transformers              4.49.0                    <pip>
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc2

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/ma-user/anaconda3/envs/python-3.9.10/lib/python3.9/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/third_party/dnnl
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.7                   Version: 23.0.7                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 106.9       39                0    / 0             |
| 0                         | 0000:C1:00.0  | 8           0    / 0          29589/ 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 110.8       40                0    / 0             |
| 0                         | 0000:C2:00.0  | 8           0    / 0          29578/ 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 107.0       39                0    / 0             |
| 0                         | 0000:81:00.0  | 7           0    / 0          29577/ 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 110.1       40                0    / 0             |
| 0                         | 0000:82:00.0  | 8           0    / 0          29578/ 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 94.7        42                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2827 / 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 87.7        42                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2828 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 94.9        41                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          2827 / 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 85.1        41                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          2829 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 91666         | python3.9                | 26795                   |
+===========================+===============+====================================================+
| 1       0                 | 92863         | python3.9                | 26793                   |
+===========================+===============+====================================================+
| 2       0                 | 92865         | python3.9                | 26793                   |
+===========================+===============+====================================================+
| 3       0                 | 92880         | python3.9                | 26793                   |
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
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux


### 🐛 Describe the bug

![Image](https://github.com/user-attachments/assets/4e604361-05da-42b4-aad3-5a1233b12fe5)

llamafactory微调后使用本项目推理，返回是这个。使用llamafactory推理是正常的，在v100上也是正常的
