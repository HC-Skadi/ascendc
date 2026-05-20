# Issue #1572: CI failed: IndexError: list index out of range

## 基本信息

- **编号**: #1572
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1572
- **创建时间**: 2025-07-01T23:30:13Z
- **关闭时间**: 2025-07-02T04:11:16Z
- **更新时间**: 2025-07-02T04:11:16Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm/commit/7f280d69c98e560427d2cbc9c3c3c13a83510dca

### 🐛 Describe the bug

```
ERROR 07-01 22:31:57 [core.py:521] EngineCore encountered a fatal error.
ERROR 07-01 22:31:57 [core.py:521] Traceback (most recent call last):
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 512, in run_engine_core
ERROR 07-01 22:31:57 [core.py:521]     engine_core.run_busy_loop()
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 539, in run_busy_loop
ERROR 07-01 22:31:57 [core.py:521]     self._process_engine_step()
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 564, in _process_engine_step
ERROR 07-01 22:31:57 [core.py:521]     outputs, model_executed = self.step_fn()
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 235, in step
ERROR 07-01 22:31:57 [core.py:521]     model_output = self.execute_model(scheduler_output)
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 221, in execute_model
ERROR 07-01 22:31:57 [core.py:521]     raise err
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 212, in execute_model
ERROR 07-01 22:31:57 [core.py:521]     return self.model_executor.execute_model(scheduler_output)
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 87, in execute_model
ERROR 07-01 22:31:57 [core.py:521]     output = self.collective_rpc("execute_model",
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 07-01 22:31:57 [core.py:521]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils.py", line 2716, in run_method
ERROR 07-01 22:31:57 [core.py:521]     return func(*args, **kwargs)
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 179, in execute_model
ERROR 07-01 22:31:57 [core.py:521]     output = self.model_runner.execute_model(scheduler_output)
ERROR 07-01 22:31:57 [core.py:521]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 07-01 22:31:57 [core.py:521]     return func(*args, **kwargs)
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1545, in execute_model
ERROR 07-01 22:31:57 [core.py:521]     self._update_states(scheduler_output)
ERROR 07-01 22:31:57 [core.py:521]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 533, in _update_states
ERROR 07-01 22:31:57 [core.py:521]     new_token_ids = req_data.new_token_ids[i]
ERROR 07-01 22:31:57 [core.py:521] IndexError: list index out of range
Processed prompts:   0%|          | 0/4 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 523, in run_engine_core
    raise e
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 512, in run_engine_core
    engine_core.run_busy_loop()
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 539, in run_busy_loop
    self._process_engine_step()
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 564, in _process_engine_step
    outputs, model_executed = self.step_fn()
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 235, in step
    model_output = self.execute_model(scheduler_output)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 221, in execute_model
    raise err
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 212, in execute_model
    return self.model_executor.execute_model(scheduler_output)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 87, in execute_model
    output = self.collective_rpc("execute_model",
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils.py", line 2716, in run_method
    return func(*args, **kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 179, in execute_model
    output = self.model_runner.execute_model(scheduler_output)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1545, in execute_model
    self._update_states(scheduler_output)
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 533, in _update_states
    new_token_ids = req_data.new_token_ids[i]
IndexError: list index out of range
```

https://github.com/vllm-project/vllm-ascend/actions/runs/16011200667/job/45169454030
