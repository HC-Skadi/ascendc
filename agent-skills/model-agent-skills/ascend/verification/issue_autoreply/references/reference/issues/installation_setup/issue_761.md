# Issue #761: [Doc]: i use docker image `quay.io/ascend/vllm-ascend:v0.8.4rc2` run model `Qwen/Qwen3-235B-A22B` error

## 基本信息

- **编号**: #761
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/761
- **创建时间**: 2025-05-06T06:44:49Z
- **关闭时间**: 2025-05-06T10:08:51Z
- **更新时间**: 2025-05-06T10:08:51Z
- **提交者**: @wanmei002
- **评论数**: 2

## 标签

documentation

## 问题描述

### 📚 The doc issue

run cmd: `vllm serve /root/.cache/huggingface/hub/models--Qwen--Qwen3-235B-A22B/snapshots/b51c4308ed84804fa6722b20722cd91e3cd17808 --served-model-name qwen3 --max-model-len 10240 --tensor-parallel-size 5 --port 8000`

error log:
```bash
INFO 05-06 06:36:54 [config.py:689] This model supports multiple tasks: {'generate', 'reward', 'score', 'embed', 'classify'}. Defaulting to 'generate'.
INFO 05-06 06:36:54 [arg_utils.py:1742] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
INFO 05-06 06:36:54 [config.py:1713] Defaulting to use mp for distributed inference
INFO 05-06 06:36:54 [config.py:1747] Disabled the custom all-reduce kernel because it is not supported on current platform.
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/workspace/vllm/vllm/entrypoints/cli/main.py", line 51, in main
    args.dispatch_function(args)
  File "/workspace/vllm/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1069, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/workspace/vllm/vllm/entrypoints/openai/api_server.py", line 166, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
  File "/workspace/vllm/vllm/engine/arg_utils.py", line 1335, in create_engine_config
    config = VllmConfig(
  File "<string>", line 19, in __init__
  File "/workspace/vllm/vllm/config.py", line 3692, in __post_init__
    self.model_config.verify_with_parallel_config(self.parallel_config)
  File "/workspace/vllm/vllm/config.py", line 872, in verify_with_parallel_config
    raise ValueError(
ValueError: Total number of attention heads (64) must be divisible by tensor parallel size (5).
[ERROR] 2025-05-06-06:36:55 (PID:332, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

#### vllm ascend not support model `Qwen/Qwen3-235B-A22B`?

### Suggest a potential alternative/fix

_No response_
