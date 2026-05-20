# Issue #218: [Bug]: AttributeError: module 'torch_npu' has no attribute '_npu_rotary_embedding'

## 基本信息

- **编号**: #218
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/218
- **创建时间**: 2025-03-02T14:58:08Z
- **关闭时间**: 2025-03-04T06:42:04Z
- **更新时间**: 2025-03-22T03:17:28Z
- **提交者**: @huangwei-xy
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.0                   Version: 23.0.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B                | OK            | 70.6        42                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           1473 / 13553      1    / 32768         |
+===========================+===============+====================================================+
| 1     910B                | OK            | 68.7        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           3191 / 15665      1    / 32768         |
+===========================+===============+====================================================+
| 2     910B                | OK            | 69.4        37                0    / 0             |
| 0                         | 0000:41:00.0  | 0           2037 / 15665      1    / 32768         |
+===========================+===============+====================================================+

package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux

```

</details>


### 🐛 Describe the bug

I have installed the following packages:

vllm                              0.1.dev1+g82fbeae.empty
vllm_ascend                       0.1.dev66+g4674095 
torch                             2.5.1
torch-npu                         2.5.1.dev20250218
torchaudio                        2.5.1
torchvision                       0.20.1

but where run “vllm serve Qwen2.5-0.5B-Instruct”，show error of : AttributeError: module 'torch_npu' has no attribute '_npu_rotary_embedding', the following is error information:

INFO 03-02 22:42:52 [parallel_state.py:948] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.32it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  1.32it/s]

INFO 03-02 22:42:57 [loader.py:422] Loading weights took 0.84 seconds
ERROR 03-02 22:42:58 [engine.py:409] module 'torch_npu' has no attribute '_npu_rotary_embedding'
ERROR 03-02 22:42:58 [engine.py:409] Traceback (most recent call last):
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 400, in run_mp_engine
ERROR 03-02 22:42:58 [engine.py:409]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 125, in from_engine_args
ERROR 03-02 22:42:58 [engine.py:409]     return cls(ipc_path=ipc_path,
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 77, in __init__
ERROR 03-02 22:42:58 [engine.py:409]     self.engine = LLMEngine(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 277, in __init__
ERROR 03-02 22:42:58 [engine.py:409]     self._initialize_kv_caches()
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 426, in _initialize_kv_caches
ERROR 03-02 22:42:58 [engine.py:409]     self.model_executor.determine_num_available_blocks())
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
ERROR 03-02 22:42:58 [engine.py:409]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 03-02 22:42:58 [engine.py:409]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/utils.py", line 2232, in run_method
ERROR 03-02 22:42:58 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-02 22:42:58 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/data/vllm-ascend/vllm_ascend/worker.py", line 226, in determine_num_available_blocks
ERROR 03-02 22:42:58 [engine.py:409]     self.model_runner.profile_run()
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-02 22:42:58 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/data/vllm-ascend/vllm_ascend/model_runner.py", line 1341, in profile_run
ERROR 03-02 22:42:58 [engine.py:409]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 03-02 22:42:58 [engine.py:409]     return func(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/data/vllm-ascend/vllm_ascend/model_runner.py", line 1125, in execute_model
ERROR 03-02 22:42:58 [engine.py:409]     hidden_or_intermediate_states = model_executable(
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 463, in forward
ERROR 03-02 22:42:58 [engine.py:409]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
ERROR 03-02 22:42:58 [engine.py:409]     return self.forward(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 339, in forward
ERROR 03-02 22:42:58 [engine.py:409]     hidden_states, residual = layer(
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 243, in forward
ERROR 03-02 22:42:58 [engine.py:409]     hidden_states = self.self_attn(
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 176, in forward
ERROR 03-02 22:42:58 [engine.py:409]     q, k = self.rotary_emb(positions, q, k)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return self._call_impl(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 03-02 22:42:58 [engine.py:409]     return forward_call(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/root/anaconda3/envs/vllmDeepseek/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
ERROR 03-02 22:42:58 [engine.py:409]     return self._forward_method(*args, **kwargs)
ERROR 03-02 22:42:58 [engine.py:409]   File "/data/vllm-ascend/vllm_ascend/ops/rotary_embedding.py", line 45, in rope_forward_oot
ERROR 03-02 22:42:58 [engine.py:409]     torch_npu._npu_rotary_embedding(
ERROR 03-02 22:42:58 [engine.py:409] AttributeError: module 'torch_npu' has no attribute '_npu_rotary_embedding'

