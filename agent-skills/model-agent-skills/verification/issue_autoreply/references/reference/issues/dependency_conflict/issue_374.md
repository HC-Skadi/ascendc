# Issue #374: [Bug]: "The model outputs ```!!!``` indefinitely."

## 基本信息

- **编号**: #374
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/374
- **创建时间**: 2025-03-21T07:11:41Z
- **关闭时间**: 2025-03-27T05:40:23Z
- **更新时间**: 2025-03-31T15:38:06Z
- **提交者**: @llmadd
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.oe2203.aarch64-aarch64-with-glibc2.35
Is XNNPACK available: True

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
Frequency boost:                 disabled
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
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
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] transformers==4.49.0
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.1               Version: 24.1.rc2.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 121.6       40                0    / 0             |
| 0                         | 0000:C1:00.0  | 10          0    / 0          57895/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 116.4       39                0    / 0             |
| 0                         | 0000:C2:00.0  | 10          0    / 0          57898/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 116.6       38                0    / 0             |
| 0                         | 0000:81:00.0  | 13          0    / 0          57856/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 123.2       41                0    / 0             |
| 0                         | 0000:82:00.0  | 10          0    / 0          57898/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 121.4       45                0    / 0             |
| 0                         | 0000:01:00.0  | 10          0    / 0          58114/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 126.1       45                0    / 0             |
| 0                         | 0000:02:00.0  | 9           0    / 0          57856/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 122.4       46                0    / 0             |
| 0                         | 0000:41:00.0  | 15          0    / 0          57948/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 119.9       46                0    / 0             |
| 0                         | 0000:42:00.0  | 14          0    / 0          57855/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 13128         | python                   | 54601                   |
+===========================+===============+====================================================+
| 1       0                 | 13604         | python                   | 54603                   |
+===========================+===============+====================================================+
| 2       0                 | 13606         | python                   | 54561                   |
+===========================+===============+====================================================+
| 3       0                 | 13608         | python                   | 54603                   |
+===========================+===============+====================================================+
| 4       0                 | 13610         | python                   | 54819                   |
+===========================+===============+====================================================+
| 5       0                 | 13612         | python                   | 54560                   |
+===========================+===============+====================================================+
| 6       0                 | 13614         | python                   | 54653                   |
+===========================+===============+====================================================+
| 7       0                 | 13616         | python                   | 54561                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux

```

</details>


### 🐛 Describe the bug

I deployed the DeepSeek-R1-Distill-Llama-70B model using vllm-ascend, but I encountered some peculiar issues. When posing the same queries, I experienced an infinite output of ```!!!!!``` with vllm-ascend, whereas the deployment with vllm proceeded without any such anomalies. I would like to inquire about the potential causes that might be triggering this problem.
And this is not an occasional occurrence, but rather a 100% reproducible issue


