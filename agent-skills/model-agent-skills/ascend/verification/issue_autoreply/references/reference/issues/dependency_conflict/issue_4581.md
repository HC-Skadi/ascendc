# Issue #4581: [Bug]: Torchair doesn't worker with v1 scheduler

## 基本信息

- **编号**: #4581
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4581
- **创建时间**: 2025-12-01T01:30:30Z
- **关闭时间**: 2025-12-10T12:08:14Z
- **更新时间**: 2025-12-10T12:08:14Z
- **提交者**: @MengqingCao
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm v0.11.2
vllm-ascend f10acddb78d5ba24ef29e18d8663e6d9a68583f3
CANN 8.3.rc2
torch 2.7.1+cpu
torch-npu 2.7.1
```

</details>


### 🐛 Describe the bug

Test cases following all failed:

```bash
=========================== short test summary info ============================
FAILED tests/e2e/multicard/test_torchair_graph_mode.py::test_e2e_deepseekv3_with_torchair - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
FAILED tests/e2e/multicard/test_torchair_graph_mode.py::test_e2e_deepseekv3_with_torchair_ms_mla - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
FAILED tests/e2e/multicard/test_torchair_graph_mode.py::test_e2e_deepseekv3_with_torchair_v1scheduler - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
======= 3 failed, 5 passed, 1 skipped, 10 warnings in 1468.15s (0:24:28) =======
```

Error log:

```bash
tests/e2e/multicard/test_torchair_graph_mode.py::test_e2e_deepseekv3_with_torchair Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
(EngineCore_DP0 pid=11535) 2025-11-29 12:09:35,774 - 11535 - vllmProfiler - INFO - VLLM_USE_V1 not set, auto-detected via vLLM 0.11.2+empty: default 1
2025-11-29 12:09:50,418 - 11655 - vllmProfiler - INFO - VLLM_USE_V1 not set, auto-detected via vLLM 0.11.2+empty: default 1
2025-11-29 12:09:50,517 - 11654 - vllmProfiler - INFO - VLLM_USE_V1 not set, auto-detected via vLLM 0.11.2+empty: default 1
(Worker_TP0 pid=11654) Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards:   0% Completed | 0/6 [00:00<?, ?it/s]
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards:  17% Completed | 1/6 [00:03<00:16,  3.37s/it]
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards:  33% Completed | 2/6 [00:09<00:18,  4.72s/it]
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards:  50% Completed | 3/6 [00:15<00:16,  5.49s/it]
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards:  67% Completed | 4/6 [00:21<00:11,  5.81s/it]
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards:  83% Completed | 5/6 [00:28<00:06,  6.03s/it]
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards: 100% Completed | 6/6 [00:34<00:00,  6.21s/it]
(Worker_TP0 pid=11654) 
Loading safetensors checkpoint shards: 100% Completed | 6/6 [00:34<00:00,  5.79s/it]
(Worker_TP0 pid=11654) 
(Worker_TP1 pid=11655) Downloading Model from https://www.modelscope.cn/ to directory: /root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3-Pruning
[rank0]:[W1129 12:10:53.758018688 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
[rank1]:[W1129 12:10:53.888542349 compiler_depend.ts:28] Warning: The oprator of MoeInitRouting will be removed from Pytorch and switch to AscendSpeed after 630. (function operator())
(Worker_TP1 pid=11655) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP1 pid=11655)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '
(Worker_TP0 pid=11654) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP0 pid=11654)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '
(Worker_TP1 pid=11655) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP1 pid=11655)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '
(Worker_TP0 pid=11654) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP0 pid=11654)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '
(Worker_TP1 pid=11655) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP1 pid=11655)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '
(Worker_TP0 pid=11654) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP0 pid=11654)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '
(Worker_TP1 pid=11655) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP1 pid=11655)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '
(Worker_TP0 pid=11654) /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/fx2ge_converter.py:1256: UserWarning: When enable frozen_parameter, Parameters and input tensors with immutable data_ptr marked by `torch._dynamo.mark_static_address()` will be considered frozen. Please make sure that the Parameters data address remain the same throughout the program runtime.
(Worker_TP0 pid=11654)   warnings.warn('When enable frozen_parameter, Parameters and input tensors with immutable data_ptr '

Adding requests:   0%|          | 0/4 [00:00<?, ?it/s]
Adding requests: 100%|██████████| 4/4 [00:00<00:00, 559.54it/s]

Processed prompts:   0%|          | 0/4 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s][rank0]:[W1129 12:12:10.091182553 compiler_depend.ts:117] Warning: Driver Version:  is invalid or not supported yet. (function operator())
[rank1]:[W1129 12:12:10.091840808 compiler_depend.ts:117] Warning: Driver Version:  is invalid or not supported yet. (function operator())
..............(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815] WorkerProc hit an exception.
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815] Traceback (most recent call last):
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     output = func(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/worker/worker_base.py", line 367, in execute_model
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 296, in execute_model
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     output = self.model_runner.execute_model(scheduler_output,
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return func(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2333, in execute_model
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_model_runner.py", line 389, in _generate_process_reqs_hidden_states
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     hidden_states = self.model(
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]                     ^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 1344, in forward
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     hidden_states = self.model(input_ids, positions, kv_caches,
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 1189, in forward
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     hidden_states, residual = layer(
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]                               ^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 1037, in forward
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     hidden_states = self.self_attn(
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return self._call_impl(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     return forward_call(*args, **kwargs)
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/models/torchair_deepseek_v2.py", line 668, in forward
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     output = self.mla_attn.impl.forward(self.mla_attn,
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_mla.py", line 1243, in forward
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     output_decode = self._forward_decode(decode_ql_nope,
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/torchair/torchair_mla.py", line 1052, in _forward_decode
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]     k_cache = torch.cat(
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815]               ^^^^^^^^^^
(Worker_TP1 pid=11655) ERROR 11-29 12:12:24 [multiproc_executor.py:815] RuntimeError: NPU out of memory. Tried to allocate 19.09 GiB (NPU 1; 60.96 GiB total capacity; 51.49 GiB already allocated; 51.49 GiB current active; 8.37 GiB free; 51.64 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
```
