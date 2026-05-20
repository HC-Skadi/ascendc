# Issue #3901: [Bug]: Qwen3-VL-30B-A3B-Instruct deploy failed.

## 基本信息

- **编号**: #3901
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3901
- **创建时间**: 2025-10-30T09:55:16Z
- **关闭时间**: 2025-10-31T01:58:54Z
- **更新时间**: 2025-10-31T01:58:54Z
- **提交者**: @ghost
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<img width="686" height="455" alt="Image" src="https://github.com/user-attachments/assets/e3616225-72d8-4e40-b6bf-87bc63949c10" />

CANN=8.2.RC1
vllm=0.11.0rc3
vllm-ascend=0.11.0rc1.dev0


### 🐛 Describe the bug

vllm serve Qwen3-VL-30B-A3B-Instruct -tp=4 --enable-expert-parallel

INFO 10-30 17:36:53 [parallel_state.py:1208] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 10-30 17:36:53 [parallel_state.py:1208] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 10-30 17:36:53 [parallel_state.py:1208] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 10-30 17:36:53 [parallel_state.py:1208] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 10-30 17:45:22 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-30 17:45:22 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-30 17:45:22 [multiproc_executor.py:558] Parent process exited, terminating worker
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]   File "/data/qiuyuan/MLLM/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]   File "/data/qiuyuan/MLLM/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]   File "/data/qiuyuan/MLLM/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708]     raise e from None
(EngineCore_DP0 pid=3497884) ERROR 10-30 17:45:26 [core.py:708] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
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
(EngineCore_DP0 pid=3497884) Process EngineCore_DP0:
(EngineCore_DP0 pid=3497884) Traceback (most recent call last):
(EngineCore_DP0 pid=3497884)   File "/data/miniconda3/envs/swift_vllm/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=3497884)     self.run()
(EngineCore_DP0 pid=3497884)   File "/data/miniconda3/envs/swift_vllm/lib/python3.10/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=3497884)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=3497884)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=3497884)     raise e
(EngineCore_DP0 pid=3497884)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=3497884)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=3497884)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=3497884)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=3497884)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=3497884)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=3497884)   File "/data/qiuyuan/MLLM/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=3497884)     self._init_executor()
(EngineCore_DP0 pid=3497884)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=3497884)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=3497884)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=3497884)     raise e from None
(EngineCore_DP0 pid=3497884) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(APIServer pid=3496060) Traceback (most recent call last):
(APIServer pid=3496060)   File "/data/miniconda3/envs/swift_vllm/bin/vllm", line 7, in <module>
(APIServer pid=3496060)     sys.exit(main())
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=3496060)     args.dispatch_function(args)
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=3496060)     uvloop.run(run_server(args))
(APIServer pid=3496060)   File "/data/miniconda3/envs/swift_vllm/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
(APIServer pid=3496060)     return loop.run_until_complete(wrapper())
(APIServer pid=3496060)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=3496060)   File "/data/miniconda3/envs/swift_vllm/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=3496060)     return await main
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=3496060)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=3496060)     async with build_async_engine_client(
(APIServer pid=3496060)   File "/data/miniconda3/envs/swift_vllm/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=3496060)     return await anext(self.gen)
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=3496060)     async with build_async_engine_client_from_engine_args(
(APIServer pid=3496060)   File "/data/miniconda3/envs/swift_vllm/lib/python3.10/contextlib.py", line 199, in __aenter__
(APIServer pid=3496060)     return await anext(self.gen)
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=3496060)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/utils/__init__.py", line 1571, in inner
(APIServer pid=3496060)     return fn(*args, **kwargs)
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=3496060)     return cls(
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=3496060)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=3496060)     return AsyncMPClient(*client_args)
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=3496060)     super().__init__(
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=3496060)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=3496060)   File "/data/miniconda3/envs/swift_vllm/lib/python3.10/contextlib.py", line 142, in __exit__
(APIServer pid=3496060)     next(self.gen)
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
(APIServer pid=3496060)     wait_for_engine_startup(
(APIServer pid=3496060)   File "/data/qiuyuan/MLLM/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
(APIServer pid=3496060)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=3496060) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=3496060) [ERROR] 2025-10-30-17:46:12 (PID:3496060, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
