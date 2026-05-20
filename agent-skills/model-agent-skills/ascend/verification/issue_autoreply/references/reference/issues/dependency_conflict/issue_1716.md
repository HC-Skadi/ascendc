# Issue #1716: [Bug]: Qwen2.5-14B-Instruct-1M 长上下文推理报错。

## 基本信息

- **编号**: #1716
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1716
- **创建时间**: 2025-07-10T03:42:34Z
- **关闭时间**: 2025-07-11T01:26:12Z
- **更新时间**: 2025-07-28T01:11:42Z
- **提交者**: @chenqi123
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 07-10 11:35:36 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 07-10 11:35:36 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 07-10 11:35:36 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 07-10 11:35:36 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 07-10 11:35:36 __init__.py:44] plugin ascend loaded.
INFO 07-10 11:35:36 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: openEuler 24.03 (LTS) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-30.oe2403)
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.38

Python version: 3.11.11 (main, Apr  7 2025, 14:52:53) [Clang 17.0.6 (ac00fd0f3aa8)] (64-bit runtime)
Python platform: Linux-4.19.90-2112.8.0.0131.oe1.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 5250 To be filled by O.E.M. CPU @ 2.6GHz
BIOS CPU family:                 280
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
Stepping:                        0x1
CPU(s) scaling MHz:              100%
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] torchvision-npu==0.20.1+gitunknown
[pip3] transformers==4.53.0
[conda] Could not collect
vLLM Version: 0.7.4.dev0+ged6e9075d.d20250704 (git sha: ed6e9075d, date: 20250704)
vLLM Ascend Version: 0.7.3.post1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=4,5,6,7
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME=/usr/local/Ascend
ATB_SPEED_HOME_PATH=/usr/local/Ascend/atb-models
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/tools/hccn_tool/:/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64/:/usr/local/python3/lib:/usr/local/lib:/usr/local/Ascend/atb-models/lib:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
VLLM_USE_V1=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1               Version: 25.0.rc1.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 98.0        38                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 93.5        38                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3398 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 98.5        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3404 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 96.9        40                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 98.1        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3402 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 94.2        44                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3399 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 102.9       44                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3397 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 91.6        44                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3396 / 65536         |
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
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

Qwen2.5-14B-Instruct-1M 长上下文推理时，报错。启动命令：VLLM_USE_V1=1 vllm serve  /data3/Qwen2.5-14B-Instruct-1M --served-model-name qwen2.5-14b \
 --max-model-len=204800  -tp=8 --block-size=128 --host=0.0.0.0 --port=8000 --gpu-memory-utilization=0.9 --disable-log-request --enable-chunked-prefill --max-num-batched-tokens 4096  
报错信息如下：
INFO:     xx.xx:54182 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 07-10 11:40:38 loggers.py:78] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374] WorkerProc hit an exception: %s
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374] Traceback (most recent call last):
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = func(*args, **kwargs)
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in execute_model
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return func(*args, **kwargs)
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 567, in execute_model
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     hidden_states = self._process_reqs(scheduler_output,
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 519, in _process_reqs
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     attn_mask = self.make_attention_mask(seq_lens=seq_lens,
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 429, in make_attention_mask
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return self.attn_mask_builder.get_splitfuse_attn_mask(
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/attention/attention.py", line 140, in get_splitfuse_attn_mask
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     right_tensor.mask_fill_(
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374]     ^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=4 pid=10184) ERROR 07-10 11:40:39 multiproc_executor.py:374] AttributeError: 'Tensor' object has no attribute 'mask_fill_'
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374] WorkerProc hit an exception: %s
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374] Traceback (most recent call last):
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = func(*args, **kwargs)
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in execute_model
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return func(*args, **kwargs)
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 567, in execute_model
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     hidden_states = self._process_reqs(scheduler_output,
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 519, in _process_reqs
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     attn_mask = self.make_attention_mask(seq_lens=seq_lens,
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 429, in make_attention_mask
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return self.attn_mask_builder.get_splitfuse_attn_mask(
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/attention/attention.py", line 140, in get_splitfuse_attn_mask
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     right_tensor.mask_fill_(
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374]     ^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=3 pid=9929) ERROR 07-10 11:40:39 multiproc_executor.py:374] AttributeError: 'Tensor' object has no attribute 'mask_fill_'
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374] WorkerProc hit an exception: %s
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374] WorkerProc hit an exception: %s
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374] Traceback (most recent call last):
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374] Traceback (most recent call last):
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = func(*args, **kwargs)
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = func(*args, **kwargs)
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in execute_model
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in execute_model
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374] WorkerProc hit an exception: %s
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374] Traceback (most recent call last):
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop
ERROR 07-10 11:40:39 core.py:291] EngineCore hit an exception: Traceback (most recent call last):
ERROR 07-10 11:40:39 core.py:291]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 284, in run_engine_core
ERROR 07-10 11:40:39 core.py:291]     engine_core.run_busy_loop()
ERROR 07-10 11:40:39 core.py:291]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 327, in run_busy_loop
ERROR 07-10 11:40:39 core.py:291]     outputs = step_fn()
ERROR 07-10 11:40:39 core.py:291]               ^^^^^^^^^
ERROR 07-10 11:40:39 core.py:291]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 154, in step
ERROR 07-10 11:40:39 core.py:291]     output = self.model_executor.execute_model(scheduler_output)
ERROR 07-10 11:40:39 core.py:291]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 07-10 11:40:39 core.py:291]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/abstract.py", line 75, in execute_model
ERROR 07-10 11:40:39 core.py:291]     output = self.collective_rpc("execute_model",
ERROR 07-10 11:40:39 core.py:291]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 07-10 11:40:39 core.py:291]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 133, in collective_rpc
ERROR 07-10 11:40:39 core.py:291]     raise e
ERROR 07-10 11:40:39 core.py:291]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 122, in collective_rpc
ERROR 07-10 11:40:39 core.py:291]     raise result
ERROR 07-10 11:40:39 core.py:291] AttributeError: 'Tensor' object has no attribute 'mask_fill_'
ERROR 07-10 11:40:39 core.py:291]
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = func(*args, **kwargs)
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return func(*args, **kwargs)
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return func(*args, **kwargs)
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in execute_model
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 567, in execute_model
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 567, in execute_model
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     hidden_states = self._process_reqs(scheduler_output,
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     hidden_states = self._process_reqs(scheduler_output,
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 519, in _process_reqs
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 519, in _process_reqs
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return func(*args, **kwargs)
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     attn_mask = self.make_attention_mask(seq_lens=seq_lens,
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     attn_mask = self.make_attention_mask(seq_lens=seq_lens,
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 567, in execute_model
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 429, in make_attention_mask
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 429, in make_attention_mask
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     hidden_states = self._process_reqs(scheduler_output,
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return self.attn_mask_builder.get_splitfuse_attn_mask(
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return self.attn_mask_builder.get_splitfuse_attn_mask(
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 519, in _process_reqs
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/attention/attention.py", line 140, in get_splitfuse_attn_mask
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/attention/attention.py", line 140, in get_splitfuse_attn_mask
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     attn_mask = self.make_attention_mask(seq_lens=seq_lens,
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374] WorkerProc hit an exception: %s
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     right_tensor.mask_fill_(
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     right_tensor.mask_fill_(
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374] Traceback (most recent call last):
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374]     ^^^^^^^^^^^^^^^^^^^^^^^
CRITICAL 07-10 11:40:39 core_client.py:191] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374]     ^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 429, in make_attention_mask
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop
(VllmWorker rank=5 pid=10441) ERROR 07-10 11:40:39 multiproc_executor.py:374] AttributeError: 'Tensor' object has no attribute 'mask_fill_'
(VllmWorker rank=2 pid=9815) ERROR 07-10 11:40:39 multiproc_executor.py:374] AttributeError: 'Tensor' object has no attribute 'mask_fill_'
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return self.attn_mask_builder.get_splitfuse_attn_mask(
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = func(*args, **kwargs)
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/attention/attention.py", line 140, in get_splitfuse_attn_mask
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 222, in execute_model
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     right_tensor.mask_fill_(
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     output = self.model_runner.execute_model(scheduler_output)
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374]     ^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=1 pid=9782) ERROR 07-10 11:40:39 multiproc_executor.py:374] AttributeError: 'Tensor' object has no attribute 'mask_fill_'
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/usr/local/python3/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return func(*args, **kwargs)
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 567, in execute_model
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     hidden_states = self._process_reqs(scheduler_output,
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 519, in _process_reqs
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     attn_mask = self.make_attention_mask(seq_lens=seq_lens,
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 429, in make_attention_mask
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     return self.attn_mask_builder.get_splitfuse_attn_mask(
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]   File "/opt/vllm-ascend/vllm_ascend/attention/attention.py", line 140, in get_splitfuse_attn_mask
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     right_tensor.mask_fill_(
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374]     ^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=6 pid=10698) ERROR 07-10 11:40:39 multiproc_executor.py:374] AttributeError: 'Tensor' object has no attribute 'mask_fill_'

