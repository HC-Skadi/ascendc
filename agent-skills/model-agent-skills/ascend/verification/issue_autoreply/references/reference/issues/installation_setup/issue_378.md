# Issue #378: [Feature]: Add Ascend multiple card inference support for LLaMAFactory via vllm-ascend

## 基本信息

- **编号**: #378
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/378
- **创建时间**: 2025-03-21T16:50:15Z
- **关闭时间**: 2025-04-16T14:17:55Z
- **更新时间**: 2025-04-16T14:17:55Z
- **提交者**: @yuhkalhic
- **评论数**: 5

## 标签

feature request

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 03-21 16:44:08 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-21 16:44:08 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-21 16:44:08 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-21 16:44:08 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-21 16:44:08 [__init__.py:44] plugin ascend loaded.
INFO 03-21 16:44:08 [__init__.py:247] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.4.0
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.31.6
Libc version: glibc-2.35

Python version: 3.10.16 (main, Dec 11 2024, 16:18:56) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-4.19.90-2102.2.0.0068.3.ctl2.aarch64-aarch64-with-glibc2.35

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
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
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
[pip3] torch==2.4.0
[pip3] torch-npu==2.4.0.post2
[pip3] transformers==4.49.0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] torch                     2.4.0                    pypi_0    pypi
[conda] torch-npu                 2.4.0.post2              pypi_0    pypi
[conda] transformers              4.49.0                   pypi_0    pypi
vLLM Version: 0.1.dev1+g70e500c (git sha: 70e500c)
vLLM Ascend Version: 0.1.dev100+g663dca7 (git sha: 663dca7)

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
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/data/env/vl/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/tools/hccn_tool/:/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64/:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/python3.10.16/lib:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.3                   Version: 23.0.3                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 94.8        44                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          4495 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 99.7        45                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3333 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 97.1        43                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3332 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 94.4        45                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3331 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 96.8        44                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3334 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 93.6        46                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3333 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 94.0        45                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3332 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 96.9        45                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3332 / 65536         |
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
version=8.0.RC3
innerversion=V100R001C19SPC001B155
compatible_version=[V100R001C13,V100R001C19],[V100R001C30]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.RC3/aarch64-linux
```

</details>


### 🐛 Describe the bug

这是llama-factory仓库中的一个采用vllm进行推理的脚本( https://github.com/hiyouga/LLaMA-Factory/blob/main/scripts/vllm_infer.py )，   用到的数据集是项目自带的示例。

这是我运行的命令：
```bash
VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_LOGGING_LEVEL=DEBUG DISABLE_VERSION_CHECK=1 ASCEND_RT_VISIBLE_DEVICES=1 python scripts/vllm_infer.py --model_name_or_path Qwen/Qwen2.5-0.5B-Instruct --template qwen --dataset alpaca_en_demo
```

这个推理脚本在单卡情况下能够正常启动，但是在多卡启动时会出现这样的报错：

<img width="896" alt="Image" src="https://github.com/user-attachments/assets/ec2560f7-be4f-4983-bc0c-21f47e84b865" />


想请问有什么解决的方法吗？
