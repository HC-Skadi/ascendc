# Issue #3551: [Bug]:qwen3-next-80b服务拉不起来

## 基本信息

- **编号**: #3551
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3551
- **创建时间**: 2025-10-20T07:15:24Z
- **关闭时间**: 2025-10-28T09:49:36Z
- **更新时间**: 2025-10-28T09:49:36Z
- **提交者**: @MindShare-AGI
- **评论数**: 3

## 标签

bug; qwen3-next

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

root@910B-36:/# NPU_VISIBLE_DEVICES=0,1,2,3 vllm serve /data2/models/Qwen3-Next-80B-A3B-Instruct --tensor-parallel-size 4 --host 0.0.0.0 --port 9069 --max-model-len 4096 --gpu-memory-utilization 0.7 --enforce-eager
INFO 10-20 06:47:54 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 10-20 06:47:54 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 10-20 06:47:54 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 10-20 06:47:55 [__init__.py:207] Platform plugin ascend is activated
WARNING 10-20 06:47:59 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 10-20 06:48:00 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 10-20 06:48:00 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
(APIServer pid=1795) INFO 10-20 06:48:01 [api_server.py:1839] vLLM API server version 0.11.0rc3
(APIServer pid=1795) INFO 10-20 06:48:01 [utils.py:233] non-default args: {'model_tag': '/data2/models/Qwen3-Next-80B-A3B-Instruct', 'host': '0.0.0.0', 'port': 9069, 'model': '/data2/models/Qwen3-Next-80B-A3B-Instruct', 'max_model_len': 4096, 'enforce_eager': True, 'tensor_parallel_size': 4, 'gpu_memory_utilization': 0.7}
(APIServer pid=1795) INFO 10-20 06:48:01 [model.py:547] Resolved architecture: Qwen3NextForCausalLM
(APIServer pid=1795) `torch_dtype` is deprecated! Use `dtype` instead!
(APIServer pid=1795) INFO 10-20 06:48:01 [model.py:1510] Using max model len 4096
(APIServer pid=1795) INFO 10-20 06:48:01 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048.
(APIServer pid=1795) INFO 10-20 06:48:01 [config.py:297] Hybrid or mamba-based model detected: disabling prefix caching since it is not yet supported.
(APIServer pid=1795) INFO 10-20 06:48:01 [config.py:308] Hybrid or mamba-based model detected: setting cudagraph mode to FULL_AND_PIECEWISE in order to optimize performance.
(APIServer pid=1795) Traceback (most recent call last):
(APIServer pid=1795)   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
(APIServer pid=1795)     sys.exit(main())
(APIServer pid=1795)              ^^^^^^
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
(APIServer pid=1795)     args.dispatch_function(args)
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
(APIServer pid=1795)     uvloop.run(run_server(args))
(APIServer pid=1795)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
(APIServer pid=1795)     return runner.run(wrapper())
(APIServer pid=1795)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1795)   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=1795)     return self._loop.run_until_complete(task)
(APIServer pid=1795)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1795)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=1795)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
(APIServer pid=1795)     return await main
(APIServer pid=1795)            ^^^^^^^^^^
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
(APIServer pid=1795)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
(APIServer pid=1795)     async with build_async_engine_client(
(APIServer pid=1795)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=1795)     return await anext(self.gen)
(APIServer pid=1795)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
(APIServer pid=1795)     async with build_async_engine_client_from_engine_args(
(APIServer pid=1795)   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=1795)     return await anext(self.gen)
(APIServer pid=1795)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 206, in build_async_engine_client_from_engine_args
(APIServer pid=1795)     vllm_config = engine_args.create_engine_config(usage_context=usage_context)
(APIServer pid=1795)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1431, in create_engine_config
(APIServer pid=1795)     config = VllmConfig(
(APIServer pid=1795)              ^^^^^^^^^^^
(APIServer pid=1795)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__
(APIServer pid=1795)     s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/config/__init__.py", line 306, in __post_init__
(APIServer pid=1795)     self.try_verify_and_update_config()
(APIServer pid=1795)   File "/vllm-workspace/vllm/vllm/config/__init__.py", line 642, in try_verify_and_update_config
(APIServer pid=1795)     HybridAttentionMambaModelConfig.verify_and_update_config(self)
(APIServer pid=1795)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_common/patch_mamba_config.py", line 27, in verify_and_update_config
(APIServer pid=1795)     ascend_config = get_ascend_config()
(APIServer pid=1795)                     ^^^^^^^^^^^^^^^^^^^
(APIServer pid=1795)   File "/vllm-workspace/vllm-ascend/vllm_ascend/ascend_config.py", line 199, in get_ascend_config
(APIServer pid=1795)     raise RuntimeError(
(APIServer pid=1795) RuntimeError: Ascend config is not initialized. Please call init_ascend_config first.
(APIServer pid=1795) [ERROR] 2025-10-20-06:48:01 (PID:1795, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
