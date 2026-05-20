# Issue #5297: [Bug]: Tencent-Hunyuan/HunyuanOCR model execute failed with linear op input shape wrong

## 基本信息

- **编号**: #5297
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5297
- **创建时间**: 2025-12-23T13:01:02Z
- **关闭时间**: 2025-12-27T10:42:48Z
- **更新时间**: 2025-12-27T10:42:48Z
- **提交者**: @leo-pony
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm: 5fbfa8d9ef15948599631baeb91e8220b2ee9bcc
vllm-ascend: PR https://github.com/vllm-project/vllm-ascend/pull/5223/changes
```

</details>


### 🐛 Describe the bug

pytest -sv tests/e2e/singlecard/test_vlm.py::test_multimodal_vl[hunyuan-vl]


Error information:
```
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868] EngineCore failed to start.
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868] Traceback (most recent call last):
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 859, in run_engine_core
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 639, in __init__
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     super().__init__(
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 111, in __init__
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/engine/core.py", line 242, in _initialize_kv_caches
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/executor/uniproc_executor.py", line 75, in collective_rpc
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     result = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/serial_utils.py", line 461, in run_method
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return func(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return func(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     self.model_runner.profile_run()
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2201, in profile_run
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     super().profile_run()
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/v1/worker/gpu_model_runner.py", line 4531, in profile_run
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     dummy_encoder_outputs = self.model.embed_multimodal(
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/models/hunyuan_vision.py", line 992, in embed_multimodal
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     image_embeddings = self._process_image_input(multimodal_input)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/models/hunyuan_vision.py", line 954, in _process_image_input
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw_list)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/models/hunyuan_vision.py", line 525, in forward
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     parts = [layer(p) for p in parts]
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]             ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/models/hunyuan_vision.py", line 525, in <listcomp>
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     parts = [layer(p) for p in parts]
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]              ^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/models/hunyuan_vision.py", line 295, in forward
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     x = x + self.self_attn(self.input_layernorm(x))
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/models/hunyuan_vision.py", line 250, in forward
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     output, _ = self.o_proj(out)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                 ^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm-ascend/vllm_ascend/ops/linear.py", line 301, in forward
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return super().forward(input_)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/layers/linear.py", line 1406, in forward
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     output_parallel = self.quant_method.apply(self, input_parallel, bias_)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/layers/linear.py", line 240, in apply
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return dispatch_unquantized_gemm()(layer, x, layer.weight, bias)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]   File "/data/mnj/code/vllm/vllm/model_executor/layers/utils.py", line 106, in default_unquantized_gemm
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]     return torch.nn.functional.linear(x, weight, bias)
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868] RuntimeError: addmm:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:112 NPU function error: call aclnnAddmm failed, error code is 161002
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868] [ERROR] 2025-12-23-12:56:15 (PID:172866, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868] [PID: 172866] 2025-12-23-12:56:15.164.100 AclNN_Parameter_Error(EZ1001): The k-axis of the two inputs are different.
(EngineCore_DP0 pid=172866) ERROR 12-23 12:56:15 [core.py:868]
```
