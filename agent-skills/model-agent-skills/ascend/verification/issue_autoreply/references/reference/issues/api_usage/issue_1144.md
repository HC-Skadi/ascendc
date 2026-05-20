# Issue #1144: [Bug]: import mindie_turbo时出现undefined symbol: _ZNK6AsdOps3Ops18GetOperationByNameERKSs

## 基本信息

- **编号**: #1144
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1144
- **创建时间**: 2025-06-10T01:54:12Z
- **关闭时间**: 2025-06-10T09:46:31Z
- **更新时间**: 2025-06-10T09:46:31Z
- **提交者**: @JackeyGuo
- **评论数**: 3

## 标签

question

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: 17.0.6 (ac00fd0f3aa8)
CMake version: version 4.0.2
Libc version: glibc-2.34

Python version: 3.10.8 (main, Jun  6 2025, 16:03:58) [GCC 10.3.1] (64-bit runtime)
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
[pip3] moxing-pytorch==2.0.1.rc0.b9ef8876
[pip3] numpy==1.26.4
[pip3] pynvml==12.0.0
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0.dev0
[pip3] transformers-stream-generator==0.0.5
[conda] No relevant packages
vLLM Version: 0.7.4.dev0+ged6e907.d20250606 (git sha: ed6e907, date: 20250606)
vLLM Ascend Version: 0.7.3.post1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=garbage_collection_threshold:0.95,max_split_size_mb:250
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/ma-user/anaconda3/envs/vllm/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/BiShengCompiler-4.1.0-aarch64-linux/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/third_party/dnnl
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
| npu-smi 23.0.5                   Version: 23.0.5                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 94.6        50                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3361 / 65536         |
+===========================+===============+============================

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

运行import mindie_turbo时会出现链接库不匹配的错误：ImportError: /home/ma-user/anaconda3/envs/vllm/lib/python3.10/site-packages/mindie_turbo/_ops.cpython-310-aarch64-linux-gnu.so: undefined symbol: _ZNK6AsdOps3Ops18GetOperationByNameERKS
