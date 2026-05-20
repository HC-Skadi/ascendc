# Issue #670: [Bug]: RuntimeError: call aclnnMatmul failed. The k-axis of the two inputs are different.

## 基本信息

- **编号**: #670
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/670
- **创建时间**: 2025-04-27T02:27:35Z
- **关闭时间**: 2025-05-08T03:33:31Z
- **更新时间**: 2025-05-08T03:33:31Z
- **提交者**: @shen-shanshan
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

Run offline/online inference on latest vllm and vllm-ascend with Qwen2.5, then get this error:

```bash
ERROR 04-27 02:22:35 [core.py:396] EngineCore failed to start.
ERROR 04-27 02:22:35 [core.py:396] Traceback (most recent call last):
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/v1/engine/core.py", line 387, in run_engine_core
ERROR 04-27 02:22:35 [core.py:396]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/v1/engine/core.py", line 329, in __init__
ERROR 04-27 02:22:35 [core.py:396]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/v1/engine/core.py", line 71, in __init__
ERROR 04-27 02:22:35 [core.py:396]     self._initialize_kv_caches(vllm_config)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/v1/engine/core.py", line 129, in _initialize_kv_caches
ERROR 04-27 02:22:35 [core.py:396]     available_gpu_memory = self.model_executor.determine_available_memory()
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/v1/executor/abstract.py", line 75, in determine_available_memory
ERROR 04-27 02:22:35 [core.py:396]     output = self.collective_rpc("determine_available_memory")
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 04-27 02:22:35 [core.py:396]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/utils.py", line 2456, in run_method
ERROR 04-27 02:22:35 [core.py:396]     return func(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 149, in determine_available_memory
ERROR 04-27 02:22:35 [core.py:396]     self.model_runner.profile_run()
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 864, in profile_run
ERROR 04-27 02:22:35 [core.py:396]     hidden_states = self._dummy_run(self.max_num_tokens)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 04-27 02:22:35 [core.py:396]     return func(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 830, in _dummy_run
ERROR 04-27 02:22:35 [core.py:396]     hidden_states = model(input_ids=input_ids,
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-27 02:22:35 [core.py:396]     return self._call_impl(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-27 02:22:35 [core.py:396]     return forward_call(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/model_executor/models/qwen2.py", line 466, in forward
ERROR 04-27 02:22:35 [core.py:396]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/compilation/decorators.py", line 172, in __call__
ERROR 04-27 02:22:35 [core.py:396]     return self.forward(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/model_executor/models/qwen2.py", line 343, in forward
ERROR 04-27 02:22:35 [core.py:396]     hidden_states, residual = layer(
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-27 02:22:35 [core.py:396]     return self._call_impl(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-27 02:22:35 [core.py:396]     return forward_call(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/model_executor/models/qwen2.py", line 242, in forward
ERROR 04-27 02:22:35 [core.py:396]     hidden_states = self.self_attn(
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-27 02:22:35 [core.py:396]     return self._call_impl(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-27 02:22:35 [core.py:396]     return forward_call(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/model_executor/models/qwen2.py", line 177, in forward
ERROR 04-27 02:22:35 [core.py:396]     output, _ = self.o_proj(attn_output)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-27 02:22:35 [core.py:396]     return self._call_impl(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/software/miniconda3/envs/vllm-v1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-27 02:22:35 [core.py:396]     return forward_call(*args, **kwargs)
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/model_executor/layers/linear.py", line 1274, in forward
ERROR 04-27 02:22:35 [core.py:396]     output_parallel = self.quant_method.apply(self,
ERROR 04-27 02:22:35 [core.py:396]   File "/home/sss/github/vllm-project/vllm/vllm/model_executor/layers/linear.py", line 202, in apply
ERROR 04-27 02:22:35 [core.py:396]     return dispatch_unquantized_gemm()(x, layer.weight, bias)
ERROR 04-27 02:22:35 [core.py:396] RuntimeError: call aclnnMatmul failed, detail:EZ1001: [PID: 50116] 2025-04-27-02:22:35.294.465 The k-axis of the two inputs are different [229376,128], [3584,3584]
ERROR 04-27 02:22:35 [core.py:396] 
ERROR 04-27 02:22:35 [core.py:396] [ERROR] 2025-04-27-02:22:35 (PID:50116, Device:0, RankID:-1) ERR01100 OPS call acl api failed
```
