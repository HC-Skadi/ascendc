# Issue #2876: [Bug]: accuracy test failed due to `Forward context is not set`

## 基本信息

- **编号**: #2876
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2876
- **创建时间**: 2025-09-12T00:39:52Z
- **关闭时间**: 2025-09-12T09:55:08Z
- **更新时间**: 2025-09-12T09:55:08Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

Accuracy test failed: https://github.com/vllm-project/vllm-ascend/actions/runs/17653675992/job/50170839744

### 🐛 Describe the bug

```
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720] Traceback (most recent call last):
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 711, in run_engine_core
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 738, in run_busy_loop
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     self._process_engine_step()
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 764, in _process_engine_step
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 292, in step
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     model_output = self.execute_model_with_error_logging(
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 278, in execute_model_with_error_logging
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     raise err
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 269, in execute_model_with_error_logging
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return model_fn(scheduler_output)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/abstract.py", line 93, in execute_model
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     output = self.collective_rpc("execute_model",
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils/__init__.py", line 3060, in run_method
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return func(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 213, in execute_model
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return func(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1576, in execute_model
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     intermediate_tensors) = (self._prepare_inputs(
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]                              ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1175, in _prepare_inputs
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     self._execute_mm_encoder(scheduler_output)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 817, in _execute_mm_encoder
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     curr_group_outputs = self.model.get_multimodal_embeddings(
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2_5_vl.py", line 1136, in get_multimodal_embeddings
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     vision_embeddings = self._process_image_input(multimodal_input)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen2_5_vl.py", line 526, in _process_image_input
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen2_5_vl.py", line 479, in forward
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     x = blk(x, cu_seqlens=cu_seqlens_now, cos=cos, sin=sin)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/qwen2_5_vl.py", line 156, in forward
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     x = x + self.mlp(self.norm2(x))
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]             ^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2_5_vl.py", line 240, in forward
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     x = self.act_fn(gate_up)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]         ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/custom_op.py", line 44, in forward
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return self._forward_method(*args, **kwargs)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/ops/activation.py", line 38, in forward_oot
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     torch.ops.vllm.maybe_prefetch_mlp_down_proj(x)
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     return self._op(*args, **(kwargs or {}))
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/ops/register_custom_ops.py", line 82, in _maybe_prefetch_mlp_down_proj_impl
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     forward_context = get_forward_context()
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]                       ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/forward_context.py", line 192, in get_forward_context
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]     assert _forward_context is not None, (
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=3446) ERROR 09-11 18:37:26 [core.py:720] AssertionError: Forward context is not set. Please use `set_forward_context` to set the forward context.

```
