# Issue #6299: [Bug]: memory leak when running GLM-4.7-W8A8

## 基本信息

- **编号**: #6299
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6299
- **创建时间**: 2026-01-27T03:16:47Z
- **关闭时间**: 2026-01-30T00:55:51Z
- **更新时间**: 2026-01-30T00:55:51Z
- **提交者**: @CatYing
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.h1002.eulerosv2r11.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          256
On-line CPU(s) list:             0-255
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 7265
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              64
Socket(s):                       4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       16 MiB (256 instances)
L1i cache:                       16 MiB (256 instances)
L2 cache:                        128 MiB (256 instances)
L3 cache:                        256 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-31
NUMA node1 CPU(s):               32-63
NUMA node2 CPU(s):               64-95
NUMA node3 CPU(s):               96-127
NUMA node4 CPU(s):               128-159
NUMA node5 CPU(s):               160-191
NUMA node6 CPU(s):               192-223
NUMA node7 CPU(s):               224-255
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.54.0
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 25.0.rc1.b010            Version: 25.0.rc1.b010                                        |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 124.9       41                0    / 0             |
| 0                         | 0000:C1:00.0  | 27          0    / 0          59718/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 122.0       40                0    / 0             |
| 0                         | 0000:C2:00.0  | 29          0    / 0          59715/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 124.0       41                0    / 0             |
| 0                         | 0000:81:00.0  | 29          0    / 0          59714/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 127.3       39                0    / 0             |
| 0                         | 0000:82:00.0  | 29          0    / 0          59716/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 128.3       45                0    / 0             |
| 0                         | 0000:01:00.0  | 30          0    / 0          59714/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 122.5       44                0    / 0             |
| 0                         | 0000:02:00.0  | 29          0    / 0          59715/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 127.4       46                0    / 0             |
| 0                         | 0000:41:00.0  | 29          0    / 0          59714/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 128.6       45                0    / 0             |
| 0                         | 0000:42:00.0  | 29          0    / 0          59715/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 1067983       |                          | 56373                   |
+===========================+===============+====================================================+
| 1       0                 | 1070524       |                          | 56373                   |
+===========================+===============+====================================================+
| 2       0                 | 1073093       |                          | 56373                   |
+===========================+===============+====================================================+
| 3       0                 | 1075396       |                          | 56373                   |
+===========================+===============+====================================================+
| 4       0                 | 1077642       |                          | 56373                   |
+===========================+===============+====================================================+
| 5       0                 | 1079652       |                          | 56374                   |
+===========================+===============+====================================================+
| 6       0                 | 1082071       |                          | 56373                   |
+===========================+===============+====================================================+
| 7       0                 | 1084428       |                          | 56373                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

```shell
export HCCL_BUFFSIZE=1024
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_USE_V1=1
export HCCL_OP_EXPANSION_MODE=AIV
export OMP_NUM_THREADS=1
export VLLM_ASCEND_ENABLE_DENSE_OPTIMIZE=1
export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_NZ=2
nohup vllm serve /data/models/GLM-4.7-W8A8/ \
        --max-model-len 131072 \
        --quantization ascend \
        --port 8899 \
        --served-model-name model \
        --reasoning-parser glm45 \
        --trust-remote-code \
        --gpu_memory_utilization 0.9 \
        --enable-auto-tool-choice  \
        --tool-call-parser glm47  \
        --async-scheduling \
        --max-num-seqs 64 \
        --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,4,8,16,32,48,64]}' \
        --tensor-parallel-size 8 \
        --enable-expert-parallel  \
        --additional-config '{"cudagraph_mode":"FULL_DECODE_ONLY","ascend_scheduler_config":{"enabled":false},"enable_multistream_moe":false,"chunked_prefill_for_mla":true,"enable_weight_nz_layout":true}' 2>&1 &
```


Memory used keeps increasing, TOP result:

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  99034 root      20   0 8374.9g 172.9g 115364 R 181.1   8.6   6209:25 VLLM::Worker_TP
  99058 root      20   0 8374.9g 172.8g 115784 R 109.6   8.6   3977:39 VLLM::Worker_TP
  99078 root      20   0 8374.9g 172.9g 114044 R 109.6   8.6   3967:10 VLLM::Worker_TP
  99098 root      20   0 8374.9g 172.8g 114352 R 109.6   8.6   3974:29 VLLM::Worker_TP
  99118 root      20   0 8374.8g 173.0g 114516 R 109.6   8.6   3968:56 VLLM::Worker_TP
  99040 root      20   0 8374.9g 173.0g 113620 R 109.3   8.6   3962:31 VLLM::Worker_TP
  99138 root      20   0 8374.9g 175.0g 113984 R 109.0   8.7   3955:42 VLLM::Worker_TP
  99159 root      20   0 8374.9g 175.6g 113776 R 109.0   8.7   3957:19 VLLM::Worker_TP
  99024 root      20   0 5057292 822612  11156 R 102.0   0.0   3506:07 VLLM::EngineCor
  99011 root      20   0 4426328 906736  15264 S   2.3   0.0  99:19.53 vllm
  95398 root      20   0 2332112 600376   8700 S   2.0   0.0 119:57.93 python



