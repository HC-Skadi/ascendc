# Issue #2546: [Misc]: e2e test fail - external launch

## 基本信息

- **编号**: #2546
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2546
- **创建时间**: 2025-08-26T06:44:41Z
- **关闭时间**: 2025-10-24T07:00:59Z
- **更新时间**: 2025-10-24T07:00:59Z
- **提交者**: @wangxiyuan
- **评论数**: 0

## 标签

help wanted; ci/build

## 问题描述

I found that the test `tests/e2e/multicard/test_external_launcher.py::test_external_launcher_and_sleepmode ` usually failed in e2e test CI. We should make it stable enought, the error log:

```
tests/e2e/multicard/test_external_launcher.py::test_external_launcher_and_sleepmode Running subprocess: /usr/local/python3.11.13/bin/python3.11 /__w/vllm-ascend/vllm-ascend/examples/offline_external_launcher.py --model Qwen/Qwen3-8B --tp-size 1 --node-size 1 --node-rank 0 --proc-per-node 2 --trust-remote-code --enable-sleep-mode --temperature 0 --model-weight-gib 16
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
acl Error, code: 207001 at /__w/vllm-ascend/vllm-ascend/csrc/camem_allocator.cpp:63
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B

Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]

Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:00<00:01,  2.02it/s]
Process Process-1:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/__w/vllm-ascend/vllm-ascend/examples/offline_external_launcher.py", line 178, in main
    llm = LLM(
          ^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/entrypoints/llm.py", line 285, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/llm_engine.py", line 153, in from_engine_args
    return cls(vllm_config=vllm_config,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/llm_engine.py", line 104, in __init__
    self.engine_core = EngineCoreClient.make_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core_client.py", line 82, in make_client
    return InprocClient(vllm_config, executor_class, log_stats)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core_client.py", line 245, in __init__
    self.engine_core = EngineCore(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 80, in __init__
    self.model_executor = executor_class(vllm_config)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/executor_base.py", line 54, in __init__
    self._init_executor()
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 129, in _init_executor
    self.collective_rpc("load_model")
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils/__init__.py", line 3007, in run_method
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 241, in load_model
    self.model_runner.load_model()
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2191, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/__init__.py", line 118, in get_model
    return loader.load_model(vllm_config=vllm_config,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/base_loader.py", line 49, in load_model
    self.load_weights(model, model_config)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/default_loader.py", line 259, in load_weights
    loaded_weights = model.load_weights(
                     ^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen3.py", line 156, in load_weights
    return loader.load_weights(weights)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 291, in load_weights
    autoloaded_weights = set(self._load_module("", self.module, weights))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 249, in _load_module
    yield from self._load_module(prefix,
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 222, in _load_module
    loaded_params = module_load_weights(weights)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2.py", line 437, in load_weights
    weight_loader(param, loaded_weight)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/linear.py", line 1337, in weight_loader
    param_data.copy_(loaded_weight)
RuntimeError: copy_between_host_and_device_opapi:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:54 NPU function error: aclrtMemcpy, error code is 507899
Error:  2025-08-26-03:59:04 (PID:28794, Device:0, RankID:0) ERR00100 PTA call acl api failed
Error: [Error]: An internal error occurs in the Driver module. 
        Rectify the fault based on the error information in the ascend log.
EL0004: [PID: 28794] 2025-08-26-03:58:55.257.127 Failed to allocate memory.
        Possible Cause: Available memory is insufficient.
        Solution: Close applications not in use.
        TraceBack (most recent call last):
        malloc physical memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        The argument is invalid.
        rtMemcpy execute failed, reason=[driver error:internal error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        synchronized memcpy failed, kind = 1, runtime result = 507899[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]


Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:02<00:09,  2.39s/it]

Process Process-2:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/__w/vllm-ascend/vllm-ascend/examples/offline_external_launcher.py", line 178, in main
    llm = LLM(
          ^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/entrypoints/llm.py", line 285, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/llm_engine.py", line 153, in from_engine_args
    return cls(vllm_config=vllm_config,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/llm_engine.py", line 104, in __init__
    self.engine_core = EngineCoreClient.make_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core_client.py", line 82, in make_client
    return InprocClient(vllm_config, executor_class, log_stats)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core_client.py", line 245, in __init__
    self.engine_core = EngineCore(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 89, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 179, in _initialize_kv_caches
    self.model_executor.determine_available_memory())
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 112, in determine_available_memory
    dist.all_reduce(memory_tensor, group=cpu_group, op=dist.ReduceOp.MIN)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2815, in all_reduce
    work.wait()
RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:534] Connection closed by peer [10.0.1.9]:45459
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B

FAILED
```

Once this error happen, other tested will fail with `oom` or `hccl` error.

## OOM error log
```
tests/e2e/multicard/test_prefix_caching.py::test_prefix_cache_with_v1_scheduler[50-Qwen/Qwen3-8B-Base] Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B-Base
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B-Base
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B-Base
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B-Base
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B-Base
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B-Base
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-8B-Base
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559] WorkerProc failed to start.
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559] Traceback (most recent call last):
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 533, in worker_main
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     worker = WorkerProc(*args, **kwargs)
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 402, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.worker.load_model()
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 241, in load_model
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.model_runner.load_model()
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2191, in load_model
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/__init__.py", line 118, in get_model
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     return loader.load_model(vllm_config=vllm_config,
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/base_loader.py", line 44, in load_model
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     model = initialize_model(vllm_config=vllm_config,
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen3.py", line 106, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.model = CustomQwen3Model(vllm_config=vllm_config,
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/decorators.py", line 183, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen3.py", line 77, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     super().__init__(vllm_config=vllm_config,
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/decorators.py", line 183, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2.py", line 316, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                                                     ^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 640, in make_layers
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                                                      ^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 641, in <listcomp>
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2.py", line 318, in <lambda>
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     lambda prefix: decoder_layer_type(config=config,
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen3.py", line 33, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     super().__init__(config=config,
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3.py", line 205, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.mlp = Qwen3MLP(
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                ^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2.py", line 72, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.gate_up_proj = MergedColumnParallelLinear(
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/linear.py", line 649, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     super().__init__(input_size=input_size,
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/linear.py", line 508, in __init__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     self.quant_method.create_weights(
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/linear.py", line 193, in create_weights
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     weight = Parameter(torch.empty(sum(output_partition_sizes),
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_device.py", line 104, in __torch_function__
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]     return func(*args, **kwargs)
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=34941) ERROR 08-26 04:04:21 [multiproc_executor.py:559] RuntimeError: NPU out of memory. Tried to allocate 98.00 MiB (NPU 0; 60.96 GiB total capacity; 6.38 GiB already allocated; 6.38 GiB current active; 16.81 MiB free; 6.65 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
```

## HCCL error log
```
tests/e2e/multicard/test_prefix_caching.py::test_prefix_cache_with_v1_scheduler[50-deepseek-ai/DeepSeek-V2-Lite-Chat] Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-V2-Lite-Chat
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-V2-Lite-Chat
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-V2-Lite-Chat
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-V2-Lite-Chat
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-V2-Lite-Chat
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-V2-Lite-Chat
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-V2-Lite-Chat
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559] WorkerProc failed to start.
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559] Traceback (most recent call last):
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 533, in worker_main
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     worker = WorkerProc(*args, **kwargs)
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 402, in __init__
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.worker.load_model()
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 241, in load_model
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.model_runner.load_model()
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2191, in load_model
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/__init__.py", line 118, in get_model
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     return loader.load_model(vllm_config=vllm_config,
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/base_loader.py", line 44, in load_model
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     model = initialize_model(vllm_config=vllm_config,
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 924, in __init__
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 845, in __init__
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                                                     ^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 640, in make_layers
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                                                      ^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 641, in <listcomp>
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 847, in <lambda>
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     lambda prefix: CustomDeepseekV2DecoderLayer(
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 686, in __init__
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.mlp = CustomDeepseekV2MoE(
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                ^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 338, in __init__
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.experts = AscendFusedMoE(
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                    ^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/ops/fused_moe.py", line 1194, in __init__
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.quant_method = AscendUnquantizedFusedMoEMethod(moe)
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/ops/fused_moe.py", line 942, in __init__
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]     self.moe_all_to_all_group_name = backend.get_hccl_comm_name(
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559] RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:148 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 7
Error: (VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559] [ERROR] 2025-08-26-04:05:21 (PID:35532, Device:0, RankID:-1) ERR02200 DIST call hccl api failed.
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559] EJ0001: [PID: 35532] 2025-08-26-04:05:21.569.071 Failed to initialize the HCCP process. Reason: Maybe the last training process is running.
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]         Solution: Wait for 10s after killing the last training process and try again.
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]         TraceBack (most recent call last):
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]         tsd client wait response fail, hostpid:2432105, device response code[1]. unknown device error.[FUNC:WaitRsp][FILE:process_mode_manager.cpp][LINE:277]
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]         Fail to get sq reg virtual addr, deviceId=0, sqId=68.[FUNC:Setup][FILE:stream.cc][LINE:686]
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]         stream setup failed, retCode=0x7020010.[FUNC:SyncGetDevMsg][FILE:api_impl.cc][LINE:6109]
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]         Sync get device msg failed, retCode=0x7020010.[FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:6159]
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]         rtGetDevMsg execute failed, reason=[driver error:internal error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker TP0 pid=35532) ERROR 08-26 04:05:22 [multiproc_executor.py:559]
```
