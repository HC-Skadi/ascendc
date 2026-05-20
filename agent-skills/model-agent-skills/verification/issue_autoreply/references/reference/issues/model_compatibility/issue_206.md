# Issue #206: [Usage]: 使用0.7.1rc1四机推理Deepseek-V3报错，RuntimeError: GroupTopkOperation CreateOperation failed!

## 基本信息

- **编号**: #206
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/206
- **创建时间**: 2025-02-28T09:03:37Z
- **关闭时间**: 2025-03-07T12:39:49Z
- **更新时间**: 2025-03-07T12:39:50Z
- **提交者**: @myliangchengyu
- **评论数**: 5

## 标签

无

## 问题描述

### Your current environment

使用**quay.io/ascend/vllm-ascend:v0.7.1rc1**镜像，ray版本2.43.0，环境搭建应该没问题，已经可以四机跑通如Qwen2.5-72B-Instruct等权重，已解决跑Deepseek_v3时报错Torch not compiled with CUDA enabled，出现新报错，报错信息如下：

 ```
ERROR 02-28 09:16:29 worker_base.py:572] Error executing method 'determine_num_available_blocks'. This might cause deadlock in distributed execution.
ERROR 02-28 09:16:29 worker_base.py:572] Traceback (most recent call last):
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 564, in execute_method
ERROR 02-28 09:16:29 worker_base.py:572]     return run_method(target, method, args, kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
ERROR 02-28 09:16:29 worker_base.py:572]     return func(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 02-28 09:16:29 worker_base.py:572]     return func(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker.py", line 226, in determine_num_available_blocks
ERROR 02-28 09:16:29 worker_base.py:572]     self.model_runner.profile_run()
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 02-28 09:16:29 worker_base.py:572]     return func(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1357, in profile_run
ERROR 02-28 09:16:29 worker_base.py:572]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 02-28 09:16:29 worker_base.py:572]     return func(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
ERROR 02-28 09:16:29 worker_base.py:572]     hidden_or_intermediate_states = model_executable(
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return self._call_impl(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return forward_call(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 682, in forward
ERROR 02-28 09:16:29 worker_base.py:572]     hidden_states = self.model(input_ids, positions, kv_caches,
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return self._call_impl(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return forward_call(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 638, in forward
ERROR 02-28 09:16:29 worker_base.py:572]     hidden_states, residual = layer(positions, hidden_states,
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return self._call_impl(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return forward_call(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 565, in forward
ERROR 02-28 09:16:29 worker_base.py:572]     hidden_states = self.mlp(hidden_states)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return self._call_impl(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return forward_call(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 158, in forward
ERROR 02-28 09:16:29 worker_base.py:572]     final_hidden_states = self.experts(
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return self._call_impl(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-28 09:16:29 worker_base.py:572]     return forward_call(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 584, in forward
ERROR 02-28 09:16:29 worker_base.py:572]     final_hidden_states = self.quant_method.apply(
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 118, in apply
ERROR 02-28 09:16:29 worker_base.py:572]     return self.forward(x=x,
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 23, in forward
ERROR 02-28 09:16:29 worker_base.py:572]     return self._forward_method(*args, **kwargs)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/ops/fused_moe.py", line 152, in forward_oot
ERROR 02-28 09:16:29 worker_base.py:572]     topk_weights, topk_ids = group_topk(
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/ops/fused_moe.py", line 49, in group_topk
ERROR 02-28 09:16:29 worker_base.py:572]     torch_npu.npu_group_topk(input=scores, out=scores, group_num=num_expert_group, k=topk_group)
ERROR 02-28 09:16:29 worker_base.py:572]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 02-28 09:16:29 worker_base.py:572]     return self._op(*args, **(kwargs or {}))
ERROR 02-28 09:16:29 worker_base.py:572] RuntimeError: GroupTopkOperation CreateOperation failed!

```
config文件为：

```
{
  "architectures": [
    "DeepseekV3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "configuration_deepseek.DeepseekV3Config",
    "AutoModel": "modeling_deepseek.DeepseekV3Model",
    "AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 0,
  "eos_token_id": 1,
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 163840,
  "model_type": "deepseek_v3",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 8,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 61,
  "num_key_value_heads": 128,
  "num_nextn_predict_layers": 1,
  "pretraining_tp": 1,
  "q_lora_rank": 1536,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32,
    "beta_slow": 1,
    "factor": 40,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "type": "yarn"
  },
  "rope_theta": 10000,
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 4,
  "topk_method": "noaux_tc",
  "torch_dtype": "float16",
  "transformers_version": "4.33.1",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 129280
}
```

在ray head节点四机的启动任务的命令为：
```
vllm serve /data02/DeepSeek-V3 \
    --served_model_name deepseek_v3 \
    -tp 16 -pp 2 \
    --distributed_executor_backend "ray" \
    --max-model-len 1024 \
    --trust-remote-code
```

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

