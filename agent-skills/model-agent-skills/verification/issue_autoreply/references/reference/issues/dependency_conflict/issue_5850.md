# Issue #5850: [Bug, CI]: DeepSeek-V3_2-W8A8-A3-dual-nodes.yaml failed cos.view shape '[19, -1]' is invalid for input of size 640

## 基本信息

- **编号**: #5850
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5850
- **创建时间**: 2026-01-13T08:24:45Z
- **关闭时间**: 2026-01-27T09:36:47Z
- **更新时间**: 2026-01-27T09:36:47Z
- **提交者**: @leo-pony
- **评论数**: 1

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
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.2.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.1.dev2038+g308beddd8 (git sha: 308beddd8)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
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
| 0     Ascend910           | OK            | 161.8       36                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3122 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2891 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 167.2       36                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3124 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           36                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2888 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 159.7       37                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3117 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           36                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 161.4       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3109 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           36                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2890 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 163.9       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3113 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           36                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2876 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 170.9       36                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3106 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2888 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 164.7       38                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3108 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           37                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 169.0       37                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3120 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           38                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2879 / 65536         |
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
```

</details>


### 🐛 Describe the bug

 run failed, error information:
```
cos = cos.view(num_tokens, -1)
(Worker_DP0_TP0_EP0 pid=12235) ERROR 01-13 07:50:04 [multiproc_executor.py:824]   File "/data/mnj/code/vllm-ascend/vllm_ascend/attention/sfa_v1.py", line 788, in forward
(Worker_DP0_TP6_EP6 pid=12816) ERROR 01-13 07:50:04 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP0_TP2_EP2 pid=12405) ERROR 01-13 07:50:04 [multiproc_executor.py:824] RuntimeError: shape '[19, -1]' is invalid for input of size 640
```

Detail log:
[master_and_slave_node_logs.txt](https://github.com/user-attachments/files/24583511/master_and_slave_node_logs.txt)

Reproduce commands:
```
test_name: "test DeepSeek-V3.2-W8A8 on A3"
model: "vllm-ascend/DeepSeek-V3.2-W8A8"
num_nodes: 2
npu_per_node: 16
env_common:
  HCCL_OP_EXPANSION_MODE: "AIV"
  VLLM_USE_MODELSCOPE: true
  HCCL_BUFFSIZE: 1024
  SERVER_PORT: 8080
  OMP_PROC_BIND: false
  OMP_NUM_THREADS: 1
  PYTORCH_NPU_ALLOC_CONF: "expandable_segments:True"
  VLLM_ASCEND_ENABLE_FLASHCOMM1: 1
  ASCEND_A3_EBA_ENABLE: 1


deployment:
  -
    server_cmd: >
      vllm serve vllm-ascend/DeepSeek-V3.2-W8A8
      --host 0.0.0.0
      --port $SERVER_PORT
      --data-parallel-size 4
      --data-parallel-size-local 2
      --data-parallel-address $LOCAL_IP
      --data-parallel-rpc-port 13399
      --tensor-parallel-size 8
      --quantization ascend
      --seed 1024
      --enable-expert-parallel
      --max-num-seqs 16
      --max-model-len 8192
      --max-num-batched-tokens 4096
      --no-enable-prefix-caching
      --gpu-memory-utilization 0.85
      --trust-remote-code
      --speculative-config '{"num_speculative_tokens":2,"method":"deepseek_mtp"}'
      --tokenizer-mode deepseek_v32
      --reasoning-parser deepseek_v3
      --api-server-count 4

  -
    server_cmd: >
      vllm serve vllm-ascend/DeepSeek-V3.2-W8A8
      --headless
      --data-parallel-size 4
      --data-parallel-rpc-port 13399
      --data-parallel-size-local 2
      --data-parallel-start-rank 2
      --data-parallel-address $MASTER_IP
      --tensor-parallel-size 8
      --quantization ascend
      --seed 1024
      --enable-expert-parallel
      --max-num-seqs 16
      --max-model-len 8192
      --max-num-batched-tokens 4096
      --no-enable-prefix-caching
      --gpu-memory-utilization 0.85
      --trust-remote-code
      --speculative-config '{"num_speculative_tokens":2,"method":"deepseek_mtp"}'
      --tokenizer-mode deepseek_v32
      --reasoning-parser deepseek_v3
benchmarks:
  perf:
    case_type: performance
    dataset_path: vllm-ascend/GSM8K-in3500-bs2800
    request_conf: vllm_api_stream_chat
    dataset_conf: gsm8k/gsm8k_gen_0_shot_cot_str_perf
    num_prompts: 512
    max_out_len: 3000
    batch_size: 512
    request_rate: 11.2
    baseline: 594.915
    threshold: 0.97
  acc:
    case_type: accuracy
    dataset_path: vllm-ascend/gsm8k-lite
    request_conf: vllm_api_general_chat
    dataset_conf: gsm8k/gsm8k_gen_0_shot_cot_chat_prompt
    max_out_len: 4096
    batch_size: 64
    baseline: 95
    threshold: 5

```
