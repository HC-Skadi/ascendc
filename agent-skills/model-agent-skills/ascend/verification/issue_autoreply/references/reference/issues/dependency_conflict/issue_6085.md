# Issue #6085: [Bug]: vllm-ascend:v0.13.0rc1运行Glm-4.7-W8A8时不能同时开启FULL_DECODE_ONLY和mtp投机，报错NotImplementedError

## 基本信息

- **编号**: #6085
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6085
- **创建时间**: 2026-01-21T07:29:37Z
- **关闭时间**: 2026-01-21T09:19:52Z
- **更新时间**: 2026-01-31T00:40:17Z
- **提交者**: @jnbgvcd
- **评论数**: 2

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
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

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
| 0     Ascend910           | OK            | 164.4       48                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          26690/ 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           47                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          26457/ 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 169.8       49                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          26689/ 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           48                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          26460/ 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 166.8       48                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          26693/ 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           49                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          26455/ 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 166.6       46                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          26688/ 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           49                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          26460/ 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 170.5       49                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          26711/ 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           51                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          26455/ 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 175.5       49                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          26692/ 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           49                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          26453/ 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 167.8       49                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          26689/ 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           52                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          26456/ 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 162.2       47                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          26690/ 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           46                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          26455/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 3742689       |                          | 23631                   |
| 0       1                 | 3743331       |                          | 23631                   |
+===========================+===============+====================================================+
| 1       0                 | 3743919       |                          | 23631                   |
| 1       1                 | 3744594       |                          | 23631                   |
+===========================+===============+====================================================+
| 2       0                 | 3745463       |                          | 23631                   |
| 2       1                 | 3746268       |                          | 23631                   |
+===========================+===============+====================================================+
| 3       0                 | 3746507       |                          | 23631                   |
| 3       1                 | 3747147       |                          | 23631                   |
+===========================+===============+====================================================+
| 4       0                 | 3742688       |                          | 23631                   |
| 4       1                 | 3743330       |                          | 23631                   |
+===========================+===============+====================================================+
| 5       0                 | 3743929       |                          | 23631                   |
| 5       1                 | 3744596       |                          | 23631                   |
+===========================+===============+====================================================+
| 6       0                 | 3745464       |                          | 23631                   |
| 6       1                 | 3746269       |                          | 23631                   |
+===========================+===============+====================================================+
| 7       0                 | 3746511       |                          | 23631                   |
| 7       1                 | 3747148       |                          | 23631                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux

<!-- Failed to upload "log.txt" -->

```



</details>


### 🐛 Describe the bug

FULL_DECODE_ONLY与mtp投机单独开启都没有问题，但是不能同时开启，报错“NotImplementedError”
启动命令：
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
export OMP_NUM_THREADS=64
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_USE_V1=1
export HCCL_DETERMINISTIC="true"
export HCCL_OP_EXPANSION_MODE=AIV
export HCCL_BUFFSIZE=1024
export OMP_NUM_THREADS=1
export VLLM_ASCEND_ENABLE_DENSE_OPTIMIZE=1
export TASK_QUEUE_ENABLE=1
export VLLM_ASCEND_ENABLE_NZ=2

vllm serve /mnt/paas/kubernetes/kubelet/GLM-4.7-w8a8  \
--host 0.0.0.0  \
--port 9000  \
--max-num-seqs 16  \
--trust-remote-code  \
--quantization ascend  \
--gpu_memory_utilization 0.9   \
--data-parallel-size 2  \
--tensor-parallel-size 8  \
--enable-expert-parallel  \
--tool-parser-plugin /mnt/paas/kubernetes/kubelet/glm47_moe_tool_parser.py  \
--tool-call-parser glm47  \
--reasoning-parser glm45  \
--enable-auto-tool-choice  \
--served-model-name GLM-4.7  \
--max-model-len 202752  \
--no-enable-prefix-caching  \
--speculative-config.method mtp  \
--speculative-config.num_speculative_tokens 1  \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [1,4,8,16,32,48,64]}'   \
--additional-config '{"cudagraph_mode":"FULL_DECODE_ONLY","ascend_scheduler_config":{"enabled":false},"enable_multistream_moe":false,"chunked_prefill_for_mla":true,"enable_weight_nz_layout":true}'   \
--async-scheduling  \


日志如下：
(Worker_DP1_TP4_EP12 pid=162123) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 272, in build_for_graph_capture
(Worker_DP0_TP5_EP5 pid=162162) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP0_EP8 pid=161983) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     attn_metadata_full_attention = builder.build_for_graph_capture(
(Worker_DP1_TP3_EP11 pid=162081) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 272, in build_for_graph_capture
(Worker_DP1_TP7_EP15 pid=162249) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP1_TP6_EP14 pid=162209) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._capture_model()
(Worker_DP0_TP2_EP2 pid=162036) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._capture_model()
(Worker_DP0_TP4_EP4 pid=162120) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 272, in build_for_graph_capture
(Worker_DP0_TP7_EP7 pid=162246) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP4_EP12 pid=162123) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP0_TP5_EP5 pid=162162) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP0_EP8 pid=161983) ERROR 01-21 02:34:16 [multiproc_executor.py:824]                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP11 pid=162081) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP1_TP7_EP15 pid=162249) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP6_EP14 pid=162209) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3037, in _capture_model
(Worker_DP0_TP2_EP2 pid=162036) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3037, in _capture_model
(Worker_DP0_TP4_EP4 pid=162120) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP1_TP4_EP12 pid=162123) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP0_EP8 pid=161983) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 272, in build_for_graph_capture
(Worker_DP1_TP3_EP11 pid=162081) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP7_EP15 pid=162249) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP6_EP14 pid=162209) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._capture_aclgraphs(
(Worker_DP0_TP2_EP2 pid=162036) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._capture_aclgraphs(
(Worker_DP0_TP4_EP4 pid=162120) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP4_EP12 pid=162123) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP0_EP8 pid=161983) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP1_TP3_EP11 pid=162081) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2972, in _capture_aclgraphs
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2972, in _capture_aclgraphs
(Worker_DP0_TP4_EP4 pid=162120) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP0_EP8 pid=161983) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._dummy_run(num_tokens,
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._dummy_run(num_tokens,
(Worker_DP1_TP0_EP8 pid=161983) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2068, in _dummy_run
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2068, in _dummy_run
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     attn_metadata = self._build_dummy_attn_metadata(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     attn_metadata = self._build_dummy_attn_metadata(
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1920, in _build_dummy_attn_metadata
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1920, in _build_dummy_attn_metadata
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     attn_metadata_full_attention = builder.build_for_graph_capture(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     attn_metadata_full_attention = builder.build_for_graph_capture(
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 272, in build_for_graph_capture
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 272, in build_for_graph_capture
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP1_TP2_EP10 pid=162039) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 371, in compile_or_warm_up_model
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self.model_runner.capture_model()
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3056, in capture_model
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._capture_model()
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3037, in _capture_model
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._capture_aclgraphs(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2972, in _capture_aclgraphs
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     self._dummy_run(num_tokens,
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2068, in _dummy_run
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     attn_metadata = self._build_dummy_attn_metadata(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1920, in _build_dummy_attn_metadata
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     attn_metadata_full_attention = builder.build_for_graph_capture(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 272, in build_for_graph_capture
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824]     raise NotImplementedError(
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824] NotImplementedError: Currently we only support building dummy metadata for DecodeOnly state
(Worker_DP0_TP6_EP6 pid=162204) ERROR 01-21 02:34:16 [multiproc_executor.py:824] 
(EngineCore_DP1 pid=161960) ERROR 01-21 02:34:16 [core.py:866] EngineCore failed to start.
(EngineCore_DP0 pid=161945) ERROR 01-21 02:34:16 [core.py:866] EngineCore failed to start.

