# Issue #2533: [Bug]: perf test failed due to AttributeError: '_OpNamespace' '_C' object has no attribute 'apply_repetition_penalties_'

## 基本信息

- **编号**: #2533
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2533
- **创建时间**: 2025-08-26T00:48:30Z
- **关闭时间**: 2025-08-28T02:55:50Z
- **更新时间**: 2025-08-28T02:55:50Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

bug; critical

## 问题描述

### Your current environment

 AttributeError: '_OpNamespace' '_C' object has no attribute 'apply_repetition_penalties_'

https://github.com/vllm-project/vllm-ascend/actions/runs/17207496219/job/48811212287?pr=2527

```
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702] EngineCore encountered a fatal error.
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702] Traceback (most recent call last):
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 693, in run_engine_core
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     engine_core.run_busy_loop()
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 720, in run_busy_loop
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     self._process_engine_step()
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 745, in _process_engine_step
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     outputs, model_executed = self.step_fn()
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]                               ^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 288, in step
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     model_output = self.execute_model_with_error_logging(
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 274, in execute_model_with_error_logging
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     raise err
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 265, in execute_model_with_error_logging
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     return model_fn(scheduler_output)
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 87, in execute_model
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     output = self.collective_rpc("execute_model",
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils/__init__.py", line 3007, in run_method
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     return func(*args, **kwargs)
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 205, in execute_model
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     return func(*args, **kwargs)
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1665, in execute_model
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     sampler_output = self.sampler(
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]                      ^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     return self._call_impl(*args, **kwargs)
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     return forward_call(*args, **kwargs)
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/sample/sampler.py", line 58, in forward
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     logits = self.apply_penalties(logits, sampling_metadata)
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/sample/sampler.py", line 209, in apply_penalties
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     logits = apply_all_penalties(
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/sample/ops/penalties.py", line 24, in apply_all_penalties
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     return apply_penalties(logits, prompt_token_ids, output_tokens_t,
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/utils.py", line 78, in apply_penalties
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     apply_repetition_penalties(logits, prompt_mask, output_mask,
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/_custom_ops.py", line 315, in apply_repetition_penalties
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     apply_repetition_penalties_cuda(logits, prompt_mask, output_mask,
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/_custom_ops.py", line 299, in apply_repetition_penalties_cuda
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     torch.ops._C.apply_repetition_penalties_(logits, prompt_mask, output_mask,
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1267, in __getattr__
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702]     raise AttributeError(
(EngineCore_0 pid=2762) ERROR 08-25 11:37:53 [core.py:702] AttributeError: '_OpNamespace' '_C' object has no attribute 'apply_repetition_penalties_'
```

### 🐛 Describe the bug

AttributeError: '_OpNamespace' '_C' object has no attribute 'apply_repetition_penalties_'

