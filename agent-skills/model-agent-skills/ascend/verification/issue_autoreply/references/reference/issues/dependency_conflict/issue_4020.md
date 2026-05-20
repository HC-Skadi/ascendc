# Issue #4020: [Bug]: When we adapt Qwen3-Next to run torch_npu.npu_fused_infer_attention_score in CANN 8.3, we get a bug says `queryD`, `keyD` and `valueD` are incompatible.

## 基本信息

- **编号**: #4020
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4020
- **创建时间**: 2025-11-06T03:25:21Z
- **关闭时间**: 2025-11-07T02:43:49Z
- **更新时间**: 2025-11-07T05:57:36Z
- **提交者**: @drslark
- **评论数**: 2

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

Python version: 3.11.10 (main, Nov  1 2025, 16:35:11) [GCC 13.3.0] (64-bit runtime)
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
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.1rc3
vLLM Ascend Version: 0.11.0rc1.dev274+gab9c54b0a (git sha: ab9c54b0a)

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
| 0     Ascend910           | OK            | 166.1       37                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3160 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2872 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 163.0       37                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3142 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 190.9       37                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          46223/ 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           38                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          45936/ 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 198.4       37                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          46223/ 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           40                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          45938/ 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 169.8       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          2914 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           38                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2869 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 163.0       37                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          2914 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           37                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2870 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 165.4       37                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          2902 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           38                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2882 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 226.6       40                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3150 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           44                0    / 0             |
| 1     15                  | 0000:83:00.0  | 44          0    / 0          60504/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| 2       0                 | 3238305       |                          | 42325                   |
| 2       1                 | 3238308       |                          | 42325                   |
+===========================+===============+====================================================+
| 3       0                 | 3238313       |                          | 42325                   |
| 3       1                 | 3238314       |                          | 42325                   |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| 7       1                 | 2718348       |                          | 57683                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux

```

</details>


### 🐛 Describe the bug

When we run Qwen3-Next and make it to run into `_forward_v1_style` in https://github.com/vllm-project/vllm-ascend/blob/main/vllm_ascend/attention/attention_v1.py.

We get a bug:

```text
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699] WorkerProc hit an exception.
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699] Traceback (most recent call last):
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 694, in worker_busy_loop
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     output = func(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 353, in execute_model
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 279, in execute_model
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return func(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2326, in execute_model
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1880, in _generate_process_reqs_hidden_states
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     hidden_states = self.model(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]                     ^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 1237, in forward
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     hidden_states = self.model(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]                     ^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 261, in __call__
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self.forward(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 991, in forward
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     hidden_states, residual = layer(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]                               ^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 881, in forward
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     self.self_attn(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_next.py", line 769, in forward
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     attn_output = self.attn(q, k, v)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]                   ^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/attention/layer.py", line 370, in forward
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     torch.ops.vllm.unified_attention_with_output(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm/vllm/attention/layer.py", line 935, in unified_attention_with_output
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     self.impl.forward(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 1201, in forward
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     intermediate_output = self._forward_v1_style(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]                           ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 707, in _forward_v1_style
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     output, _ = torch_npu.npu_fused_infer_attention_score(
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]     return self._op(*args, **(kwargs or {}))
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699] RuntimeError: npu_fused_infer_attention_score_symint:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:208 NPU function error: call aclnnFusedInferAttentionScoreV3 failed, error code is 561002
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699] [ERROR] 2025-11-06-11:21:05 (PID:948496, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699] E89999: Inner Error!
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699] E89999[PID: 948496] 2025-11-06-11:21:05.612.749 (E89999):  When layout is TND, queryD(256), keyD(256) and valueD(256) must be same equal 192/128/64, or queryD and keyD equal 192 and valueD equal 128.[FUNC:CheckInputShapeWhenLayoutIsTND][FILE:prompt_flash_attention_tiling.cpp][LINE:3701]
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]         TraceBack (most recent call last):
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]        tiling process fo ifa failed[FUNC:TilingFusedInferAttentionScore][FILE:fused_infer_attention_score_tiling.cpp][LINE:1845]
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]        FusedInferAttentionScore do tiling failed, ret is -1.
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]        Check NnopbaseExecutorDoTiling(executor) failed
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]        Check NnopbaseExecutorMatchCache(executor) failed
(Worker_TP0 pid=948496) ERROR 11-06 11:21:05 [multiproc_executor.py:699]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
```
