# Issue #3324: [Bug]: 长上下文导致内存爆炸

## 基本信息

- **编号**: #3324
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3324
- **创建时间**: 2025-10-09T02:58:13Z
- **关闭时间**: 2025-10-16T08:55:07Z
- **更新时间**: 2025-10-16T08:55:07Z
- **提交者**: @zzc98
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
root@root:/vllm-workspace/vllm-ascend# python collect_env.py 
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35

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
[pip3] pyzmq==27.0.2
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.0
[conda] Could not collect
vLLM Version: 0.10.1.1
vLLM Ascend Version: 0.10.1rc1

ENV Variables:
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
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/op
skernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/As
cend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/loc
al/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/
op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 153.7       45                0    / 0             |
| 0                         | 0000:C1:00.0  | 39          0    / 0          62810/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 155.2       44                0    / 0             |
| 0                         | 0000:C2:00.0  | 39          0    / 0          62697/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 144.7       43                0    / 0             |
| 0                         | 0000:81:00.0  | 38          0    / 0          62697/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 155.3       43                0    / 0             |
| 0                         | 0000:82:00.0  | 35          0    / 0          62698/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 162.2       52                0    / 0             |
| 0                         | 0000:01:00.0  | 35          0    / 0          62697/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 158.6       52                0    / 0             |
| 0                         | 0000:02:00.0  | 36          0    / 0          62698/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 160.1       50                0    / 0             |
| 0                         | 0000:41:00.0  | 38          0    / 0          62697/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 167.5       67                0    / 0             |
| 0                         | 0000:42:00.0  | 34          0    / 0          62698/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 849           | /usr/local/pyth          | 117                     |
| 0       0                 | 842           | /usr/local/pyth          | 59017                   |
| 0       0                 | 843           | /usr/local/pyth          | 117                     |
| 0       0                 | 844           | /usr/local/pyth          | 117                     |
| 0       0                 | 845           | /usr/local/pyth          | 117                     |
| 0       0                 | 846           | /usr/local/pyth          | 117                     |
| 0       0                 | 847           | /usr/local/pyth          | 117                     |
| 0       0                 | 848           | /usr/local/pyth          | 117                     |
+===========================+===============+====================================================+
| 1       0                 | 843           | /usr/local/pyth          | 59363                   |
+===========================+===============+====================================================+
| 2       0                 | 844           | /usr/local/pyth          | 59363                   |
+===========================+===============+====================================================+
| 3       0                 | 845           | /usr/local/pyth          | 59363                   |
+===========================+===============+====================================================+
| 4       0                 | 846           | /usr/local/pyth          | 59363                   |
+===========================+===============+====================================================+
| 5       0                 | 847           | /usr/local/pyth          | 59363                   |
+===========================+===============+====================================================+
| 6       0                 | 848           | /usr/local/pyth          | 59363                   |
+===========================+===============+====================================================+
| 7       0                 | 849           | /usr/local/pyth          | 59363                   |
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

当部署大模型时，设置不同的上文下会在拉起模型时占用不同大小的内存。在部署glm-4.6-air时，设置模型上下文为100k时，内存会逐渐涨到90%，能正常拉起模型，但是降低到20%。当模型上下文设置为128k时（这个模型的最大上下文），内存会涨到99%，卡住整个系统，导致模型拉不起来。这个模型大约110B，机器内存1T，显存512G，设置短上下文拉起模型后显示kvcache足够容纳110592。
拉起模型命令
```shell
# 成功
vllm serve /root/model/GLM-4.5-Air --host 0.0.0.0 --port 1028 --max-model-len 102400 --served-model-name glm-4.5-air --tensor-parallel-size 8 --gpu-memory-utilization 0.85 --enable-auto-tool-choice  --tool-call-parser glm45 --rea
soning-parser glm45 --max-num-seqs 1

# 失败
vllm serve /root/model/GLM-4.5-Air --host 0.0.0.0 --port 1028 --max-model-len 131072 --served-model-name glm-4.5-air --tensor-parallel-size 8 --gpu-memory-utilization 0.85 --enable-auto-tool-choice  --tool-call-parser glm45 --rea
soning-parser glm45 --max-num-seqs 1
```
