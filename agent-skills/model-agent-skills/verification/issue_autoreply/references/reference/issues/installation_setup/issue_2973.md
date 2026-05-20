# Issue #2973: [Doc]: example offline_external_launcher.py running failed at parallel initialized stage

## 基本信息

- **编号**: #2973
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2973
- **创建时间**: 2025-09-17T03:54:38Z
- **关闭时间**: 2025-09-30T08:12:07Z
- **更新时间**: 2025-09-30T08:12:07Z
- **提交者**: @leo-pony
- **评论数**: 1

## 标签

documentation

## 问题描述

### 📚 The doc issue

vllm-ascend: v0.10.2.rc1
script:
```
             python examples/offline_external_launcher.py \
                --model="Qwen/Qwen3-30B-A3B" \
                --tp-size=4 \
                --proc-per-node=2 \
                --enable-expert-parallel
```

Error information:
```
INFO 09-17 03:45:12 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-17 03:45:12 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-17 03:45:12 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-17 03:45:12 [__init__.py:207] Platform plugin ascend is activated
WARNING 09-17 03:45:16 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 09-17 03:45:16 [registry.py:483] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:Qwen3NextForCausalLM.
WARNING 09-17 03:45:16 [registry.py:483] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:Qwen3NextForCausalLM.
INFO 09-17 03:45:16 [utils.py:328] non-default args: {'seed': 0, 'distributed_executor_backend': 'external_launcher', 'tensor_parallel_size': 4, 'enable_expert_parallel': True, 'disable_log_stats': True, 'model': 'Qwen/Qwen3-30B-A3B'}
INFO 09-17 03:45:16 [utils.py:328] non-default args: {'seed': 0, 'distributed_executor_backend': 'external_launcher', 'tensor_parallel_size': 4, 'enable_expert_parallel': True, 'disable_log_stats': True, 'model': 'Qwen/Qwen3-30B-A3B'}
INFO 09-17 03:45:16 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 09-17 03:45:16 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
INFO 09-17 03:45:35 [__init__.py:742] Resolved architecture: Qwen3MoeForCausalLM
`torch_dtype` is deprecated! Use `dtype` instead!
INFO 09-17 03:45:35 [__init__.py:1815] Using max model len 40960
INFO 09-17 03:45:36 [parallel.py:348] Disabling V1 multiprocessing for external launcher.
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
INFO 09-17 03:45:37 [__init__.py:742] Resolved architecture: Qwen3MoeForCausalLM
`torch_dtype` is deprecated! Use `dtype` instead!
INFO 09-17 03:45:37 [__init__.py:1815] Using max model len 40960
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
INFO 09-17 03:45:38 [parallel.py:348] Disabling V1 multiprocessing for external launcher.
INFO 09-17 03:45:38 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192.
INFO 09-17 03:45:38 [platform.py:137] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
INFO 09-17 03:45:38 [platform.py:223] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 09-17 03:45:38 [utils.py:350] Calculated maximum supported batch sizes for ACL graph: 11
WARNING 09-17 03:45:38 [utils.py:353] Currently, communication is performed using FFTS+ method, which reduces the number of available streams and, as a result, limits the range of runtime shapes that can be handled. To both improve communication performance and increase the number of supported shapes, set HCCL_OP_EXPANSION_MODE=AIV.
INFO 09-17 03:45:38 [utils.py:372] Adjusted ACL graph batch sizes for Qwen3MoeForCausalLM model (layers: 48): 67 → 11 sizes
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
INFO 09-17 03:45:40 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192.
INFO 09-17 03:45:40 [platform.py:137] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
INFO 09-17 03:45:40 [platform.py:223] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 09-17 03:45:40 [utils.py:350] Calculated maximum supported batch sizes for ACL graph: 11
WARNING 09-17 03:45:40 [utils.py:353] Currently, communication is performed using FFTS+ method, which reduces the number of available streams and, as a result, limits the range of runtime shapes that can be handled. To both improve communication performance and increase the number of supported shapes, set HCCL_OP_EXPANSION_MODE=AIV.
INFO 09-17 03:45:40 [utils.py:372] Adjusted ACL graph batch sizes for Qwen3MoeForCausalLM model (layers: 48): 67 → 11 sizes
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
INFO 09-17 03:45:43 [core.py:76] Initializing a V1 LLM engine (v0.10.2) with config: model='Qwen/Qwen3-30B-A3B', speculative_config=None, tokenizer='Qwen/Qwen3-30B-A3B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-30B-A3B, enable_prefix_caching=True, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,456,408,352,304,248,192,144,88,40,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
Downloading Model from https://www.modelscope.cn to directory: /shared/cache/modelscope/models/Qwen/Qwen3-30B-A3B
INFO 09-17 03:45:44 [core.py:76] Initializing a V1 LLM engine (v0.10.2) with config: model='Qwen/Qwen3-30B-A3B', speculative_config=None, tokenizer='Qwen/Qwen3-30B-A3B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-30B-A3B, enable_prefix_caching=True, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,456,408,352,304,248,192,144,88,40,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
Process Process-1:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm-workspace/vllm-ascend/examples/offline_external_launcher.py", line 178, in main
    llm = LLM(
          ^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/llm.py", line 282, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 493, in from_engine_args
    return engine_cls.from_vllm_config(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/llm_engine.py", line 134, in from_vllm_config
    return cls(vllm_config=vllm_config,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/llm_engine.py", line 111, in __init__
    self.engine_core = EngineCoreClient.make_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 82, in make_client
    return InprocClient(vllm_config, executor_class, log_stats)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 245, in __init__
    self.engine_core = EngineCore(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 82, in __init__
    self.model_executor = executor_class(vllm_config)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
    self._init_executor()
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 132, in _init_executor
    self.collective_rpc("init_device")
  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3060, in run_method
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 611, in init_device
    self.worker.init_device()  # type: ignore
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 157, in init_device
    device = self._init_device()
             ^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 151, in _init_device
    self._init_worker_distributed_environment()
  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 323, in _init_worker_distributed_environment
    ensure_model_parallel_initialized(
  File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 1185, in ensure_model_parallel_initialized
    initialize_model_parallel(tensor_model_parallel_size,
  File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 1098, in initialize_model_parallel
    all_ranks = torch.arange(world_size).reshape(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: shape '[-1, 1, 1, 4]' is invalid for input of size 2
```

### Suggest a potential alternative/fix

_No response_
