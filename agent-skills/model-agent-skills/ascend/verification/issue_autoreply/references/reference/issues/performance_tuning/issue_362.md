# Issue #362: [Bug]: VLLM-Ascend在910b2上推理deepseek模型非常慢，只有7token/s

## 基本信息

- **编号**: #362
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/362
- **创建时间**: 2025-03-20T02:32:42Z
- **关闭时间**: 2025-06-11T06:17:10Z
- **更新时间**: 2025-06-13T14:22:01Z
- **提交者**: @doit-5618
- **评论数**: 6

## 标签

performance

## 问题描述

### Your current environment


INFO 03-20 02:24:16 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-20 02:24:16 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-20 02:24:16 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-20 02:24:16 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-20 02:24:16 __init__.py:42] plugin ascend loaded.
INFO 03-20 02:24:17 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-20 02:24:17 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-20 02:24:17 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-20 02:24:17 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-20 02:24:17 __init__.py:42] plugin ascend loaded.
INFO 03-20 02:24:17 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-20 02:24:17 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-20 02:24:17 __init__.py:174] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-131-generic-aarch64-with-glibc2.35
Is XNNPACK available: True

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
[pip3] pyzmq==26.2.1
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250218
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0
[conda] Could not collect
vLLM Version: 0.7.1
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.7                   Version: 23.0.7                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 96.5        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          29954/ 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 98.7        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          29951/ 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 94.2        35                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          29950/ 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 91.5        38                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          29951/ 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 96.6        36                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3347 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 96.0        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3350 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 97.5        35                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3347 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 93.8        37                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3347 / 65536         |
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
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux


### 🐛 Describe the bug

<img width="741" alt="Image" src="https://github.com/user-attachments/assets/102981be-3b80-46a1-9172-edf1dbb00262" />
我用4卡910b2部署deepseek，推理速度非常慢，只有7token/s，我记得在a800中可以达到60token/s。请问是我的配置有问题吗？
vllm是拉的镜像：
root@unicom:/workspace# pip list | grep vll
vllm                              0.7.1+empty
vllm_ascend                       0.0.0
启动指令：
VLLM_USE_MODELSCOPE=true NPU_VISIBLE_DEVICES=4,5,6,7 ASCEND_RT_VISIBLE_DEVICES=4,5,6,7  vllm serve /workspace/ds-model --trust-remote-code --served-model-name ds-model --max-model-len 23792 --tensor-parallel-size 4 --gpu_memory_utilization 0.98 --max_num_seqs 2048 --port 8000


curl http://172.104.223.75:8000/v1/completions -H "Content-Type: application/json" -d '{"model": "ds-model", "prompt": "描述一下北京的秋天", "max_tokens": 512}'

