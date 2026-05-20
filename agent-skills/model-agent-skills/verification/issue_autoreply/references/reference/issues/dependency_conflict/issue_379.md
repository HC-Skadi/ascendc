# Issue #379: [Bug]:  AttributeError: module 'torch_npu' has no attribute '_npu_rotary_embedding'

## 基本信息

- **编号**: #379
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/379
- **创建时间**: 2025-03-24T05:49:18Z
- **关闭时间**: 2025-03-24T07:10:03Z
- **更新时间**: 2025-03-31T15:37:04Z
- **提交者**: @RyanOvO
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

python: 3.10
torch: 2.5.1
torch-npu: 2.5.1rc1
cann: 8.0.RC2.2
vllm-ascend: 0.7.3 rc1
vlllm: 0.7.3



### 🐛 Describe the bug

```
[rank1]: Traceback (most recent call last):
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/cli/rlhf.py", line 5, in <module>
[rank1]:     rlhf_main()
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/llm/train/rlhf.py", line 96, in rlhf_main
[rank1]:     return SwiftRLHF(args).main()
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/llm/base.py", line 47, in main
[rank1]:     result = self.run()
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/llm/train/sft.py", line 137, in run
[rank1]:     trainer = trainer_cls(
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/trainers/rlhf_trainer/grpo_trainer.py", line 226, in __init__
[rank1]:     self.prepare_vllm(model, fast_infer_device)
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/trainers/rlhf_trainer/grpo_trainer.py", line 375, in prepare_vllm
[rank1]:     self.engine = cls(
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/llm/infer/infer_engine/grpo_vllm_engine.py", line 88, in __init__
[rank1]:     self._prepare_engine()
[rank1]:   File "/home/hwtest/hzy/swift-grpo-npu/swift/llm/infer/infer_engine/grpo_vllm_engine.py", line 93, in _prepare_engine
[rank1]:     engine = LLM(**self.engine_args.__dict__)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/utils.py", line 1022, in inner
[rank1]:     return fn(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 242, in __init__
[rank1]:     self.llm_engine = self.engine_class.from_engine_args(
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 489, in from_engine_args
[rank1]:     engine = cls(
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
[rank1]:     self._initialize_kv_caches()
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
[rank1]:     self.model_executor.determine_num_available_blocks())
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 132, in determine_num_available_blocks
[rank1]:     a, b = super().determine_num_available_blocks()
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
[rank1]:     results = self.collective_rpc("determine_num_available_blocks")
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank1]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 227, in determine_num_available_blocks
[rank1]:     self.model_runner.profile_run()
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1360, in profile_run
[rank1]:     self.execute_model(model_input, kv_caches, intermediate_tensors)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank1]:     return func(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1140, in execute_model
[rank1]:     hidden_or_intermediate_states = model_executable(
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank1]:     return self._call_impl(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank1]:     return forward_call(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward
[rank1]:     hidden_states = self.model(input_ids, positions, kv_caches,
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
[rank1]:     return self.forward(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward
[rank1]:     hidden_states, residual = layer(
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank1]:     return self._call_impl(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank1]:     return forward_call(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 247, in forward
[rank1]:     hidden_states = self.self_attn(
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank1]:     return self._call_impl(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank1]:     return forward_call(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 178, in forward
[rank1]:     q, k = self.rotary_emb(positions, q, k)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank1]:     return self._call_impl(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank1]:     return forward_call(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
[rank1]:     return self._forward_method(*args, **kwargs)
[rank1]:   File "/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/site-packages/vllm_ascend/ops/rotary_embedding.py", line 45, in rope_forward_oot
[rank1]:     torch_npu._npu_rotary_embedding(
[rank1]: AttributeError: module 'torch_npu' has no attribute '_npu_rotary_embedding'
[ERROR] 2025-03-24-13:34:28 (PID:553687, Device:2, RankID:-1) ERR99999 UNKNOWN applicaiton exception
/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/tempfile.py:869: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/root/.cache/modelscope/hub/tmp/hf_datasets-_l2pfbk8'>
  _warnings.warn(warn_message, ResourceWarning)
/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/tempfile.py:869: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/root/.cache/modelscope/hub/offload_cache/tmp1r8fi0zv'>
  _warnings.warn(warn_message, ResourceWarning)
/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/tempfile.py:869: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/tmp/tmp9cop1ilc'>
  _warnings.warn(warn_message, ResourceWarning)
[ERROR] 2025-03-24-13:34:29 (PID:553686, Device:1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/tempfile.py:869: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/root/.cache/modelscope/hub/tmp/hf_datasets-b8nnvzw8'>
  _warnings.warn(warn_message, ResourceWarning)
/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/tempfile.py:869: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/root/.cache/modelscope/hub/offload_cache/tmpqyned81w'>
  _warnings.warn(warn_message, ResourceWarning)
/root/miniconda3/envs/hzy_dev_vllm/lib/python3.10/tempfile.py:869: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/tmp/tmpm5z4x890'>
  _warnings.warn(warn_message, ResourceWarning)
```

how to fix it?
