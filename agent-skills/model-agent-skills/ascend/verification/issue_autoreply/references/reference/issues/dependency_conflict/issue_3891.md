# Issue #3891: [Bug]: Run Qwen3-VL-30B-A3B-Instruct failed. `moe_comm_method` is None: 'NoneType' object has no attribute 'prepare'

## 基本信息

- **编号**: #3891
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3891
- **创建时间**: 2025-10-30T03:06:47Z
- **关闭时间**: 2025-11-04T01:16:20Z
- **更新时间**: 2025-11-04T01:16:20Z
- **提交者**: @shen-shanshan
- **评论数**: 0

## 标签

bug; module:multimodal

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm: release/v0.11.1
vllm-ascend: main
```

</details>


### 🐛 Describe the bug

Run:

```bash
vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen3-VL-30B-A3B-Instruct \
--max_model_len 16384 \
--tensor-parallel-size 4 \
--enable-expert-parallel \
--enforce-eager
```

Log:

```
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703] WorkerProc hit an exception.
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703] Traceback (most recent call last):
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 698, in worker_busy_loop
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     output = func(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 230, in determine_available_memory
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     self.model_runner.profile_run()
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2814, in profile_run
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     hidden_states = self._dummy_run(
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return func(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2778, in _dummy_run
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2585, in _generate_dummy_run_hidden_states
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 1698, in forward
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     hidden_states = self.language_model.model(
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 304, in __call__
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self.forward(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl_moe.py", line 109, in forward
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     hidden_states, residual = layer(
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 392, in forward
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     hidden_states = self.mlp(hidden_states)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 197, in forward
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     final_hidden_states = self.experts(
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self._call_impl(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return forward_call(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 46, in forward
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self._forward_method(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/custom_op.py", line 81, in forward_oot
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self.forward_native(*args, **kwargs)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2206, in forward_native
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     fused_output = torch.ops.vllm.moe_forward(
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/root/miniconda3/envs/vllm/lib/python3.10/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self._op(*args, **(kwargs or {}))
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2604, in moe_forward
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 335, in forward_impl
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703]     hidden_states, router_logits, mc2_mask, context_metadata = forward_context.moe_comm_method.prepare(
(Worker_TP0_EP0 pid=125825) ERROR 10-30 03:01:59 [multiproc_executor.py:703] AttributeError: 'NoneType' object has no attribute 'prepare'
```
