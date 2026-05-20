# Issue #1401: [Installation]: Failed to find function aclmdlRICaptureBegin

## 基本信息

- **编号**: #1401
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1401
- **创建时间**: 2025-06-24T11:42:52Z
- **关闭时间**: 2025-07-17T06:29:41Z
- **更新时间**: 2025-07-17T06:29:41Z
- **提交者**: @glowwormX
- **评论数**: 7

## 标签

installation

## 问题描述

### Your current environment

```text
npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 89.6        48                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          2859 / 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 86.4        46                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2848 / 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 87.8        44                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          2847 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 93.2        49                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2847 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+


cat /home/xxx/cann81/Ascend/ascend-toolkit/latest/aarch64-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21B087
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/home/xxx/cann81/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux


Name: torch-npu
Version: 2.5.1.post1.dev20250619
Name: vllm-ascend
Version: 0.9.1rc1
```


### How you are installing vllm and vllm-ascend

```sh
pip install vllm==0.9.1
pip install vllm-ascend==0.9.1rc1
pip install torch_npu==2.5.1.post1.dev20250619
```

我在conda中安装的环境，启动脚本：
```sh
source /home/xxx/cann81/Ascend/ascend-toolkit/set_env.sh
source /home/xxx/cann81/nnal/nnal/atb/set_env.sh
pip show torch_npu
pip show vllm-ascend
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
export VLLM_USE_V1=1
python3 -m vllm.entrypoints.openai.api_server --model "Qwen2_5/Qwen2.5-7B/" \
    --trust-remote-code \
    --max-model-len=16384 --gpu-memory-utilization=0.9 \
    --tensor-parallel-size=1
```


日志：
```
Name: torch-npu
Version: 2.5.1.post1.dev20250619
Summary: NPU bridge for PyTorch
Home-page: https://gitee.com/ascend/pytorch
Author: 
Author-email: 
License: BSD License
Location: /cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages
Requires: torch
Required-by: vllm-ascend
Name: vllm-ascend
Version: 0.9.1rc1
Summary: vLLM Ascend backend plugin
Home-page: https://github.com/vllm-project/vllm-ascend
Author: vLLM-Ascend team
Author-email: 
License: Apache 2.0
Location: /cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages
Requires: cmake, decorator, einops, msgpack, numba, numpy, packaging, pip, pybind11, pyyaml, quart, scipy, setuptools, setuptools-scm, torch, torch-npu, torchvision, wheel
Required-by: 
INFO 06-24 19:41:27 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-24 19:41:27 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-24 19:41:28 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-24 19:41:28 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-24 19:41:28 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-24 19:41:28 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-24 19:41:32 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/transformers_utils/tokenizer_group.py
/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch_npu/__init__.py
INFO 06-24 19:41:51 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-24 19:41:51 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-24 19:41:53 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-24 19:41:53 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-24 19:41:53 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-24 19:41:53 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-24 19:41:56 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
WARNING 06-24 19:42:00 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-24 19:42:00 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-24 19:42:00 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-24 19:42:00 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-24 19:42:00 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-24 19:42:00 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-24 19:42:02 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-24 19:42:02 [api_server.py:1287] vLLM API server version 0.9.1
INFO 06-24 19:42:04 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-24 19:42:04 [cli_args.py:309] non-default args: {'model': 'Qwen2_5/Qwen2.5-7B/', 'trust_remote_code': True, 'max_model_len': 16384}
INFO 06-24 19:42:23 [config.py:823] This model supports multiple tasks: {'classify', 'generate', 'embed', 'reward', 'score'}. Defaulting to 'generate'.
WARNING 06-24 19:42:23 [arg_utils.py:1647] Detected VLLM_USE_V1=1 with npu. Usage should be considered experimental. Please report any issues on Github.
INFO 06-24 19:42:23 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-24 19:42:23 [config.py:2195] Chunked prefill is enabled with max_num_batched_tokens=2048.
INFO 06-24 19:42:23 [platform.py:177] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 06-24 19:42:23 [utils.py:297] Calculated maximum supported batch sizes for ACL graph: 66
INFO 06-24 19:42:23 [utils.py:312] Adjusted ACL graph batch sizes for Qwen2ForCausalLM model (layers: 28): 67 → 66 sizes
WARNING 06-24 19:42:29 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 06-24 19:42:30 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-24 19:42:30 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-24 19:42:31 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-24 19:42:31 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-24 19:42:31 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-24 19:42:31 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-24 19:42:35 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
INFO 06-24 19:42:37 [core.py:455] Waiting for init message from front-end.
INFO 06-24 19:42:37 [platform.py:177] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 06-24 19:42:37 [utils.py:297] Calculated maximum supported batch sizes for ACL graph: 66
INFO 06-24 19:42:37 [utils.py:323] No adjustment needed for ACL graph batch sizes: Qwen2ForCausalLM model (layers: 28) with 66 sizes
WARNING 06-24 19:42:39 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-24 19:42:39 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-24 19:42:39 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-24 19:42:39 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-24 19:42:39 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-24 19:42:39 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-24 19:42:39 [core.py:70] Initializing a V1 LLM engine (v0.9.1) with config: model='Qwen2_5/Qwen2.5-7B/', speculative_config=None, tokenizer='Qwen2_5/Qwen2.5-7B/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen2_5/Qwen2.5-7B/, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.unified_ascend_attention_with_output","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":512,"local_cache_dir":null}
WARNING 06-24 19:42:39 [utils.py:579] The environment variable HOST_IP is deprecated and ignored, as it is often used by Docker and other software to interact with the container's network stack. Please use VLLM_HOST_IP instead to set the IP address for vLLM processes to communicate with each other.
WARNING 06-24 19:42:40 [utils.py:2737] Methods determine_num_available_blocks,device_config,get_cache_block_size_bytes not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xfffd8b7c6d70>
WARNING 06-24 19:42:53 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 06-24 19:42:55 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-24 19:42:55 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-24 19:42:56 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-24 19:42:56 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-24 19:42:56 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-24 19:42:56 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-24 19:43:00 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
INFO 06-24 19:43:05 [parallel_state.py:1065] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 06-24 19:43:05 [model_runner_v1.py:1829] Starting to load model Qwen2_5/Qwen2.5-7B/...
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:03<00:10,  3.51s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:07<00:07,  3.64s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:10<00:03,  3.49s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:14<00:00,  3.54s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:14<00:00,  3.55s/it]

INFO 06-24 19:43:20 [default_loader.py:272] Loading weights took 14.54 seconds
INFO 06-24 19:43:23 [model_runner_v1.py:1848] Loading model weights took 14.2713 GB
INFO 06-24 19:43:30 [backends.py:462] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/11252448fd/rank_0_0 for vLLM's torch.compile
INFO 06-24 19:43:30 [backends.py:472] Dynamo bytecode transform time: 6.29 s
INFO 06-24 19:43:32 [backends.py:173] Compiling a graph for general shape takes 1.74 s
INFO 06-24 19:43:55 [monitor.py:34] torch.compile takes 8.03 s in total
INFO 06-24 19:43:56 [kv_cache_utils.py:715] GPU KV cache size: 209,792 tokens
INFO 06-24 19:43:56 [kv_cache_utils.py:719] Maximum concurrency for 16,384 tokens per request: 12.80x
ERROR 06-24 19:43:57 [core.py:515] EngineCore failed to start.
ERROR 06-24 19:43:57 [core.py:515] Traceback (most recent call last):
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 506, in run_engine_core
ERROR 06-24 19:43:57 [core.py:515]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 390, in __init__
ERROR 06-24 19:43:57 [core.py:515]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 83, in __init__
ERROR 06-24 19:43:57 [core.py:515]     self._initialize_kv_caches(vllm_config)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 168, in _initialize_kv_caches
ERROR 06-24 19:43:57 [core.py:515]     self.model_executor.initialize_from_config(kv_cache_configs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/v1/executor/abstract.py", line 66, in initialize_from_config
ERROR 06-24 19:43:57 [core.py:515]     self.collective_rpc("compile_or_warm_up_model")
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 06-24 19:43:57 [core.py:515]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/utils.py", line 2671, in run_method
ERROR 06-24 19:43:57 [core.py:515]     return func(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm_ascend/worker/worker_v1.py", line 205, in compile_or_warm_up_model
ERROR 06-24 19:43:57 [core.py:515]     self.model_runner.capture_model()
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2072, in capture_model
ERROR 06-24 19:43:57 [core.py:515]     self._dummy_run(num_tokens)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-24 19:43:57 [core.py:515]     return func(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 1774, in _dummy_run
ERROR 06-24 19:43:57 [core.py:515]     hidden_states = model(
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-24 19:43:57 [core.py:515]     return self._call_impl(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-24 19:43:57 [core.py:515]     return forward_call(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 477, in forward
ERROR 06-24 19:43:57 [core.py:515]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 246, in __call__
ERROR 06-24 19:43:57 [core.py:515]     model_output = self.forward(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 336, in forward
ERROR 06-24 19:43:57 [core.py:515]     def forward(
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-24 19:43:57 [core.py:515]     return self._call_impl(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-24 19:43:57 [core.py:515]     return forward_call(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn
ERROR 06-24 19:43:57 [core.py:515]     return fn(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped
ERROR 06-24 19:43:57 [core.py:515]     return self._wrapped_call(self, *args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/fx/graph_module.py", line 361, in __call__
ERROR 06-24 19:43:57 [core.py:515]     raise e
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/fx/graph_module.py", line 348, in __call__
ERROR 06-24 19:43:57 [core.py:515]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-24 19:43:57 [core.py:515]     return self._call_impl(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-24 19:43:57 [core.py:515]     return forward_call(*args, **kwargs)
ERROR 06-24 19:43:57 [core.py:515]   File "<eval_with_key>.58", line 206, in forward
ERROR 06-24 19:43:57 [core.py:515]     submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_bias_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_bias_ = None
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9_pool):
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch_npu/npu/graphs.py", line 310, in __enter__
ERROR 06-24 19:43:57 [core.py:515]     self.npu_graph.capture_begin(
ERROR 06-24 19:43:57 [core.py:515]   File "/cache/miniconda3_envs/cache_mini_vllm_0.9.1/lib/python3.10/site-packages/torch_npu/npu/graphs.py", line 210, in capture_begin
ERROR 06-24 19:43:57 [core.py:515]     super().capture_begin(pool=pool, capture_error_mode=capture_error_mode)
ERROR 06-24 19:43:57 [core.py:515] RuntimeError: Failed to find function aclmdlRIC.1/lib/python3.10/site-packages/vllm_ascend/compilation/piecewise_backend.py", line 192, in __call__
ERROR 06-24 19:43:57 [core.py:515]     with torch.npu.graph(aclgraph, pool=self.graphaptureBegin
ERROR 06-24 19:43:57 [core.py:515] [ERROR] 2025-06-24-19:43:57 (PID:589552, Device:0, RankID:-1) ERR00008 PTA resource not found
```
