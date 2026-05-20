# Issue #1162: [Bug]: test_ngram_correctness failed due to PagedAttentionOperation inner error

## 基本信息

- **编号**: #1162
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1162
- **创建时间**: 2025-06-10T13:24:45Z
- **关闭时间**: 2025-12-23T12:48:31Z
- **更新时间**: 2025-12-23T12:48:31Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

Since https://github.com/vllm-project/vllm-ascend/commit/cd2f14a1b3563a70c70908b07c76f6d3fa282b0c , https://github.com/vllm-project/vllm-ascend/pull/1023

```
self = <vllm.v1.engine.core_client.SyncMPClient object at 0xfffd05d1d960>

    def get_output(self) -> EngineCoreOutputs:
        # If an exception arises in process_outputs_socket task,
        # it is forwarded to the outputs_queue so we can raise it
        # from this (run_output_handler) task to shut down the server.
        outputs = self.outputs_queue.get()
        if isinstance(outputs, Exception):
>           raise self._format_exception(outputs) from None
E           vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.

vllm-empty/vllm/v1/engine/core_client.py:647: EngineDeadError
=========================== short test summary info ============================
FAILED tests/long_term/spec_decode/e2e/test_v1_spec_decode.py::test_ngram_correctness - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
=================== 1 failed, 2 skipped in 112.64s (0:01:52) ===================
```

### 🐛 Describe the bug

```
ERROR 06-09 23:33:03 [core.py:502] EngineCore encountered a fatal error.
ERROR 06-09 23:33:03 [core.py:502] Traceback (most recent call last):
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 493, in run_engine_core
ERROR 06-09 23:33:03 [core.py:502]     engine_core.run_busy_loop()
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 520, in run_busy_loop
ERROR 06-09 23:33:03 [core.py:502]     self._process_engine_step()
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 545, in _process_engine_step
ERROR 06-09 23:33:03 [core.py:502]     outputs = self.step_fn()
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 226, in step
ERROR 06-09 23:33:03 [core.py:502]     model_output = self.execute_model(scheduler_output)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 213, in execute_model
ERROR 06-09 23:33:03 [core.py:502]     raise err
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 207, in execute_model
ERROR 06-09 23:33:03 [core.py:502]     return self.model_executor.execute_model(scheduler_output)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 86, in execute_model
ERROR 06-09 23:33:03 [core.py:502]     output = self.collective_rpc("execute_model",
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 06-09 23:33:03 [core.py:502]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils.py", line 2605, in run_method
ERROR 06-09 23:33:03 [core.py:502]     return func(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 180, in execute_model
ERROR 06-09 23:33:03 [core.py:502]     output = self.model_runner.execute_model(scheduler_output)
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-09 23:33:03 [core.py:502]     return func(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1212, in execute_model
ERROR 06-09 23:33:03 [core.py:502]     sample_indices) = (self._process_reqs(scheduler_output,
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1005, in _process_reqs
ERROR 06-09 23:33:03 [core.py:502]     hidden_states = self.model(
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-09 23:33:03 [core.py:502]     return self._call_impl(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-09 23:33:03 [core.py:502]     return forward_call(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/llama.py", line 580, in forward
ERROR 06-09 23:33:03 [core.py:502]     model_output = self.model(input_ids, positions, intermediate_tensors,
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/decorators.py", line 172, in __call__
ERROR 06-09 23:33:03 [core.py:502]     return self.forward(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/llama.py", line 391, in forward
ERROR 06-09 23:33:03 [core.py:502]     hidden_states, residual = layer(positions, hidden_states, residual)
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-09 23:33:03 [core.py:502]     return self._call_impl(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-09 23:33:03 [core.py:502]     return forward_call(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/llama.py", line 304, in forward
ERROR 06-09 23:33:03 [core.py:502]     hidden_states = self.self_attn(positions=positions,
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-09 23:33:03 [core.py:502]     return self._call_impl(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-09 23:33:03 [core.py:502]     return forward_call(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/llama.py", line 203, in forward
ERROR 06-09 23:33:03 [core.py:502]     output, _ = self.o_proj(attn_output)
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-09 23:33:03 [core.py:502]     return self._call_impl(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-09 23:33:03 [core.py:502]     return forward_call(*args, **kwargs)
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/linear.py", line 1288, in forward
ERROR 06-09 23:33:03 [core.py:502]     output_parallel = self.quant_method.apply(self,
ERROR 06-09 23:33:03 [core.py:502]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/linear.py", line 202, in apply
ERROR 06-09 23:33:03 [core.py:502]     return dispatch_unquantized_gemm()(x, layer.weight, bias)
ERROR 06-09 23:33:03 [core.py:502] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is PagedAttentionOperation.
ERROR 06-09 23:33:03 [core.py:502] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
ERROR 06-09 23:33:03 [core.py:502] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
```
https://github.com/vllm-project/vllm-ascend/actions/runs/15546744407/job/43769613936
