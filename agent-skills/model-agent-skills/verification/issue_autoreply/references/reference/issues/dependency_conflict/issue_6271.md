# Issue #6271: [Bug]: vllm-ascend v0.13.0rc2 下载openeuler镜像，Qwen3VL-8B-Instruct拉服务报错'aclOpExecutor' 未定义

## 基本信息

- **编号**: #6271
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6271
- **创建时间**: 2026-01-26T09:05:04Z
- **关闭时间**: 2026-01-26T09:20:39Z
- **更新时间**: 2026-01-26T09:20:39Z
- **提交者**: @HrDrLi
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-99.oe2403sp2)
Clang version: 17.0.6 ( 17.0.6-45.oe2403sp2)
CMake version: version 4.2.1
Libc version: glibc-2.38

Python version: 3.11.14 (main, Jan 21 2026, 07:06:26) [GCC 12.3.1 (openEuler 12.3.1-99.oe2403sp2)] (64-bit runtime)
Python platform: Linux-5.10.0-153.56.0.134.oe2203sp2.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250 To be filled by O.E.M. CPU @ 2.6GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
Stepping:                           0x1
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0.post1
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.6
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc2

ENV Variables:
ASCEND_TOOLKIT_LATEST_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/cann-8.5.0
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/cann-8.5.0/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/cann-8.5.0/lib64:/usr/local/Ascend/cann-8.5.0/lib64/plugin/opskernel:/usr/local/Ascend/cann-8.5.0/lib64/plugin/nnengine:/usr/local/Ascend/cann-8.5.0/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64/plugin:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/cann-8.5.0
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/cann-8.5.0
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 94.8        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3407 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 90.5        34                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 90.6        33                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 98.8        35                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 139.7       45                0    / 0             |
| 0                         | 0000:01:00.0  | 25          0    / 0          21784/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 95.8        37                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 97.8        38                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 90.8        39                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3413 / 65536         |
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
| 4       0                 | 1601114       | python                   | 18429                   |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.5.0
innerversion=V100R001C25SPC001B232
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/cann-8.5.0


</details>


### 🐛 Describe the bug

docker run -itd  \
--privileged=true \
--name vllm-ascend-v0.13.0rc2-OpenEuler --network=host --pid=host --detach=true --shm-size=64g \
--device=/dev/davinci0 --device=/dev/davinci1 --device=/dev/davinci2 \
--device=/dev/davinci3 --device=/dev/davinci4 --device=/dev/davinci5 \
--device=/dev/davinci6 --device=/dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/sbin:/usr/local/sbin \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
-v /opt/data/usr/:/data/ \
-p $PORT:8000 \
-v /home/usr:/home/usr \
quay.io/ascend/vllm-ascend:v0.13.0rc2-openeuler /bin/bash

docker exec -it vllm-ascend-v0.13.0rc2-OpenEuler bash

export ASCEND_RT_VISIBLE_DEVICES=7
source /usr/local/Ascend/cann-8.5.0/set_env.sh
vllm serve ./model/Qwen3-VL-8B-Instruct \
  --host 0.0.0.0 \
  --port 33030 \
  --tensor-parallel-size 1 \
  --max-num-seqs 4 \
  --max-num-batched-tokens 4096 \
  --trust-remote-code \
  --no-enable-prefix-caching \
  --gpu-memory-utilization 0.85 \
  --max-model-len 32768 \
  --served-model-name qwen3-vl-8b

Error msg:

[qwen3-vl-8b.log](https://github.com/user-attachments/files/24856536/qwen3-vl-8b.log)
