# Issue #5375: [Bug]: run test case in local failed: moe_expert_num = len(expert_map) TypeError: object of type 'NoneType' has no len()

## 基本信息

- **编号**: #5375
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5375
- **创建时间**: 2025-12-25T13:13:09Z
- **关闭时间**: 2025-12-26T12:26:23Z
- **更新时间**: 2025-12-26T12:26:23Z
- **提交者**: @leo-pony
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
code of v0.13.0
```

</details>


### 🐛 Describe the bug

pytest -sv tests/e2e/singlecard/spec_decode_v1/test_v1_mtp_correctness.py::test_mtp1_correctness_eager

(Worker_EP0 pid=168807)
(Worker_EP0 pid=168807) INFO 12-25 12:19:14 [model_runner_v1.py:2224] Loading model weights took 11.2871 GB
 WorkerProc hit an exception.
 Traceback (most recent call last):
   File "/mnt/code/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
     output = func(*args, **kwargs)
              ^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
     return func(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
     self.model_runner.profile_run()
   File "/mnt/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2194, in profile_run
     self._dummy_run(mc2_tokens_capacity,
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
     return func(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2140, in _dummy_run
     hidden_states = self._generate_dummy_run_hidden_states(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1923, in _generate_dummy_run_hidden_states
     hidden_states = self.model(input_ids=input_ids,
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
     return forward_call(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/model_executor/models/deepseek_v2.py", line 1470, in forward
     hidden_states = self.model(
                     ^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/compilation/decorators.py", line 372, in __call__
     return self.forward(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/patch/worker/patch_deepseek.py", line 47, in forward
     hidden_states, residual = layer(positions, hidden_states, residual,
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
     return forward_call(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/model_executor/models/deepseek_v2.py", line 1227, in forward
     hidden_states = self.mlp(hidden_states)
                     ^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
     return forward_call(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/model_executor/models/deepseek_v2.py", line 356, in forward
     fused_moe_out = self.experts(
                     ^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
     return self._call_impl(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
     return forward_call(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 457, in forward
     shared_out, fused_out = AscendFusedMoE.forward(
                             ^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/model_executor/custom_op.py", line 47, in forward
     return self._forward_method(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/model_executor/custom_op.py", line 82, in forward_oot
     return self.forward_native(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1731, in forward_native
     shared_output, fused_output = torch.ops.vllm.moe_forward_shared(
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1243, in __call__
     return self._op(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2118, in moe_forward_shared
     return self.forward_impl(hidden_states, router_logits)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 481, in forward_impl
     fused_output = AscendFusedMoE.forward_impl(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 367, in forward_impl
     final_hidden_states = self.quant_method.apply(
                           ^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 124, in apply
     return moe_comm_method.fused_experts(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 121, in fused_experts
     results = self.token_dispatcher.token_dispatch(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 198, in token_dispatch
     kwargs_mc2 = self.get_dispatch_mc2_kwargs(hidden_states, topk_weights,
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 144, in get_dispatch_mc2_kwargs
     moe_expert_num = len(expert_map)
                      ^^^^^^^^^^^^^^^
 TypeError: object of type 'NoneType' has no len()
