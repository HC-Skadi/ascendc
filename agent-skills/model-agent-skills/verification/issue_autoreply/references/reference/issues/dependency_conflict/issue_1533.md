# Issue #1533: [Bug]: qwen3-1.7B using aclgraph report due to version `GLIBC_2.32' not found

## 基本信息

- **编号**: #1533
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1533
- **创建时间**: 2025-06-30T11:37:18Z
- **关闭时间**: 2025-07-08T10:46:04Z
- **更新时间**: 2025-07-15T09:15:09Z
- **提交者**: @wuxi1117
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
vllm 0.9.1
vllm-ascend 0.9.1rc1
CANN version=8.1.T18
```

</details>


### 🐛 Describe the bug

```python
# demo
from vllm import LLM, SamplingParams

import os
os.environ["VLLM_USE_V1"] = "1"

prompts = [
    "Hello, my name is",
]

# Create a sampling params object.
# sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# Create an LLM.
llm = LLM(model="Qwen3/Qwen3-1.7B")


# Generate texts from the prompts.
outputs = llm.generate(prompts)
```

```error 
(torch2_2) [ma-user wwwx]$python3 llm_test.py
INFO 06-30 19:21:33 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-30 19:21:33 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-30 19:21:36 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-30 19:21:36 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-30 19:21:36 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-30 19:21:36 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-30 19:21:40 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
WARNING 06-30 19:21:46 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-30 19:21:46 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-30 19:21:46 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-30 19:21:46 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-30 19:21:46 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-30 19:21:46 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-30 19:22:08 [config.py:823] This model supports multiple tasks: {'score', 'embed', 'classify', 'generate', 'reward'}. Defaulting to 'generate'.
WARNING 06-30 19:22:08 [arg_utils.py:1647] Detected VLLM_USE_V1=1 with npu. Usage should be considered experimental. Please report any issues on Github.
INFO 06-30 19:22:08 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-30 19:22:08 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=8192.
INFO 06-30 19:22:08 [platform.py:177] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 06-30 19:22:08 [utils.py:297] Calculated maximum supported batch sizes for ACL graph: 66
INFO 06-30 19:22:08 [utils.py:312] Adjusted ACL graph batch sizes for Qwen3ForCausalLM model (layers: 28): 67 → 66 sizes
INFO 06-30 19:22:09 [core.py:455] Waiting for init message from front-end.
INFO 06-30 19:22:09 [platform.py:177] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 06-30 19:22:09 [utils.py:297] Calculated maximum supported batch sizes for ACL graph: 66
INFO 06-30 19:22:09 [utils.py:323] No adjustment needed for ACL graph batch sizes: Qwen3ForCausalLM model (layers: 28) with 66 sizes
INFO 06-30 19:22:09 [core.py:70] Initializing a V1 LLM engine (v0.9.1) with config: model='Qwen3/Qwen3-1.7B', speculative_config=None, tokenizer='Qwen3/Qwen3-1.7B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen3/Qwen3-1.7B, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.unified_ascend_attention_with_output","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":512,"local_cache_dir":null}
WARNING 06-30 19:22:09 [utils.py:579] The environment variable HOST_IP is deprecated and ignored, as it is often used by Docker and other software to interact with the container's network stack. Please use VLLM_HOST_IP instead to set the IP address for vLLM processes to communicate with each other.
WARNING 06-30 19:22:09 [camem.py:63] Failed to import vllm_ascend_C:/usr/lib64/libc.so.6: version `GLIBC_2.32' not found (required by /home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/vllm_ascend_C.cpython-310-aarch64-linux-gnu.so). Sleep mode will be disabled. 
WARNING 06-30 19:22:09 [utils.py:2737] Methods determine_num_available_blocks,device_config,get_cache_block_size_bytes not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xfffcfc516740>
INFO 06-30 19:22:09 [worker_v1.py:284] Profiling enabled. Traces will be saved to: ./trace
INFO 06-30 19:22:18 [parallel_state.py:1065] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 06-30 19:22:20 [model_runner_v1.py:1829] Starting to load model Qwen3/Qwen3-1.7B...
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:02<00:02,  2.15s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:02<00:00,  1.08s/it]

INFO 06-30 19:22:23 [default_loader.py:272] Loading weights took 2.51 seconds
INFO 06-30 19:22:24 [model_runner_v1.py:1848] Loading model weights took 3.2153 GB
INFO 06-30 19:22:32 [backends.py:462] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9ed77760b6/rank_0_0 for vLLM's torch.compile
INFO 06-30 19:22:32 [backends.py:472] Dynamo bytecode transform time: 7.77 s
INFO 06-30 19:22:35 [backends.py:173] Compiling a graph for general shape takes 1.95 s
INFO 06-30 19:22:45 [monitor.py:34] torch.compile takes 9.72 s in total
INFO 06-30 19:22:46 [kv_cache_utils.py:715] GPU KV cache size: 472,320 tokens
INFO 06-30 19:22:46 [kv_cache_utils.py:719] Maximum concurrency for 40,960 tokens per request: 11.53x
ERROR 06-30 19:22:47 [core.py:515] EngineCore failed to start.
ERROR 06-30 19:22:47 [core.py:515] Traceback (most recent call last):
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 506, in run_engine_core
ERROR 06-30 19:22:47 [core.py:515]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 390, in __init__
ERROR 06-30 19:22:47 [core.py:515]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 83, in __init__
ERROR 06-30 19:22:47 [core.py:515]     self._initialize_kv_caches(vllm_config)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 168, in _initialize_kv_caches
ERROR 06-30 19:22:47 [core.py:515]     self.model_executor.initialize_from_config(kv_cache_configs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/executor/abstract.py", line 66, in initialize_from_config
ERROR 06-30 19:22:47 [core.py:515]     self.collective_rpc("compile_or_warm_up_model")
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 06-30 19:22:47 [core.py:515]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 2671, in run_method
ERROR 06-30 19:22:47 [core.py:515]     return func(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/worker/worker_v1.py", line 205, in compile_or_warm_up_model
ERROR 06-30 19:22:47 [core.py:515]     self.model_runner.capture_model()
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2072, in capture_model
ERROR 06-30 19:22:47 [core.py:515]     self._dummy_run(num_tokens)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-30 19:22:47 [core.py:515]     return func(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1774, in _dummy_run
ERROR 06-30 19:22:47 [core.py:515]     hidden_states = model(
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-30 19:22:47 [core.py:515]     return self._call_impl(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-30 19:22:47 [core.py:515]     return forward_call(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/model_executor/models/qwen3.py", line 301, in forward
ERROR 06-30 19:22:47 [core.py:515]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 246, in __call__
ERROR 06-30 19:22:47 [core.py:515]     model_output = self.forward(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 336, in forward
ERROR 06-30 19:22:47 [core.py:515]     def forward(
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-30 19:22:47 [core.py:515]     return self._call_impl(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-30 19:22:47 [core.py:515]     return forward_call(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
ERROR 06-30 19:22:47 [core.py:515]     return fn(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
ERROR 06-30 19:22:47 [core.py:515]     return self._wrapped_call(self, *args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/fx/graph_module.py", line 361, in __call__
ERROR 06-30 19:22:47 [core.py:515]     raise e
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/fx/graph_module.py", line 348, in __call__
ERROR 06-30 19:22:47 [core.py:515]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-30 19:22:47 [core.py:515]     return self._call_impl(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-30 19:22:47 [core.py:515]     return forward_call(*args, **kwargs)
ERROR 06-30 19:22:47 [core.py:515]   File "<eval_with_key>.58", line 234, in forward
ERROR 06-30 19:22:47 [core.py:515]     submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = None
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/compilation/piecewise_backend.py", line 205, in __call__
ERROR 06-30 19:22:47 [core.py:515]     entry.output = weak_ref_tensors(output)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 1925, in weak_ref_tensors
ERROR 06-30 19:22:47 [core.py:515]     return tuple(weak_ref_tensor(t) for t in tensors)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 1925, in <genexpr>
ERROR 06-30 19:22:47 [core.py:515]     return tuple(weak_ref_tensor(t) for t in tensors)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 1908, in weak_ref_tensor
ERROR 06-30 19:22:47 [core.py:515]     return torch.ops._C.weak_ref_tensor(tensor)
ERROR 06-30 19:22:47 [core.py:515]   File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/_ops.py", line 1225, in __getattr__
ERROR 06-30 19:22:47 [core.py:515]     raise AttributeError(
ERROR 06-30 19:22:47 [core.py:515] AttributeError: '_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'
Process EngineCore_0:
Traceback (most recent call last):
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 519, in run_engine_core
    raise e
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 506, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 390, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 83, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 168, in _initialize_kv_caches
    self.model_executor.initialize_from_config(kv_cache_configs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/executor/abstract.py", line 66, in initialize_from_config
    self.collective_rpc("compile_or_warm_up_model")
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 2671, in run_method
    return func(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/worker/worker_v1.py", line 205, in compile_or_warm_up_model
    self.model_runner.capture_model()
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2072, in capture_model
    self._dummy_run(num_tokens)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1774, in _dummy_run
    hidden_states = model(
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/model_executor/models/qwen3.py", line 301, in forward
    hidden_states = self.model(input_ids, positions, intermediate_tensors,
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 246, in __call__
    model_output = self.forward(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 336, in forward
    def forward(
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
    return fn(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
    return self._wrapped_call(self, *args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/fx/graph_module.py", line 361, in __call__
    raise e
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/fx/graph_module.py", line 348, in __call__
    return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "<eval_with_key>.58", line 234, in forward
    submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_k_norm_parameters_weight_ = None
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm_ascend/compilation/piecewise_backend.py", line 205, in __call__
    entry.output = weak_ref_tensors(output)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 1925, in weak_ref_tensors
    return tuple(weak_ref_tensor(t) for t in tensors)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 1925, in <genexpr>
    return tuple(weak_ref_tensor(t) for t in tensors)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/utils.py", line 1908, in weak_ref_tensor
    return torch.ops._C.weak_ref_tensor(tensor)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/torch/_ops.py", line 1225, in __getattr__
    raise AttributeError(
AttributeError: '_OpNamespace' '_C' object has no attribute 'weak_ref_tensor'
Traceback (most recent call last):
  File "/home/ma-user/work/wwwx/llm_test.py", line 17, in <module>
    llm = LLM(model="Qwen3/Qwen3-1.7B")
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 243, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 501, in from_engine_args
    return engine_cls.from_vllm_config(
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/llm_engine.py", line 124, in from_vllm_config
    return cls(vllm_config=vllm_config,
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/llm_engine.py", line 101, in __init__
    self.engine_core = EngineCoreClient.make_client(
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 75, in make_client
    return SyncMPClient(vllm_config, executor_class, log_stats)
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 558, in __init__
    super().__init__(
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 422, in __init__
    self._init_engines_direct(vllm_config, local_only,
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 491, in _init_engines_direct
    self._wait_for_engine_startup(handshake_socket, input_address,
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/engine/core_client.py", line 511, in _wait_for_engine_startup
    wait_for_engine_startup(
  File "/home/ma-user/anaconda3/envs/torch2_2/lib/python3.10/site-packages/vllm/v1/utils.py", line 494, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[ERROR] 2025-06-30-19:22:48 (PID:1154078, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

```
