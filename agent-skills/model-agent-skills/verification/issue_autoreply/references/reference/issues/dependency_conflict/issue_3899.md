# Issue #3899: [Bug]: Inference with `W8A8` needs more NPU memory than `bfloat16`

## 基本信息

- **编号**: #3899
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3899
- **创建时间**: 2025-10-30T08:41:52Z
- **关闭时间**: 2025-12-23T08:45:13Z
- **更新时间**: 2025-12-23T08:45:13Z
- **提交者**: @zhoux77899
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 24.04.3 LTS (aarch64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.39

Python version: 3.11.10 (main, Oct 25 2025, 16:55:00) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.39

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         -
BIOS Model name:                    Kunpeng 920 7285Z To be filled by O.E.M. CPU @ 3.0GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        3000.0000
CPU min MHz:                        400.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                          20 MiB (320 instances)
L1i cache:                          20 MiB (320 instances)
L2 cache:                           400 MiB (320 instances)
L3 cache:                           560 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-79
NUMA node1 CPU(s):                  80-159
NUMA node2 CPU(s):                  160-239
NUMA node3 CPU(s):                  240-319
NUMA node4 CPU(s):                  320-399
NUMA node5 CPU(s):                  400-479
NUMA node6 CPU(s):                  480-559
NUMA node7 CPU(s):                  560-639
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
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1.dev20251014
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.1rc5.dev34+g48eb8eba5 (git sha: 48eb8eba5)
vLLM Ascend Version: 0.9.0rc3.dev851+gd603520ff.d20251029 (git sha: d603520ff, date: 20251029)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/lib::/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/lib::/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib
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
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 165.4       37                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3173 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 162.3       37                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3168 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 160.3       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3166 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           36                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 165.6       37                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3166 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           39                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 170.9       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3163 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           37                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2880 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 162.2       37                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3161 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2885 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 164.1       36                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3163 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           37                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2882 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 164.5       39                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3152 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           38                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2893 / 65536         |
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
version=8.3.RC1
innerversion=V100R001C23SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

I use the following config to serve a model, and test the performance with inputs of `32K` and outputs of `4K`

```yaml
# `bfloat16`
# model: Qwen3-235B-A22B
# `w8a8`
# model: Qwen3-235B-A22B-W8A8
# quantization: ascend
served-model-name: qwen3_moe
tensor-parallel-size: 8
data-parallel-size: 2
data-parallel-size-local: 2
data-parallel-rpc-port: 4567
enable-expert-parallel: true
trust-remote-code: true
enforce-eager: false
no-enable-prefix-caching: true
async-scheduling: false
max_num_seqs: 8
max-num-batched-tokens: 16384
max-model-len: 40960
gpu-memory-utilization: 0.95
host: 127.0.0.1
port: 38713
rope-scaling: '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}'
additional-config: '{"ascend_scheduler_config":{"enabled":false}}'
compilation-config: '{"cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[1,2,4,8]}'
```

But I get the OOM error in `W8A8` quantized model inference.

```
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703]     global_input_tokens_local_experts_indices = torch.repeat_interleave(
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703]                                                 ^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is SelfAttentionOperation.
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703] [ERROR] 2025-10-30-16:22:05 (PID:1355611, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703] [PID: 1355611] 2025-10-30-16:22:05.620.760 Memory_Allocation_Failure(EL0004): Failed to allocate memory.
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703]         Possible Cause: Available memory is insufficient.
[1;36m(Worker_DP0_TP0_EP0 pid=1355611)[0;0m ERROR 10-30 16:22:05 [multiproc_executor.py:703]         Solution: Close applications not in use.
```
