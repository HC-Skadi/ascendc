# Issue #495: [Bug]: NotImplementedError: Custom routing function is not supported now

## 基本信息

- **编号**: #495
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/495
- **创建时间**: 2025-04-09T14:31:14Z
- **关闭时间**: 2025-05-14T03:48:54Z
- **更新时间**: 2025-05-14T03:48:54Z
- **提交者**: @Yikun
- **评论数**: 4

## 标签

feature request

## 问题描述

### Your current environment

vllm 0.8.3
vllm ascend main

### 🐛 Describe the bug

```
14:23:35 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks.
 Traceback (most recent call last):
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
     output = run_method(worker, method, args, kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2347, in run_method
     return func(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
     return func(*args, **kwargs)
   File "/vllm-ascend/vllm_ascend/worker/worker.py", line 222, in determine_num_available_blocks
     self.model_runner.profile_run()
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
     return func(*args, **kwargs)
   File "/vllm-ascend/vllm_ascend/worker/model_runner.py", line 967, in profile_run
     self.execute_model(model_input, kv_caches, intermediate_tensors)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
     return func(*args, **kwargs)
   File "/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1139, in execute_model
     hidden_or_intermediate_states = model_executable(
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
     return forward_call(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/mllama4.py", line 811, in forward
     return self.language_model(input_ids, positions, intermediate_tensors,
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
     return forward_call(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 541, in forward
     model_output = self.model(input_ids, positions, intermediate_tensors,
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
     return self.forward(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 360, in forward
     hidden_states, residual = layer(positions, hidden_states, residual)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
     return forward_call(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/llama4.py", line 321, in forward
     hidden_states = self.feed_forward(hidden_states)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
     return forward_call(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/llama4.py", line 98, in forward
     routed_out = self.experts(
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
     return forward_call(*args, **kwargs)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 838, in forward
     return self.forward_impl(hidden_states, router_logits)
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 857, in forward_impl
     final_hidden_states = self.quant_method.apply(
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 164, in apply
     return self.forward(
   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
     return self._forward_method(*args, **kwargs)
   File "/vllm-ascend/vllm_ascend/ops/fused_moe.py", line 308, in forward_oot
     topk_weights, topk_ids = select_experts(
   File "/vllm-ascend/vllm_ascend/ops/fused_moe.py", line 239, in select_experts
     raise NotImplementedError(
 NotImplementedError: Custom routing function is not supported now
```
