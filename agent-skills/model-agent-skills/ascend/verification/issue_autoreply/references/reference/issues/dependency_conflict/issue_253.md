# Issue #253: [Bug]: ERROR 03-06 09:35:19 worker_base.py:572] TypeError: 'NoneType' object is not callable

## 基本信息

- **编号**: #253
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/253
- **创建时间**: 2025-03-06T11:04:08Z
- **关闭时间**: 2025-04-09T16:17:29Z
- **更新时间**: 2025-04-09T16:17:30Z
- **提交者**: @man-in-sky
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

[env]
vllm/vllm-ascend：0.7.1-rc1
model：Deepseek-R1-BF16
machine：2x16P


### 🐛 Describe the bug

[command]
python -m vllm.entrypoints.openai.api_server --model="./deepseek-r1_bf16/" --trust-remote-code --enforce-eager --max-model-len 4096 --distributed_executor_backend "ray" --tensor-parallel-size 16 --pipeline-parallel-size 2 --disable-log-requests --disable-log-stats --disable-frontend-multiprocessing --port 7878

[ERROR]
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572] Error executing method 'determine_num_available_blocks'. This might cause deadlock in distributed execution.
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572] Traceback (most recent call last):
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 564, in execute_method
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return run_method(target, method, args, kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return func(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return func(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker.py", line 226, in determine_num_available_blocks
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     self.model_runner.profile_run()
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return func(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1357, in profile_run
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     self.execute_model(model_input, kv_caches, intermediate_tensors)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return func(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     hidden_or_intermediate_states = model_executable(
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self._call_impl(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return forward_call(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 682, in forward
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     hidden_states = self.model(input_ids, positions, kv_caches,
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self._call_impl(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return forward_call(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 638, in forward
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     hidden_states, residual = layer(positions, hidden_states,
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self._call_impl(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return forward_call(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 565, in forward
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     hidden_states = self.mlp(hidden_states)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self._call_impl(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return forward_call(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 158, in forward
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     final_hidden_states = self.experts(
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self._call_impl(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return forward_call(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 584, in forward
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     final_hidden_states = self.quant_method.apply(
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 118, in apply
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self.forward(x=x,
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 23, in forward
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self._forward_method(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 63, in forward_oot
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return self.forward_native(*args, **kwargs)
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 156, in forward_cuda
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572]     return fused_experts(hidden_states=x,
(RayWorkerWrapper pid=26938, ip=10.174.30.223) ERROR 03-06 09:35:19 worker_base.py:572] TypeError: 'NoneType' object is not callable

[anlysis]
In this script：vllm/model_executor/layers/fused_moe/layer.py
                       print current_platform.is_cuda_alike() is false，so fused_experts is setting None
How can i solve it?
