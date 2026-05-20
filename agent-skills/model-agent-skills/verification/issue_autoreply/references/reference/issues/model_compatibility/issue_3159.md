# Issue #3159: vllm-ascend0.10.2rc1 - A3 - Qwen3-235B-A22B W8A8 + DP2 + TP8 + EP + alcgraph 起服务报错

## 基本信息

- **编号**: #3159
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3159
- **创建时间**: 2025-09-24T11:46:59Z
- **关闭时间**: 2025-12-15T13:40:59Z
- **更新时间**: 2025-12-15T13:40:59Z
- **提交者**: @sanlio36
- **评论数**: 3

## 标签

无

## 问题描述

> # ✅ Qwen3-235B-A22B W8A8 + DP2 + TP8 + EP + alcgraph
> ## command:
> ```bash
> 
> vllm serve /root/.cache/modelscope/hub/models/vllm-ascend/Qwen3-235B-A22B-W8A8 \
> --served-model-name qwen3 --port 1025 --host 11.87.189.101 \
> --data-parallel-size 2 \
> --tensor-parallel-size 8 \
> --seed 1024 \
> --quantization ascend \
> --enable-expert-parallel \
> --max-num-seqs 16 \
> --max-model-len 4096 \
> --trust-remote-code \
> --no-enable-prefix-caching \
> --gpu-memory-utilization 0.7  &
> ```
> ## output:
> ```
> [1;36m(Worker_DP0_TP3_EP3 pid=918102)[0;0m INFO 09-24 09:47:53 [backends.py:215] Compiling a graph for dynamic shape takes 4.13 s
> [1;36m(Worker_DP0_TP5_EP5 pid=919166)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.05 s
> [1;36m(Worker_DP1_TP2_EP10 pid=917591)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.03 s
> [1;36m(Worker_DP1_TP7_EP15 pid=920204)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.04 s
> [1;36m(Worker_DP1_TP6_EP14 pid=919678)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.07 s
> [1;36m(Worker_DP0_TP7_EP7 pid=920218)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.10 s
> [1;36m(Worker_DP1_TP3_EP11 pid=918105)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.08 s
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.15 s
> [1;36m(Worker_DP0_TP4_EP4 pid=918628)[0;0m INFO 09-24 09:47:54 [backends.py:215] Compiling a graph for dynamic shape takes 4.11 s
> [1;36m(Worker_DP0_TP2_EP2 pid=917588)[0;0m INFO 09-24 09:47:55 [backends.py:215] Compiling a graph for dynamic shape takes 4.11 s
> [1;36m(Worker_DP1_TP4_EP12 pid=918626)[0;0m INFO 09-24 09:47:55 [backends.py:215] Compiling a graph for dynamic shape takes 4.30 s
> [1;36m(Worker_DP0_TP1_EP1 pid=917512)[0;0m INFO 09-24 09:47:55 [backends.py:215] Compiling a graph for dynamic shape takes 4.17 s
> [1;36m(Worker_DP0_TP0_EP0 pid=917469)[0;0m INFO 09-24 09:47:56 [backends.py:215] Compiling a graph for dynamic shape takes 4.16 s
> [1;36m(Worker_DP1_TP5_EP13 pid=919153)[0;0m INFO 09-24 09:47:56 [backends.py:215] Compiling a graph for dynamic shape takes 4.14 s
> [1;36m(Worker_DP1_TP0_EP8 pid=917468)[0;0m INFO 09-24 09:47:57 [backends.py:215] Compiling a graph for dynamic shape takes 4.18 s
> [1;36m(Worker_DP1_TP1_EP9 pid=917513)[0;0m INFO 09-24 09:47:57 [backends.py:215] Compiling a graph for dynamic shape takes 4.11 s
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654] WorkerProc hit an exception.
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654] Traceback (most recent call last):
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 649, in worker_busy_loop
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     output = func(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 169, in determine_available_memory
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     self.model_runner.profile_run()
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2251, in profile_run
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     hidden_states = self._dummy_run(self.max_num_tokens,
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return func(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2222, in _dummy_run
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     hidden_states = self._generate_dummy_run_hidden_states(
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2070, in _generate_dummy_run_hidden_states
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     hidden_states = self.model(input_ids=input_ids,
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 387, in forward
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 305, in __call__
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     output = self.compiled_callable(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 655, in _fn
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return fn(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/qwen3_moe.py", line 280, in forward
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     def forward(
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return fn(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return self._wrapped_call(self, *args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     raise e
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return self._call_impl(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     return forward_call(*args, **kwargs)
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]   File "<eval_with_key>.190", line 1712, in forward
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]     submod_2 = self.submod_2(getitem_3, s0, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_scale_reciprocal, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_offset, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_deq_scale_, getitem_4, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_bias_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_bias_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_scale_reciprocal, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_offset, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_deq_scale_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_quant_bias_, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_bias_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_bias_, getitem_5, s1, getitem_6);  getitem_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_scale_reciprocal = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_aclnn_input_offset = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_deq_scale_ = getitem_4 = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_bias_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_bias_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_scale_reciprocal = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_aclnn_input_offset = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_deq_scale_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_quant_bias_ = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_bias_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_bias_ = None
> [1;36m(Worker_DP0_TP6_EP6 pid=919692)[0;0m ERROR 09-24 09:48:02 [multiproc_executor.py:654]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> ``` 

 _Originally posted by @zhangxinyuehfad in [#3022](https://github.com/vllm-project/vllm-ascend/issues/3022#issuecomment-3311362891)_
