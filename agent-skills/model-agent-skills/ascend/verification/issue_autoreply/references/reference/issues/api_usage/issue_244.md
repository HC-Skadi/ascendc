# Issue #244: [Doc]: 部署大模型返回结果乱码

## 基本信息

- **编号**: #244
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/244
- **创建时间**: 2025-03-05T09:53:38Z
- **关闭时间**: 2025-04-10T09:20:18Z
- **更新时间**: 2025-04-10T09:20:19Z
- **提交者**: @gyr-kdgc
- **评论数**: 6

## 标签

question

## 问题描述

### 📚 The doc issue

<details>日志：
INFO 03-05 17:41:32 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-05 17:41:32 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-05 17:41:32 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-05 17:41:32 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-05 17:41:32 __init__.py:42] plugin ascend loaded.
INFO 03-05 17:41:34 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-05 17:41:34 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-05 17:41:34 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-05 17:41:34 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-05 17:41:34 __init__.py:42] plugin ascend loaded.
INFO 03-05 17:41:34 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-05 17:41:34 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-05 17:41:34 __init__.py:174] Platform plugin ascend is activated
INFO 03-05 17:41:38 api_server.py:838] vLLM API server version 0.7.1
INFO 03-05 17:41:38 api_server.py:839] args: Namespace(host=None, port=11468, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/workspace/llm_models/Qwen2.5-7B-Instruct/', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=2048, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.5, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_seqs=30, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=True, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['deepseek-r1-14b'], qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False)
INFO 03-05 17:41:38 api_server.py:204] Started engine process with PID 13720
INFO 03-05 17:41:46 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-05 17:41:46 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-05 17:41:46 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-05 17:41:46 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-05 17:41:46 __init__.py:42] plugin ascend loaded.
INFO 03-05 17:41:47 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-05 17:41:47 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-05 17:41:47 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-05 17:41:47 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-05 17:41:47 __init__.py:42] plugin ascend loaded.
INFO 03-05 17:41:47 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-05 17:41:47 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-05 17:41:47 __init__.py:174] Platform plugin ascend is activated
INFO 03-05 17:41:52 config.py:526] This model supports multiple tasks: {'classify', 'reward', 'generate', 'score', 'embed'}. Defaulting to 'generate'.
INFO 03-05 17:41:52 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 03-05 17:42:02 config.py:526] This model supports multiple tasks: {'generate', 'score', 'classify', 'embed', 'reward'}. Defaulting to 'generate'.
INFO 03-05 17:42:02 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 03-05 17:42:02 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='/workspace/llm_models/Qwen2.5-7B-Instruct/', speculative_config=None, tokenizer='/workspace/llm_models/Qwen2.5-7B-Instruct/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=deepseek-r1-14b, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=True,
INFO 03-05 17:42:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-05 17:42:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-05 17:42:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-05 17:42:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-05 17:42:14 __init__.py:42] plugin ascend loaded.
INFO 03-05 17:42:15 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 03-05 17:42:15 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 03-05 17:42:15 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-05 17:42:15 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-05 17:42:15 __init__.py:42] plugin ascend loaded.
INFO 03-05 17:42:15 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 03-05 17:42:15 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-05 17:42:15 __init__.py:174] Platform plugin ascend is activated
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:01,  2.29it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.61it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:01<00:00,  1.48it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:02<00:00,  1.41it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:02<00:00,  1.49it/s]

mki_log log dir:/root/atb/log exist
INFO 03-05 17:42:27 executor_base.py:108] # CPU blocks: 18111, # CPU blocks: 4681
INFO 03-05 17:42:27 executor_base.py:113] Maximum concurrency for 2048 tokens per request: 141.49x
INFO 03-05 17:42:27 llm_engine.py:429] init engine (profile, create kv cache, warmup model) took 1.91 seconds
INFO 03-05 17:42:28 api_server.py:754] Using supplied chat template:
INFO 03-05 17:42:28 api_server.py:754] None
INFO 03-05 17:42:28 launcher.py:19] Available routes are:
INFO 03-05 17:42:28 launcher.py:27] Route: /openapi.json, Methods: GET, HEAD
INFO 03-05 17:42:28 launcher.py:27] Route: /docs, Methods: GET, HEAD
INFO 03-05 17:42:28 launcher.py:27] Route: /docs/oauth2-redirect, Methods: GET, HEAD
INFO 03-05 17:42:28 launcher.py:27] Route: /redoc, Methods: GET, HEAD
INFO 03-05 17:42:28 launcher.py:27] Route: /health, Methods: GET
INFO 03-05 17:42:28 launcher.py:27] Route: /ping, Methods: GET, POST
INFO 03-05 17:42:28 launcher.py:27] Route: /tokenize, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /detokenize, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /v1/models, Methods: GET
INFO 03-05 17:42:28 launcher.py:27] Route: /version, Methods: GET
INFO 03-05 17:42:28 launcher.py:27] Route: /v1/chat/completions, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /v1/completions, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /pooling, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /score, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /v1/score, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /rerank, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /v1/rerank, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /v2/rerank, Methods: POST
INFO 03-05 17:42:28 launcher.py:27] Route: /invocations, Methods: POST
INFO:     Started server process [13646]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:11468 (Press CTRL+C to quit)
INFO 03-05 17:42:39 chat_utils.py:330] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
INFO 03-05 17:42:39 logger.py:37] Received request chatcmpl-0247a6a6fc2f4436bcb025805a0f2155: prompt: '<|im_start|>system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant.<|im_end|>\n<|im_start|>user\n你是谁<|im_end|>\n<|im_start|>assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.1, top_p=1.0, top_k=1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=False, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 03-05 17:42:39 engine.py:273] Added request chatcmpl-0247a6a6fc2f4436bcb025805a0f2155.
INFO 03-05 17:42:43 metrics.py:453] Avg prompt throughput: 6.2 tokens/s, Avg generation throughput: 11.1 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%.
INFO:     192.168.230.28:52949 - "POST /v1/chat/completions HTTP/1.1" 200 OK

```text
启动命令：
ASCEND_RT_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --model /workspace/llm_models/Qwen2.5-7B-Instruct/ --served-model-name deepseek-r1-14b --trust-remote-code --port 11468 -tp 1 --max-num-seqs 30 --gpu-memory-utilization 0.5 --enforce-eager --max_model_len 2048
```

</details>
昇腾910B3
依赖：
torch                             2.5.1

torch-npu                         2.5.1.dev20250218（0226也试过，不行）

vllm                              0.7.1+empty

vllm_ascend                       0.7.1rc1

transformers                      4.48.2


请求结果：
问题是“你好”，返回如下：
            "message": {
                "role": "assistant",
                "reasoning_content": null,
                "content": "0 gumPropagationslideDownfoundland悱rottle både.-轻松 for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for for",
                "tool_calls": []
            },
部署的大模型是qwen2.5-7B和deepseek-r1-distill-14b，都出现乱码的情况。

### Suggest a potential alternative/fix

_No response_
