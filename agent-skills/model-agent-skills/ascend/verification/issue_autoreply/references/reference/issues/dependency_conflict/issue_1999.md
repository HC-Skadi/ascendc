# Issue #1999: [Bug]: Flaky test failed: Qwen/Qwen3-30B-A3B accuracy failed under HDK 23.0.6

## 基本信息

- **编号**: #1999
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1999
- **创建时间**: 2025-07-25T01:15:04Z
- **关闭时间**: 2025-12-23T12:45:41Z
- **更新时间**: 2025-12-23T12:45:41Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

It seems all flaky test are using `23.0.6`, but `23.0.5` no error.

<details>
<summary>npu-smi info</summary>

```
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.6                   Version: 23.0.6                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 93.2        41                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2820 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 96.7        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2823 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 92.4        41                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2820 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 96.3        40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2822 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C[15](https://github.com/vllm-project/vllm-ascend/actions/runs/16497263917/job/46645959156#step:4:17)],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```

</details>

Key error 1: `NPU function error: c10_npu::acl::AclmdlRIExecuteAsync(model_ri_, c10_npu::getCurrentNPUStream()), error code is 507000`
https://github.com/vllm-project/vllm-ascend/actions/runs/16497263917/job/46645959156#step:18:3760
https://github.com/vllm-project/vllm-ascend/actions/runs/16436605833/job/46447725812#step:18:3660
https://github.com/vllm-project/vllm-ascend/actions/runs/16432508290/job/46436424122#step:18:3720
https://github.com/vllm-project/vllm-ascend/actions/runs/16410175951/job/46363331242#step:18:3660

Key error 2: `RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.`

https://github.com/vllm-project/vllm-ascend/actions/runs/16227120546/job/45821525378

### 🐛 Describe the bug

Key error1: `NPU function error: c10_npu::acl::AclmdlRIExecuteAsync(model_ri_, c10_npu::getCurrentNPUStream()), error code is 507000`

<details>
<summary>detail error log</summary>

```
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 190, in execute_model
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     output = self.model_runner.execute_model(scheduler_output,
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1424, in execute_model
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     num_scheduled_tokens_np) = (self._process_reqs(
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1150, in _process_reqs
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     hidden_states = self.model(
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_moe.py", line 525, in forward
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/decorators.py", line 246, in __call__
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_moe.py", line 350, in forward
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     def forward(
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 361, in __call__
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     raise e
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 348, in __call__
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "<eval_with_key>.98", line 626, in forward
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     submod_80 = self.submod_80(getitem_198, s0, l_self_modules_layers_modules_39_modules_self_attn_modules_o_proj_parameters_weight_, getitem_199, l_self_modules_layers_modules_39_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_39_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_40_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_40_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_40_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_40_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  getitem_198 = l_self_modules_layers_modules_39_modules_self_attn_modules_o_proj_parameters_weight_ = getitem_199 = l_self_modules_layers_modules_39_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_39_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_40_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_40_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_40_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_40_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/compilation/piecewise_backend.py", line 224, in __call__
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     entry.aclgraph.replay()
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/graphs.py", line 225, in replay
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522]     super().replay()
(VllmWorker rank=2 pid=5826) ERROR 07-22 07:46:52 [multiproc_executor.py:522] RuntimeError: replay:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:201 NPU function error: c10_npu::acl::AclmdlRIExecuteAsync(model_ri_, c10_npu::getCurrentNPUStream()), error code is 507000
```

</details>

Keyerror 2: `RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.`

<details>
<summary>detail error log</summary>

```
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 217, in execute_model
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     output = self.model_runner.execute_model(scheduler_output,
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1403, in execute_model
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     num_scheduled_tokens_np) = (self._process_reqs(
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1129, in _process_reqs
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     hidden_states = self.model(
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_moe.py", line 525, in forward
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/compilation/decorators.py", line 246, in __call__
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     model_output = self.forward(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen3_moe.py", line 350, in forward
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     def forward(
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 361, in __call__
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     raise e
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 348, in __call__
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "<eval_with_key>.98", line 633, in forward
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     submod_82 = self.submod_82(getitem_203, s0, l_self_modules_layers_modules_40_modules_self_attn_modules_o_proj_parameters_weight_, getitem_204, l_self_modules_layers_modules_40_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_40_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_41_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_41_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_41_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_41_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  getitem_203 = l_self_modules_layers_modules_40_modules_self_attn_modules_o_proj_parameters_weight_ = getitem_204 = l_self_modules_layers_modules_40_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_40_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_41_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_41_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_41_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_41_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/__w/vllm-ascend/vllm-ascend/vllm-ascend/vllm_ascend/compilation/piecewise_backend.py", line 128, in __call__
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self.compiled_graph_for_general_shape(*args)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 361, in __call__
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     raise e
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 348, in __call__
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "<eval_with_key>.83", line 20, in forward
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     all_reduce_1 = torch.ops._c10d_functional.all_reduce(moe_forward, 'sum', '3')
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522]     return self._op(*args, **(kwargs or {}))
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is HcclAllreduce.
(VllmWorker rank=1 pid=7549) ERROR 07-11 19:06:51 [multiproc_executor.py:522] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
```

</details>
