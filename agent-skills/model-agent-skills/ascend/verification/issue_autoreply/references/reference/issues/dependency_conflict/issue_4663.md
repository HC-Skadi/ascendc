# Issue #4663: [Bug]: Qwen3-Omni-30B-A3B-Thinking模型服务拉起失败

## 基本信息

- **编号**: #4663
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4663
- **创建时间**: 2025-12-03T07:37:02Z
- **关闭时间**: 2025-12-15T03:17:42Z
- **更新时间**: 2025-12-15T03:17:42Z
- **提交者**: @Zhiwen-Liu
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
root@hostname-a75s0:/workspace# python collect_env.py
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.oe2203sp3.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             256
On-line CPU(s) list:                0-255
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 7265
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 64
Socket(s):                          4
Stepping:                           0x1
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          16 MiB (256 instances)
L1i cache:                          16 MiB (256 instances)
L2 cache:                           128 MiB (256 instances)
L3 cache:                           256 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-31
NUMA node1 CPU(s):                  32-63
NUMA node2 CPU(s):                  64-95
NUMA node3 CPU(s):                  96-127
NUMA node4 CPU(s):                  128-159
NUMA node5 CPU(s):                  160-191
NUMA node6 CPU(s):                  192-223
NUMA node7 CPU(s):                  224-255
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
[pip3] torch==2.8.0
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.2.dev7+ge10703fe8 (git sha: e10703fe8)
vLLM Ascend Version: 0.11.0rc1.dev490+g0a1e0337a (git sha: 0a1e0337a)

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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 105.7       40                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3414 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 91.1        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3410 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 95.9        40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3408 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 99.7        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3409 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 94.3        45                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3409 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 97.8        43                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3409 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 99.2        43                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3409 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 98.8        44                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3409 / 65536         |
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

vllm使用版本：v0.11.2+cherry-pick 28798
vllm-ascend使用版本：main

运行启动命令：
vllm serve /data/models/Qwen3-Omni-30B-A3B-Thinking --host 0.0.0.0 --port 8000 --tensor-parallel-size 2
报错：
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815] WorkerProc hit an exception.
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 235, in determine_available_memory
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     self.model_runner.profile_run()
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3062, in profile_run
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     hidden_states = self._dummy_run(
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2971, in _dummy_run
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     self.aclgraph_dispatcher.dispatch(num_tokens=num_tokens, uniform_decode=uniform_decode, has_lora=has_lora)
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815] TypeError: CudagraphDispatcher.dispatch() got an unexpected keyword argument 'num_tokens'
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 235, in determine_available_memory
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     self.model_runner.profile_run()
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3062, in profile_run
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     hidden_states = self._dummy_run(
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2971, in _dummy_run
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815]     self.aclgraph_dispatcher.dispatch(num_tokens=num_tokens, uniform_decode=uniform_decode, has_lora=has_lora)
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815] TypeError: CudagraphDispatcher.dispatch() got an unexpected keyword argument 'num_tokens'
(Worker_TP0 pid=11211) ERROR 12-03 07:26:33 [multiproc_executor.py:815] 
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842] EngineCore failed to start.
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842] Traceback (most recent call last):
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 833, in run_engine_core
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 606, in __init__
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]     super().__init__(
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 231, in _initialize_kv_caches
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 358, in collective_rpc
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]     return aggregate(get_response())
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]                      ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 341, in get_response
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842]     raise RuntimeError(
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:33 [core.py:842] RuntimeError: Worker failed with error 'CudagraphDispatcher.dispatch() got an unexpected keyword argument 'num_tokens'', please check the stack trace above for the root cause
(EngineCore_DP0 pid=11075) ERROR 12-03 07:26:42 [multiproc_executor.py:230] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
(EngineCore_DP0 pid=11075) Process EngineCore_DP0:
(EngineCore_DP0 pid=11075) Traceback (most recent call last):
(EngineCore_DP0 pid=11075)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=11075)     self.run()
(EngineCore_DP0 pid=11075)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=11075)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 846, in run_engine_core
(EngineCore_DP0 pid=11075)     raise e
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 833, in run_engine_core
(EngineCore_DP0 pid=11075)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=11075)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 606, in __init__
(EngineCore_DP0 pid=11075)     super().__init__(
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP0 pid=11075)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=11075)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 231, in _initialize_kv_caches
(EngineCore_DP0 pid=11075)     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=11075)                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=11075)     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=11075)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 358, in collective_rpc
(EngineCore_DP0 pid=11075)     return aggregate(get_response())
(EngineCore_DP0 pid=11075)                      ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=11075)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 341, in get_response
(EngineCore_DP0 pid=11075)     raise RuntimeError(
(EngineCore_DP0 pid=11075) RuntimeError: Worker failed with error 'CudagraphDispatcher.dispatch() got an unexpected keyword argument 'num_tokens'', please check the stack trace above for the root cause
(APIServer pid=10937) Traceback (most recent call last):
(APIServer pid=10937)   File "/usr/local/python3.11.13/bin/vllm", line 7, in <module>
(APIServer pid=10937)     sys.exit(main())
(APIServer pid=10937)              ^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main
(APIServer pid=10937)     args.dispatch_function(args)
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 60, in cmd
(APIServer pid=10937)     uvloop.run(run_server(args))
(APIServer pid=10937)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
(APIServer pid=10937)     return runner.run(wrapper())
(APIServer pid=10937)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=10937)     return self._loop.run_until_complete(task)
(APIServer pid=10937)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=10937)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=10937)     return await main
(APIServer pid=10937)            ^^^^^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 2024, in run_server
(APIServer pid=10937)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 2043, in run_server_worker
(APIServer pid=10937)     async with build_async_engine_client(
(APIServer pid=10937)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=10937)     return await anext(self.gen)
(APIServer pid=10937)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 195, in build_async_engine_client
(APIServer pid=10937)     async with build_async_engine_client_from_engine_args(
(APIServer pid=10937)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=10937)     return await anext(self.gen)
(APIServer pid=10937)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 236, in build_async_engine_client_from_engine_args
(APIServer pid=10937)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=10937)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/utils/func_utils.py", line 116, in inner
(APIServer pid=10937)     return fn(*args, **kwargs)
(APIServer pid=10937)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 203, in from_vllm_config
(APIServer pid=10937)     return cls(
(APIServer pid=10937)            ^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 133, in __init__
(APIServer pid=10937)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=10937)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 121, in make_async_mp_client
(APIServer pid=10937)     return AsyncMPClient(*client_args)
(APIServer pid=10937)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 808, in __init__
(APIServer pid=10937)     super().__init__(
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 469, in __init__
(APIServer pid=10937)     with launch_core_engines(vllm_config, executor_class, log_stats) as (
(APIServer pid=10937)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=10937)     next(self.gen)
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 907, in launch_core_engines
(APIServer pid=10937)     wait_for_engine_startup(
(APIServer pid=10937)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 964, in wait_for_engine_startup
(APIServer pid=10937)     raise RuntimeError(
(APIServer pid=10937) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=10937) [ERROR] 2025-12-03-07:26:44 (PID:10937, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
