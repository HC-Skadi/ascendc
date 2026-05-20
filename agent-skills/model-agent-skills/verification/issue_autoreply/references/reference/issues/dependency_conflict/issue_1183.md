# Issue #1183: [Bug]: run gemma3-27b in vllm-ascend 0.9.0rc1  V1 has error

## 基本信息

- **编号**: #1183
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1183
- **创建时间**: 2025-06-12T02:42:29Z
- **关闭时间**: 2025-06-15T03:12:08Z
- **更新时间**: 2025-06-15T03:12:08Z
- **提交者**: @cxcxflying
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

image: quay.io/ascend/vllm-ascend:v0.9.0rc1-openeuler 


### 🐛 Describe the bug

1. start vllm openai.api_server
VLLM_USE_V1=1  python -m vllm.entrypoints.openai.api_server --model ./model/gemma-3-27b-it \
--max-num-seqs=64 \
--max-model-len=8192 \
--max-num-batched-tokens=8192 \
--tensor-parallel-size=2 \
--block-size=128 \
--dtype bfloat16 \
--host=0.0.0.0 \
--port=8000 \
--gpu-memory-utilization=0.9 \
--trust-remote-code \
--enable-chunked-prefill

2.the error is

INFO 06-12 02:45:15 [platform.py:183] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/python3.10.17/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1376, in <module>
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1324, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 153, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 173, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
  File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1172, in create_engine_config
    config = VllmConfig(
  File "<string>", line 20, in __init__
  File "/vllm-workspace/vllm/vllm/config.py", line 4364, in __post_init__
    current_platform.check_and_update_config(self)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 189, in check_and_update_config
    update_aclgraph_sizes(vllm_config)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/utils.py", line 134, in update_aclgraph_sizes
    num_hidden_layers = vllm_config.model_config.hf_config.num_hidden_layers
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/configuration_utils.py", line 214, in __getattribute__
    return super().__getattribute__(key)
AttributeError: 'Gemma3Config' object has no attribute 'num_hidden_layers'
