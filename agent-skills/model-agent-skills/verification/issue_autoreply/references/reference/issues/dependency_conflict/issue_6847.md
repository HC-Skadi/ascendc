# Issue #6847: [Bug]: 910B2双机推理GLM-5启动失败

## 基本信息

- **编号**: #6847
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6847
- **创建时间**: 2026-02-27T07:26:50Z
- **关闭时间**: 2026-02-27T09:28:01Z
- **更新时间**: 2026-02-28T00:56:09Z
- **提交者**: @zhanghw0354
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
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
[pip3] transformers==5.2.0.dev0
[pip3] triton-ascend==3.2.0
[conda] Could not collect
vLLM Version: 0.16.0rc2.dev3+g978a37c82 (git sha: 978a37c82)
vLLM Ascend Version: 0.14.0rc2.dev150+gff3a50d01 (git sha: ff3a50d01)

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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 92.9        45                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3395 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 92.7        44                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 89.3        46                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 89.4        45                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 90.1        46                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3391 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 90.6        49                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3393 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 87.4        47                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3392 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 93.5        49                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3392 / 65536         |
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

按照官方文档[GLM5.html#multi-node-deployment](https://docs.vllm.ai/projects/ascend/en/main/tutorials/models/GLM5.html#multi-node-deployment)，使用910B2服务器双机推理GLM5模型，DP主节点报错，服务无法启动，相关日志如下（日志内容较多，前面无关部分未粘贴）：         
Loading safetensors checkpoint shards:  53% Completed | 52/99 [06:21<21:23, 27.31s/it]
Loading safetensors checkpoint shards:  54% Completed | 53/99 [06:52<21:54, 28.58s/it]
Loading safetensors checkpoint shards:  55% Completed | 54/99 [07:27<22:47, 30.38s/it]
Loading safetensors checkpoint shards:  56% Completed | 55/99 [07:56<21:57, 29.95s/it]
(ApiServer_0 pid=10466) Process ApiServer_0:
(ApiServer_0 pid=10466) Traceback (most recent call last):
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(ApiServer_0 pid=10466)     self.run()
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 108, in run
(ApiServer_0 pid=10466)     self._target(*self._args, **self._kwargs)
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 300, in run_api_server_worker_proc
(ApiServer_0 pid=10466)     uvloop.run(
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
(ApiServer_0 pid=10466)     return runner.run(wrapper())
(ApiServer_0 pid=10466)            ^^^^^^^^^^^^^^^^^^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/asyncio/runners.py", line 118, in run
(ApiServer_0 pid=10466)     return self._loop.run_until_complete(task)
(ApiServer_0 pid=10466)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_0 pid=10466)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
(ApiServer_0 pid=10466)     return await main
(ApiServer_0 pid=10466)            ^^^^^^^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 476, in run_server_worker
(ApiServer_0 pid=10466)     async with build_async_engine_client(
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(ApiServer_0 pid=10466)     return await anext(self.gen)
(ApiServer_0 pid=10466)            ^^^^^^^^^^^^^^^^^^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 96, in build_async_engine_client
(ApiServer_0 pid=10466)     async with build_async_engine_client_from_engine_args(
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(ApiServer_0 pid=10466)     return await anext(self.gen)
(ApiServer_0 pid=10466)            ^^^^^^^^^^^^^^^^^^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 137, in build_async_engine_client_from_engine_args
(ApiServer_0 pid=10466)     async_llm = AsyncLLM.from_vllm_config(
(ApiServer_0 pid=10466)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 222, in from_vllm_config
(ApiServer_0 pid=10466)     return cls(
(ApiServer_0 pid=10466)            ^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 148, in __init__
(ApiServer_0 pid=10466)     self.engine_core = EngineCoreClient.make_async_mp_client(
(ApiServer_0 pid=10466)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 123, in make_async_mp_client
(ApiServer_0 pid=10466)     return DPLBAsyncMPClient(*client_args)
(ApiServer_0 pid=10466)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 1232, in __init__
(ApiServer_0 pid=10466)     super().__init__(
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 1061, in __init__
(ApiServer_0 pid=10466)     super().__init__(
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 835, in __init__
(ApiServer_0 pid=10466)     super().__init__(
(ApiServer_0 pid=10466)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 541, in __init__
(ApiServer_0 pid=10466)     raise TimeoutError(
(ApiServer_0 pid=10466) TimeoutError: Timed out waiting for engines to send initial message on input socket.
(ApiServer_1 pid=10467) Process ApiServer_1:
(ApiServer_1 pid=10467) Traceback (most recent call last):
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(ApiServer_1 pid=10467)     self.run()
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 108, in run
(ApiServer_1 pid=10467)     self._target(*self._args, **self._kwargs)
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 300, in run_api_server_worker_proc
(ApiServer_1 pid=10467)     uvloop.run(
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
(ApiServer_1 pid=10467)     return runner.run(wrapper())
(ApiServer_1 pid=10467)            ^^^^^^^^^^^^^^^^^^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/asyncio/runners.py", line 118, in run
(ApiServer_1 pid=10467)     return self._loop.run_until_complete(task)
(ApiServer_1 pid=10467)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_1 pid=10467)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
(ApiServer_1 pid=10467)     return await main
(ApiServer_1 pid=10467)            ^^^^^^^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 476, in run_server_worker
(ApiServer_1 pid=10467)     async with build_async_engine_client(
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(ApiServer_1 pid=10467)     return await anext(self.gen)
(ApiServer_1 pid=10467)            ^^^^^^^^^^^^^^^^^^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 96, in build_async_engine_client
(ApiServer_1 pid=10467)     async with build_async_engine_client_from_engine_args(
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(ApiServer_1 pid=10467)     return await anext(self.gen)
(ApiServer_1 pid=10467)            ^^^^^^^^^^^^^^^^^^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 137, in build_async_engine_client_from_engine_args
(ApiServer_1 pid=10467)     async_llm = AsyncLLM.from_vllm_config(
(ApiServer_1 pid=10467)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 222, in from_vllm_config
(ApiServer_1 pid=10467)     return cls(
(ApiServer_1 pid=10467)            ^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 148, in __init__
(ApiServer_1 pid=10467)     self.engine_core = EngineCoreClient.make_async_mp_client(
(ApiServer_1 pid=10467)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 123, in make_async_mp_client
(ApiServer_1 pid=10467)     return DPLBAsyncMPClient(*client_args)
(ApiServer_1 pid=10467)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 1232, in __init__
(ApiServer_1 pid=10467)     super().__init__(
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 1061, in __init__
(ApiServer_1 pid=10467)     super().__init__(
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 835, in __init__
(ApiServer_1 pid=10467)     super().__init__(
(ApiServer_1 pid=10467)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 541, in __init__
(ApiServer_1 pid=10467)     raise TimeoutError(
(ApiServer_1 pid=10467) TimeoutError: Timed out waiting for engines to send initial message on input socket.
(ApiServer_0 pid=10466) sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
(ApiServer_1 pid=10467) sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
Loading safetensors checkpoint shards:  57% Completed | 56/99 [08:26<21:31, 30.04s/it]
Loading safetensors checkpoint shards:  58% Completed | 57/99 [08:57<21:15, 30.38s/it]
Loading safetensors checkpoint shards:  59% Completed | 58/99 [09:35<22:17, 32.63s/it]
Loading safetensors checkpoint shards:  60% Completed | 59/99 [10:08<21:47, 32.68s/it]
Loading safetensors checkpoint shards:  61% Completed | 60/99 [10:42<21:33, 33.18s/it]
Loading safetensors checkpoint shards:  62% Completed | 61/99 [11:13<20:29, 32.34s/it]
Loading safetensors checkpoint shards:  63% Completed | 62/99 [11:39<18:53, 30.63s/it]
Loading safetensors checkpoint shards:  64% Completed | 63/99 [12:13<18:57, 31.61s/it]
Loading safetensors checkpoint shards:  65% Completed | 64/99 [12:46<18:37, 31.92s/it]
Loading safetensors checkpoint shards:  66% Completed | 65/99 [13:19<18:23, 32.46s/it]
Loading safetensors checkpoint shards:  67% Completed | 66/99 [13:54<18:14, 33.16s/it]
Loading safetensors checkpoint shards:  68% Completed | 67/99 [14:22<16:44, 31.39s/it]
Loading safetensors checkpoint shards:  69% Completed | 68/99 [14:50<15:46, 30.53s/it]
Loading safetensors checkpoint shards:  70% Completed | 69/99 [15:26<16:04, 32.16s/it]
Loading safetensors checkpoint shards:  71% Completed | 70/99 [15:59<15:39, 32.38s/it]
Loading safetensors checkpoint shards:  72% Completed | 71/99 [16:31<15:02, 32.24s/it]
Loading safetensors checkpoint shards:  73% Completed | 72/99 [16:59<13:56, 31.00s/it]
Loading safetensors checkpoint shards:  74% Completed | 73/99 [17:28<13:13, 30.54s/it]
Loading safetensors checkpoint shards:  75% Completed | 74/99 [17:53<12:00, 28.84s/it]
Loading safetensors checkpoint shards:  76% Completed | 75/99 [18:26<12:01, 30.05s/it]
Loading safetensors checkpoint shards:  77% Completed | 76/99 [18:58<11:41, 30.50s/it]
Loading safetensors checkpoint shards:  78% Completed | 77/99 [19:31<11:30, 31.41s/it]
Loading safetensors checkpoint shards:  79% Completed | 78/99 [19:59<10:38, 30.41s/it]
Loading safetensors checkpoint shards:  80% Completed | 79/99 [20:31<10:17, 30.86s/it]
Loading safetensors checkpoint shards:  81% Completed | 80/99 [21:05<10:05, 31.86s/it]
Loading safetensors checkpoint shards:  82% Completed | 81/99 [21:40<09:47, 32.66s/it]
Loading safetensors checkpoint shards:  83% Completed | 82/99 [22:13<09:16, 32.73s/it]
Loading safetensors checkpoint shards:  84% Completed | 83/99 [22:44<08:37, 32.33s/it]
Loading safetensors checkpoint shards:  85% Completed | 84/99 [23:14<07:55, 31.70s/it]
Loading safetensors checkpoint shards:  86% Completed | 85/99 [23:43<07:11, 30.84s/it]
Loading safetensors checkpoint shards:  87% Completed | 86/99 [24:16<06:49, 31.50s/it]
Loading safetensors checkpoint shards:  88% Completed | 87/99 [24:50<06:24, 32.05s/it]
Loading safetensors checkpoint shards:  89% Completed | 88/99 [25:21<05:49, 31.75s/it]
Loading safetensors checkpoint shards:  90% Completed | 89/99 [25:52<05:14, 31.46s/it]
Loading safetensors checkpoint shards:  91% Completed | 90/99 [26:21<04:36, 30.75s/it]
Loading safetensors checkpoint shards:  92% Completed | 91/99 [26:49<04:00, 30.12s/it]
Loading safetensors checkpoint shards:  93% Completed | 92/99 [27:03<02:56, 25.25s/it]
Loading safetensors checkpoint shards:  94% Completed | 93/99 [27:19<02:13, 22.29s/it]
Loading safetensors checkpoint shards:  95% Completed | 94/99 [27:33<01:39, 19.80s/it]
Loading safetensors checkpoint shards:  96% Completed | 95/99 [27:47<01:13, 18.27s/it]
Loading safetensors checkpoint shards:  97% Completed | 96/99 [27:57<00:47, 15.70s/it]
Loading safetensors checkpoint shards:  98% Completed | 97/99 [27:57<00:22, 11.05s/it]
Loading safetensors checkpoint shards:  99% Completed | 98/99 [28:03<00:09,  9.46s/it]
Loading safetensors checkpoint shards: 100% Completed | 99/99 [28:12<00:00,  9.36s/it]
Loading safetensors checkpoint shards: 100% Completed | 99/99 [28:12<00:00, 17.10s/it]
(Worker_DP0_TP0_EP0 pid=10536) 
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:00:03 [default_loader.py:293] Loading weights took 1692.49 seconds
INFO 02-27 15:00:13 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:13 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:13 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:13 [__init__.py:212] Platform plugin ascend is activated
INFO 02-27 15:00:13 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:13 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:13 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:13 [__init__.py:212] Platform plugin ascend is activated
INFO 02-27 15:00:13 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:13 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:13 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:13 [__init__.py:212] Platform plugin ascend is activated
INFO 02-27 15:00:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:14 [__init__.py:212] Platform plugin ascend is activated
INFO 02-27 15:00:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:14 [__init__.py:212] Platform plugin ascend is activated
INFO 02-27 15:00:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:14 [__init__.py:212] Platform plugin ascend is activated
INFO 02-27 15:00:14 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:14 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:14 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:14 [__init__.py:212] Platform plugin ascend is activated
INFO 02-27 15:00:15 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-27 15:00:15 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-27 15:00:15 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-27 15:00:15 [__init__.py:212] Platform plugin ascend is activated
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:00:31 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:00:32 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:00:33 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:00:33 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:00:33 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:00:34 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:00:34 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:00:34 [fused_moe.py:465] SharedFusedMoE shared experts split computation matches the integrated computation.
(Worker_DP0_TP6_EP6 pid=11806) WARNING 02-27 15:00:34 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:00:34 [model_runner_v1.py:2315] Loading drafter model...
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:00:35 [compilation.py:903] Using OOT custom backend for compilation.
(Worker_DP0_TP0_EP0 pid=10536) WARNING 02-27 15:00:35 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:00:35 [model_runner_v1.py:2315] Loading drafter model...
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:00:35 [unquantized.py:131] Using OOT backend for Unquantized MoE
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:00:36 [compilation.py:903] Using OOT custom backend for compilation.
Loading safetensors checkpoint shards:   0% Completed | 0/99 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   1% Completed | 1/99 [00:00<00:23,  4.18it/s]
(Worker_DP0_TP4_EP4 pid=11356) WARNING 02-27 15:00:36 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:00:36 [model_runner_v1.py:2315] Loading drafter model...
Loading safetensors checkpoint shards:   2% Completed | 2/99 [00:00<00:24,  3.95it/s]
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:00:36 [compilation.py:903] Using OOT custom backend for compilation.
(Worker_DP0_TP7_EP7 pid=12049) WARNING 02-27 15:00:36 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:00:36 [model_runner_v1.py:2315] Loading drafter model...
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:00:36 [compilation.py:903] Using OOT custom backend for compilation.
(Worker_DP0_TP5_EP5 pid=11575) WARNING 02-27 15:00:37 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:00:37 [model_runner_v1.py:2315] Loading drafter model...
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:00:37 [compilation.py:903] Using OOT custom backend for compilation.
(Worker_DP0_TP2_EP2 pid=10936) WARNING 02-27 15:00:37 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP3_EP3 pid=11144) WARNING 02-27 15:00:37 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:00:37 [model_runner_v1.py:2315] Loading drafter model...
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:00:37 [model_runner_v1.py:2315] Loading drafter model...
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:00:37 [compilation.py:903] Using OOT custom backend for compilation.
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:00:37 [compilation.py:903] Using OOT custom backend for compilation.
(Worker_DP0_TP1_EP1 pid=10693) WARNING 02-27 15:00:38 [sfa_v1.py:523] Currently mlapo only supports W8A8 quantization in SFA scenario.Some layers in your model are not quantized with W8A8,thus mlapo is disabled for these layers.
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:00:38 [model_runner_v1.py:2315] Loading drafter model...
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:00:38 [compilation.py:903] Using OOT custom backend for compilation.
Loading safetensors checkpoint shards:   3% Completed | 3/99 [00:03<02:43,  1.71s/it]
Loading safetensors checkpoint shards:   4% Completed | 4/99 [00:05<02:42,  1.71s/it]
Loading safetensors checkpoint shards:   5% Completed | 5/99 [00:07<02:45,  1.76s/it]
Loading safetensors checkpoint shards:   6% Completed | 6/99 [00:10<03:08,  2.03s/it]
Loading safetensors checkpoint shards:   7% Completed | 7/99 [00:10<02:11,  1.43s/it]
Loading safetensors checkpoint shards:   8% Completed | 8/99 [00:10<01:34,  1.04s/it]
Loading safetensors checkpoint shards:   9% Completed | 9/99 [00:10<01:09,  1.30it/s]
Loading safetensors checkpoint shards:  10% Completed | 10/99 [00:10<00:52,  1.69it/s]
Loading safetensors checkpoint shards:  11% Completed | 11/99 [00:11<00:41,  2.13it/s]
Loading safetensors checkpoint shards:  12% Completed | 12/99 [00:11<00:33,  2.61it/s]
Loading safetensors checkpoint shards:  13% Completed | 13/99 [00:11<00:27,  3.09it/s]
Loading safetensors checkpoint shards:  14% Completed | 14/99 [00:11<00:24,  3.54it/s]
Loading safetensors checkpoint shards:  15% Completed | 15/99 [00:11<00:21,  3.94it/s]
Loading safetensors checkpoint shards:  16% Completed | 16/99 [00:11<00:19,  4.23it/s]
Loading safetensors checkpoint shards:  17% Completed | 17/99 [00:12<00:18,  4.51it/s]
Loading safetensors checkpoint shards:  18% Completed | 18/99 [00:12<00:17,  4.73it/s]
Loading safetensors checkpoint shards:  19% Completed | 19/99 [00:12<00:16,  4.91it/s]
Loading safetensors checkpoint shards:  20% Completed | 20/99 [00:12<00:15,  5.01it/s]
Loading safetensors checkpoint shards:  21% Completed | 21/99 [00:12<00:15,  5.03it/s]
Loading safetensors checkpoint shards:  22% Completed | 22/99 [00:13<00:15,  5.06it/s]
Loading safetensors checkpoint shards:  23% Completed | 23/99 [00:13<00:14,  5.12it/s]
Loading safetensors checkpoint shards:  24% Completed | 24/99 [00:13<00:14,  5.11it/s]
Loading safetensors checkpoint shards:  25% Completed | 25/99 [00:13<00:14,  5.18it/s]
Loading safetensors checkpoint shards:  26% Completed | 26/99 [00:13<00:14,  5.21it/s]
Loading safetensors checkpoint shards:  27% Completed | 27/99 [00:14<00:13,  5.23it/s]
Loading safetensors checkpoint shards:  28% Completed | 28/99 [00:14<00:13,  5.19it/s]
Loading safetensors checkpoint shards:  29% Completed | 29/99 [00:14<00:13,  5.22it/s]
Loading safetensors checkpoint shards:  30% Completed | 30/99 [00:14<00:13,  5.25it/s]
Loading safetensors checkpoint shards:  31% Completed | 31/99 [00:14<00:12,  5.28it/s]
Loading safetensors checkpoint shards:  32% Completed | 32/99 [00:14<00:12,  5.28it/s]
Loading safetensors checkpoint shards:  33% Completed | 33/99 [00:15<00:12,  5.30it/s]
Loading safetensors checkpoint shards:  34% Completed | 34/99 [00:15<00:12,  5.21it/s]
Loading safetensors checkpoint shards:  35% Completed | 35/99 [00:15<00:12,  5.23it/s]
Loading safetensors checkpoint shards:  36% Completed | 36/99 [00:15<00:12,  5.02it/s]
Loading safetensors checkpoint shards:  37% Completed | 37/99 [00:15<00:12,  5.12it/s]
Loading safetensors checkpoint shards:  38% Completed | 38/99 [00:16<00:11,  5.15it/s]
Loading safetensors checkpoint shards:  39% Completed | 39/99 [00:16<00:11,  5.12it/s]
Loading safetensors checkpoint shards:  40% Completed | 40/99 [00:16<00:11,  5.16it/s]
Loading safetensors checkpoint shards:  41% Completed | 41/99 [00:16<00:11,  5.21it/s]
Loading safetensors checkpoint shards:  42% Completed | 42/99 [00:16<00:10,  5.24it/s]
Loading safetensors checkpoint shards:  43% Completed | 43/99 [00:17<00:10,  5.25it/s]
Loading safetensors checkpoint shards:  44% Completed | 44/99 [00:17<00:10,  5.25it/s]
Loading safetensors checkpoint shards:  45% Completed | 45/99 [00:17<00:10,  5.18it/s]
Loading safetensors checkpoint shards:  46% Completed | 46/99 [00:17<00:10,  5.22it/s]
Loading safetensors checkpoint shards:  47% Completed | 47/99 [00:17<00:09,  5.25it/s]
Loading safetensors checkpoint shards:  48% Completed | 48/99 [00:18<00:09,  5.20it/s]
Loading safetensors checkpoint shards:  49% Completed | 49/99 [00:18<00:09,  5.23it/s]
Loading safetensors checkpoint shards:  51% Completed | 50/99 [00:18<00:09,  5.26it/s]
Loading safetensors checkpoint shards:  52% Completed | 51/99 [00:18<00:09,  5.18it/s]
Loading safetensors checkpoint shards:  53% Completed | 52/99 [00:18<00:09,  5.19it/s]
Loading safetensors checkpoint shards:  54% Completed | 53/99 [00:19<00:08,  5.23it/s]
Loading safetensors checkpoint shards:  55% Completed | 54/99 [00:19<00:08,  5.23it/s]
Loading safetensors checkpoint shards:  56% Completed | 55/99 [00:19<00:08,  5.25it/s]
Loading safetensors checkpoint shards:  57% Completed | 56/99 [00:19<00:08,  5.25it/s]
Loading safetensors checkpoint shards:  58% Completed | 57/99 [00:19<00:08,  5.18it/s]
Loading safetensors checkpoint shards:  59% Completed | 58/99 [00:20<00:07,  5.13it/s]
Loading safetensors checkpoint shards:  60% Completed | 59/99 [00:20<00:07,  5.09it/s]
Loading safetensors checkpoint shards:  61% Completed | 60/99 [00:20<00:07,  5.12it/s]
Loading safetensors checkpoint shards:  62% Completed | 61/99 [00:20<00:07,  5.16it/s]
Loading safetensors checkpoint shards:  63% Completed | 62/99 [00:20<00:07,  5.14it/s]
Loading safetensors checkpoint shards:  64% Completed | 63/99 [00:20<00:07,  5.11it/s]
Loading safetensors checkpoint shards:  65% Completed | 64/99 [00:21<00:06,  5.15it/s]
Loading safetensors checkpoint shards:  66% Completed | 65/99 [00:21<00:06,  5.21it/s]
Loading safetensors checkpoint shards:  67% Completed | 66/99 [00:21<00:06,  5.23it/s]
Loading safetensors checkpoint shards:  68% Completed | 67/99 [00:21<00:06,  5.24it/s]
Loading safetensors checkpoint shards:  69% Completed | 68/99 [00:21<00:05,  5.20it/s]
Loading safetensors checkpoint shards:  70% Completed | 69/99 [00:22<00:05,  5.22it/s]
Loading safetensors checkpoint shards:  71% Completed | 70/99 [00:22<00:05,  5.21it/s]
Loading safetensors checkpoint shards:  72% Completed | 71/99 [00:22<00:05,  5.25it/s]
Loading safetensors checkpoint shards:  73% Completed | 72/99 [00:22<00:05,  5.26it/s]
Loading safetensors checkpoint shards:  74% Completed | 73/99 [00:22<00:04,  5.24it/s]
Loading safetensors checkpoint shards:  75% Completed | 74/99 [00:23<00:04,  5.19it/s]
Loading safetensors checkpoint shards:  76% Completed | 75/99 [00:23<00:04,  5.20it/s]
Loading safetensors checkpoint shards:  77% Completed | 76/99 [00:23<00:04,  5.18it/s]
Loading safetensors checkpoint shards:  78% Completed | 77/99 [00:23<00:04,  5.21it/s]
Loading safetensors checkpoint shards:  79% Completed | 78/99 [00:23<00:04,  5.20it/s]
Loading safetensors checkpoint shards:  80% Completed | 79/99 [00:24<00:03,  5.21it/s]
Loading safetensors checkpoint shards:  81% Completed | 80/99 [00:24<00:03,  5.17it/s]
Loading safetensors checkpoint shards:  82% Completed | 81/99 [00:24<00:03,  5.21it/s]
Loading safetensors checkpoint shards:  83% Completed | 82/99 [00:24<00:03,  5.24it/s]
Loading safetensors checkpoint shards:  84% Completed | 83/99 [00:24<00:03,  5.25it/s]
Loading safetensors checkpoint shards:  85% Completed | 84/99 [00:25<00:02,  5.27it/s]
Loading safetensors checkpoint shards:  86% Completed | 85/99 [00:25<00:02,  5.26it/s]
Loading safetensors checkpoint shards:  87% Completed | 86/99 [00:25<00:02,  5.19it/s]
Loading safetensors checkpoint shards:  88% Completed | 87/99 [00:25<00:02,  5.21it/s]
Loading safetensors checkpoint shards:  89% Completed | 88/99 [00:25<00:02,  5.23it/s]
Loading safetensors checkpoint shards:  90% Completed | 89/99 [00:25<00:01,  5.25it/s]
Loading safetensors checkpoint shards:  91% Completed | 90/99 [00:26<00:01,  5.26it/s]
Loading safetensors checkpoint shards:  92% Completed | 91/99 [00:26<00:01,  5.27it/s]
Loading safetensors checkpoint shards:  93% Completed | 92/99 [00:38<00:25,  3.68s/it]
Loading safetensors checkpoint shards:  94% Completed | 93/99 [00:38<00:15,  2.64s/it]
Loading safetensors checkpoint shards:  96% Completed | 95/99 [00:38<00:05,  1.45s/it]
Loading safetensors checkpoint shards:  97% Completed | 96/99 [00:38<00:03,  1.14s/it]
Loading safetensors checkpoint shards:  98% Completed | 97/99 [00:45<00:05,  2.62s/it]
Loading safetensors checkpoint shards: 100% Completed | 99/99 [00:45<00:00,  2.18it/s]
(Worker_DP0_TP0_EP0 pid=10536) 
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:01:21 [default_loader.py:293] Loading weights took 45.56 seconds
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:01:21 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:01:22 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:01:22 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:01:22 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:01:22 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:01:23 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:01:23 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:01:23 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:01:24 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:01:24 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:01:24 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:01:25 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:01:25 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:01:26 [eagle_proposer.py:236] Detected MTP model. Sharing target model embedding weights with the draft model.
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:01:26 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:01:27 [model_runner_v1.py:2323] Loading model weights took 27.4936 GB
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:01:39 [backends.py:916] Using cache directory: /root/.cache/vllm/torch_compile_cache/3a4e73236f/rank_0_0/backbone for vLLM's torch.compile
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:01:39 [backends.py:976] Dynamo bytecode transform time: 10.55 s
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:05 [backends.py:368] Compiling a graph for compile range (1, 4098) takes 20.51 s
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:05 [monitor.py:34] torch.compile takes 31.05 s in total
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:17 [backends.py:976] Dynamo bytecode transform time: 0.51 s
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:19 [backends.py:368] Compiling a graph for compile range (1, 4098) takes 0.80 s
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:19 [monitor.py:34] torch.compile takes 32.36 s in total
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:02:22 [worker.py:338] Available memory: 28138531840, total memory: 65452113920
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:02:22 [worker.py:338] Available memory: 28139834368, total memory: 65452113920
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:02:22 [worker.py:338] Available memory: 28140903424, total memory: 65452113920
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:02:22 [worker.py:338] Available memory: 28138171392, total memory: 65452113920
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:02:22 [worker.py:338] Available memory: 28138785792, total memory: 65452113920
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:22 [worker.py:338] Available memory: 27732827136, total memory: 65452113920
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:02:23 [worker.py:338] Available memory: 28141235200, total memory: 65452113920
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:02:23 [worker.py:338] Available memory: 28139035648, total memory: 65452113920
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:23 [kv_cache_utils.py:1307] GPU KV cache size: 249,216 tokens
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:23 [kv_cache_utils.py:1312] Maximum concurrency for 131,072 tokens per request: 1.90x
Capturing CUDA graphs (decode, FULL):   0%|                                                                                          | 0/2 [00:00<?, ?it/s][rank2]:[W227 15:02:27.671845301 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank7]:[W227 15:02:27.671845411 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank4]:[W227 15:02:27.671918193 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank6]:[W227 15:02:27.671918163 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank5]:[W227 15:02:27.672026296 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank0]:[W227 15:02:27.672076007 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank3]:[W227 15:02:27.672163169 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank1]:[W227 15:02:27.675683912 compiler_depend.ts:207] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
Capturing CUDA graphs (decode, FULL): 100%|██████████████████████████████████████████████████████████████████████████████████| 2/2 [00:04<00:00,  2.13s/it]
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:31 [gpu_model_runner.py:5246] Graph capturing finished in 7 secs, took 0.29 GiB
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:31 [core.py:278] init engine (profile, create kv cache, warmup model) took 63.98 seconds
INFO 02-27 15:02:41 [coordinator.py:200] All engine subscriptions received by DP coordinator
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:41 [vllm.py:689] Asynchronous scheduling is enabled.
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:41 [ascend_config.py:412] Dynamic EPLB is False
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:41 [ascend_config.py:413] The number of redundant experts is 0
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:41 [ascend_config.py:54] Linear layer sharding enabled with config: None. Note: This feature works optimally with FLASHCOMM2 and DSA-CP enabled; using it without these features may result in significant performance degradation.
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:41 [platform.py:310] FULL_DECODE_ONLY compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327] 
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             **********************************************************************************
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * WARNING: You have enabled the *full graph* feature.
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * This is an early experimental stage and may involve various unknown issues.
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * A known problem is that capturing too many batch sizes can lead to OOM
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * (Out of Memory) errors or inference hangs. If you encounter such issues,
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * consider reducing `gpu_memory_utilization` or manually specifying a smaller
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * batch size for graph capture.
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * For more details, please refer to:
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             * https://docs.vllm.ai/en/stable/configuration/conserving_memory.html#reduce-cuda-graphs
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             **********************************************************************************
(EngineCore_DP0 pid=10314) WARNING 02-27 15:02:41 [platform.py:327]             
INFO 02-27 15:02:41 [utils.py:248] Waiting for API servers to complete ...
(EngineCore_DP0 pid=10314) INFO 02-27 15:02:41 [platform.py:435] Set PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ERROR 02-27 15:02:41 [utils.py:289] Exception occurred while running API servers: Process ApiServer_0 (PID: 10466) died with exit code 1
ERROR 02-27 15:02:41 [utils.py:289] Traceback (most recent call last):
ERROR 02-27 15:02:41 [utils.py:289]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/utils.py", line 276, in wait_for_completion_or_failure
ERROR 02-27 15:02:41 [utils.py:289]     raise RuntimeError(
ERROR 02-27 15:02:41 [utils.py:289] RuntimeError: Process ApiServer_0 (PID: 10466) died with exit code 1
INFO 02-27 15:02:41 [utils.py:292] Terminating remaining processes ...
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:02:42 [multiproc_executor.py:732] Parent process exited, terminating worker
(Worker_DP0_TP2_EP2 pid=10936) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
(Worker_DP0_TP5_EP5 pid=11575) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
(Worker_DP0_TP6_EP6 pid=11806) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
(Worker_DP0_TP3_EP3 pid=11144) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
(Worker_DP0_TP7_EP7 pid=12049) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
(Worker_DP0_TP4_EP4 pid=11356) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
(Worker_DP0_TP1_EP1 pid=10693) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
(Worker_DP0_TP0_EP0 pid=10536) INFO 02-27 15:02:42 [multiproc_executor.py:785] WorkerProc shutting down.
Traceback (most recent call last):
  File "/usr/local/python3.11.14/bin/vllm", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 108, in cmd
    run_multi_api_server(args)
  File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 282, in run_multi_api_server
    wait_for_completion_or_failure(
  File "/usr/local/python3.11.14/lib/python3.11/site-packages/vllm/v1/utils.py", line 276, in wait_for_completion_or_failure
    raise RuntimeError(
RuntimeError: Process ApiServer_0 (PID: 10466) died with exit code 1
[ERROR] 2026-02-27-15:02:47 (PID:10161, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
/usr/local/python3.11.14/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
