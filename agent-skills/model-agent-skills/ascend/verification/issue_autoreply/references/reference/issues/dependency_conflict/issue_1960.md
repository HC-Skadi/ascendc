# Issue #1960: [Bug]: BAAI/bge-reranker-v2-m3 failed to start in graph and eager mode due to Text-only XLMRobertaForSequenceClassification not be supported

## 基本信息

- **编号**: #1960
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1960
- **创建时间**: 2025-07-23T06:55:25Z
- **关闭时间**: 2025-11-11T11:37:55Z
- **更新时间**: 2025-11-11T11:37:55Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

vllm version: v0.9.2rc1
```
VLLM_USE_MODELSCOPE=True vllm  serve BAAI/bge-reranker-v2-m3 --trust_remote_code --enforce-eager &

VLLM_USE_MODELSCOPE=True vllm  serve BAAI/bge-reranker-v2-m3  --trust_remote_code &
```

### 🐛 Describe the bug

bug:
```
INFO 07-22 07:01:33 [config.py:1472] Using max model len 8192
WARNING 07-22 07:01:33 [arg_utils.py:1735] ['XLMRobertaForSequenceClassification'] is not supported by the V1 Engine. Falling back to V0.
INFO 07-22 07:01:33 [config.py:4601] Only "last" pooling supports chunked prefill and prefix caching; disabling both.
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/cli/main.py", line 65, in main
    args.dispatch_function(args)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/cli/serve.py", line 55, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 1431, in run_server
    await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 1451, in run_server_worker
    async with build_async_engine_client(args, client_config) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
  File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/engine/arg_utils.py", line 1286, in create_engine_config
    config = VllmConfig(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__
    s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
pydantic_core._pydantic_core.ValidationError: 1 validation error for VllmConfig
  Value error, vLLM Ascend does not support V0 engine. [type=value_error, input_value=ArgsKwargs((), {'model_co...additional_config': {}}), input_type=ArgsKwargs]
    For further information visit https://errors.pydantic.dev/2.11/v/value_error
[ERROR] 2025-07-22-07:01:33 (PID:16357, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

```
