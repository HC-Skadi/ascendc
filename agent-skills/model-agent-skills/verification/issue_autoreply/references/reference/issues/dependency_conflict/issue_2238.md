# Issue #2238: [Bug]: 使用的docker，机子上有8张卡，启动1个模型没问题，但同时启动2个模型会报错

## 基本信息

- **编号**: #2238
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2238
- **创建时间**: 2025-08-06T06:48:50Z
- **关闭时间**: 2025-08-06T07:43:00Z
- **更新时间**: 2025-10-21T02:38:24Z
- **提交者**: @penond
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

gpu：ascend 910b
vllm: 0.9.2
vllm-ascend: 0.9.2

### 🐛 Describe the bug

启动命令1：【正常】
docker run --restart=always \
--name vllm-1 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /data/models/Qwen2.5-VL-7B-Instruct:/data/Qwen2.5-VL-7B-Instruct \
-p 8111:8000 \
-e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 \
-it $IMAGE \
vllm serve /data/Qwen2.5-VL-7B-Instruct --served-model-name Qwen2.5-VL-7B-Instruct --tensor-parallel-size 4

第二个启动命令：【失败】
docker run --restart=always \
--name vllm-2 \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /data/models/Qwen2.5-VL-32B-Instruct:/data/Qwen2.5-VL-32B-Instruct \
-p 8222:8000 \
-e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 \
-it $IMAGE \
vllm serve /data/Qwen2.5-VL-32B-Instruct --served-model-name Qwen2.5-VL-32B-Instruct --tensor-parallel-size 4

第二个启动命令的异常信息：
[ERROR] RUNTIME(557,python3):2025-08-06-06:31:38.004.461 [api_impl.cc:5925]557 GetDevErrMsg:ctx is NULL!
[ERROR] RUNTIME(557,python3):2025-08-06-06:31:38.004.531 [api_impl.cc:6001]557 GetDevMsg:Failed to GetDeviceErrMsg, retCode=0x7070001.
[ERROR] RUNTIME(557,python3):2025-08-06-06:31:38.004.583 [api_error.cc:3864]557 GetDevMsg:GetDeviceMsg failed, getMsgType=0.
[ERROR] RUNTIME(557,python3):2025-08-06-06:31:38.004.639 [api_c_device.cc:450]557 rtGetDevMsg:ErrCode=107002, desc=[context pointer null], InnerCode=0x7070001
[ERROR] RUNTIME(557,python3):2025-08-06-06:31:38.004.690 [error_message_manage.cc:48]557 FuncErrorReason:report error module_name=EE1001
[ERROR] RUNTIME(557,python3):2025-08-06-06:31:38.004.741 [error_message_manage.cc:48]557 FuncErrorReason:rtGetDevMsg execute failed, reason=[context pointer null]
[ERROR] IDEDD(554,python3):2025-08-06-06:31:38.494.860 [adx_dsmi.cpp:54][tid:588] Get physical device number failed, err: 87
[ERROR] IDEDD(556,python3):2025-08-06-06:31:38.497.603 [adx_dsmi.cpp:54][tid:591] Get physical device number failed, err: 87
[ERROR] IDEDD(555,python3):2025-08-06-06:31:38.499.922 [adx_dsmi.cpp:54][tid:594] Get physical device number failed, err: 87
[ERROR] IDEDD(557,python3):2025-08-06-06:31:38.500.306 [adx_dsmi.cpp:54][tid:597] Get physical device number failed, err: 87
[ERROR] IDEDD(554,python3):2025-08-06-06:31:38.995.165 [adx_dsmi.cpp:54][tid:588] Get physical device number failed, err: 87
[ERROR] IDEDD(556,python3):2025-08-06-06:31:38.997.999 [adx_dsmi.cpp:54][tid:591] Get physical device number failed, err: 87
[ERROR] IDEDD(555,python3):2025-08-06-06:31:39.000.301 [adx_dsmi.cpp:54][tid:594] Get physical device number failed, err: 87
[ERROR] IDEDD(557,python3):2025-08-06-06:31:39.000.483 [adx_dsmi.cpp:54][tid:597] Get physical device number failed, err: 87
[INFO] IDEDD(554,python3):2025-08-06-06:31:39.495.339 [adx_server_manager.cpp:236][tid:588] server manager stop
[INFO] IDEDD(556,python3):2025-08-06-06:31:39.498.198 [adx_server_manager.cpp:236][tid:591] server manager stop
[INFO] IDEDD(555,python3):2025-08-06-06:31:39.500.496 [adx_server_manager.cpp:236][tid:594] server manager stop
[INFO] IDEDD(557,python3):2025-08-06-06:31:39.500.608 [adx_server_manager.cpp:236][tid:597] server manager stop
[INFO] RUNTIME(554,python3):2025-08-06-06:31:39.885.422 [runtime.cc:1540] 554 ~Runtime: deconstruct runtime
[INFO] RUNTIME(554,python3):2025-08-06-06:31:39.887.381 [runtime.cc:1547] 554 ~Runtime: wait monitor success, use=0.
[INFO] RUNTIME(554,python3):2025-08-06-06:31:39.889.130 [task_fail_callback_data_manager.cc:63] 554 ~TaskFailCallBackManager: Destructor.
[INFO] RUNTIME(556,python3):2025-08-06-06:31:39.926.419 [runtime.cc:1540] 556 ~Runtime: deconstruct runtime
[INFO] RUNTIME(556,python3):2025-08-06-06:31:39.928.476 [runtime.cc:1547] 556 ~Runtime: wait monitor success, use=0.
[INFO] RUNTIME(556,python3):2025-08-06-06:31:39.930.163 [task_fail_callback_data_manager.cc:63] 556 ~TaskFailCallBackManager: Destructor.
[INFO] RUNTIME(557,python3):2025-08-06-06:31:39.976.142 [runtime.cc:1540] 557 ~Runtime: deconstruct runtime
[INFO] RUNTIME(557,python3):2025-08-06-06:31:39.978.081 [runtime.cc:1547] 557 ~Runtime: wait monitor success, use=0.
[INFO] RUNTIME(557,python3):2025-08-06-06:31:39.979.815 [task_fail_callback_data_manager.cc:63] 557 ~TaskFailCallBackManager: Destructor.
[INFO] RUNTIME(555,python3):2025-08-06-06:31:39.995.301 [runtime.cc:1540] 555 ~Runtime: deconstruct runtime
[INFO] RUNTIME(555,python3):2025-08-06-06:31:39.997.152 [runtime.cc:1547] 555 ~Runtime: wait monitor success, use=0.
[INFO] RUNTIME(555,python3):2025-08-06-06:31:39.998.901 [task_fail_callback_data_manager.cc:63] 555 ~TaskFailCallBackManager: Destructor.
ERROR 08-06 06:31:40 [core.py:586] EngineCore failed to start.
ERROR 08-06 06:31:40 [core.py:586] Traceback (most recent call last):
ERROR 08-06 06:31:40 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core
ERROR 08-06 06:31:40 [core.py:586]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 08-06 06:31:40 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 404, in __init__
ERROR 08-06 06:31:40 [core.py:586]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 08-06 06:31:40 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 75, in __init__
ERROR 08-06 06:31:40 [core.py:586]     self.model_executor = executor_class(vllm_config)
ERROR 08-06 06:31:40 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
ERROR 08-06 06:31:40 [core.py:586]     self._init_executor()
ERROR 08-06 06:31:40 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 93, in _init_executor
ERROR 08-06 06:31:40 [core.py:586]     self.workers = WorkerProc.wait_for_ready(unready_workers)
ERROR 08-06 06:31:40 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 422, in wait_for_ready
ERROR 08-06 06:31:40 [core.py:586]     raise e from None
ERROR 08-06 06:31:40 [core.py:586] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 590, in run_engine_core
    raise e
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 404, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 75, in __init__
    self.model_executor = executor_class(vllm_config)
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 93, in _init_executor
    self.workers = WorkerProc.wait_for_ready(unready_workers)
  File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 422, in wait_for_ready
    raise e from None
Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
[INFO] RUNTIME(421,python3):2025-08-06-06:31:41.610.166 [task_fail_callback_data_manager.cc:63] 421 ~TaskFailCallBackManager: Destructor.
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 65, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 55, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1431, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1451, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 162, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 124, in __init__
    self.engine_core = EngineCoreClient.make_async_mp_client(
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 96, in make_async_mp_client
    return AsyncMPClient(*client_args)
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 666, in __init__
    super().__init__(
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 403, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 434, in launch_core_engines
    wait_for_engine_startup(
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 484, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-08-06-06:31:41 (PID:281, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
[INFO] RUNTIME(281,python3):2025-08-06-06:31:43.316.867 [task_fail_callback_data_manager.cc:63] 281 ~TaskFailCallBackManager: Destructor.

