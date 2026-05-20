# Issue #2544: [Bug]: alsbench  test failed due to AttributeError: '_OpNamespace' '_C' object has no attribute 'apply_repetition_penalties_'

## 基本信息

- **编号**: #2544
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2544
- **创建时间**: 2025-08-26T06:19:28Z
- **关闭时间**: 2025-08-29T01:15:30Z
- **更新时间**: 2025-08-29T01:15:30Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

alsbench  test error when vllm(v0.10.1.1) and vllm-ascend(0f81e032f04b72f4dd0c7fefd62b7220942c545a) 




### 🐛 Describe the bug

```
vllm serve Qwen/Qwen2.5-7B-Instruct --dtype bfloat16 --max_model_len 14336 --max-num-batched-tokens 14336 
ais_bench --models vllm_api_general_chat --datasets demo_gsm8k_gen_4_shot_cot_chat_prompt --summarizer example
```
error:
```
(APIServer pid=38261) INFO 08-25 08:42:18 [loggers.py:123] Engine 000: Avg prompt throughput: 125.2 tokens/s, Avg generation throughput: 133.8 tokens/s, Running: 3 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.1%, Prefix cache hit rate: 0.0%
(APIServer pid=38261) INFO 08-25 08:42:28 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 19.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(APIServer pid=38261) INFO 08-25 08:42:38 [loggers.py:123] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(APIServer pid=38261) INFO 08-25 08:44:40 [chat_utils.py:470] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.1.1) with config: model='Qwen/Qwen2.5-7B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=14336, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen2.5-7B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"/root/.cache/vllm/torch_compile_cache/57024fa0b4","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.unified_ascend_attention_with_output","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":"/root/.cache/vllm/torch_compile_cache/57024fa0b4/rank_0_0/backbone"},
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [dump_input.py:76] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=chatcmpl-ce39ce4f06d24733a0ad97a04189b172,prompt_token_ids_len=1519,mm_kwargs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.03, temperature=0.5, top_p=0.95, top_k=10, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=512, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={chatcmpl-ce39ce4f06d24733a0ad97a04189b172: 1519}, total_num_scheduled_tokens=1519, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[12], finished_req_ids=[], free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=1, num_waiting_reqs=0, step_counter=0, current_wave=0, kv_cache_usage=0.002328497223714865, prefix_cache_stats=PrefixCacheStats(reset=False, requests=1, queries=1519, hits=0), spec_decoding_stats=None, num_corrupted_reqs=0)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702] EngineCore encountered a fatal error.
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702] Traceback (most recent call last):
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 693, in run_engine_core
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     engine_core.run_busy_loop()
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 720, in run_busy_loop
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     self._process_engine_step()
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 745, in _process_engine_step
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     outputs, model_executed = self.step_fn()
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]                               ^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 288, in step
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     model_output = self.execute_model_with_error_logging(
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 274, in execute_model_with_error_logging
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     raise err
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 265, in execute_model_with_error_logging
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     return model_fn(scheduler_output)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 87, in execute_model
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     output = self.collective_rpc("execute_model",
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3007, in run_method
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     return func(*args, **kwargs)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 205, in execute_model
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     return func(*args, **kwargs)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1665, in execute_model
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     sampler_output = self.sampler(
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]                      ^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     return self._call_impl(*args, **kwargs)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     return forward_call(*args, **kwargs)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/sample/sampler.py", line 58, in forward
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     logits = self.apply_penalties(logits, sampling_metadata)
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/sample/sampler.py", line 209, in apply_penalties
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     logits = apply_all_penalties(
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]              ^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/v1/sample/ops/penalties.py", line 24, in apply_all_penalties
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     return apply_penalties(logits, prompt_token_ids, output_tokens_t,
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/model_executor/layers/utils.py", line 78, in apply_penalties
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     apply_repetition_penalties(logits, prompt_mask, output_mask,
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/_custom_ops.py", line 315, in apply_repetition_penalties
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     apply_repetition_penalties_cuda(logits, prompt_mask, output_mask,
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/vllm-workspace/vllm/vllm/_custom_ops.py", line 299, in apply_repetition_penalties_cuda
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     torch.ops._C.apply_repetition_penalties_(logits, prompt_mask, output_mask,
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1267, in __getattr__
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702]     raise AttributeError(
(EngineCore_0 pid=38549) ERROR 08-25 08:44:40 [core.py:702] AttributeError: '_OpNamespace' '_C' object has no attribute 'apply_repetition_penalties_'
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430] AsyncLLM output_handler failed.
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430] Traceback (most recent call last):
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 389, in output_handler
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430]     outputs = await engine_core.get_output_async()
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 843, in get_output_async
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430]     raise self._format_exception(outputs) from None
(APIServer pid=38261) ERROR 08-25 08:44:40 [async_llm.py:430] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     127.0.0.1:34628 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(APIServer pid=38261) INFO:     Shutting down
(APIServer pid=38261) INFO:     Waiting for application shutdown.
(APIServer pid=38261) INFO:     Application shutdown complete.
(APIServer pid=38261) INFO:     Finished server process [38261]
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

```
