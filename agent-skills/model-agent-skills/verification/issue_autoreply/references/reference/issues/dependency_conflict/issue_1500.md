# Issue #1500: [Bug]:将910b2上跑通的环境迁移到310p后出现了bug

## 基本信息

- **编号**: #1500
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1500
- **创建时间**: 2025-06-28T08:01:59Z
- **关闭时间**: 2025-12-23T11:25:58Z
- **更新时间**: 2025-12-23T11:25:58Z
- **提交者**: @xzl12080
- **评论数**: 5

## 标签

bug; 310p

## 问题描述

### Your current environment

torch=2.5.1
torch-npu=2.5.1
vllm=0.7.3
vllm-ascend=0.7.3
cann=8.0.0

### 🐛 Describe the bug

  warnings.warn(msg, ImportWarning)
/root/miniconda3/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, whi
ch currently does not support them, if you need to enable them, please do not use transfer_to_npu.
  warnings.warn(msg, RuntimeWarning)
WARNING 06-28 15:57:14 utils.py:2262] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter n
ot implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd46ac8df0>
INFO 06-28 15:57:20 model_runner.py:902] Starting to load model models/Qwen2-0.5B...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.46it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.45it/s]

INFO 06-28 15:57:45 model_runner.py:907] Loading model weights took 0.9394 GB
mki_log log dir:/root/atb/log exist
[rank0]: Traceback (most recent call last):
[rank0]:   File "/root/sys_project/xzl.py", line 13, in <module>
[rank0]:     llm = LLM(model="models/Qwen2-0.5B",tensor_parallel_size=1, trust_remote_code=True)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/utils.py", line 1022, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 242, in __init__
[rank0]:     self.llm_engine = self.engine_class.from_engine_args(
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 489, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
[rank0]:     self._initialize_kv_caches()
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
[rank0]:     self.model_executor.determine_num_available_blocks())
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
[rank0]:     results = self.collective_rpc("determine_num_available_blocks")
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 255, in determine_num_available_blocks
[rank0]:     self.model_runner.profile_run()
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1490, in profile_run
[rank0]:     self.execute_model(model_input, kv_caches, intermediate_tensors)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1270, in execute_model
[rank0]:     hidden_or_intermediate_states = model_executable(
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward
[rank0]:     hidden_states = self.model(input_ids, positions, kv_caches,
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
[rank0]:     return self.forward(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward
[rank0]:     hidden_states, residual = layer(
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 247, in forward
[rank0]:     hidden_states = self.self_attn(
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 178, in forward
[rank0]:     q, k = self.rotary_emb(positions, q, k)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
[rank0]:     return self._forward_method(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/vllm_ascend/ops/rotary_embedding.py", line 44, in rope_forward_oot
[rank0]:     torch_npu._npu_rotary_embedding(
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 54, in wrapper
[rank0]:     return api_func(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 62, in generated_function
[rank0]:     return getattr(torch.ops.atb, api_name)(*args, **kwargs)
[rank0]:   File "/root/miniconda3/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
[rank0]:     return self._op(*args, **(kwargs or {}))
[rank0]: RuntimeError: setup failed!
[ERROR] 2025-06-28-15:57:56 (PID:118889, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
