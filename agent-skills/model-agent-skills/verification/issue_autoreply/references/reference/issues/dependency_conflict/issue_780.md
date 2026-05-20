# Issue #780: [Bug]:

## 基本信息

- **编号**: #780
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/780
- **创建时间**: 2025-05-07T08:57:59Z
- **关闭时间**: 2025-05-14T06:41:29Z
- **更新时间**: 2025-05-14T06:41:29Z
- **提交者**: @caomengqing
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

```bash
(turbo_c) xxx@xxx-docker:~/code/vllm-ascend$ VLLM_USE_V1=1 python examples/offline_inference_npu.py 
INFO 05-07 05:58:29 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-07 05:58:29 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-07 05:58:29 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-07 05:58:29 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-07 05:58:29 __init__.py:44] plugin ascend loaded.
INFO 05-07 05:58:29 __init__.py:198] Platform plugin ascend is activated
INFO 05-07 05:58:30 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-07 05:58:30 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-07 05:58:30 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-07 05:58:30 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-07 05:58:30 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-07 05:58:30 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-07 05:58:30 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-07 05:58:30 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-07 05:58:30 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 05-07 05:58:30 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 05-07 05:58:30 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-07 05:58:30 arg_utils.py:1385] Setting max_num_batched_tokens to 8192 for LLM_CLASS usage context.
INFO 05-07 05:58:30 config.py:208] Replacing legacy 'type' key with 'rope_type'
INFO 05-07 05:58:42 config.py:549] This model supports multiple tasks: {'reward', 'classify', 'score', 'embed', 'generate'}. Defaulting to 'generate'.
INFO 05-07 05:58:42 config.py:1555] Chunked prefill is enabled with max_num_batched_tokens=8192.
WARNING 05-07 05:58:42 platform.py:110] Compilation level 3 is not supported on NPU now, forcing compilation level to NO_COMPILATION
WARNING 05-07 05:58:42 platform.py:142] Prefix caching is now supported for V1 on NPU, but it is still experimental and there may be issues with accuracy.
INFO 05-07 05:58:42 config.py:3329] MLA is enabled; forcing chunked prefill and prefix caching to be disabled.
INFO 05-07 05:58:43 core.py:50] Initializing a V1 LLM engine (v0.7.3) with config: model='/home/xxx/cache/modelscope/models/deepseek-ai/DeepSeek-V2-Lite-Chat', speculative_config=None, tokenizer='/home/xxx/cache/modelscope/models/deepseek-ai/DeepSeek-V2-Lite-Chat', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=1024, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/home/xxx/cache/modelscope/models/deepseek-ai/DeepSeek-V2-Lite-Chat, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output"],"use_inductor":true,"compile_sizes":[],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":512}
WARNING 05-07 05:58:43 utils.py:2262] Methods add_lora,cache_config,determine_available_memory,determine_num_available_blocks,device_config,get_cache_block_size_bytes,list_loras,load_config,pin_lora,remove_lora,scheduler_config not implemented in <vllm_ascend.worker.worker_v1.NPUWorker object at 0xfffd1401bdf0>
WARNING 05-07 05:58:43 _custom_ops.py:21] Failed to import from vllm._C with ImportError('libnuma.so.1: cannot open shared object file: No such file or directory')
INFO 05-07 05:58:43 utils.py:31] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo.
INFO 05-07 05:58:45 model_runner_v1.py:810] Starting to load model /home/xxx/cache/modelscope/models/deepseek-ai/DeepSeek-V2-Lite-Chat...
ERROR 05-07 05:58:46 core.py:291] EngineCore hit an exception: Traceback (most recent call last):
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 283, in run_engine_core
ERROR 05-07 05:58:46 core.py:291]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 238, in __init__
ERROR 05-07 05:58:46 core.py:291]     super().__init__(vllm_config, executor_class, log_stats)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 56, in __init__
ERROR 05-07 05:58:46 core.py:291]     self.model_executor = executor_class(vllm_config)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 05-07 05:58:46 core.py:291]     self._init_executor()
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/executor/uniproc_executor.py", line 47, in _init_executor
ERROR 05-07 05:58:46 core.py:291]     self.collective_rpc("load_model")
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 05-07 05:58:46 core.py:291]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/utils.py", line 2196, in run_method
ERROR 05-07 05:58:46 core.py:291]     return func(*args, **kwargs)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 235, in load_model
ERROR 05-07 05:58:46 core.py:291]     self.model_runner.load_model()
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/miniconda3/envs/turbo_c/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading
ERROR 05-07 05:58:46 core.py:291]     func(self)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 813, in load_model
ERROR 05-07 05:58:46 core.py:291]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 05-07 05:58:46 core.py:291]     return loader.load_model(vllm_config=vllm_config)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/model_loader/loader.py", line 406, in load_model
ERROR 05-07 05:58:46 core.py:291]     model = _initialize_model(vllm_config=vllm_config)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
ERROR 05-07 05:58:46 core.py:291]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 271, in __init__
ERROR 05-07 05:58:46 core.py:291]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 199, in __init__
ERROR 05-07 05:58:46 core.py:291]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/models/utils.py", line 557, in make_layers
ERROR 05-07 05:58:46 core.py:291]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/models/utils.py", line 558, in <listcomp>
ERROR 05-07 05:58:46 core.py:291]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 201, in <lambda>
ERROR 05-07 05:58:46 core.py:291]     lambda prefix: CustomDeepseekV2DecoderLayer(
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 135, in __init__
ERROR 05-07 05:58:46 core.py:291]     self.self_attn = attn_cls(
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/models/deepseek_v2.py", line 417, in __init__
ERROR 05-07 05:58:46 core.py:291]     self.rotary_emb = get_rope(qk_rope_head_dim,
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/layers/rotary_embedding.py", line 1099, in get_rope
ERROR 05-07 05:58:46 core.py:291]     rotary_emb = DeepseekScalingRotaryEmbedding(
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/layers/rotary_embedding.py", line 649, in __init__
ERROR 05-07 05:58:46 core.py:291]     super().__init__(head_size, rotary_dim, max_position_embeddings, base,
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/layers/rotary_embedding.py", line 98, in __init__
ERROR 05-07 05:58:46 core.py:291]     cache = self._compute_cos_sin_cache()
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/layers/rotary_embedding.py", line 671, in _compute_cos_sin_cache
ERROR 05-07 05:58:46 core.py:291]     inv_freq = self._compute_inv_freq(self.scaling_factor)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/code/vllm-cpu/vllm/vllm/model_executor/layers/rotary_embedding.py", line 653, in _compute_inv_freq
ERROR 05-07 05:58:46 core.py:291]     pos_freqs = self.base**(torch.arange(
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/miniconda3/envs/turbo_c/lib/python3.10/site-packages/torch/utils/_device.py", line 106, in __torch_function__
ERROR 05-07 05:58:46 core.py:291]     return func(*args, **kwargs)
ERROR 05-07 05:58:46 core.py:291]   File "/home/xxx/miniconda3/envs/turbo_c/lib/python3.10/site-packages/torch/cuda/__init__.py", line 310, in _lazy_init
ERROR 05-07 05:58:46 core.py:291]     raise AssertionError("Torch not compiled with CUDA enabled")
ERROR 05-07 05:58:46 core.py:291] AssertionError: Torch not compiled with CUDA enabled
ERROR 05-07 05:58:46 core.py:291] 
CRITICAL 05-07 05:58:46 core_client.py:191] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.
Killed
```
