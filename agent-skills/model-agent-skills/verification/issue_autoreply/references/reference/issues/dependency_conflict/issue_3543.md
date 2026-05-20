# Issue #3543: [Misc]: Qwen3-VL-30B-A3B-Instruct部署报错

## 基本信息

- **编号**: #3543
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3543
- **创建时间**: 2025-10-20T03:54:24Z
- **关闭时间**: 2025-10-23T01:30:36Z
- **更新时间**: 2025-10-27T07:19:14Z
- **提交者**: @Sunxiaohu0406
- **评论数**: 4

## 标签

module:multimodal

## 问题描述

### Anything you want to discuss about vllm on ascend.

镜像：quay.io/ascend/vllm-ascend:v0.11.0rc0

容器：
docker run --name vllm-ascend -it -d --ipc=host \
--privileged=true \
-w /data \
--device=/dev/davinci0 \
--device=/dev/davinci1 \
--device=/dev/davinci2 \
--device=/dev/davinci3 \
--device=/dev/davinci4 \
--device=/dev/davinci5 \
--device=/dev/davinci6 \
--device=/dev/davinci7 \
--device=/dev/davinci_manager \
--device=/dev/hisi_hdc \
--device=/dev/devmm_svm \
--entrypoint=bash \
-v /usr/local/Ascend/driver:/usr/local/Ascend/driver \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/sbin:/usr/local/sbin \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /data:/data \
-v /tmp:/tmp \
-v /usr/share/zoneinfo/Asia/Shanghai:/etc/localtime \
-p 50066:50066 \
-e http_proxy=$http_proxy \
-e https_proxy=$https_proxy \
quay.io/ascend/vllm-ascend:v0.11.0rc0


服务：
vllm serve /data/test/Qwen3-VL-30B-A3B-Instruct \
--host 0.0.0.0 \
--port 50066 \
--served-model-name qwen3vl \
--tensor-parallel-size 4 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.85



报错：
al_subscribe_addr='ipc:///tmp/1cf29284-4fd8-4ba3-bed1-539848833442', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 10-20 11:34:15 [parallel_state.py:1208] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 10-20 11:34:15 [parallel_state.py:1208] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 10-20 11:34:15 [parallel_state.py:1208] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3, EP rank 3
INFO 10-20 11:34:15 [parallel_state.py:1208] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2, EP rank 2
INFO 10-20 11:48:01 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-20 11:48:01 [multiproc_executor.py:558] Parent process exited, terminating worker
INFO 10-20 11:48:01 [multiproc_executor.py:558] Parent process exited, terminating worker
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708]     raise e from None
(EngineCore_DP0 pid=703) ERROR 10-20 11:48:05 [core.py:708] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(EngineCore_DP0 pid=703) Process EngineCore_DP0:
(EngineCore_DP0 pid=703) Traceback (most recent call last):
(EngineCore_DP0 pid=703)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=703)     self.run()
(EngineCore_DP0 pid=703)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=703)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=703)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=703)     raise e
(EngineCore_DP0 pid=703)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=703)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=703)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=703)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=703)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=703)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=703)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=703)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=703)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=703)     self._init_executor()
(EngineCore_DP0 pid=703)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 106, in _init_executor
(EngineCore_DP0 pid=703)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=703)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=703)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 509, in wait_for_ready
(EngineCore_DP0 pid=703)     raise e from None
(EngineCore_DP0 pid=703) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
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
(APIServer pid=432) Traceback (most recent call last):
(APIServer pid=432)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=432)     sys.exit(main())
(APIServer pid=432)              ^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=432)     args.dispatch_function(args)
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=432)     uvloop.run(run_server(args))
(APIServer pid=432)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=432)     return runner.run(wrapper())
(APIServer pid=432)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=432)     return self._loop.run_until_complete(task)
(APIServer pid=432)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=432)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=432)     return await main
(APIServer pid=432)            ^^^^^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=432)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=432)     async with build_async_engine_client(
(APIServer pid=432)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=432)     return await anext(self.gen)
(APIServer pid=432)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=432)     async with build_async_engine_client_from_engine_args(
(APIServer pid=432)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=432)     return await anext(self.gen)
(APIServer pid=432)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
(APIServer pid=432)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=432)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1571, in inner
(APIServer pid=432)     return fn(*args, **kwargs)
(APIServer pid=432)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
(APIServer pid=432)     return cls(
(APIServer pid=432)            ^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=432)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=432)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=432)     return AsyncMPClient(*client_args)
(APIServer pid=432)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
(APIServer pid=432)     super().__init__(
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
(APIServer pid=432)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=432)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=432)     next(self.gen)
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
(APIServer pid=432)     wait_for_engine_startup(
(APIServer pid=432)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
(APIServer pid=432)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=432) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore_DP0': 1}
(APIServer pid=432) [ERROR] 2025-10-20-11:48:57 (PID:432, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 120 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 5 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

