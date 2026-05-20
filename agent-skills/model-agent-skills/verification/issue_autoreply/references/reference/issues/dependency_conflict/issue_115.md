# Issue #115: [Bug]: Qwen2-VL-72B-Instruct Inference failure

## 基本信息

- **编号**: #115
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/115
- **创建时间**: 2025-02-19T16:26:54Z
- **关闭时间**: 2025-04-01T10:27:46Z
- **更新时间**: 2025-04-01T10:27:48Z
- **提交者**: @invokerbyxv
- **评论数**: 4

## 标签

bug

## 问题描述

**npu-smi info**

```
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 92.2        33                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          54601/ 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 88.9        31                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          54599/ 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 89.9        32                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          54599/ 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 92.8        32                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          54599/ 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 90.6        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3374 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 89.1        35                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3374 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 90.1        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3375 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 96.1        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3374 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 266776        | python3                  | 51277                   |
+===========================+===============+====================================================+
| 1       0                 | 267174        | python3                  | 51277                   |
+===========================+===============+====================================================+
| 2       0                 | 267176        | python3                  | 51277                   |
+===========================+===============+====================================================+
| 3       0                 | 267178        | python3                  | 51277                   |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
```

---

**run cmd**

```bash
docker run -dit \
--env ASCEND_LAUNCH_BLOCKING=1 \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /data/Qwen2-VL-72B-Instruct:/data/Qwen2-VL-72B-Instruct \
-p 10001:8000 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
--shm-size 16G \
--name vllm-npu-vl \
quay.io/ascend/vllm-ascend:v0.7.1rc1 python3 -m vllm.entrypoints.openai.api_server --model /data/Qwen2-VL-72B-Instruct --served-model-name chat --uvicorn-log-level debug --disable-log-stats --host 0.0.0.0 --port 8000 --trust-remote-code --gpu-memory-utilization 0.9 --tensor-parallel-size 4 --limit-mm-per-prompt image=6
```
---

**full docker logs**
```log
INFO 02-19 16:02:58 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-19 16:02:58 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-19 16:02:58 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-19 16:02:58 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-19 16:02:58 __init__.py:42] plugin ascend loaded.
INFO 02-19 16:02:59 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-19 16:02:59 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-19 16:02:59 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-19 16:02:59 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-19 16:02:59 __init__.py:42] plugin ascend loaded.
INFO 02-19 16:02:59 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-19 16:02:59 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-19 16:02:59 __init__.py:174] Platform plugin ascend is activated
INFO 02-19 16:03:01 api_server.py:838] vLLM API server version 0.7.1
INFO 02-19 16:03:01 api_server.py:839] args: Namespace(host='0.0.0.0', port=8000, uvicorn_log_level='debug', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/data/Qwen2-VL-72B-Instruct', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=4, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_seqs=None, max_logprobs=20, disable_log_stats=True, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt={'image': 6}, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['chat'], qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False)
INFO 02-19 16:03:01 api_server.py:204] Started engine process with PID 208
INFO 02-19 16:03:08 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-19 16:03:08 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-19 16:03:08 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-19 16:03:08 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-19 16:03:08 __init__.py:42] plugin ascend loaded.
INFO 02-19 16:03:08 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-19 16:03:08 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-19 16:03:08 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-19 16:03:08 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-19 16:03:08 __init__.py:42] plugin ascend loaded.
INFO 02-19 16:03:08 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-19 16:03:08 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-19 16:03:08 __init__.py:174] Platform plugin ascend is activated
INFO 02-19 16:03:12 config.py:526] This model supports multiple tasks: {'classify', 'embed', 'reward', 'score', 'generate'}. Defaulting to 'generate'.
INFO 02-19 16:03:12 config.py:1383] Defaulting to use mp for distributed inference
INFO 02-19 16:03:12 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 02-19 16:03:21 config.py:526] This model supports multiple tasks: {'generate', 'embed', 'classify', 'reward', 'score'}. Defaulting to 'generate'.
INFO 02-19 16:03:21 config.py:1383] Defaulting to use mp for distributed inference
INFO 02-19 16:03:21 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 02-19 16:03:21 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='/data/Qwen2-VL-72B-Instruct', speculative_config=None, tokenizer='/data/Qwen2-VL-72B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=chat, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True,
WARNING 02-19 16:03:22 multiproc_worker_utils.py:298] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
(VllmWorkerProcess pid=480) INFO 02-19 16:03:22 multiproc_worker_utils.py:227] Worker ready; awaiting tasks
(VllmWorkerProcess pid=482) INFO 02-19 16:03:22 multiproc_worker_utils.py:227] Worker ready; awaiting tasks
(VllmWorkerProcess pid=484) INFO 02-19 16:03:22 multiproc_worker_utils.py:227] Worker ready; awaiting tasks
INFO 02-19 16:03:34 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-19 16:03:34 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-19 16:03:34 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-19 16:03:34 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-19 16:03:34 __init__.py:42] plugin ascend loaded.
INFO 02-19 16:03:35 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-19 16:03:35 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-19 16:03:35 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-19 16:03:35 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-19 16:03:35 __init__.py:42] plugin ascend loaded.
INFO 02-19 16:03:35 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
WARNING 02-19 16:03:35 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-19 16:03:35 __init__.py:174] Platform plugin ascend is activated
INFO 02-19 16:03:41 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1, 2, 3], buffer_handle=(3, 4194304, 6, 'psm_5c28e1d3'), local_subscribe_port=36915, remote_subscribe_port=None)
INFO 02-19 16:03:42 config.py:2974] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=480) INFO 02-19 16:03:42 config.py:2974] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=482) INFO 02-19 16:03:42 config.py:2974] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
(VllmWorkerProcess pid=484) INFO 02-19 16:03:42 config.py:2974] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
Loading safetensors checkpoint shards: 100% 38/38 [00:22<00:00,  1.69it/s]
(VllmWorkerProcess pid=482) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=480) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=484) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=484) Computed max_num_seqs (min(256, 32768 // 114688)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=480) Computed max_num_seqs (min(256, 32768 // 114688)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=482) Computed max_num_seqs (min(256, 32768 // 114688)) to be less than 1. Setting it to the minimum value of 1.
Computed max_num_seqs (min(256, 32768 // 114688)) to be less than 1. Setting it to the minimum value of 1.
(VllmWorkerProcess pid=484) It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
(VllmWorkerProcess pid=480) It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
(VllmWorkerProcess pid=482) It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
(VllmWorkerProcess pid=484) Token indices sequence length is longer than the specified maximum sequence length for this model (114688 > 32768). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=480) Token indices sequence length is longer than the specified maximum sequence length for this model (114688 > 32768). Running this sequence through the model will result in indexing errors
Token indices sequence length is longer than the specified maximum sequence length for this model (114688 > 32768). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=482) Token indices sequence length is longer than the specified maximum sequence length for this model (114688 > 32768). Running this sequence through the model will result in indexing errors
(VllmWorkerProcess pid=484) WARNING 02-19 16:04:25 profiling.py:184] The context length (32768) of the model is too short to hold the multi-modal embeddings in the worst case (114688 tokens in total, out of which {'image': 98304, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=480) WARNING 02-19 16:04:26 profiling.py:184] The context length (32768) of the model is too short to hold the multi-modal embeddings in the worst case (114688 tokens in total, out of which {'image': 98304, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
WARNING 02-19 16:04:26 profiling.py:184] The context length (32768) of the model is too short to hold the multi-modal embeddings in the worst case (114688 tokens in total, out of which {'image': 98304, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
(VllmWorkerProcess pid=482) WARNING 02-19 16:04:28 profiling.py:184] The context length (32768) of the model is too short to hold the multi-modal embeddings in the worst case (114688 tokens in total, out of which {'image': 98304, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
..../usr/local/python3.10/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py:112: UserWarning: HCCL doesn't support gather at the moment. Implemented with allgather instead.
  warnings.warn("HCCL doesn't support gather at the moment. Implemented with allgather instead.")
INFO 02-19 16:05:31 executor_base.py:108] # CPU blocks: 10019, # CPU blocks: 3276
INFO 02-19 16:05:31 executor_base.py:113] Maximum concurrency for 32768 tokens per request: 4.89x
INFO 02-19 16:05:33 llm_engine.py:429] init engine (profile, create kv cache, warmup model) took 87.11 seconds
INFO 02-19 16:05:34 api_server.py:754] Using supplied chat template:
INFO 02-19 16:05:34 api_server.py:754] None
INFO 02-19 16:05:34 launcher.py:19] Available routes are:
INFO 02-19 16:05:34 launcher.py:27] Route: /openapi.json, Methods: GET, HEAD
INFO 02-19 16:05:34 launcher.py:27] Route: /docs, Methods: GET, HEAD
INFO 02-19 16:05:34 launcher.py:27] Route: /docs/oauth2-redirect, Methods: GET, HEAD
INFO 02-19 16:05:34 launcher.py:27] Route: /redoc, Methods: GET, HEAD
INFO 02-19 16:05:34 launcher.py:27] Route: /health, Methods: GET
INFO 02-19 16:05:34 launcher.py:27] Route: /ping, Methods: GET, POST
INFO 02-19 16:05:34 launcher.py:27] Route: /tokenize, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /detokenize, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /v1/models, Methods: GET
INFO 02-19 16:05:34 launcher.py:27] Route: /version, Methods: GET
INFO 02-19 16:05:34 launcher.py:27] Route: /v1/chat/completions, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /v1/completions, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /pooling, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /score, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /v1/score, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /rerank, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /v1/rerank, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /v2/rerank, Methods: POST
INFO 02-19 16:05:34 launcher.py:27] Route: /invocations, Methods: POST
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO 02-19 16:05:43 chat_utils.py:330] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-format` to override this.
INFO 02-19 16:05:43 logger.py:37] Received request chatcmpl-f38f28fdfd554ca38d4db30cef9077e0: prompt: '<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>What is the text in the illustrate?<|im_end|>\n<|im_start|>assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=32738, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO 02-19 16:05:46 engine.py:273] Added request chatcmpl-f38f28fdfd554ca38d4db30cef9077e0.
('Warning: torch.save with "_use_new_zipfile_serialization = False" is not recommended for npu tensor, which may bring unexpected errors and hopefully set "_use_new_zipfile_serialization = True"', 'if it is necessary to use this, please convert the npu tensor to cpu tensor for saving')
....(VllmWorkerProcess pid=482) /usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py:612: UserWarning: current tensor is running as_strided, don't perform inplace operations on the returned value. If you encounter this warning and have precision issues, you can try torch.npu.config.allow_internal_format = False to resolve precision issues. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:123.)
(VllmWorkerProcess pid=482)   x = x.unsqueeze(1)
/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py:612: UserWarning: current tensor is running as_strided, don't perform inplace operations on the returned value. If you encounter this warning and have precision issues, you can try torch.npu.config.allow_internal_format = False to resolve precision issues. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:123.)
  x = x.unsqueeze(1)
(VllmWorkerProcess pid=484) /usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py:612: UserWarning: current tensor is running as_strided, don't perform inplace operations on the returned value. If you encounter this warning and have precision issues, you can try torch.npu.config.allow_internal_format = False to resolve precision issues. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:123.)
(VllmWorkerProcess pid=484)   x = x.unsqueeze(1)
(VllmWorkerProcess pid=480) /usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py:612: UserWarning: current tensor is running as_strided, don't perform inplace operations on the returned value. If you encounter this warning and have precision issues, you can try torch.npu.config.allow_internal_format = False to resolve precision issues. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:123.)
(VllmWorkerProcess pid=480)   x = x.unsqueeze(1)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop.
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] Traceback (most recent call last):
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 234, in _run_worker_process
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return func(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 91, in start_worker_execution_loop
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = self.execute_model(execute_model_req=None)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 411, in execute_model
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = self.model_runner.execute_model(
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return func(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     hidden_or_intermediate_states = model_executable(
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1346, in forward
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     inputs_embeds = self.get_input_embeddings_v0(
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1281, in get_input_embeddings_v0
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     image_embeds = self._process_image_input(image_input)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1191, in _process_image_input
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 614, in forward
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     x = blk(x, cu_seqlens=cu_seqlens, rotary_pos_emb=rotary_pos_emb)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 400, in forward
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     x = x + self.attn(self.norm1(x),
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 345, in forward
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = F.scaled_dot_product_attention(q,
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] RuntimeError: call aclnnFlashAttentionScore failed, detail:EZ9999: Inner Error!
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] EZ9999: [PID: 480] 2025-02-19-16:05:47.408.512 atten mask dim should be 2 or 4, but got 3[FUNC:AnalyzeOptionalInput][FILE:flash_attention_score_tiling_general.cpp][LINE:1473]
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]         TraceBack (most recent call last):
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        fail to analyze context info.[FUNC:GetShapeAttrsInfo][FILE:flash_attention_score_tiling_general.cpp][LINE:835]
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Tiling failed
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Tiling Failed.
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Kernel GetWorkspace failed. opType: 40
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Kernel Run failed. opType: 40, FlashAttentionScore
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        launch failed for FlashAttentionScore, errno:561103.
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]
(VllmWorkerProcess pid=480) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] [ERROR] 2025-02-19-16:05:47 (PID:480, Device:1, RankID:-1) ERR01100 OPS call acl api failed
ERROR 02-19 16:05:47 engine.py:137] RuntimeError('call aclnnFlashAttentionScore failed, detail:EZ9999: Inner Error!\nEZ9999: [PID: 208] 2025-02-19-16:05:47.402.090 atten mask dim should be 2 or 4, but got 3[FUNC:AnalyzeOptionalInput][FILE:flash_attention_score_tiling_general.cpp][LINE:1473]\n        TraceBack (most recent call last):\n       fail to analyze context info.[FUNC:GetShapeAttrsInfo][FILE:flash_attention_score_tiling_general.cpp][LINE:835]\n       Tiling failed\n       Tiling Failed.\n       Kernel GetWorkspace failed. opType: 50\n       Kernel Run failed. opType: 50, FlashAttentionScore\n       launch failed for FlashAttentionScore, errno:561103.\n\n[ERROR] 2025-02-19-16:05:47 (PID:208, Device:0, RankID:-1) ERR01100 OPS call acl api failed')
ERROR 02-19 16:05:47 engine.py:137] Traceback (most recent call last):
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 135, in start
ERROR 02-19 16:05:47 engine.py:137]     self.run_engine_loop()
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 198, in run_engine_loop
ERROR 02-19 16:05:47 engine.py:137]     request_outputs = self.engine_step()
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 216, in engine_step
ERROR 02-19 16:05:47 engine.py:137]     raise e
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 207, in engine_step
ERROR 02-19 16:05:47 engine.py:137]     return self.engine.step()
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1384, in step
ERROR 02-19 16:05:47 engine.py:137]     outputs = self.model_executor.execute_model(
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 273, in execute_model
ERROR 02-19 16:05:47 engine.py:137]     driver_outputs = self._driver_execute_model(execute_model_req)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 142, in _driver_execute_model
ERROR 02-19 16:05:47 engine.py:137]     return self.driver_worker.execute_model(execute_model_req)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 411, in execute_model
ERROR 02-19 16:05:47 engine.py:137]     output = self.model_runner.execute_model(
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 02-19 16:05:47 engine.py:137]     return func(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
ERROR 02-19 16:05:47 engine.py:137]     hidden_or_intermediate_states = model_executable(
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-19 16:05:47 engine.py:137]     return self._call_impl(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-19 16:05:47 engine.py:137]     return forward_call(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1346, in forward
ERROR 02-19 16:05:47 engine.py:137]     inputs_embeds = self.get_input_embeddings_v0(
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1281, in get_input_embeddings_v0
ERROR 02-19 16:05:47 engine.py:137]     image_embeds = self._process_image_input(image_input)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1191, in _process_image_input
ERROR 02-19 16:05:47 engine.py:137]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-19 16:05:47 engine.py:137]     return self._call_impl(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-19 16:05:47 engine.py:137]     return forward_call(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 614, in forward
ERROR 02-19 16:05:47 engine.py:137]     x = blk(x, cu_seqlens=cu_seqlens, rotary_pos_emb=rotary_pos_emb)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-19 16:05:47 engine.py:137]     return self._call_impl(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-19 16:05:47 engine.py:137]     return forward_call(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 400, in forward
ERROR 02-19 16:05:47 engine.py:137]     x = x + self.attn(self.norm1(x),
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 02-19 16:05:47 engine.py:137]     return self._call_impl(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 02-19 16:05:47 engine.py:137]     return forward_call(*args, **kwargs)
ERROR 02-19 16:05:47 engine.py:137]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 345, in forward
ERROR 02-19 16:05:47 engine.py:137]     output = F.scaled_dot_product_attention(q,
ERROR 02-19 16:05:47 engine.py:137] RuntimeError: call aclnnFlashAttentionScore failed, detail:EZ9999: Inner Error!
ERROR 02-19 16:05:47 engine.py:137] EZ9999: [PID: 208] 2025-02-19-16:05:47.402.090 atten mask dim should be 2 or 4, but got 3[FUNC:AnalyzeOptionalInput][FILE:flash_attention_score_tiling_general.cpp][LINE:1473]
ERROR 02-19 16:05:47 engine.py:137]         TraceBack (most recent call last):
ERROR 02-19 16:05:47 engine.py:137]        fail to analyze context info.[FUNC:GetShapeAttrsInfo][FILE:flash_attention_score_tiling_general.cpp][LINE:835]
ERROR 02-19 16:05:47 engine.py:137]        Tiling failed
ERROR 02-19 16:05:47 engine.py:137]        Tiling Failed.
ERROR 02-19 16:05:47 engine.py:137]        Kernel GetWorkspace failed. opType: 50
ERROR 02-19 16:05:47 engine.py:137]        Kernel Run failed. opType: 50, FlashAttentionScore
ERROR 02-19 16:05:47 engine.py:137]        launch failed for FlashAttentionScore, errno:561103.
ERROR 02-19 16:05:47 engine.py:137]
ERROR 02-19 16:05:47 engine.py:137] [ERROR] 2025-02-19-16:05:47 (PID:208, Device:0, RankID:-1) ERR01100 OPS call acl api failed
CRITICAL 02-19 16:05:47 launcher.py:99] MQLLMEngine is already dead, terminating server process
INFO:     172.17.0.1:37064 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop.
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] Traceback (most recent call last):
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 234, in _run_worker_process
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return func(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 91, in start_worker_execution_loop
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = self.execute_model(execute_model_req=None)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 411, in execute_model
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = self.model_runner.execute_model(
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return func(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     hidden_or_intermediate_states = model_executable(
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1346, in forward
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     inputs_embeds = self.get_input_embeddings_v0(
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1281, in get_input_embeddings_v0
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     image_embeds = self._process_image_input(image_input)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1191, in _process_image_input
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 614, in forward
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     x = blk(x, cu_seqlens=cu_seqlens, rotary_pos_emb=rotary_pos_emb)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 400, in forward
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     x = x + self.attn(self.norm1(x),
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 345, in forward
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = F.scaled_dot_product_attention(q,
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] RuntimeError: call aclnnFlashAttentionScore failed, detail:EZ9999: Inner Error!
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] EZ9999: [PID: 482] 2025-02-19-16:05:47.408.055 atten mask dim should be 2 or 4, but got 3[FUNC:AnalyzeOptionalInput][FILE:flash_attention_score_tiling_general.cpp][LINE:1473]
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]         TraceBack (most recent call last):
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        fail to analyze context info.[FUNC:GetShapeAttrsInfo][FILE:flash_attention_score_tiling_general.cpp][LINE:835]
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Tiling failed
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Tiling Failed.
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Kernel GetWorkspace failed. opType: 40
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Kernel Run failed. opType: 40, FlashAttentionScore
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        launch failed for FlashAttentionScore, errno:561103.
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]
(VllmWorkerProcess pid=482) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] [ERROR] 2025-02-19-16:05:47 (PID:482, Device:2, RankID:-1) ERR01100 OPS call acl api failed
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop.
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] Traceback (most recent call last):
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 234, in _run_worker_process
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return func(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 91, in start_worker_execution_loop
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = self.execute_model(execute_model_req=None)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 411, in execute_model
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = self.model_runner.execute_model(
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return func(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1139, in execute_model
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     hidden_or_intermediate_states = model_executable(
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1346, in forward
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     inputs_embeds = self.get_input_embeddings_v0(
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1281, in get_input_embeddings_v0
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     image_embeds = self._process_image_input(image_input)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 1191, in _process_image_input
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 614, in forward
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     x = blk(x, cu_seqlens=cu_seqlens, rotary_pos_emb=rotary_pos_emb)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 400, in forward
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     x = x + self.attn(self.norm1(x),
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_vl.py", line 345, in forward
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]     output = F.scaled_dot_product_attention(q,
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] RuntimeError: call aclnnFlashAttentionScore failed, detail:EZ9999: Inner Error!
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] EZ9999: [PID: 484] 2025-02-19-16:05:47.409.566 atten mask dim should be 2 or 4, but got 3[FUNC:AnalyzeOptionalInput][FILE:flash_attention_score_tiling_general.cpp][LINE:1473]
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]         TraceBack (most recent call last):
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        fail to analyze context info.[FUNC:GetShapeAttrsInfo][FILE:flash_attention_score_tiling_general.cpp][LINE:835]
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Tiling failed
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Tiling Failed.
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Kernel GetWorkspace failed. opType: 40
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        Kernel Run failed. opType: 40, FlashAttentionScore
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]        launch failed for FlashAttentionScore, errno:561103.
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240]
(VllmWorkerProcess pid=484) ERROR 02-19 16:05:47 multiproc_worker_utils.py:240] [ERROR] 2025-02-19-16:05:47 (PID:484, Device:3, RankID:-1) ERR01100 OPS call acl api failed
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [1]
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 317, in _bootstrap
    util._exit_function()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 334, in _exit_function
    _run_finalizers(0)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 300, in _run_finalizers
    finalizer()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 54, in wrapper
    return func(cls, *args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 219, in finalize
    cls.global_mgr.finalize()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/utils/multiprocess_util.py", line 84, in finalize
    self.mgr.shutdown()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/util.py", line 224, in __call__
    res = self._callback(*self._args, **self._kwargs)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 674, in _finalize_manager
    process.join(timeout=1.0)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 149, in join
    res = self._popen.wait(timeout)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/popen_fork.py", line 40, in wait
    if not wait([self.sentinel], timeout):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/connection.py", line 931, in wait
    ready = selector.select(timeout)
  File "/usr/local/python3.10/lib/python3.10/selectors.py", line 416, in select
    fd_event_list = self._selector.poll(timeout)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 372, in signal_handler
    raise KeyboardInterrupt("MQLLMEngine terminated")
KeyboardInterrupt: MQLLMEngine terminated
INFO 02-19 16:05:50 multiproc_worker_utils.py:139] Terminating local vLLM worker processes
```
