# Issue #2315: [Bug]: vllm-ascend v0.9.2rc1-310p always crash (with ERR99999 UNKNOWN application exception) when running in Server with Ascend-310P3 NPU

## 基本信息

- **编号**: #2315
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2315
- **创建时间**: 2025-08-11T08:57:53Z
- **关闭时间**: 2025-12-23T11:32:06Z
- **更新时间**: 2025-12-23T11:32:07Z
- **提交者**: @kylewanginchina
- **评论数**: 3

## 标签

bug; 310p

## 问题描述

### Your current environment

[root@server01 ~]# npu-smi info

NPU-SMI 24.1.0.1                          Version: 24.1.0.1
+--------------------------------------------------------------------------------------------------+
| NPU   Chip        Name/       Health   | Power(W)   Temp(C)      Memory-Usage(MB)   Hugepages-Usage(page) |
| Device            Bus-Id               | AICore(%)                                                     |
|==================================================================================================|
| 1792  310P3       OK          NA       47               3404 / 44280           0 / 0               |
| 0                 0000:07:00.0         0                NA                                             |
+--------------------------------------------------------------------------------------------------+
| 1792  310P3       OK          NA       47               263 / 43693            0 / 0               |
| 1                 0000:07:00.0         0                NA                                             |
+--------------------------------------------------------------------------------------------------+
| NPU     Chip          Process Id     Process Name     Process Memory(MB)                             |
+--------------------------------------------------------------------------------------------------+
| No running processes found in NPU 1792                                                           |
+--------------------------------------------------------------------------------------------------+

### 🐛 Describe the bug

[root@server01 data]# export IMAGE=quay.io/ascend/vllm-ascend:v0.9.2rc1-310p
[root@server01 data]# docker run -d \
> --name vllm-ascend \
> --device /dev/davinci0 \
> --device /dev/davinci1 \
> --device /dev/davinci_manager \
> --device /dev/devmm_svm \
> --device /dev/hisi_hdc \
> -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
> -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
> -v /etc/ascend_install.info:/etc/ascend_install.info \
> -v /root/.cache:/root/.cache \
> -p 800:800 \
> -v /data/deepflow:/mnt \
> -e VLLM_LOG_CONF_FILE=/root/true \
> -e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 \
> --restart=unless-stopped $IMAGE \
> vllm serve /mnt/Qwen3-32B --tensor-parallel-size 2 --max-model-len 16384 --gpu-memory-utilization 0.9 --port 800
WARNING: IPv4 forwarding is disabled. Networking will not work.
3a64672f9b2a76f34f83464d6e7af2810744a801f133587dbd8952
[root@server01 data]# docker ps
CONTAINER ID   IMAGE                                     COMMAND                  CREATED          STATUS          PORTS                    NAMES
3a64672f9b2a   quay.io/ascend/vllm-ascend:v0.9.2rc1-310p   "/bin/bash -c '...'"   9 seconds ago    Up 8 seconds    0.0.0.0:800->800/tcp   vllm-ascend

(Note: there maybe some words error because the content is extracted from picture base on OCR)

INFO 08-08 07:32:48 | _init_.py:41] All plugins in this group will be loaded. Set 'VLLM_PLUGINS' to control which plugins to load.
INFO 08-08 07:32:48 | _init_.py:239] platform plugin ascend is activated
INFO 08-08 07:32:48 | _init_.py:39] Available plugins for group vllm.platform_plugins:
INFO 08-08 07:32:48 | _init_.py:41] ascend -> vllm.ascend:register
INFO 08-08 07:32:48 | _init_.py:44] All plugins in this group will be loaded. Set 'VLLM_PLUGINS' to control which plugins to load.
INFO 08-08 07:32:48 | _init_.py:235] platform plugin ascend is activated
WARNING 08-08 07:32:50 | custom_op.py:28] Failed to import triton_utils_v2 with ModuleNotFoundError("No module named 'vllm._C'").
INFO 08-08 07:32:53 | importing.py:89] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 08-08 07:32:53 | importing.py:89] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 08-08 07:32:53 | importing.py:89] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture deepseekMTPModel is already registered, and will be overwritten by the new model class vllm.ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture Qwen2VForConditionalGeneration is already registered, and will be overwritten by the new model class vllm.ascend.models.qwen2_5_vl:AscendQwen2VForConditionalGeneration.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture Qwen2_5_VlForConditionalGeneration is already registered, and will be overwritten by the new model class vllm.ascend.models.qwen2_5_vl:AscendQwen2_5_VlForConditionalGeneration.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm.ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm.ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm.ascend.models.qwen3_moe:CustomQwenMoeForCausalLM.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture DeepseekHTTPModel is already registered, and will be overwritten by the new model class vllm.ascend.models.deepseek_http:CustomHTTPModel.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture Qwen2VlForConditionalGeneration is already registered, and will be overwritten by the new model class vllm.ascend.models.qwen2_vl:AscendQwen2VlForConditionalGeneration.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture Qwen2_5_VlForConditionalGeneration is already registered, and will be overwritten by the new model class vllm.ascend.models.qwen2_5_vl:AscendQwen2_5_VlForConditionalGeneration.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm.ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm.ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 08-08 07:32:53 | registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm.ascend.models.qwen3_moe:CustomQwenMoeForCausalLM.
(vllmworker rank=0 pid=357) INFO 08-08 07:32:54 |shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_rank=0), buffer_handle=(1, 10485760, 10, 'psm_b079cd08'), local_subscribe_addr='/tmp/tmpcfec2ea-86a2-45b7-880f-324f2a795caa', remote_subscribe_addr=None, remote_addr=(pvd=False)
(vllmworker rank=1 pid=358) INFO 08-08 07:32:54 |shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_rank=0), buffer_handle=(
WARNING 08-08 07:32:53 | registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm.ascend.models.qwen3_moe:CustomQwenMoeForCausalLM.
(vllmworker rank=0 pid=357) INFO 08-08 07:32:54 |shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_rank=0), buffer_handle=(1, 10485760, 10, 'psm_b079cd08'), local_subscribe_addr='/tmp/tmpcfec2ea-86a2-45b7-880f-324f2a795caa', remote_subscribe_addr=None, remote_addr=(pvd=False)
(vllmworker rank=1 pid=358) INFO 08-08 07:32:54 |shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_rank=0), buffer_handle=(1, 10485760, 10, 'psm_92919c15'), local_subscribe_addr='/tmp/tmp7aa14a22-c51f-4f70-ac8f-23e3e199f101', remote_subscribe_addr=None, remote_addr=(pvd=False)
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] WorkerProc failed to start.
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] Traceback (most recent call last):
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   File "/vllm-workspace/vllm/vllm/executor/multiprocess_executor.py", line 461, in worker_main
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]     worker = WorkerProc(*args, **kwargs)
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   File "/vllm-workspace/vllm/vllm/executor/multiprocess_executor.py", line 357, in __init__
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]     self.worker.init_device()
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   File "/vllm-workspace/vllm/vllm/worker/base.py", line 606, in init_device
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]     self.worker.init_device() # type: ignore
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   File "/vllm-workspace/vllm/vllm/ascend/worker/worker_vl.py", line 132, in init_device
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]     NPUPlatform.set_device(device)
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   File "/vllm-workspace/vllm/vllm/ascend/platform.py", line 90, in torch_npu_set_device
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]     torch.npu.set_device(device)
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   File "/usr/local/python3.10/site-packages/torch_npu/npu/utils.py", line 80, in set_device
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]     torch.npu._C.npu_setDevice(device_id)
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] RuntimeError: SetPrecisionMode:Build/Makefiles/torch_npu.dir/compiler/depll-ts-1st/csrc/function_error_at_npu_native:aclrtSetCompileOpt(aclCompileOpt::ACL_PRECISION_MODE, precision_mode), error code is 500001
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] ERROR 2025-08-08 07:32:55.177.929 357:rankd-1|/pytorch_deploy-v1.1-eacp-whl/torch_npu/csrc/core/npu/NPUFunctions.cpp:216] aclrtSetCompileOpt failed,ret:500001
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] [Error]: The internal ACL of the system is incorrect.
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] Rectify the fault based on the error information in the ascend log
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] EH9999: [pid: 357] 2025-08-08-07:32:55.177.931 [Inner] [PLATFORM]PlatformInfoInit runtime platform info failed. SocVersion Ascend@910B[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] EH9999: [pid: 357] 2025-08-08-07:32:55.177.931 [Inner] [PLATFORM]PlatformInfoInit runtime platform info failed. SocVersion Ascend@910B[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487] Traceback (most recent call last):
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   GELIB: [INNER]Initialize failed. [FUNC:][Initialize][FILE:ge_lib.cc][LINE:384]
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   GEInitialize failed [FUNC:GeInitialize][FILE:ge_api.cc][LINE:371]
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   [Initialize][GE]GEInitialize failed. ge result = 4294967295 [FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:161]
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   [Init][Compiler]Init compiler failed [FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
(vllmworker rank=0 pid=357) ERROR 08-08 07:32:55 |multiprocess_executor.py:487]   [Set][Options]OpCompilerProcessor init failed [FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
ERROR 08-08 07:32:59 |core.py:586] EngineCore failed to start.
ERROR 08-08 07:32:59 |core.py:586] Traceback (most recent call last):
ERROR 08-08 07:32:59 |core.py:586]   File "/vllm-workspace/vllm/vllm/engine/core.py", line 577, in run_engine_core
ERROR 08-08 07:32:59 |core.py:586]     engine_core.engine.init_workers(self)
ERROR 08-08 07:32:59 |core.py:586]   File "/vllm-workspace/vllm/vllm/engine/core.py", line 404, in __init__
ERROR 08-08 07:32:59 |core.py:586]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 08-08 07:32:59 |core.py:586]   File "/vllm-workspace/vllm/vllm/engine/core.py", line 75, in __init__
ERROR 08-08 07:32:59 |core.py:586]     self.model_executor = executor_class(vllm_config)
ERROR 08-08 07:32:59 |core.py:586]   File "/vllm-workspace/vllm/vllm/executor/base.py", line 53, in __init__
ERROR 08-08 07:32:59 |core.py:586]     self._init_executor()
ERROR 08-08 07:32:59 |core.py:586]   File "/vllm-workspace/vllm/vllm/executor/multiprocess_executor.py", line 95, in _init_executor
ERROR 08-08 07:32:59 |core.py:586]     self.workers = WorkerProc.init_for_ready(unready_workers)
ERROR 08-08 07:32:59 |core.py:586]   File "/vllm-workspace/vllm/vllm/executor/multiprocess_executor.py", line 422, in wait_for_ready
ERROR 08-08 07:32:59 |core.py:586]     raise e from None
ERROR 08-08 07:32:59 |core.py:586] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
Process EngineCore:
Traceback (most recent call last):
  File "/usr/local/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 590, in run_engine_core
    raise e
Traceback (most recent call last):
  File "/usr/local/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 590, in run_engine_core
    raise e
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 577, in run_engine_core
    engine_core.engine.init_workers(self)
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 404, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 75, in __init__
    self.model_executor = executor_class(vllm_config)
  File "/vllm-workspace/vllm/vllm/executor/base.py", line 53, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/executor/multiprocess_executor.py", line 95, in _init_executor
    self.workers = WorkerProc.init_for_ready(unready_workers)
  File "/vllm-workspace/vllm/vllm/executor/multiprocess_executor.py", line 422, in wait_for_ready
    raise e from None
Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/vllm-0.4.0-py3.10-linux-x86_64.egg/vllm/entrypoints/vllm_cli.py", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli_main.py", line 65, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli_serve.py", line 55, in cmd
    loop.run_until_complete(
  File "/usr/local/python3.10/asyncio/base_events.py", line 62, in run_until_complete
    return future.result()
  File "/usr/local/python3.10/asyncio/base_events.py", line 1518, in loop_run_until_complete
    self._run_once()
  File "/usr/local/python3.10/asyncio/base_events.py", line 61, in _run_once
    handle._run()
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1431, in run_server
    await run_server_worker(listen_address, sock, args, **kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1451, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10/contextlib.py", line 199, in __aenter__
    return await self.gen.__anext__()
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/contextlib.py", line 199, in __aenter__
    return await self.gen.__anext__()
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/engine/async_llm.py", line 162, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 124, in __init__
    self.engine_core = EngineCoreProc(self.max_async_mp_client)
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 463, in __init__
    self.process.start()
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 596, in __init__
    with launch_engine_cores(vllm_config, executor_class,
  File "/usr/local/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 604, in launch_engine_cores
    wait_for_engine_startup()
  File "/vllm-workspace/vllm/vllm/engine/utils.py", line 484, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed.")
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli_serve.py", line 55, in cmd
    loop.run_until_complete(
  File "/usr/local/python3.10/asyncio/base_events.py", line 62, in run_until_complete
    return future.result()
  File "/usr/local/python3.10/asyncio/base_events.py", line 1518, in loop_run_until_complete
    self._run_once()
  File "/usr/local/python3.10/asyncio/base_events.py", line 61, in _run_once
    handle._run()
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1431, in run_server
    await run_server_worker(listen_address, sock, args, **kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1451, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10/contextlib.py", line 199, in __aenter__
    return await self.gen.__anext__()
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/contextlib.py", line 199, in __aenter__
    return await self.gen.__anext__()
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
    async_llm = AsyncLLM.from_vllm_config(
  File "/vllm-workspace/vllm/vllm/engine/async_llm.py", line 162, in from_vllm_config
    return cls(
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 124, in __init__
    self.engine_core = EngineCoreProc(self.max_async_mp_client)
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 463, in __init__
    with launch_engine_cores(vllm_config, executor_class,
  File "/usr/local/python3.10/contextlib.py", line 142, in __exit__
    next(self.gen)
  File "/vllm-workspace/vllm/vllm/engine/core.py", line 604, in launch_engine_cores
    wait_for_engine_startup()
  File "/vllm-workspace/vllm/vllm/engine/utils.py", line 484, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed.")
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): [0]
[2025-08-08 07:32:55.210] [data] [PID:1, Device: -1] [RANKID:-1] ERR99999 UNKNOWN application exception
