# Issue #2266: [Bug]: v0.10.0rc1启动Qwen3-235B-A22B报错

## 基本信息

- **编号**: #2266
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2266
- **创建时间**: 2025-08-07T09:06:12Z
- **关闭时间**: 2025-11-11T07:13:37Z
- **更新时间**: 2025-11-11T07:13:37Z
- **提交者**: @89412825
- **评论数**: 20

## 标签

bug

## 问题描述

root@pm-971d:/workspace# vllm serve /root/.cache/Qwen3-235B-A22B \
> --host 0.0.0.0 \
> --port 8000 \
> --data-parallel-size 4 \
> --data-parallel-size-local 2 \
> --data-parallel-address $local_ip \
> --data-parallel-rpc-port 13389 \
> --tensor-parallel-size 4 \
> --seed 1024 \
> --served-model-name Qwen3-235B-A22B \
> --enable-expert-parallel \
> --max-num-seqs 16 \
> --max-model-len 32768 \
> --max-num-batched-tokens 9000 \
> --trust-remote-code \
> --no-enable-prefix-caching \
> --gpu-memory-utilization 0.9 \
> --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'
INFO 08-07 09:10:34 [__init__.py:38] Available plugins for group vllm.platform_plugins:
INFO 08-07 09:10:34 [__init__.py:40] - ascend -> vllm_ascend:register
INFO 08-07 09:10:34 [__init__.py:43] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 08-07 09:10:34 [__init__.py:226] Platform plugin ascend is activated
WARNING 08-07 09:10:36 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 08-07 09:10:38 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 08-07 09:10:39 [registry.py:430] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 08-07 09:10:39 [registry.py:430] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 08-07 09:10:39 [registry.py:430] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 08-07 09:10:39 [registry.py:430] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 08-07 09:10:39 [registry.py:430] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 08-07 09:10:39 [registry.py:430] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 08-07 09:10:39 [registry.py:430] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
INFO 08-07 09:10:40 [api_server.py:1755] vLLM API server version 0.10.0
INFO 08-07 09:10:40 [cli_args.py:261] non-default args: {'model_tag': '/root/.cache/Qwen3-235B-A22B', 'host': '0.0.0.0', 'model': '/root/.cache/Qwen3-235B-A22B', 'trust_remote_code': True, 'seed': 1024, 'max_model_len': 32768, 'served_model_name': ['Qwen3-235B-A22B'], 'tensor_parallel_size': 4, 'data_parallel_size': 4, 'data_parallel_size_local': 2, 'data_parallel_address': '192.168.1.3', 'data_parallel_rpc_port': 13389, 'enable_expert_parallel': True, 'enable_prefix_caching': False, 'max_num_batched_tokens': 9000, 'max_num_seqs': 16, 'additional_config': {'ascend_scheduler_config': {'enabled': True}, 'torchair_graph_config': {'enabled': True}}}
INFO 08-07 09:10:53 [config.py:1604] Using max model len 32768
INFO 08-07 09:10:54 [config.py:2434] Chunked prefill is enabled with max_num_batched_tokens=9000.
Traceback (most recent call last):
  File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 52, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
    return runner.run(wrapper())
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
           ^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1791, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1811, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1277, in create_engine_config
    config = VllmConfig(
             ^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__
    s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
  File "/vllm-workspace/vllm/vllm/config.py", line 4651, in __post_init__
    current_platform.check_and_update_config(self)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 141, in check_and_update_config
    check_ascend_config(vllm_config, enforce_eager)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/ascend_config.py", line 141, in check_ascend_config
    raise NotImplementedError(
NotImplementedError: Torchair graph mode only works with following model types:['deepseek', 'pangu'].
[ERROR] 2025-08-07-09:10:54 (PID:17767, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

