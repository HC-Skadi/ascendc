# Issue #2812: [Bug]: 0.10.1rc1 启动qwen3报错

## 基本信息

- **编号**: #2812
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2812
- **创建时间**: 2025-09-08T08:35:09Z
- **关闭时间**: 2025-11-11T06:52:58Z
- **更新时间**: 2025-11-11T06:52:58Z
- **提交者**: @glowwormX
- **评论数**: 9

## 标签

bug

## 问题描述

### Your current environment

vllm                              0.10.1.1
vllm-ascend                       0.10.1rc1
torch                             2.7.1+cpu
torch_npu                         2.7.1.dev20250724
torchaudio                        2.6.0
torchvision                       0.22.1
'CANN:8.2.RC1'

### 🐛 Describe the bug

```
pip list|grep vllm
pip list|grep torch
python -c "import torch;import torch_npu; import pprint; pprint.pprint(f'CANN:{torch.version.cann}')"

export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256

python3 -m vllm.entrypoints.openai.api_server --model "Qwen3/Qwen3-8B/" \
    --served-model-name 'vllm_server' \
    --trust-remote-code \
    --max-model-len=16384 --gpu-memory-utilization=0.95 \
    --tensor-parallel-size=2
```

打印: 
```
vllm                              0.10.1.1
vllm-ascend                       0.10.1rc1
torch                             2.7.1+cpu
torch_npu                         2.7.1.dev20250724
torchaudio                        2.6.0
torchvision                       0.22.1
'CANN:8.2.RC1'


INFO 09-08 16:29:02 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-08 16:29:02 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-08 16:29:02 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-08 16:29:02 [__init__.py:232] Platform plugin ascend is activated
INFO 09-08 16:29:03 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-08 16:29:03 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-08 16:29:03 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-08 16:29:03 [__init__.py:232] Platform plugin ascend is activated
INFO 09-08 16:29:05 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
INFO 09-08 16:29:06 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 09-08 16:29:06 [registry.py:458] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700] EngineCore failed to start.
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700] Traceback (most recent call last):
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 691, in run_engine_core
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 492, in __init__
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 80, in __init__
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]     self.model_executor = executor_class(vllm_config)
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]     self._init_executor()
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 96, in _init_executor
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 472, in wait_for_ready
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700]     raise e from None
(EngineCore_0 pid=619559) ERROR 09-08 16:29:06 [core.py:700] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_0 pid=619559) Process EngineCore_0:
(EngineCore_0 pid=619559) Traceback (most recent call last):
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_0 pid=619559)     self.run()
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_0 pid=619559)     self._target(*self._args, **self._kwargs)
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 704, in run_engine_core
(EngineCore_0 pid=619559)     raise e
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 691, in run_engine_core
(EngineCore_0 pid=619559)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_0 pid=619559)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 492, in __init__
(EngineCore_0 pid=619559)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 80, in __init__
(EngineCore_0 pid=619559)     self.model_executor = executor_class(vllm_config)
(EngineCore_0 pid=619559)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_0 pid=619559)     self._init_executor()
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 96, in _init_executor
(EngineCore_0 pid=619559)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_0 pid=619559)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=619559)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 472, in wait_for_ready
(EngineCore_0 pid=619559)     raise e from None
(EngineCore_0 pid=619559) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(APIServer pid=618238) Traceback (most recent call last):
(APIServer pid=618238)   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=618238)   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1920, in <module>
(APIServer pid=618238)     uvloop.run(run_server(args))
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=618238)     return runner.run(wrapper())
(APIServer pid=618238)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=618238)     return self._loop.run_until_complete(task)
(APIServer pid=618238)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=618238)     return await main
(APIServer pid=618238)            ^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1850, in run_server
(APIServer pid=618238)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1870, in run_server_worker
(APIServer pid=618238)     async with build_async_engine_client(
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=618238)     return await anext(self.gen)
(APIServer pid=618238)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 178, in build_async_engine_client
(APIServer pid=618238)     async with build_async_engine_client_from_engine_args(
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=618238)     return await anext(self.gen)
(APIServer pid=618238)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 220, in build_async_engine_client_from_engine_args
(APIServer pid=618238)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=618238)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/utils/__init__.py", line 1557, in inner
(APIServer pid=618238)     return fn(*args, **kwargs)
(APIServer pid=618238)            ^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 174, in from_vllm_config
(APIServer pid=618238)     return cls(
(APIServer pid=618238)            ^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 120, in __init__
(APIServer pid=618238)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=618238)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
(APIServer pid=618238)     return AsyncMPClient(*client_args)
(APIServer pid=618238)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 767, in __init__
(APIServer pid=618238)     super().__init__(
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 446, in __init__
(APIServer pid=618238)     with launch_core_engines(vllm_config, executor_class,
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=618238)     next(self.gen)
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 706, in launch_core_engines
(APIServer pid=618238)     wait_for_engine_startup(
(APIServer pid=618238)   File "/cache/vllm_0_10_1rc1_reinstall/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 759, in wait_for_engine_startup
(APIServer pid=618238)     raise RuntimeError("Engine core initialization failed. "
(APIServer pid=618238) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
```

