# Issue #2567: [Bug]: vllm-ascend/Qwen3-30B-A3B-W8A8 + EP + TP start failed due to AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027

## 基本信息

- **编号**: #2567
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2567
- **创建时间**: 2025-08-27T03:07:05Z
- **关闭时间**: 2025-12-03T07:08:11Z
- **更新时间**: 2025-12-03T07:08:11Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 1

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

vllm : v0.10.0
vllm-ascend : v0.10.0rc1


### 🐛 Describe the bug

command:
```
VLLM_USE_MODELSCOPE=True vllm serve /root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-30B-A3B-W8A8  --max_model_len 8192 --tensor_parallel_size 2  --trust_remote_code --dtype auto --quantization ascend  &

# add config --compilation_config '{"cudagraph_capture_sizes": [16, 32, 64, 128]}' also failed 
VLLM_USE_MODELSCOPE=True vllm serve /root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-30B-A3B-W8A8  --tensor_parallel_size 4  --dtype auto --trust_remote_code --quantization ascend  --enable-expert-parallel --compilation_config '{"cudagraph_capture_sizes": [16, 32, 64, 128]}' &
```
```
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] WorkerProc hit an exception.
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] Traceback (most recent call last):
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 597, in worker_busy_loop
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     output = func(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 256, in compile_or_warm_up_model
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self.model_runner.capture_model()
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2491, in capture_model
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self._capture_model()
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2472, in _capture_model
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self._capture_aclgraphs(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2448, in _capture_aclgraphs
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self._dummy_run(num_tokens,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return func(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2069, in _dummy_run
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     hidden_states = self._generate_dummy_run_hidden_states(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1923, in _generate_dummy_run_hidden_states
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     hidden_states = self.model(input_ids=input_ids,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 391, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 312, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     model_output = self.forward(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 284, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     def forward(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return fn(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     raise e
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "<eval_with_key>.98", line 689, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     submod_2 = self.submod_2(getitem_3, s0, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_scale_reciprocal, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_offset, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_deq_scale_, getitem_4, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_scale_reciprocal, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_offset, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_deq_scale_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_quant_bias_, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  getitem_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_scale_reciprocal = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_offset = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_deq_scale_ = getitem_4 = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_scale_reciprocal = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_offset = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_deq_scale_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_quant_bias_ = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 153, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     output = self.runnable(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/compilation/cuda_piecewise_backend.py", line 96, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self.compiled_graph_for_general_shape(*args)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     raise e
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "<eval_with_key>.3", line 20, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     moe_forward = torch.ops.vllm.moe_forward(view_2, linear, 'model.layers.0.mlp.experts');  view_2 = linear = None
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._op(*args, **(kwargs or {}))
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1771, in moe_forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self.forward_impl(hidden_states, router_logits)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1681, in forward_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     final_hidden_states = self.quant_method.apply(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 333, in apply
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self.quant_method.apply(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 983, in apply
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return fused_experts_with_all2all(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 433, in fused_experts_with_all2all
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     quantized_tokens, expanded_row_idx, global_expert_tokens, token_scales = init_routing_quant(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                                                                              ^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 384, in init_routing_quant
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     global_expert_tokens = torch.bincount(expanded_expert_idx,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] [ERROR] 2025-08-27-01:44:46 (PID:102322, Device:2, RankID:-1) ERR00100 PTA call acl api failed.
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] EE9999: Inner Error!
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] EE9999: [PID: 102322] 2025-08-27-01:44:46.558.672 Not allow to synchronize captured-stream, stream_id=9.[FUNC:StreamSynchronize][FILE:api_error.cc][LINE:960]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]         TraceBack (most recent call last):
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]        rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]        synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] Traceback (most recent call last):
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 597, in worker_busy_loop
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     output = func(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]              ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 256, in compile_or_warm_up_model
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self.model_runner.capture_model()
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2491, in capture_model
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self._capture_model()
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2472, in _capture_model
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self._capture_aclgraphs(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2448, in _capture_aclgraphs
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     self._dummy_run(num_tokens,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return func(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2069, in _dummy_run
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     hidden_states = self._generate_dummy_run_hidden_states(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1923, in _generate_dummy_run_hidden_states
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     hidden_states = self.model(input_ids=input_ids,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 391, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 312, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     model_output = self.forward(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 284, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     def forward(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return fn(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     raise e
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "<eval_with_key>.98", line 689, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     submod_2 = self.submod_2(getitem_3, s0, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_scale_reciprocal, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_offset, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_deq_scale_, getitem_4, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_scale_reciprocal, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_offset, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_deq_scale_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_quant_bias_, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  getitem_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_scale_reciprocal = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_offset = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_deq_scale_ = getitem_4 = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_scale_reciprocal = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_offset = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_deq_scale_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_quant_bias_ = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_ = None
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 153, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     output = self.runnable(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/compilation/cuda_piecewise_backend.py", line 96, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self.compiled_graph_for_general_shape(*args)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._wrapped_call(self, *args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     raise e
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._call_impl(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return forward_call(*args, **kwargs)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "<eval_with_key>.3", line 20, in forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     moe_forward = torch.ops.vllm.moe_forward(view_2, linear, 'model.layers.0.mlp.experts');  view_2 = linear = None
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self._op(*args, **(kwargs or {}))
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1771, in moe_forward
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self.forward_impl(hidden_states, router_logits)
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1681, in forward_impl
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     final_hidden_states = self.quant_method.apply(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 333, in apply
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return self.quant_method.apply(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 983, in apply
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     return fused_experts_with_all2all(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 433, in fused_experts_with_all2all
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     quantized_tokens, expanded_row_idx, global_expert_tokens, token_scales = init_routing_quant(
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                                                                              ^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 384, in init_routing_quant
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]     global_expert_tokens = torch.bincount(expanded_expert_idx,
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] [ERROR] 2025-08-27-01:44:46 (PID:102322, Device:2, RankID:-1) ERR00100 PTA call acl api failed.
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] EE9999: Inner Error!
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602] EE9999: [PID: 102322] 2025-08-27-01:44:46.558.672 Not allow to synchronize captured-stream, stream_id=9.[FUNC:StreamSynchronize][FILE:api_error.cc][LINE:960]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]         TraceBack (most recent call last):
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]        rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]        synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorker TP2 pid=102322) ERROR 08-27 01:44:46 [multiproc_executor.py:602]

```
