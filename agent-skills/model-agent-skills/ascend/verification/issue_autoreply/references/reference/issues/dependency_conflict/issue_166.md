# Issue #166: [Doc]: ModuleNotFoundError: No module named 'torch_npu'

## 基本信息

- **编号**: #166
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/166
- **创建时间**: 2025-02-26T02:16:39Z
- **关闭时间**: 2025-03-06T15:08:26Z
- **更新时间**: 2025-03-06T15:08:26Z
- **提交者**: @ZRJ026
- **评论数**: 3

## 标签

bug

## 问题描述

### 📚 The doc issue

I followed the documentation to start the container using the image quay.io/ascend/vllm-ascend:main sha256:ffc14020a3bdd25bd29cd5bf749d86e85dd1b75df7fdd9bb383a52578116b5b0
  and the command:
`vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
`
However, I encountered the following error:
```
INFO 02-26 02:05:13 [__init__.py:198] Platform plugin ascend is activated
Failed to import torch_npu.
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 65, in main
    cmd.subparser_init(subparsers).set_defaults(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 59, in subparser_init
    return make_arg_parser(serve_parser)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/cli_args.py", line 257, in make_arg_parser
    parser = AsyncEngineArgs.add_cli_args(parser)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1430, in add_cli_args
    current_platform.pre_register_and_update(parser)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/platform.py", line 68, in pre_register_and_update
    from vllm_ascend.quantization.quant_config import \
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 22, in <module>
    import torch_npu  # noqa: F401
ModuleNotFoundError: No module named 'torch_npu'`

After installing torch_npu version 2.5.1rc1 using the command:
`pip install torch_npu==2.5.1rc1
`
The error has changed from missing the torch_npu module to the following:
`ERROR 02-26 02:14:15 [engine.py:400]     torch_npu.npu_rope(
ERROR 02-26 02:14:15 [engine.py:400] AttributeError: module 'torch_npu' has no attribute 'npu_rope'
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 402, in run_mp_engine
    raise e
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
    engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
    return cls(ipc_path=ipc_path,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
    self._initialize_kv_caches()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2232, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker.py", line 228, in determine_num_available_blocks
    self.model_runner.profile_run()
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1358, in profile_run
    self.execute_model(model_input, kv_caches, intermediate_tensors)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1142, in execute_model
    hidden_or_intermediate_states = model_executable(
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 463, in forward
    hidden_states = self.model(input_ids, positions, intermediate_tensors,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
    return self.forward(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 339, in forward
    hidden_states, residual = layer(
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 243, in forward
    hidden_states = self.self_attn(
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 176, in forward
    q, k = self.rotary_emb(positions, q, k)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
    return self._forward_method(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/ops/rotary_embedding.py", line 45, in rope_forward_oot
    torch_npu.npu_rope(
AttributeError: module 'torch_npu' has no attribute 'npu_rope'
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 73, in main
    args.dispatch_function(args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 34, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 946, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 138, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 232, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-02-26-02:14:22 (PID:240, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

### Suggest a potential alternative/fix

_No response_
