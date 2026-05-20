# Issue #3034: [Bug]: Ray+AclGraph+Qwen3_w8a8 run distributed server on 2 nodes failed.

## 基本信息

- **编号**: #3034
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3034
- **创建时间**: 2025-09-19T06:50:33Z
- **关闭时间**: 2025-10-31T08:30:27Z
- **更新时间**: 2025-12-11T13:15:41Z
- **提交者**: @paulyu12
- **评论数**: 17

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
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-138-generic-aarch64-with-glibc2.35

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
Core(s) per cluster:                  48
Socket(s):                            -
Cluster(s):                           4
Stepping:                             0x1
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                            12 MiB (192 instances)
L1i cache:                            12 MiB (192 instances)
L2 cache:                             96 MiB (192 instances)
L3 cache:                             192 MiB (8 instances)
NUMA node(s):                         4
NUMA node0 CPU(s):                    0-47
NUMA node1 CPU(s):                    48-95
NUMA node2 CPU(s):                    96-143
NUMA node3 CPU(s):                    144-191
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[conda] Could not collect
vLLM Version: 0.10.2
vLLM Ascend Version: 0.10.2rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ASCEND_80380672_N_1_2D_PORT_12300_TCP_PORT=12300
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=7,6,5,4,3,2,1,0
ASCEND_80380672_N_1_2D_SERVICE_PORT_DYE7FD=12300
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ASCEND_80380672_N_1_2D_PORT_12300_TCP=tcp://10.39.24.79:12300
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_80380672_N_1_2D_PORT_12300_TCP_PROTO=tcp
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_80380672_N_1_2D_SERVICE_PORT=12300
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_80380672_N_1_2D_SERVICE_HOST=10.39.24.79
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_80380672_N_1_2D_PORT_12300_TCP_ADDR=10.39.24.79
ASCEND_80380672_N_1_2D_PORT=tcp://10.39.24.79:12300
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
| 0     910B3               | OK            | 94.8        39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3538 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 91.8        37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 88.2        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 88.7        37                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 96.6        43                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3399 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 88.0        41                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 95.1        43                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3396 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 92.4        43                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3395 / 65536         |
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
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux

```

</details>


### 🐛 Describe the bug

vllm-ascend, 18/9/2025, commit id: 0c04bf1e3692693da07455177d1c70932c814358

When I ran distributed server according to the guide (https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi_node_ray.html), I got the an error. 

The launch command is following:
```shell
vllm serve /model/Qwen3-235B-A22B-W8A8 \
--distributed-executor-backend ray \
--host 0.0.0.0 \
--port 8004 \
--tensor-parallel-size 8 \
--pipeline-parallel-size 2 \
--seed 1024 \
--served-model-name qwen3-moe \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 6144 \
--max-num-batched-tokens 6144 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.9
```

The error log is in the following attached file:
[error.log](https://github.com/user-attachments/files/22421239/error.log)

