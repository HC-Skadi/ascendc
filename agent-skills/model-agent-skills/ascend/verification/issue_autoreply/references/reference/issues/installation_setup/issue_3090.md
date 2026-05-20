# Issue #3090: AttributeError: '_OpNamespace' '_C_ascend' object has no attribute 'weak_ref_tensor'

## 基本信息

- **编号**: #3090
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3090
- **创建时间**: 2025-09-22T07:28:08Z
- **关闭时间**: 2025-10-27T06:50:01Z
- **更新时间**: 2025-10-27T06:50:01Z
- **提交者**: @XuMinhan
- **评论数**: 1

## 标签

无

## 问题描述

### 📚 Title

**infer  的时候，出现的报错**




**安装 bash 脚本**

echo "正在安装 vLLM (原版)"
chmod -R 777 ${vllm_dir}
cp -r ${vllm_dir} /cache/vllm
cd /cache/vllm
VLLM_TARGET_DEVICE=empty pip install -v -e . 

echo "vLLM 安装完成"

echo "正在安装 vLLM-Ascend (昇腾版)"
chmod -R 777 ${vllm_ascend_dir}
cp -r ${vllm_ascend_dir} /cache/vllm-ascend
cd /cache/vllm-ascend
pip install -v  . 
echo "vLLM-Ascend 安装完成"



**已安装依赖**


vllm                                     0.10.2                     /cache/vllm
vllm-ascend                              0.10.2rc1

torch                                    2.7.1
torch_npu                                2.7.1.dev20250724




**报错如下**

[1;36m(EngineCore_DP0 pid=241794)[0;0m WARNING 09-18 10:33:14 [camem.py:64] Failed to import vllm_ascend_C:libvllm_ascend_kernels.so: cannot open shared object file: No such file or directory. Sleep mode will be disabled. 
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:33:26 [parallel_state.py:1165] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:33:26 [model_runner_v1.py:2345] Starting to load model /opt/huawei/dataset/model_dataset/MiniCPM-V-4_5...
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:09<00:27,  9.31s/it]
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:20<00:19,  9.98s/it]
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:25<00:08,  8.51s/it]
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:36<00:00,  9.23s/it]
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:36<00:00,  9.21s/it]
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:07 [default_loader.py:268] Loading weights took 37.35 seconds
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:08 [model_runner_v1.py:2373] Loading model weights took 16.5326 GB
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:20 [backends.py:539] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/12a86a0c53/rank_0_0/backbone for vLLM's torch.compile
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:20 [backends.py:550] Dynamo bytecode transform time: 10.19 s
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:23 [backends.py:215] Compiling a graph for dynamic shape takes 2.72 s
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:27 [monitor.py:34] torch.compile takes 12.91 s in total
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:28 [worker_v1.py:198] Available memory: 39442891776, total memory: 65452113920
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:28 [kv_cache_utils.py:864] GPU KV cache size: 267,392 tokens
[1;36m(EngineCore_DP0 pid=241794)[0;0m INFO 09-18 10:34:28 [kv_cache_utils.py:868] Maximum concurrency for 4,096 tokens per request: 65.28x
[1;36m(EngineCore_DP0 pid=241794)[0;0m 
Capturing ACL graphs (mixed prefill-decode, PIECEWISE):   0%|          | 0/3 [00:00<?, ?it/s]
Capturing ACL graphs (mixed prefill-decode, PIECEWISE):   0%|          | 0/3 [00:00<?, ?it/s]
[1;36m(EngineCore_DP0 pid=241794)[0;0m /cache/vllm/vllm/v1/engine/core.py:709: ResourceWarning: Unclosed context <zmq.Context() at 0xffff3aad6540>
[1;36m(EngineCore_DP0 pid=241794)[0;0m   engine_core = EngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718] EngineCore failed to start.
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718] Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/v1/engine/core.py", line 709, in run_engine_core
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     engine_core = EngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/v1/engine/core.py", line 505, in __init__
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/v1/engine/core.py", line 91, in __init__
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     self._initialize_kv_caches(vllm_config)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/v1/engine/core.py", line 215, in _initialize_kv_caches
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     self.model_executor.initialize_from_config(kv_cache_configs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/v1/executor/abstract.py", line 74, in initialize_from_config
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     self.collective_rpc("compile_or_warm_up_model")
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     answer = run_method(self.driver_worker, method, args, kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/utils/__init__.py", line 3060, in run_method
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return func(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/worker_v1.py", line 264, in compile_or_warm_up_model
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     self.model_runner.capture_model()
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2931, in capture_model
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     self._capture_model()
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2912, in _capture_model
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     self._capture_aclgraphs(
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2889, in _capture_aclgraphs
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     self._dummy_run(num_tokens,
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return func(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2222, in _dummy_run
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     hidden_states = self._generate_dummy_run_hidden_states(
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2070, in _generate_dummy_run_hidden_states
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     hidden_states = self.model(input_ids=input_ids,
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return forward_call(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/model_executor/models/minicpmv.py", line 1186, in forward
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     hidden_states = self.llm.model(
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/compilation/decorators.py", line 312, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     model_output = self.forward(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/cache/vllm/vllm/model_executor/models/qwen2.py", line 342, in forward
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     def forward(
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return forward_call(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return fn(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return self._wrapped_call(self, *args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/fx/graph_module.py", line 406, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     raise e
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/fx/graph_module.py", line 393, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return forward_call(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "<eval_with_key>.74", line 297, in forward
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     submod_0 = self.submod_0(l_inputs_embeds_, s0, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s1);  l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_ = l_positions_ = None
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/compilation/acl_graph.py", line 164, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     entry.output = weak_ref_tensors(output)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/utils.py", line 618, in weak_ref_tensors
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return tuple(weak_ref_tensor(t) for t in tensors)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/utils.py", line 618, in <genexpr>
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return tuple(weak_ref_tensor(t) for t in tensors)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/utils.py", line 601, in weak_ref_tensor
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     return torch.ops._C_ascend.weak_ref_tensor(tensor)
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/_ops.py", line 1267, in __getattr__
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718]     raise AttributeError(
[1;36m(EngineCore_DP0 pid=241794)[0;0m ERROR 09-18 10:34:29 [core.py:718] AttributeError: '_OpNamespace' '_C_ascend' object has no attribute 'weak_ref_tensor'
[1;36m(EngineCore_DP0 pid=241794)[0;0m Process EngineCore_DP0:
[1;36m(EngineCore_DP0 pid=241794)[0;0m Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/multiprocessing/process.py", line 315, in _bootstrap
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self.run()
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/multiprocessing/process.py", line 108, in run
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self._target(*self._args, **self._kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/v1/engine/core.py", line 722, in run_engine_core
[1;36m(EngineCore_DP0 pid=241794)[0;0m     raise e
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/v1/engine/core.py", line 709, in run_engine_core
[1;36m(EngineCore_DP0 pid=241794)[0;0m     engine_core = EngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/v1/engine/core.py", line 505, in __init__
[1;36m(EngineCore_DP0 pid=241794)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/v1/engine/core.py", line 91, in __init__
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self._initialize_kv_caches(vllm_config)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/v1/engine/core.py", line 215, in _initialize_kv_caches
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self.model_executor.initialize_from_config(kv_cache_configs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/v1/executor/abstract.py", line 74, in initialize_from_config
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self.collective_rpc("compile_or_warm_up_model")
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
[1;36m(EngineCore_DP0 pid=241794)[0;0m     answer = run_method(self.driver_worker, method, args, kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/utils/__init__.py", line 3060, in run_method
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return func(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/worker_v1.py", line 264, in compile_or_warm_up_model
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self.model_runner.capture_model()
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2931, in capture_model
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self._capture_model()
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2912, in _capture_model
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self._capture_aclgraphs(
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2889, in _capture_aclgraphs
[1;36m(EngineCore_DP0 pid=241794)[0;0m     self._dummy_run(num_tokens,
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return func(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2222, in _dummy_run
[1;36m(EngineCore_DP0 pid=241794)[0;0m     hidden_states = self._generate_dummy_run_hidden_states(
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2070, in _generate_dummy_run_hidden_states
[1;36m(EngineCore_DP0 pid=241794)[0;0m     hidden_states = self.model(input_ids=input_ids,
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return forward_call(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/model_executor/models/minicpmv.py", line 1186, in forward
[1;36m(EngineCore_DP0 pid=241794)[0;0m     hidden_states = self.llm.model(
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/compilation/decorators.py", line 312, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m     model_output = self.forward(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/cache/vllm/vllm/model_executor/models/qwen2.py", line 342, in forward
[1;36m(EngineCore_DP0 pid=241794)[0;0m     def forward(
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return forward_call(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return fn(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return self._wrapped_call(self, *args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/fx/graph_module.py", line 406, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m     raise e
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/fx/graph_module.py", line 393, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return forward_call(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "<eval_with_key>.74", line 297, in forward
[1;36m(EngineCore_DP0 pid=241794)[0;0m     submod_0 = self.submod_0(l_inputs_embeds_, s0, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s1);  l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_ = l_positions_ = None
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/compilation/acl_graph.py", line 164, in __call__
[1;36m(EngineCore_DP0 pid=241794)[0;0m     entry.output = weak_ref_tensors(output)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/utils.py", line 618, in weak_ref_tensors
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return tuple(weak_ref_tensor(t) for t in tensors)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/utils.py", line 618, in <genexpr>
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return tuple(weak_ref_tensor(t) for t in tensors)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/vllm_ascend/utils.py", line 601, in weak_ref_tensor
[1;36m(EngineCore_DP0 pid=241794)[0;0m     return torch.ops._C_ascend.weak_ref_tensor(tensor)
[1;36m(EngineCore_DP0 pid=241794)[0;0m   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/_ops.py", line 1267, in __getattr__
[1;36m(EngineCore_DP0 pid=241794)[0;0m     raise AttributeError(
[1;36m(EngineCore_DP0 pid=241794)[0;0m AttributeError: '_OpNamespace' '_C_ascend' object has no attribute 'weak_ref_tensor'
Traceback (most recent call last):
  File "/opt/huawei/schedule-train/algorithm/miniCPM_V_4_5_vllm/miniCPM_infer_vllm_test.py", line 317, in <module>
    main(args)
  File "/opt/huawei/schedule-train/algorithm/miniCPM_V_4_5_vllm/miniCPM_infer_vllm_test.py", line 263, in main
    llm = LLM(**engine_args)
  File "/cache/vllm/vllm/entrypoints/llm.py", line 282, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
  File "/cache/vllm/vllm/engine/llm_engine.py", line 493, in from_engine_args
    return engine_cls.from_vllm_config(
  File "/cache/vllm/vllm/v1/engine/llm_engine.py", line 134, in from_vllm_config
    return cls(vllm_config=vllm_config,
  File "/cache/vllm/vllm/v1/engine/llm_engine.py", line 111, in __init__
    self.engine_core = EngineCoreClient.make_client(
  File "/cache/vllm/vllm/v1/engine/core_client.py", line 80, in make_client
    return SyncMPClient(vllm_config, executor_class, log_stats)
  File "/cache/vllm/vllm/v1/engine/core_client.py", line 602, in __init__
    super().__init__(
  File "/cache/vllm/vllm/v1/engine/core_client.py", line 453, in __init__
    self.resources.engine_manager = engine_manager
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/contextlib.py", line 126, in __exit__
    next(self.gen)
  File "/cache/vllm/vllm/v1/engine/utils.py", line 729, in launch_core_engines
    wait_for_engine_startup(
  File "/cache/vllm/vllm/v1/engine/utils.py", line 782, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-09-18-10:34:30 (PID:241337, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute




