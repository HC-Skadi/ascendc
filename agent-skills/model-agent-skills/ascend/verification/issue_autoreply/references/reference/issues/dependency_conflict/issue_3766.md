# Issue #3766: [Bug]: Qwen3-VL-30B with shape invalid for input

## 基本信息

- **编号**: #3766
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3766
- **创建时间**: 2025-10-25T09:34:17Z
- **关闭时间**: 2025-10-25T10:06:09Z
- **更新时间**: 2026-01-06T01:13:51Z
- **提交者**: @leisuzz
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

vllm=0.11.0+empty                
vllm_ascend=0.11.0rc1.dev157+gfed8145ae
Qwen3-VL 8B is working, but 30B is not working due to the MOE part.


### 🐛 Describe the bug

```
File "vllm/vllm/entrypoints/llm.py", line 401, in generate
[36m(TaskRunner pid=1241632)[0m     outputs = self._run_engine(use_tqdm=use_tqdm)
[36m(TaskRunner pid=1241632)[0m               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/entrypoints/llm.py", line 1600, in _run_engine
[36m(TaskRunner pid=1241632)[0m     step_outputs = self.llm_engine.step()
[36m(TaskRunner pid=1241632)[0m                    ^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/v1/engine/llm_engine.py", line 265, in step
[36m(TaskRunner pid=1241632)[0m     outputs = self.engine_core.get_output()
[36m(TaskRunner pid=1241632)[0m               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/v1/engine/core_client.py", line 248, in get_output
[36m(TaskRunner pid=1241632)[0m     outputs, _ = self.engine_core.step_fn()
[36m(TaskRunner pid=1241632)[0m                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/v1/engine/core.py", line 284, in step
[36m(TaskRunner pid=1241632)[0m     model_output = self.execute_model_with_error_logging(
[36m(TaskRunner pid=1241632)[0m                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/v1/engine/core.py", line 270, in execute_model_with_error_logging
[36m(TaskRunner pid=1241632)[0m     raise err
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/v1/engine/core.py", line 261, in execute_model_with_error_logging
[36m(TaskRunner pid=1241632)[0m     return model_fn(scheduler_output)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/v1/executor/abstract.py", line 103, in execute_model
[36m(TaskRunner pid=1241632)[0m     output = self.collective_rpc("execute_model",
[36m(TaskRunner pid=1241632)[0m              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
[36m(TaskRunner pid=1241632)[0m     return [run_method(self.driver_worker, method, args, kwargs)]
[36m(TaskRunner pid=1241632)[0m             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/utils/__init__.py", line 3122, in run_method
[36m(TaskRunner pid=1241632)[0m     return func(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm-ascend/vllm_ascend/worker/worker_v1.py", line 270, in execute_model
[36m(TaskRunner pid=1241632)[0m     output = self.model_runner.execute_model(scheduler_output,
[36m(TaskRunner pid=1241632)[0m              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[36m(TaskRunner pid=1241632)[0m     return func(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1959, in execute_model
[36m(TaskRunner pid=1241632)[0m     hidden_states = self._generate_process_reqs_hidden_states(
[36m(TaskRunner pid=1241632)[0m                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1565, in _generate_process_reqs_hidden_states
[36m(TaskRunner pid=1241632)[0m     hidden_states = self.model(
[36m(TaskRunner pid=1241632)[0m                     ^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[36m(TaskRunner pid=1241632)[0m     return self._call_impl(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[36m(TaskRunner pid=1241632)[0m     return forward_call(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/model_executor/models/qwen3_vl.py", line 1576, in forward
[36m(TaskRunner pid=1241632)[0m     hidden_states = self.language_model.model(
[36m(TaskRunner pid=1241632)[0m                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/compilation/decorators.py", line 225, in __call__
[36m(TaskRunner pid=1241632)[0m     return self.forward(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/model_executor/models/qwen3_vl_moe.py", line 108, in forward
[36m(TaskRunner pid=1241632)[0m     hidden_states, residual = layer(
[36m(TaskRunner pid=1241632)[0m                               ^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[36m(TaskRunner pid=1241632)[0m     return self._call_impl(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[36m(TaskRunner pid=1241632)[0m     return forward_call(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/model_executor/models/qwen3_moe.py", line 359, in forward
[36m(TaskRunner pid=1241632)[0m     hidden_states = self.self_attn(
[36m(TaskRunner pid=1241632)[0m                     ^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[36m(TaskRunner pid=1241632)[0m     return self._call_impl(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[36m(TaskRunner pid=1241632)[0m     return forward_call(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/model_executor/models/qwen3_moe.py", line 286, in forward
[36m(TaskRunner pid=1241632)[0m     q, k = self.rotary_emb(positions, q, k)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[36m(TaskRunner pid=1241632)[0m     return self._call_impl(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "/root/miniconda3/envs/qwen3vl_1023/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[36m(TaskRunner pid=1241632)[0m     return forward_call(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/model_executor/custom_op.py", line 44, in forward
[36m(TaskRunner pid=1241632)[0m     return self._forward_method(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 409, in forward_oot
[36m(TaskRunner pid=1241632)[0m     return super().forward_oot(positions, query, key)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/model_executor/custom_op.py", line 79, in forward_oot
[36m(TaskRunner pid=1241632)[0m     return self.forward_native(*args, **kwargs)
[36m(TaskRunner pid=1241632)[0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m   File "vllm/vllm/model_executor/layers/rotary_embedding/mrope.py", line 302, in forward_native
[36m(TaskRunner pid=1241632)[0m     query = query.view(num_tokens, -1, self.head_size)
[36m(TaskRunner pid=1241632)[0m             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[36m(TaskRunner pid=1241632)[0m RuntimeError: shape '[6484, -1, 128]' is invalid for input of size 26556416
```
