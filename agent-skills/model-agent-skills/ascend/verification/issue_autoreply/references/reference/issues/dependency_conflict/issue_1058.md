# Issue #1058: [Bug][CI Failure]: TypeError: `InputBatch.__init__()` got an unexpected keyword argument `block_size`

## 基本信息

- **编号**: #1058
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1058
- **创建时间**: 2025-06-04T03:24:16Z
- **关闭时间**: 2025-06-09T15:03:03Z
- **更新时间**: 2025-06-09T15:03:03Z
- **提交者**: @shen-shanshan
- **评论数**: 1

## 标签

bug; help wanted

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

Run vllm-ascend test for V1 engine in CI, get this error:

```bash
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 519, in run_engine_core
    raise e
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 506, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 390, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 83, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 168, in _initialize_kv_caches
    self.model_executor.initialize_from_config(kv_cache_configs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 64, in initialize_from_config
    self.collective_rpc("initialize_from_config",
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils.py", line 2656, in run_method
    return func(*args, **kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/worker/worker_base.py", line 600, in initialize_from_config
    self.worker.initialize_from_config(kv_cache_config)  # type: ignore
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 205, in initialize_from_config
    self.model_runner.initialize_kv_cache(kv_cache_config)
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1268, in initialize_kv_cache
    self.input_batch = InputBatch(
TypeError: InputBatch.__init__() got an unexpected keyword argument 'block_size'
```

This is due to the changes at https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_input_batch.py#L66 and https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L2095-L2097.

Help wanted to sync these changes with vllm upstream.
