# Issue #2523: [Bug]: Deepseek runs failed with ep>=16 for graph mode

## 基本信息

- **编号**: #2523
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2523
- **创建时间**: 2025-08-25T08:06:40Z
- **关闭时间**: 2025-08-27T01:30:26Z
- **更新时间**: 2025-12-03T01:58:05Z
- **提交者**: @Potabk
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
python collect_env.py 
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 09:30:19) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
Model:                                0
Thread(s) per core:                   1
Core(s) per cluster:                  80
Socket(s):                            -
Cluster(s):                           4
Stepping:                             0x0
Frequency boost:                      disabled
CPU max MHz:                          3000.0000
CPU min MHz:                          400.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                            20 MiB (320 instances)
L1i cache:                            20 MiB (320 instances)
L2 cache:                             400 MiB (320 instances)
L3 cache:                             560 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-39
NUMA node1 CPU(s):                    40-79
NUMA node2 CPU(s):                    80-119
NUMA node3 CPU(s):                    120-159
NUMA node4 CPU(s):                    160-199
NUMA node5 CPU(s):                    200-239
NUMA node6 CPU(s):                    240-279
NUMA node7 CPU(s):                    280-319
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
[pip3] pyzmq==27.0.0
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.55.2
[conda] Could not collect
vLLM Version: 0.10.1.dev791+g941f56858 (git sha: 941f56858)
vLLM Ascend Version: 0.1.dev103+g7bec1a9b9 (git sha: 7bec1a9b9)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=true
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3.7               Version: 24.1.rc3.7                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 174.8       39                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          4197 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           37                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3253 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 184.4       37                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3472 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3259 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 177.3       37                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3469 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           36                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3262 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 189.4       37                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3468 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           36                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3266 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 175.4       39                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3480 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           37                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3252 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 176.9       38                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3479 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3188 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 177.7       37                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3401 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           36                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 184.2       36                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3400 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           38                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 602983        | /usr/local/pyth          | 117                     |
| 0       0                 | 601869        | /usr/local/pyth          | 117                     |
| 0       0                 | 602241        | /usr/local/pyth          | 117                     |
| 0       0                 | 600022        | /usr/local/pyth          | 117                     |
| 0       0                 | 599746        | /usr/local/pyth          | 117                     |
| 0       0                 | 601498        | /usr/local/pyth          | 117                     |
| 0       0                 | 601127        | /usr/local/pyth          | 117                     |
| 0       0                 | 599876        | /usr/local/pyth          | 117                     |
| 0       1                 | 599876        | /usr/local/pyth          | 117                     |
+===========================+===============+====================================================+
| 1       0                 | 600022        | /usr/local/pyth          | 117                     |
| 1       1                 | 600385        | /usr/local/pyth          | 117                     |
+===========================+===============+====================================================+
| 2       0                 | 600756        | /usr/local/pyth          | 117                     |
| 2       1                 | 601127        | /usr/local/pyth          | 117                     |
+===========================+===============+====================================================+
| 3       0                 | 601498        | /usr/local/pyth          | 117                     |
| 3       1                 | 601869        | /usr/local/pyth          | 117                     |
+===========================+===============+====================================================+
| 4       0                 | 602241        | /usr/local/pyth          | 117                     |
| 4       1                 | 602612        | /usr/local/pyth          | 117                     |
+===========================+===============+====================================================+
| 5       0                 | 602983        | /usr/local/pyth          | 117                     |
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

vllm version: main(https://github.com/vllm-project/vllm/commit/2da02dd0d8879ee5085e33979698468b3ea68c56)
vllm-ascend: main(https://github.com/vllm-project/vllm-ascend/commit/0f81e032f04b72f4dd0c7fefd62b7220942c545a)

test script:

```bash
nic_name="enp23s0f3"
local_ip="172.22.0.212"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export HCCL_BUFFSIZE=512

vllm serve /home/cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-W8A8 \
--host 0.0.0.0 \
--port 8004 \
--tensor-parallel-size 16 \
--seed 1024 \
--served-model-name deepseek_v3 \
--enable-expert-parallel \
--max-num-seqs 16 \
--max-model-len 8192 \
--quantization ascend \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.9 \
--additional-config '{"ascend_scheduler_config":{"enabled":false},"torchair_graph_config":{"enabled":true}}'
```
```bash
curl http://localhost:8004/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "deepseek_v3",
        "prompt": "tell me how to sleep well",
        "max_tokens": 100,
        "temperature": 0
    }'
```

the error log shows that when processing reqs, the operator `npu_moe_distribute_combine_v2` has  Illegal input shape `Value [input assist_info_for_combine shape] for Op [MoeDistributeCombineV2_58] is invalid. Reason: contains negative or zero dimension`
