# Issue #3395: [Bug]: Qwen2 VL 7B accuracy test failed

## 基本信息

- **编号**: #3395
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3395
- **创建时间**: 2025-10-12T02:27:00Z
- **关闭时间**: 2025-10-29T07:32:15Z
- **更新时间**: 2025-10-29T07:32:15Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

```
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710] Traceback (most recent call last):
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 701, in run_engine_core
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 728, in run_busy_loop
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     self._process_engine_step()
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 754, in _process_engine_step
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 284, in step
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     model_output = self.execute_model_with_error_logging(
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 270, in execute_model_with_error_logging
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     raise err
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 261, in execute_model_with_error_logging
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     return model_fn(scheduler_output)
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 103, in execute_model
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     output = self.collective_rpc("execute_model",
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils/__init__.py", line 3122, in run_method
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     return func(*args, **kwargs)
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 254, in execute_model
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     return func(*args, **kwargs)
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1859, in execute_model
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     max_query_len) = (self._prepare_inputs(scheduler_output,
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1336, in _prepare_inputs
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 954, in _execute_mm_encoder
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2_vl.py", line 1458, in get_multimodal_embeddings
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     vision_embeddings = self._process_image_input(image_input)
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2_vl.py", line 1385, in _process_image_input
(EngineCore_DP0 pid=3452) ERROR 10-12 02:10:43 [core.py:710]     image_embeds = self.visual(pixel_values,

```

### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/actions/runs/18437579139/job/52533183528?pr=3394
