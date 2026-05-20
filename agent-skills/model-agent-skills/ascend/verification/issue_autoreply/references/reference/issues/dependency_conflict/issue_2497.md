# Issue #2497: [Bug]: Qwen3-235B-A22B-W8A8 跑不起来

## 基本信息

- **编号**: #2497
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2497
- **创建时间**: 2025-08-22T09:49:11Z
- **关闭时间**: 2025-11-11T13:22:04Z
- **更新时间**: 2025-11-11T13:22:04Z
- **提交者**: @qxde01
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

git clone 20250822  vllm-ascend 代码，build ubuntu docker 镜像

` vllm serve /data/models/Qwen3-235B-A22B-W8A8 --tensor-parallel-size 8 --max-model-len 32768 --served-model-name qwen3 --quantization ascend`
报错：
(VllmWorker TP2 pid=21356) INFO 08-22 09:46:10 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP4 pid=21358) INFO 08-22 09:46:10 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP1 pid=21355) INFO 08-22 09:46:10 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP5 pid=21359) INFO 08-22 09:46:10 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP7 pid=21361) INFO 08-22 09:46:11 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP3 pid=21357) INFO 08-22 09:46:11 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP6 pid=21360) INFO 08-22 09:46:11 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP0 pid=21354) INFO 08-22 09:46:11 [model_runner_v1.py:2145] Starting to load model /data/models/Qwen3-235B-A22B-W8A8...
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559] WorkerProc failed to start.
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559] Traceback (most recent call last):
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 533, in worker_main
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     worker = WorkerProc(*args, **kwargs)
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 402, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.worker.load_model()
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 236, in load_model
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.model_runner.load_model()
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2148, in load_model
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 118, in get_model
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     return loader.load_model(vllm_config=vllm_config,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 44, in load_model
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     model = initialize_model(vllm_config=vllm_config,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 348, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.model = CustomQwen3MoeModel(vllm_config=vllm_config,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 183, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 269, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                                                     ^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 640, in make_layers
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                                                      ^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 641, in <listcomp>
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 271, in <lambda>
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     lambda prefix: CustomQwen3MoeDecoderLayer(
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 146, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.self_attn = Qwen3MoeAttention(
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                      ^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 215, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 941, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     super().__init__(input_size=input_size,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 494, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     super().__init__(input_size,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 269, in __init__
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     if self.is_layer_skipped_ascend(prefix,
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 130, in is_layer_skipped_ascend
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP1 pid=21355) ERROR 08-22 09:46:12 [multiproc_executor.py:559] KeyError: 'model.layers.0.self_attn.q_proj.weight'
(VllmWorker TP1 pid=21355) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(VllmWorker TP5 pid=21359) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(VllmWorker TP3 pid=21357) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(VllmWorker TP6 pid=21360) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(VllmWorker TP4 pid=21358) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(VllmWorker TP2 pid=21356) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(VllmWorker TP0 pid=21354) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(VllmWorker TP7 pid=21361) INFO 08-22 09:46:12 [multiproc_executor.py:520] Parent process exited, terminating worker
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700] EngineCore failed to start.
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700] Traceback (most recent call last):
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 691, in run_engine_core
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 492, in __init__
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 80, in __init__
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]     self.model_executor = executor_class(vllm_config)
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]     self._init_executor()
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 96, in _init_executor
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 472, in wait_for_ready
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700]     raise e from None
(EngineCore_0 pid=21218) ERROR 08-22 09:46:16 [core.py:700] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_0 pid=21218) Process EngineCore_0:
(EngineCore_0 pid=21218) Traceback (most recent call last):
(EngineCore_0 pid=21218)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_0 pid=21218)     self.run()
(EngineCore_0 pid=21218)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_0 pid=21218)     self._target(*self._args, **self._kwargs)
(EngineCore_0 pid=21218)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 704, in run_engine_core
(EngineCore_0 pid=21218)     raise e
(EngineCore_0 pid=21218)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 691, in run_engine_core
(EngineCore_0 pid=21218)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_0 pid=21218)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=21218)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 492, in __init__
(EngineCore_0 pid=21218)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_0 pid=21218)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 80, in __init__
(EngineCore_0 pid=21218)     self.model_executor = executor_class(vllm_config)
(EngineCore_0 pid=21218)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=21218)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_0 pid=21218)     self._init_executor()
(EngineCore_0 pid=21218)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 96, in _init_executor
(EngineCore_0 pid=21218)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_0 pid=21218)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=21218)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 472, in wait_for_ready
(EngineCore_0 pid=21218)     raise e from None
(EngineCore_0 pid=21218) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(APIServer pid=20948) Traceback (most recent call last):
(APIServer pid=20948)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=20948)     sys.exit(main())
(APIServer pid=20948)              ^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=20948)     args.dispatch_function(args)
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 50, in cmd
(APIServer pid=20948)     uvloop.run(run_server(args))
(APIServer pid=20948)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=20948)     return runner.run(wrapper())
(APIServer pid=20948)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=20948)     return self._loop.run_until_complete(task)
(APIServer pid=20948)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=20948)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=20948)     return await main
(APIServer pid=20948)            ^^^^^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1850, in run_server
(APIServer pid=20948)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1870, in run_server_worker
(APIServer pid=20948)     async with build_async_engine_client(
(APIServer pid=20948)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=20948)     return await anext(self.gen)
(APIServer pid=20948)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 178, in build_async_engine_client
(APIServer pid=20948)     async with build_async_engine_client_from_engine_args(
(APIServer pid=20948)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=20948)     return await anext(self.gen)
(APIServer pid=20948)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 220, in build_async_engine_client_from_engine_args
(APIServer pid=20948)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=20948)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1557, in inner
(APIServer pid=20948)     return fn(*args, **kwargs)
(APIServer pid=20948)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 174, in from_vllm_config
(APIServer pid=20948)     return cls(
(APIServer pid=20948)            ^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 120, in __init__
(APIServer pid=20948)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=20948)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=20948)     return AsyncMPClient(*client_args)
(APIServer pid=20948)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 767, in __init__
(APIServer pid=20948)     super().__init__(
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 446, in __init__
(APIServer pid=20948)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=20948)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=20948)     next(self.gen)
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 706, in launch_core_engines
(APIServer pid=20948)     wait_for_engine_startup(
(APIServer pid=20948)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 759, in wait_for_engine_startup
(APIServer pid=20948)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=20948) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=20948) [ERROR] 2025-08-22-09:46:18 (PID:20948, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
root@c3f37a6ca64d:/data/models# /usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

