# Issue #1760: [Bug]: Qwen2.5-Omni-7B failed to start in graph mode due to no 'num_hidden_layers'

## 基本信息

- **编号**: #1760
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1760
- **创建时间**: 2025-07-12T15:48:05Z
- **关闭时间**: 2025-07-26T12:14:45Z
- **更新时间**: 2025-07-29T01:37:46Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

v0.9.2rc1 image:
```
vllm serve Qwen/Qwen2.5-Omni-7B
```

#### Issue1: ImportError: Please install vllm[audio] for audio support
```
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2213, in __getattr__
    importlib.import_module(name)
  File "/usr/local/python3.10.17/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'librosa'
```
Solution: `pip install qwen-omni-utils -U`, we need add a doc for qwen omni

#### Issue 2: AttributeError: 'Qwen2_5OmniConfig' object has no attribute 'num_hidden_layers'
Workaround: Use eager mode with `--enforce-eager`

### 🐛 Describe the bug

```
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
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
  File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1286, in create_engine_config
    config = VllmConfig(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/pydantic/_internal/_dataclasses.py", line 123, in __init__
    s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s)
  File "/vllm-workspace/vllm/vllm/config.py", line 4624, in __post_init__
    current_platform.check_and_update_config(self)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 180, in check_and_update_config
    update_aclgraph_sizes(vllm_config)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/utils.py", line 307, in update_aclgraph_sizes
    num_hidden_layers = vllm_config.model_config.hf_config.num_hidden_layers
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/configuration_utils.py", line 211, in __getattribute__
    return super().__getattribute__(key)
AttributeError: 'Qwen2_5OmniConfig' object has no attribute 'num_hidden_layers'
```

https://github.com/vllm-project/vllm-ascend/blob/d118bf8a26111bd669f3cb210a1b9a61ecb5dae1/vllm_ascend/utils.py#L307C5-L307C22
