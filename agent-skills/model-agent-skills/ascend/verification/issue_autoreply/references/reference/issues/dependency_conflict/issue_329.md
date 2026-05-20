# Issue #329: [Bug]: ModuleNotFoundError: No module named 'triton'

## 基本信息

- **编号**: #329
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/329
- **创建时间**: 2025-03-14T01:52:04Z
- **关闭时间**: 2025-05-14T02:08:44Z
- **更新时间**: 2025-06-25T09:10:35Z
- **提交者**: @ZRJ026
- **评论数**: 12

## 标签

bug

## 问题描述

### Your current environment

8*910B3


### 🐛 Describe the bug

docker image: quay.io/ascend/vllm-ascend@sha256:fba4e91ac8122d3feb864a87d2ac69a26550a2ca00c74d992dda9c146fd2291e
command: python -m vllm.entrypoints.openai.api_server         --model="/data/DeepSeek-R1-origin"        --trust-remote-code        --enforce-eager               --distributed_executor_backend "ray"        --tensor-parallel-size 16        --disable-log-requests        --disable-log-stats        --disable-frontend-multiprocessing        --port 8000

> INFO 03-14 01:49:23 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-14 01:49:23 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-14 01:49:23 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-14 01:49:23 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-14 01:49:23 [__init__.py:44] plugin ascend loaded.
INFO 03-14 01:49:23 [__init__.py:247] Platform plugin ascend is activated
INFO 03-14 01:49:26 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 03-14 01:49:26 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 03-14 01:49:26 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 03-14 01:49:26 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-14 01:49:26 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 03-14 01:49:26 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-14 01:49:27 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 03-14 01:49:27 [registry.py:362] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
INFO 03-14 01:49:27 [api_server.py:912] vLLM API server version 0.1.dev1+ge22ee1e
INFO 03-14 01:49:27 [api_server.py:913] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, enable_ssl_refresh=False, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=True, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/DeepSeek-R1-origin', task='auto', tokenizer=None, hf_config_path=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend='ray', pipeline_parallel_size=1, tensor_parallel_size=16, enable_expert_parallel=False, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=None, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=True, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=True, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, use_tqdm_on_load=True, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', worker_extension_cls='', generation_config='auto', override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, enable_reasoning=False, reasoning_parser=None, disable_log_requests=True, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False)
INFO 03-14 01:49:27 [config.py:208] Replacing legacy 'type' key with 'rope_type'
INFO 03-14 01:49:38 [config.py:576] This model supports multiple tasks: {'classify', 'embed', 'score', 'reward', 'generate'}. Defaulting to 'generate'.
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/python3.10/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 992, in <module>
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 163, in build_async_engine_client_from_engine_args
    engine_client = AsyncLLMEngine.from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 644, in from_engine_args
    engine_config = engine_args.create_engine_config(usage_context)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1204, in create_engine_config
    model_config = self.create_model_config()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1130, in create_model_config
    return ModelConfig(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/config.py", line 418, in __init__
    self._verify_quantization()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/config.py", line 629, in _verify_quantization
    method = get_quantization_config(name)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/__init__.py", line 93, in get_quantization_config
    from .gguf import GGUFConfig
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/gguf.py", line 13, in <module>
    from vllm.model_executor.layers.fused_moe.fused_moe import moe_align_block_size
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/fused_moe.py", line 9, in <module>
    import triton
ModuleNotFoundError: No module named 'triton'
[ERROR] 2025-03-14-01:49:38 (PID:2143, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

