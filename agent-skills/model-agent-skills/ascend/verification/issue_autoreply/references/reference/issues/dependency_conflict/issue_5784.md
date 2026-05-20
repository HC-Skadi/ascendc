# Issue #5784: [Bug, CI]: DeepSeek-R1-W8A8-longseq A3 multi-node run failed

## 基本信息

- **编号**: #5784
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5784
- **创建时间**: 2026-01-12T02:09:00Z
- **关闭时间**: 2026-01-15T03:10:18Z
- **更新时间**: 2026-01-15T03:10:18Z
- **提交者**: @leo-pony
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:57:00) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
BIOS Model name:                      Kunpeng 920 7285Z
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   80
Socket(s):                            4
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.1.dev2012+gded5f8aa9 (git sha: ded5f8aa9)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
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
| npu-smi 25.2.1                   Version: 25.2.1                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 162.2       36                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3112 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           37                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2887 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 167.3       36                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3123 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           36                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2884 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 159.7       37                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3110 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 161.3       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3109 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           37                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2883 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 163.4       36                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3120 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           36                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2876 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 170.4       36                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3112 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2894 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 165.4       38                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3114 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           36                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2891 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 168.7       36                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3120 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           38                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2880 / 65536         |
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
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
root@liteserver-for-vllm-ascend-00001:/data/mnj/code/vllm-ascend#
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

DeepSeek-R1-W8A8-longseq A3 multi-node run failed:
tests/e2e/nightly/multi_node/config/Qwen3-235B-W8A8-longseq.yaml
**Short error log:**
```
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:31:33 [mooncake_connector.py:160] Force freed request: chatcmpl-ef4d6818-d419-4850-9b95-a3219a353310
(EngineCore_DP0 pid=1194930) INFO 01-12 01:31:33 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-d3a162d1-e802-40fa-a4ad-a6c037446f4d
(APIServer pid=1194908) INFO:     172.22.0.188:41572 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     172.22.0.188:57484 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(EngineCore_DP0 pid=1194930) INFO 01-12 01:31:33 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-615c1b16-028d-46dd-acd5-bd85769b0fd7
(APIServer pid=1194908) INFO:     172.22.0.188:41582 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     172.22.0.188:57512 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:38814 - "GET /health HTTP/1.1" 200 OK
(EngineCore_DP0 pid=1194930) INFO 01-12 01:31:36 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-1e549298-bf5a-466f-a6d5-fc402b1807a2
(APIServer pid=1194908) INFO:     172.22.0.188:41572 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     172.22.0.188:57522 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:47762 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO 01-12 01:31:40 [loggers.py:248] Engine 000: Avg prompt throughput: 25.8 tokens/s, Avg generation throughput: 0.3 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 22.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%
(Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP1_TP2_DCP2_EP10 pid=1195469) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP1_TP5_DCP5_EP13 pid=1195643) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP1_TP0_DCP0_EP8 pid=1195353) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP4_DCP4_EP4 pid=1195121) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP5_DCP5_EP5 pid=1195179) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP7_DCP7_EP7 pid=1195295) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP2_DCP2_EP2 pid=1195005) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP6_DCP6_EP6 pid=1195237) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP1_TP3_DCP3_EP11 pid=1195527) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP1_DCP1_EP1 pid=1194953) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP1_TP1_DCP1_EP9 pid=1195411) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP3_DCP3_EP3 pid=1195063) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP0_TP0_DCP0_EP0 pid=1194945) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(Worker_PCP1_TP7_DCP7_EP15 pid=1195760) INFO 01-12 01:31:40 [mooncake_connector.py:160] Force freed request: chatcmpl-c50987d6-5c32-4e6a-8843-48eeb67dc7a5
(EngineCore_DP0 pid=1194930) INFO 01-12 01:31:41 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-d744892f-f040-4f8f-b4b8-84f0f18d3361
(APIServer pid=1194908) INFO:     172.22.0.188:41572 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     172.22.0.188:57050 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:47774 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:58242 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO 01-12 01:31:50 [loggers.py:248] Engine 000: Avg prompt throughput: 10.0 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 22.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%
(EngineCore_DP0 pid=1194930) INFO 01-12 01:31:52 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-e8863c71-5bb5-4cd1-9023-4105241967b5
(APIServer pid=1194908) INFO:     172.22.0.188:47968 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     172.22.0.188:57030 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:58258 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:56464 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO 01-12 01:32:00 [loggers.py:248] Engine 000: Avg prompt throughput: 14.6 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 22.5%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%
(Worker_PCP0_TP4_DCP4_EP4 pid=1195121) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP3_DCP3_EP11 pid=1195527) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP0_TP6_DCP6_EP6 pid=1195237) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP0_DCP0_EP8 pid=1195353) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP0_TP4_DCP4_EP4 pid=1195121) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP1_TP3_DCP3_EP11 pid=1195527) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP6_DCP6_EP6 pid=1195237) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP0_DCP0_EP8 pid=1195353) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP1_DCP1_EP1 pid=1194953) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP2_DCP2_EP10 pid=1195469) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP0_TP5_DCP5_EP5 pid=1195179) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP5_DCP5_EP13 pid=1195643) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP0_TP3_DCP3_EP3 pid=1195063) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP1_DCP1_EP1 pid=1194953) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP1_TP2_DCP2_EP10 pid=1195469) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP5_DCP5_EP5 pid=1195179) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP2_DCP2_EP2 pid=1195005) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP5_DCP5_EP13 pid=1195643) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP3_DCP3_EP3 pid=1195063) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP2_DCP2_EP2 pid=1195005) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP0_DCP0_EP0 pid=1194945) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP0_TP0_DCP0_EP0 pid=1194945) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP0_TP7_DCP7_EP7 pid=1195295) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP0_TP7_DCP7_EP7 pid=1195295) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP1_TP7_DCP7_EP15 pid=1195760) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP7_DCP7_EP15 pid=1195760) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(Worker_PCP1_TP1_DCP1_EP9 pid=1195411) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-59284fa9-1440-44a3-ba2b-94c75f5b7f9a
(Worker_PCP1_TP1_DCP1_EP9 pid=1195411) INFO 01-12 01:32:02 [mooncake_connector.py:160] Force freed request: chatcmpl-aadf9e6a-37ff-46b6-a645-93670b00c688
(EngineCore_DP0 pid=1194930) INFO 01-12 01:32:02 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-a514e74a-932e-4a44-94cd-fbcac389f9e7
(APIServer pid=1194908) INFO:     172.22.0.188:57846 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     172.22.0.188:55110 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:56472 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:55592 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO 01-12 01:32:10 [loggers.py:248] Engine 000: Avg prompt throughput: 12.1 tokens/s, Avg generation throughput: 0.1 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 22.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%
(APIServer pid=1194908) INFO:     172.22.0.212:55608 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:54436 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO 01-12 01:32:20 [loggers.py:248] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 22.1%, Prefix cache hit rate: 0.0%, External prefix cache hit rate: 0.0%
(APIServer pid=1194908) INFO:     172.22.0.212:54444 - "GET /health HTTP/1.1" 200 OK
(APIServer pid=1194908) INFO:     172.22.0.212:52298 - "GET /health HTTP/1.1" 200 OK
(Worker_PCP1_TP1_DCP1_EP9 pid=1195411) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP1_DCP1_EP9 pid=1195411) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP1_DCP1_EP9 pid=1195411) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP4_DCP4_EP4 pid=1195121) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP1_DCP1_EP1 pid=1194953) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP4_DCP4_EP4 pid=1195121) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP7_DCP7_EP7 pid=1195295) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP0_DCP0_EP0 pid=1194945) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP1_DCP1_EP1 pid=1194953) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP4_DCP4_EP4 pid=1195121) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP1_TP7_DCP7_EP15 pid=1195760) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP5_DCP5_EP13 pid=1195643) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP2_DCP2_EP10 pid=1195469) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP2_DCP2_EP2 pid=1195005) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP7_DCP7_EP7 pid=1195295) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP0_DCP0_EP8 pid=1195353) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP1_DCP1_EP1 pid=1194953) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP0_DCP0_EP0 pid=1194945) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP3_DCP3_EP11 pid=1195527) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP7_DCP7_EP15 pid=1195760) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP5_DCP5_EP13 pid=1195643) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP7_DCP7_EP7 pid=1195295) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP1_TP2_DCP2_EP10 pid=1195469) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP2_DCP2_EP2 pid=1195005) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP3_DCP3_EP11 pid=1195527) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP0_DCP0_EP8 pid=1195353) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP0_DCP0_EP0 pid=1194945) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP1_TP7_DCP7_EP15 pid=1195760) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP1_TP5_DCP5_EP13 pid=1195643) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP3_DCP3_EP3 pid=1195063) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP1_TP2_DCP2_EP10 pid=1195469) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP2_DCP2_EP2 pid=1195005) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP1_TP3_DCP3_EP11 pid=1195527) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP1_TP0_DCP0_EP8 pid=1195353) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP6_DCP6_EP6 pid=1195237) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP5_DCP5_EP5 pid=1195179) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ea199e7b-65c4-4ba5-a0b7-4504dcef6e1d
(Worker_PCP0_TP3_DCP3_EP3 pid=1195063) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP6_DCP6_EP6 pid=1195237) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP5_DCP5_EP5 pid=1195179) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-3ecaf224-111d-4a56-8101-5c6c16b33ad7
(Worker_PCP0_TP3_DCP3_EP3 pid=1195063) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP6_DCP6_EP6 pid=1195237) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(Worker_PCP0_TP5_DCP5_EP5 pid=1195179) INFO 01-12 01:32:32 [mooncake_connector.py:160] Force freed request: chatcmpl-ebf5810d-6603-440e-8933-a0f4f169c8ef
(EngineCore_DP0 pid=1194930) INFO 01-12 01:32:32 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-dc853501-8799-400c-b8c4-5760cbb79d8d
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     172.22.0.188:57082 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(EngineCore_DP0 pid=1194930) INFO 01-12 01:32:33 [mooncake_connector.py:1050] Delaying free of 1 blocks for request chatcmpl-fe9b54c0-7bf1-426e-9b70-7f61a39b1d2f
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868] Traceback (most recent call last):
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 859, in run_engine_core
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 886, in run_busy_loop
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]     self._process_engine_step()
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 919, in _process_engine_step
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 358, in step
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]     engine_core_outputs = self.scheduler.update_from_output(
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/core/sched/scheduler.py", line 1223, in update_from_output
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]     self._update_from_kv_xfer_finished(kv_connector_output)
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/core/sched/scheduler.py", line 1650, in _update_from_kv_xfer_finished
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]     assert req_id in self.requests
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1194930) ERROR 01-12 01:32:33 [core.py:868] AssertionError
(Worker_PCP0_TP4_DCP4_EP4 pid=1195121) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP0_DCP0_EP8 pid=1195353) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP1_DCP1_EP9 pid=1195411) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP0_TP7_DCP7_EP7 pid=1195295) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP0_TP0_DCP0_EP0 pid=1194945) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP0_TP3_DCP3_EP3 pid=1195063) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP0_TP6_DCP6_EP6 pid=1195237) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP3_DCP3_EP11 pid=1195527) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP4_DCP4_EP12 pid=1195585) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP0_TP2_DCP2_EP2 pid=1195005) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP0_TP1_DCP1_EP1 pid=1194953) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP0_TP5_DCP5_EP5 pid=1195179) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP2_DCP2_EP10 pid=1195469) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP7_DCP7_EP15 pid=1195760) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP5_DCP5_EP13 pid=1195643) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(Worker_PCP1_TP6_DCP6_EP14 pid=1195701) INFO 01-12 01:32:33 [multiproc_executor.py:709] Parent process exited, terminating worker
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538] AsyncLLM output_handler failed.
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538] Traceback (most recent call last):
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538]   File "/data/mnj/code/vllm/vllm/v1/engine/async_llm.py", line 490, in output_handler
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538]     outputs = await engine_core.get_output_async()
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538]   File "/data/mnj/code/vllm/vllm/v1/engine/core_client.py", line 895, in get_output_async
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538]     raise self._format_exception(outputs) from None
(APIServer pid=1194908) ERROR 01-12 01:32:33 [async_llm.py:538] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 1 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 2 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 3 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
All 3 attempts failed for /chat/completions.
Error occurred in disagg prefill proxy server - /chat/completions endpoint
Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
Traceback (most recent call last):
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 689, in _handle_completions
    instance_info = await _handle_select_instance(api, req_data,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 644, in _handle_select_instance
    response = await send_request_to_service(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 577, in send_request_to_service
    raise last_exc
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 566, in send_request_to_service
    response.raise_for_status()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500

INFO:     172.22.0.188:57572 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/applications.py", line 1139, in __call__
    await super().__call__(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/applications.py", line 107, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 736, in app
    await route.handle(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 290, in handle
    await self.app(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 119, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 105, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 385, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 284, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 521, in wrapper
    return handler_task.result()
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 870, in handle_chat_completions
    return await _handle_completions("/chat/completions", request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 689, in _handle_completions
    instance_info = await _handle_select_instance(api, req_data,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 644, in _handle_select_instance
    response = await send_request_to_service(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 577, in send_request_to_service
    raise last_exc
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 566, in send_request_to_service
    response.raise_for_status()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 1 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 2 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 3 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
All 3 attempts failed for /chat/completions.
Error occurred in disagg prefill proxy server - /chat/completions endpoint
Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
Traceback (most recent call last):
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 689, in _handle_completions
    instance_info = await _handle_select_instance(api, req_data,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 644, in _handle_select_instance
    response = await send_request_to_service(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 577, in send_request_to_service
    raise last_exc
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 566, in send_request_to_service
    response.raise_for_status()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500

INFO:     172.22.0.188:54396 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/applications.py", line 1139, in __call__
    await super().__call__(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/applications.py", line 107, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 736, in app
    await route.handle(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 290, in handle
    await self.app(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 119, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 105, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 385, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 284, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 521, in wrapper
    return handler_task.result()
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 870, in handle_chat_completions
    return await _handle_completions("/chat/completions", request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 689, in _handle_completions
    instance_info = await _handle_select_instance(api, req_data,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 644, in _handle_select_instance
    response = await send_request_to_service(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 577, in send_request_to_service
    raise last_exc
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 566, in send_request_to_service
    response.raise_for_status()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 1 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 2 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 3 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
All 3 attempts failed for /chat/completions.
Error occurred in disagg prefill proxy server - /chat/completions endpoint
Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
Traceback (most recent call last):
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 689, in _handle_completions
    instance_info = await _handle_select_instance(api, req_data,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 644, in _handle_select_instance
    response = await send_request_to_service(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 577, in send_request_to_service
    raise last_exc
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 566, in send_request_to_service
    response.raise_for_status()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500

INFO:     172.22.0.188:54400 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 409, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/applications.py", line 1139, in __call__
    await super().__call__(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/applications.py", line 107, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/errors.py", line 186, in __call__
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
    await self.app(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 716, in __call__
    await self.middleware_stack(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 736, in app
    await route.handle(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/routing.py", line 290, in handle
    await self.app(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 119, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    raise exc
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 105, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 385, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/fastapi/routing.py", line 284, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 521, in wrapper
    return handler_task.result()
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 870, in handle_chat_completions
    return await _handle_completions("/chat/completions", request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 689, in _handle_completions
    instance_info = await _handle_select_instance(api, req_data,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 644, in _handle_select_instance
    response = await send_request_to_service(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 577, in send_request_to_service
    raise last_exc
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 566, in send_request_to_service
    response.raise_for_status()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 1 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 2 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
(APIServer pid=1194908) INFO:     172.22.0.188:49602 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
Attempt 3 failed for /chat/completions: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
All 3 attempts failed for /chat/completions.
Error occurred in disagg prefill proxy server - /chat/completions endpoint
Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
Traceback (most recent call last):
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 689, in _handle_completions
    instance_info = await _handle_select_instance(api, req_data,
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 644, in _handle_select_instance
    response = await send_request_to_service(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 577, in send_request_to_service
    raise last_exc
  File "/data/mnj/code/vllm-ascend/examples/disaggregated_prefill_v1/load_balance_proxy_server_example.py", line 566, in send_request_to_service
    response.raise_for_status()
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/httpx/_models.py", line 829, in raise_for_status
    raise HTTPStatusError(message, request=request, response=self)
httpx.HTTPStatusError: Server error '500 Internal Server Error' for url 'http://172.22.0.188:8080/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500

INFO:     172.22.0.188:54416 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
```

**Detail log file see attach.**

[plog-1194945_20260112013238956.log](https://github.com/user-attachments/files/24556450/plog-1194945_20260112013238956.log)
[vllm_server.log](https://github.com/user-attachments/files/24556449/vllm_server.log)
