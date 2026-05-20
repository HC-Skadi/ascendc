# Issue #1155: [Bug]: failed to run qwen2.5-vl-7b with TP=2: ACL stream synchronize failed

## 基本信息

- **编号**: #1155
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1155
- **创建时间**: 2025-06-10T10:16:24Z
- **关闭时间**: 2025-10-28T02:46:50Z
- **更新时间**: 2025-10-28T02:49:05Z
- **提交者**: @linyinli
- **评论数**: 3

## 标签

bug; module:mindie-turbo; module:multimodal

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.22.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jun  9 2025, 12:58:25) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.oe2203.aarch64-aarch64-with-glibc2.35

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
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3.post1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=16
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ATB_CONTEXT_HOSTTILING_RING=1
ATB_OPERATION_EXECUTE_ASYNC=1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_CONTEXT_HOSTTILING_SIZE=102400
PYTORCH_INSTALL_PATH=/usr/lib/python3.11/site-packages/torch
PYTORCH_NPU_INSTALL_PATH=/usr/lib/python3.11/site-packages/torch_npu
ATB_SPEED_HOME_PATH=/usr/local/Ascend/atb-models
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/lib/python3.11/site-packages/torch_npu/lib:/usr/lib/python3.11/site-packages/torch/lib:/usr/local/Ascend/atb-models/lib:/usr/local/Ascend/nnal/atb/lates
t/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolki
t/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest
/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/
linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_USE_TILING_COPY_STREAM=0
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2                 Version: 24.1.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 96.6        54                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          13281/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 95.7        53                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          13260/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 100.0       52                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3369 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 103.6       54                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3369 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 4       0                 | 17011         | python                   | 9963                    |
+===========================+===============+====================================================+
| 5       0                 | 17544         | python                   | 9942                    |
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
```

</details>


### 🐛 Describe the bug

```
vllm serve /cache/
model_scope/Qwen/Qwen2.5-VL-7B-Instruct --max-model-len 8192 --tensor-parallel-size=2 --host 0.0.0.0 --port 40027 --served-model-name qwen2.5-vl-7b
```

<img width="1467" alt="Image" src="https://github.com/user-attachments/assets/56c1df40-ca3e-4710-abce-4d0489bd23d9" />

<img width="1452" alt="Image" src="https://github.com/user-attachments/assets/2a85bc82-a4b4-40f6-8554-d40eeba2ac2d" />

<img width="1438" alt="Image" src="https://github.com/user-attachments/assets/3b6367fe-7135-4517-bb16-4055b5c8c211" />

<img width="1436" alt="Image" src="https://github.com/user-attachments/assets/7899579f-c867-466b-8761-36a118828e13" />
