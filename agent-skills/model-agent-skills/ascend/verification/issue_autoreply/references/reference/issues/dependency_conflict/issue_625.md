# Issue #625: [Bug]: 基于Dockerfile构建容器运行qwen2.5-vl报错

## 基本信息

- **编号**: #625
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/625
- **创建时间**: 2025-04-23T02:24:36Z
- **关闭时间**: 2025-04-24T07:21:58Z
- **更新时间**: 2025-04-24T07:21:58Z
- **提交者**: @LongjiaoLI
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary></summary>

```text
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
docker build -t vllm-ascend-dev-image:latest -f ./Dockerfile .
```

</details>


### 🐛 Describe the bug

'NoneType' object is not iterable
ERROR 04-23 02:03:54 [engine.py:448] Traceback (most recent call last):
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 04-23 02:03:54 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 04-23 02:03:54 [engine.py:448]     return cls(
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 04-23 02:03:54 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 285, in __init__
ERROR 04-23 02:03:54 [engine.py:448]     self._initialize_kv_caches()
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 434, in _initialize_kv_caches
ERROR 04-23 02:03:54 [engine.py:448]     self.model_executor.determine_num_available_blocks())
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 103, in determine_num_available_blocks
ERROR 04-23 02:03:54 [engine.py:448]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 04-23 02:03:54 [engine.py:448]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
ERROR 04-23 02:03:54 [engine.py:448]     return func(*args, **kwargs)
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 04-23 02:03:54 [engine.py:448]     return func(*args, **kwargs)
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 257, in determine_num_available_blocks
ERROR 04-23 02:03:54 [engine.py:448]     self.model_runner.profile_run()
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 04-23 02:03:54 [engine.py:448]     return func(*args, **kwargs)
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1127, in profile_run
ERROR 04-23 02:03:54 [engine.py:448]     model_input = self.prepare_model_input(
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1231, in prepare_model_input
ERROR 04-23 02:03:54 [engine.py:448]     model_input = self._prepare_model_input_tensors(
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1045, in _prepare_model_input_tensors
ERROR 04-23 02:03:54 [engine.py:448]     return builder.build()  # type: ignore
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 560, in build
ERROR 04-23 02:03:54 [engine.py:448]     input_positions = flatten_2d_lists(input_positions)
ERROR 04-23 02:03:54 [engine.py:448]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 918, in flatten_2d_lists
ERROR 04-23 02:03:54 [engine.py:448]     return [item for sublist in lists for item in sublist]
ERROR 04-23 02:03:54 [engine.py:448] TypeError: 'NoneType' object is not iterable
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 450, in run_mp_engine
    raise e
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
    engine = MQLLMEngine.from_vllm_config(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
    return cls(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 285, in __init__
    self._initialize_kv_caches()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 434, in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 103, in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 257, in determine_num_available_blocks
    self.model_runner.profile_run()
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1127, in profile_run
    model_input = self.prepare_model_input(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1231, in prepare_model_input
    model_input = self._prepare_model_input_tensors(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1045, in _prepare_model_input_tensors
    return builder.build()  # type: ignore
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 560, in build
    input_positions = flatten_2d_lists(input_positions)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 918, in flatten_2d_lists
    return [item for sublist in lists for item in sublist]
TypeError: 'NoneType' object is not iterable
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 51, in main
    args.dispatch_function(args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1069, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 269, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-04-23-02:03:58 (PID:12896, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
