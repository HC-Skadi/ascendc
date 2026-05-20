# Issue #3314: [Bug]: qwen3-30b-A3b fails to start when model_len not set

## 基本信息

- **编号**: #3314
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3314
- **创建时间**: 2025-10-05T15:44:08Z
- **关闭时间**: 2025-10-24T01:37:14Z
- **更新时间**: 2025-12-30T09:38:24Z
- **提交者**: @zhujiaxin
- **评论数**: 4

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
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.2
[conda] Could not collect
vLLM Version: 0.11.0rc3
vLLM Ascend Version: 0.11.0rc0

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
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
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 99.0        44                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          63074/ 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 97.8        47                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          63130/ 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 91.4        43                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          63131/ 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 99.8        45                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          63130/ 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 94.1        43                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3383 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 97.2        45                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3380 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 100.6       44                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 96.4        44                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 4286          | VLLMWorker_TP            | 117                     |
| 0       0                 | 4287          | VLLMWorker_TP            | 117                     |
| 0       0                 | 4288          | VLLMWorker_TP            | 117                     |
| 0       0                 | 4285          | VLLMWorker_TP            | 59543                   |
+===========================+===============+====================================================+
| 1       0                 | 4286          | VLLMWorker_TP            | 59799                   |
+===========================+===============+====================================================+
| 2       0                 | 4287          | VLLMWorker_TP            | 59799                   |
+===========================+===============+====================================================+
| 3       0                 | 4288          | VLLMWorker_TP            | 59799                   |
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
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux


free -h
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       9.8Gi       1.5Ti       8.0Mi       1.2Gi       1.5Ti
Swap:             0B          0B          0B
```

</details>


### 🐛 Describe the bug

"Qwen3-30b-A3b fails to start when model_len is not set, using the Docker image quay.io/ascend/vllm-ascend:v0.11.0rc0.

Following the tutorials, I start vllm-ascend with:
```text 
vllm serve /opt/model_file/qwen3-30b-a3b --tensor-parallel-size 8 --enable_expert_parallel
```
I also try 
```text 
vllm serve /opt/model_file/qwen3-30b-a3b --tensor-parallel-size 4 --enable_expert_parallel
```
but encounter same error:
```text 
INFO 10-05 14:53:34 [parallel_state.py:1208] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 10-05 14:53:34 [parallel_state.py:1208] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 10-05 14:53:34 [parallel_state.py:1208] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 10-05 14:53:34 [parallel_state.py:1208] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 10-05 15:02:25 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-05 15:02:25 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-05 15:02:25 [multiproc_executor.py:558] Parent process exited, terminating worker
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708]     raise e from None
(EngineCore_DP0 pid=20421) ERROR 10-05 15:02:29 [core.py:708] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(EngineCore_DP0 pid=20421) Process EngineCore_DP0:
(EngineCore_DP0 pid=20421) Traceback (most recent call last):
(EngineCore_DP0 pid=20421)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=20421)     self.run()
(EngineCore_DP0 pid=20421)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=20421)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=20421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=20421)     raise e
(EngineCore_DP0 pid=20421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=20421)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=20421)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=20421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=20421)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=20421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=20421)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=20421)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=20421)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=20421)     self._init_executor()
(EngineCore_DP0 pid=20421)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=20421)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=20421)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=20421)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=20421)     raise e from None
(EngineCore_DP0 pid=20421) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(APIServer pid=20283) Traceback (most recent call last):
(APIServer pid=20283)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=20283)     sys.exit(main())
(APIServer pid=20283)              ^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=20283)     args.dispatch_function(args)
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=20283)     uvloop.run(run_server(args))
(APIServer pid=20283)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=20283)     return runner.run(wrapper())
(APIServer pid=20283)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=20283)     return self._loop.run_until_complete(task)
(APIServer pid=20283)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=20283)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=20283)     return await main
(APIServer pid=20283)            ^^^^^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=20283)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=20283)     async with build_async_engine_client(
(APIServer pid=20283)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=20283)     return await anext(self.gen)
(APIServer pid=20283)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=20283)     async with build_async_engine_client_from_engine_args(
(APIServer pid=20283)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=20283)     return await anext(self.gen)
(APIServer pid=20283)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=20283)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=20283)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1571, in inner
(APIServer pid=20283)     return fn(*args, **kwargs)
(APIServer pid=20283)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=20283)     return cls(
(APIServer pid=20283)            ^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=20283)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=20283)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=20283)     return AsyncMPClient(*client_args)
(APIServer pid=20283)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=20283)     super().__init__(
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=20283)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=20283)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=20283)     next(self.gen)
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
(APIServer pid=20283)     wait_for_engine_startup(
(APIServer pid=20283)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
(APIServer pid=20283)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=20283) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=20283) [ERROR] 2025-10-05-15:03:13 (PID:20283, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
root@pm-7df1:/workspace# /usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 120 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 5 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '```
Checking the system status, the system memory is at 100% when the error occurs.
When I set `max_model_len=65536`, everything works properly. 
So how can I use max_model_len greater than `65536`?"
