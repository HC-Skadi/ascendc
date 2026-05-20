# Issue #501: [Usage]: DeepSeek-R1-BF16 4*910B2 Loading safetensors checkpoint shards: 100% 后卡住

## 基本信息

- **编号**: #501
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/501
- **创建时间**: 2025-04-10T11:24:26Z
- **关闭时间**: 2025-04-11T01:21:16Z
- **更新时间**: 2025-04-11T01:21:16Z
- **提交者**: @15626471095
- **评论数**: 0

## 标签

无

## 问题描述

### Your current environment

```text
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 91.1        49                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 91.6        50                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3373 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 88.1        48                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 92.4        50                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3375 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 91.7        50                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3372 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 92.1        52                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3374 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 90.9        49                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3373 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 87.8        50                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3375 / 65536         |
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


package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux


Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-136.12.0.86.r1526_92.hce2.aarch64-aarch64-with-glibc2.35
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

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
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] transformers==4.50.3
[conda] Could not collect
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: 0.7.3
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
```


### How would you like to use vllm on ascend

python -m vllm.entrypoints.openai.api_server -tp 32 --trust-remote-code --host 0.0.0.0 --port 8085 --gpu-memory-utilization 0.95 --model /share/model/deepseek-ai/DeepSeek-R1-BF16/ --served-model-name DeepSeek-R1 --max-model-len 16384 --distributed_executor_backend "ray" --disable-frontend-multiprocessing


Loading safetensors checkpoint shards:  99% Completed | 161/163 [01:29<00:01,  1.70it/s]
Loading safetensors checkpoint shards:  99% Completed | 162/163 [01:29<00:00,  1.69it/s]
Loading safetensors checkpoint shards: 100% Completed | 163/163 [01:30<00:00,  1.69it/s]
Loading safetensors checkpoint shards: 100% Completed | 163/163 [01:30<00:00,  1.81it/s]

然后卡住不动

