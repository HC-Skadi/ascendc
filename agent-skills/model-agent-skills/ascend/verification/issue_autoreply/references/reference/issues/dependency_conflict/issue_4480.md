# Issue #4480: [Bug]: accuarcy test issues when upgrade to vllm 0.11.2

## 基本信息

- **编号**: #4480
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4480
- **创建时间**: 2025-11-27T02:31:08Z
- **关闭时间**: 2025-12-15T04:05:46Z
- **更新时间**: 2025-12-15T04:05:46Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 1

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

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
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
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.1.2
[pip3] torch==2.7.1
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.11.2
vLLM Ascend Version: 0.11.0rc1.dev393+g3c9d947d7.d20251124 (git sha: 3c9d947d7, date: 20251124)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
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
| npu-smi 24.1.rc3.7               Version: 24.1.rc3.7                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 174.3       37                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3440 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3205 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 184.0       37                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3432 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3208 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 176.8       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3443 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           36                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3196 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 188.1       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3433 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           36                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3210 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 175.2       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3439 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           36                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3205 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 177.1       36                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3433 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3205 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 176.9       35                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3452 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           34                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3194 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 183.1       35                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3447 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           37                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          3192 / 65536         |
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

details : **https://github.com/vllm-project/vllm-ascend/actions/runs/19710770746/job/56470464626**

1. Qwen/Qwen3-30B-A3B accuracy test lower
 ```
gsm8k | exact_match,strict-match: ground_truth=0.89 | measured=0.4344 | success=❌
gsm8k | exact_match,flexible-extract: ground_truth=0.85 | measured=0.3177 | success=❌
ceval-valid | acc,none: ground_truth=0.84 | measured=0.6716 | **success=❌**
```

2. vllm-ascend/Qwen3-30B-A3B-W8A8 accuracy test lower 
```
gsm8k | exact_match,strict-match: ground_truth=0.9 | measured=0.4223 | success=❌
gsm8k | exact_match,flexible-extract: ground_truth=0.8 | measured=0.2707 | success=❌
```

<details>
<summary> 3. Qwen/Qwen2.5-omini start failed </summary>

```text
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] WorkerProc hit an exception.
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/worker/worker_base.py", line 367, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 290, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2291, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     max_query_len) = (self._prepare_inputs(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1624, in _prepare_inputs
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self._execute_mm_encoder(scheduler_output)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1082, in _execute_mm_encoder
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     curr_group_outputs = self.model.embed_multimodal(**mm_kwargs_group)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1496, in embed_multimodal
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeddings = self._process_image_input(multimodal_input)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1375, in _process_image_input
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen2_5_vl_without_padding.py", line 454, in forward
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     rotary_pos_emb = self.rot_pos_emb(grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 448, in rot_pos_emb
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     pos_ids = [
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]               ^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 449, in <listcomp>
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self.rot_pos_ids(h, w, self.spatial_merge_size)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 422, in rot_pos_ids
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     hpos_ids = np.broadcast_to(np.arange(h).reshape(h, 1), (h, w))
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                                ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_tensor.py", line 1225, in __array__
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.numpy()
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] TypeError: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/worker/worker_base.py", line 367, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 290, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2291, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     max_query_len) = (self._prepare_inputs(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1624, in _prepare_inputs
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self._execute_mm_encoder(scheduler_output)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1082, in _execute_mm_encoder
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     curr_group_outputs = self.model.embed_multimodal(**mm_kwargs_group)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1496, in embed_multimodal
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeddings = self._process_image_input(multimodal_input)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1375, in _process_image_input
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen2_5_vl_without_padding.py", line 454, in forward
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     rotary_pos_emb = self.rot_pos_emb(grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 448, in rot_pos_emb
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     pos_ids = [
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]               ^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 449, in <listcomp>
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self.rot_pos_ids(h, w, self.spatial_merge_size)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 422, in rot_pos_ids
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     hpos_ids = np.broadcast_to(np.arange(h).reshape(h, 1), (h, w))
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                                ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_tensor.py", line 1225, in __array__
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.numpy()
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] TypeError: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.


```
</details>




<details>
<summary> 4. Qwen/Qwen3-VL-30B-A3B-Instruct start failed </summary>

```text
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] WorkerProc hit an exception.
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/worker/worker_base.py", line 367, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 290, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2291, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     max_query_len) = (self._prepare_inputs(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1624, in _prepare_inputs
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self._execute_mm_encoder(scheduler_output)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1082, in _execute_mm_encoder
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     curr_group_outputs = self.model.embed_multimodal(**mm_kwargs_group)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1496, in embed_multimodal
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeddings = self._process_image_input(multimodal_input)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1375, in _process_image_input
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen2_5_vl_without_padding.py", line 454, in forward
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     rotary_pos_emb = self.rot_pos_emb(grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 448, in rot_pos_emb
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     pos_ids = [
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]               ^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 449, in <listcomp>
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self.rot_pos_ids(h, w, self.spatial_merge_size)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 422, in rot_pos_ids
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     hpos_ids = np.broadcast_to(np.arange(h).reshape(h, 1), (h, w))
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                                ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_tensor.py", line 1225, in __array__
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.numpy()
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] TypeError: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/worker/worker_base.py", line 367, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 290, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2291, in execute_model
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     max_query_len) = (self._prepare_inputs(scheduler_output,
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1624, in _prepare_inputs
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self._execute_mm_encoder(scheduler_output)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1082, in _execute_mm_encoder
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     curr_group_outputs = self.model.embed_multimodal(**mm_kwargs_group)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1496, in embed_multimodal
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeddings = self._process_image_input(multimodal_input)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 1375, in _process_image_input
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen2_5_vl_without_padding.py", line 454, in forward
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     rotary_pos_emb = self.rot_pos_emb(grid_thw)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 448, in rot_pos_emb
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     pos_ids = [
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]               ^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 449, in <listcomp>
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     self.rot_pos_ids(h, w, self.spatial_merge_size)
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_vl.py", line 422, in rot_pos_ids
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     hpos_ids = np.broadcast_to(np.arange(h).reshape(h, 1), (h, w))
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]                                ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_tensor.py", line 1225, in __array__
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]     return self.numpy()
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^
(Worker_TP0_EP0 pid=5925) ERROR 11-26 17:09:24 [multiproc_executor.py:815] TypeError: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.


```
</details>

