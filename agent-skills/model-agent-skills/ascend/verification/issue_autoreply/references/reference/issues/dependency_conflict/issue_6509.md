# Issue #6509: [Bug]: eagle3 speculative method  with graph_mode FULL_DECODE_ONLY  failed  in 0.14.0RC1  AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'

## 基本信息

- **编号**: #6509
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6509
- **创建时间**: 2026-02-03T11:20:38Z
- **关闭时间**: 2026-02-10T05:49:10Z
- **更新时间**: 2026-02-28T03:52:23Z
- **提交者**: @gao12312
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.9.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: 15.0.7
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.14 (main, Jan 19 2026, 07:36:53) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-2107.6.0.0251.43.oe1.bclinux.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
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
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.9.0+cpu
[pip3] torch_npu==2.9.0
[pip3] torchvision==0.24.0
[pip3] transformers==4.57.6
[conda] Could not collect
vLLM Version: 0.14.1
vLLM Ascend Version: 0.14.0rc1

ENV Variables:
ASCEND_TOOLKIT_LATEST_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_VISIBLE_DEVICES=1,2,3,4,5,6,7,0
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/cann-8.5.0
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/cann-8.5.0/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/cann-8.5.0/lib64:/usr/local/Ascend/cann-8.5.0/lib64/plugin/opskernel:/usr/local/Ascend/cann-8.5.0/lib64/plugin/nnengine:/usr/local/Ascend/cann-8.5.0/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64/plugin:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/python3.11.14/lib:
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
| npu-smi 25.5.0                   Version: 25.5.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 98.4        37                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3431 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 94.7        37                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3429 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 96.3        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3427 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 93.7        38                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3427 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 100.7       44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3427 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 91.8        42                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3427 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 94.4        41                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3427 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 90.9        41                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3427 / 65536         |
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
version=8.5.0
innerversion=V100R001C25SPC001B232
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/cann-8.5.0
```

</details>


### 🐛 Describe the bug


```python 
#!/bin/sh
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=512
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE="AIV"
export TASK_QUEUE_ENABLE=1
export CPU_AFFINITY_CONF=2

vllm serve /workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-Instruct-2507-w8a8-QuaRot \
--prefill-context-parallel-size 1 \
--decode-context-parallel-size 1 \
--tensor-parallel-size 8  \
--data-parallel-size 1 \
--enable-expert-parallel  \
--served-model-name "qwen" \
--max-model-len 16384  \
--quantization ascend  \
--max-num-batched-tokens 7168 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.9 \
--compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}' \
--speculative_config '{"model": "/workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-Instruct-2507-eagle3-transformed", "num_speculative_tokens": 1, "method":"eagle3","draft_tensor_parallel_size": 1,"disable_padded_drafter_batch": false}' \


the logs as following :
(APIServer pid=968) WARNING 02-03 19:11:07 [warnings.py:110] /vllm-workspace/vllm/vllm/entrypoints/utils.py:220: DeprecationWarning: max_tokens is deprecated in favor of the max_completion_tokens field
(APIServer pid=968) INFO:     127.0.0.1:58044 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(Worker_TP0_EP0 pid=1584) INFO 02-03 19:11:07 [acl_graph.py:185] Replaying aclgraph
(Worker_TP6_EP6 pid=2675) INFO 02-03 19:11:07 [acl_graph.py:185] Replaying aclgraph
(Worker_TP5_EP5 pid=2465) INFO 02-03 19:11:07 [acl_graph.py:185] Replaying aclgraph
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822] WorkerProc hit an exception.
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP6_EP6 pid=2675) ERROR 02-03 19:11:07 [multiproc_executor.py:822] 
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822] WorkerProc hit an exception.
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP5_EP5 pid=2465) ERROR 02-03 19:11:07 [multiproc_executor.py:822] 
(Worker_TP2_EP2 pid=1883) INFO 02-03 19:11:07 [acl_graph.py:185] Replaying aclgraph
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822] WorkerProc hit an exception.
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP2_EP2 pid=1883) ERROR 02-03 19:11:07 [multiproc_executor.py:822] 
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822] WorkerProc hit an exception.
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 351, in sample_tokens
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return self.model_runner.sample_tokens(grammar_output)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1581, in sample_tokens
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     propose_draft_token_ids(sampler_output.sampled_token_ids)
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1543, in propose_draft_token_ids
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._draft_token_ids = self.propose_draft_token_ids(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1300, in propose_draft_token_ids
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     draft_token_ids = self.drafter._propose(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                       ^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 564, in _propose
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     self._update_full_graph_params(forward_context,
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1181, in _update_full_graph_params
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     update_full_graph_params(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 223, in update_full_graph_params
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     impl_cls.update_graph_params(
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 439, in update_graph_params
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]     attn_metadata = forward_context.draft_attn_metadatas
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822] AttributeError: 'ForwardContext' object has no attribute 'draft_attn_metadatas'
(Worker_TP0_EP0 pid=1584) ERROR 02-03 19:11:07 [multiproc_executor.py:822] 
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [dump_input.py:72] Dumping input data for V1 LLM engine (v0.14.1) with config: model='/workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-Instruct-2507-w8a8-QuaRot', speculative_config=SpeculativeConfig(method='eagle3', model='/workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-Instruct-2507-eagle3-transformed', num_spec_tokens=1), tokenizer='/workspace/cache/aiops-sh2/models/Qwen3-235B-A22B-Instruct-2507-w8a8-QuaRot', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=ascend, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False, enable_mfu_metrics=False, enable_mm_processor_stats=False, enable_logging_iteration_details=False), seed=0, served_model_name=qwen, enable_prefix_caching=False, enable_chunked_prefill=True, pooler_config=None, compilation_config={'level': None, 'mode': <CompilationMode.VLLM_COMPILE: 3>, 'debug_dump_path': None, 'cache_dir': '', 'compile_cache_save_format': 'binary', 'backend': 'vllm_ascend.compilation.compiler_interface.AscendCompiler', 'custom_ops': ['all'], 'splitting_ops': [], 'compile_mm_encoder': False, 'compile_sizes': [], 'compile_ranges_split_points': [7168], 'inductor_compile_config': {'enable_auto_functionalized_v2': False, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': <CUDAGraphMode.FULL_DECODE_ONLY: (2, 0)>, 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 272, 288, 304, 320, 336, 352, 368, 384, 400, 416, 432, 448, 464, 480, 496, 512], 'cudagraph_copy_inputs': False, 'cudagraph_specialize_lora': True, 'use_inductor_graph_partition': False, 'pass_config': {'fuse_norm_quant': True, 'fuse_act_quant': True, 'fuse_attn_quant': False, 'eliminate_noops': True, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': False}, 'max_cudagraph_capture_size': 512, 'dynamic_shapes_config': {'type': <DynamicShapesType.BACKED: 'backed'>, 'evaluate_guards': False, 'assume_32_bit_indexing': True}, 'local_cache_dir': None}, 
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [dump_input.py:79] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=chatcmpl-a2186ed5a6174238-99ef5790,prompt_token_ids_len=11,prefill_token_ids_len=None,mm_features=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=200, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None,prompt_embeds_shape=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[],resumed_req_ids=set(),new_token_ids_lens=[],all_token_ids_lens={},new_block_ids=[],num_computed_tokens=[],num_output_tokens=[]), num_scheduled_tokens={chatcmpl-a2186ed5a6174238-99ef5790: 11}, total_num_scheduled_tokens=11, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[0], finished_req_ids=[], free_encoder_mm_hashes=[], preempted_req_ids=[], has_structured_output_requests=false, pending_structured_output_tokens=false, num_invalid_spec_tokens=null, kv_connector_metadata=null, ec_connector_metadata=null)
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [dump_input.py:81] Dumping scheduler stats: SchedulerStats(num_running_reqs=1, num_waiting_reqs=0, step_counter=0, current_wave=0, kv_cache_usage=0.00038138825324185444, prefix_cache_stats=PrefixCacheStats(reset=False, requests=0, queries=0, hits=0, preempted_requests=0, preempted_queries=0, preempted_hits=0), connector_prefix_cache_stats=None, kv_cache_eviction_events=[], spec_decoding_stats=None, kv_connector_stats=None, waiting_lora_adapters={}, running_lora_adapters={}, cudagraph_stats=None, perf_stats=None)
(Worker_TP4_EP4 pid=2261) INFO 02-03 19:11:07 [acl_graph.py:185] Replaying aclgraph
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938] Traceback (most recent call last):
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 929, in run_engine_core
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 956, in run_busy_loop
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     self._process_engine_step()
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 989, in _process_engine_step
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 487, in step_with_batch_queue
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     model_output = future.result()
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]                    ^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 80, in result
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     return super().result()
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]            ^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/usr/local/python3.11.14/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     return self.__get_result()
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/usr/local/python3.11.14/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     raise self._exception
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 84, in wait_for_response
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     response = self.aggregate(get_response())
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938]     raise RuntimeError(
(EngineCore_DP0 pid=1482) ERROR 02-03 19:11:07 [core.py:938] RuntimeError: Worker failed with error ''ForwardContext' object has no attribute 'draft_attn_metadatas'', please check the stack trace above for the root cause
(Worker_TP0_EP0 pid=1584) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(Worker_TP4_EP4 pid=2261) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546] AsyncLLM output_handler failed.
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546] Traceback (most recent call last):
(Worker_TP2_EP2 pid=1883) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 502, in output_handler
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546]     outputs = await engine_core.get_output_async()
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 899, in get_output_async
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546]     raise self._format_exception(outputs) from None
(Worker_TP7_EP7 pid=2894) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(APIServer pid=968) ERROR 02-03 19:11:07 [async_llm.py:546] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
(Worker_TP1_EP1 pid=1709) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(Worker_TP3_EP3 pid=2066) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343] Error in chat completion stream generator.
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343] Traceback (most recent call last):
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]   File "/vllm-workspace/vllm/vllm/entrypoints/openai/serving_chat.py", line 715, in chat_completion_stream_generator
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]     async for res in result_generator:
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 437, in generate
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]     out = q.get_nowait() or await q.get()
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]                             ^^^^^^^^^^^^^
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]   File "/vllm-workspace/vllm/vllm/v1/engine/output_processor.py", line 77, in get
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]     raise output
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 502, in output_handler
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]     outputs = await engine_core.get_output_async()
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 899, in get_output_async
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343]     raise self._format_exception(outputs) from None
(APIServer pid=968) ERROR 02-03 19:11:07 [serving_chat.py:1343] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
(Worker_TP6_EP6 pid=2675) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(Worker_TP5_EP5 pid=2465) INFO 02-03 19:11:07 [multiproc_executor.py:707] Parent process exited, terminating worker
(APIServer pid=968) INFO:     Shutting down
(APIServer pid=968) INFO:     Waiting for application shutdown.
(APIServer pid=968) INFO:     Application shutdown complete.
(APIServer pid=968) INFO:     Finished server process [968]
(APIServer pid=968) sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
/usr/local/python3.11.14/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '


