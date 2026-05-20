# Issue #1425: [Bug]: [v0.9.1rc1] 310P3 start success , reasoning exit vllm

## 基本信息

- **编号**: #1425
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1425
- **创建时间**: 2025-06-25T08:14:49Z
- **关闭时间**: 2025-11-11T06:40:09Z
- **更新时间**: 2025-11-11T06:40:10Z
- **提交者**: @onewaystreetcoder
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
ASCEND_RT_VISIBLE_DEVICES=0 vllm serve /models/Qwen2.5-3B-Instruct --served-model-name Qwen2.5-3B-Instruct --enable-auto-tool-choice --tool-call-parser hermes --max-model-len 32768 --port 8000 --trust-remote-code --dtype float16 --kv-cache-dtype fp8 --enforce-eager
INFO 06-23 13:44:04 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-23 13:44:04 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-23 13:44:05 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-23 13:44:05 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-23 13:44:05 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-23 13:44:05 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-23 13:44:08 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
WARNING 06-23 13:44:12 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-23 13:44:12 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-23 13:44:12 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-23 13:44:12 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-23 13:44:12 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-23 13:44:12 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-23 13:44:13 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 13:44:15 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 13:44:16 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 13:44:17 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 13:44:17 [api_server.py:1287] vLLM API server version 0.9.1
INFO 06-23 13:44:18 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 13:44:18 [cli_args.py:309] non-default args: {'enable_auto_tool_choice': True, 'tool_call_parser': 'hermes', 'model': '/models/Qwen2.5-3B-Instruct', 'trust_remote_code': True, 'dtype': 'float16', 'max_model_len': 32768, 'enforce_eager': True, 'served_model_name': ['Qwen2.5-3B-Instruct'], 'kv_cache_dtype': 'fp8'}
INFO 06-23 13:44:32 [config.py:823] This model supports multiple tasks: {'embed', 'reward', 'score', 'classify', 'generate'}. Defaulting to 'generate'.
WARNING 06-23 13:44:32 [arg_utils.py:1642] --kv-cache-dtype is not supported by the V1 Engine. Falling back to V0.
INFO 06-23 13:44:32 [config.py:1559] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor
INFO 06-23 13:44:32 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-23 13:44:32 [platform.py:164] Compilation disabled, using eager mode by default
INFO 06-23 13:44:32 [api_server.py:265] Started engine process with PID 17133
WARNING 06-23 13:44:36 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 06-23 13:44:37 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-23 13:44:37 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-23 13:44:38 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-23 13:44:38 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-23 13:44:38 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-23 13:44:38 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-23 13:44:41 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
WARNING 06-23 13:44:45 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-23 13:44:45 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-23 13:44:45 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-23 13:44:45 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-23 13:44:45 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-23 13:44:45 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-23 13:44:45 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='/models/Qwen2.5-3B-Instruct', speculative_config=None, tokenizer='/models/Qwen2.5-3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=fp8,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen2.5-3B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":0,"local_cache_dir":null}, use_cached_outputs=True,
WARNING 06-23 13:44:45 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffaf5d07cd0>
WARNING 06-23 13:44:52 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 06-23 13:44:53 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-23 13:44:53 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-23 13:44:54 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 06-23 13:44:54 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 06-23 13:44:54 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-23 13:44:54 [__init__.py:235] Platform plugin ascend is activated
WARNING 06-23 13:44:58 [_custom_ops.py:22] Failed to import from vllm._C with ImportError('/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108ListType3getERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
INFO 06-23 13:45:02 [parallel_state.py:1065] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
INFO 06-23 13:45:02 [model_runner.py:995] Starting to load model /models/Qwen2.5-3B-Instruct...
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:00<00:00,  2.15it/s]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:01<00:00,  1.21it/s]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:01<00:00,  1.29it/s]

INFO 06-23 13:45:13 [default_loader.py:272] Loading weights took 1.56 seconds
INFO 06-23 13:45:14 [model_runner.py:1000] Loading model weights took 5.7917 GB
.[rank0]:[W623 13:45:18.430189590 compiler_depend.ts:79] Warning: [Check][offset] Check input storage_offset[%ld] = 0 failed, result is untrustworthy151935 (function operator())
.INFO 06-23 13:45:34 [executor_base.py:113] # npu blocks: 466, # CPU blocks: 1820
INFO 06-23 13:45:34 [executor_base.py:118] Maximum concurrency for 32768 tokens per request: 1.82x
INFO 06-23 13:45:35 [llm_engine.py:428] init engine (profile, create kv cache, warmup model) took 20.31 seconds
.INFO 06-23 13:45:35 [serving_chat.py:81] "auto" tool choice has been enabled please note that while the parallel_tool_calls client option is preset for compatibility reasons, it will be ignored.
WARNING 06-23 13:45:35 [config.py:1363] Default sampling parameters have been overridden by the model's Hugging Face generation config recommended from the model creator. If this is not intended, please relaunch vLLM instance with `--generation-config vllm`.
INFO 06-23 13:45:35 [serving_chat.py:118] Using default chat sampling params from model: {'repetition_penalty': 1.05, 'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
INFO 06-23 13:45:35 [serving_completion.py:66] Using default completion sampling params from model: {'repetition_penalty': 1.05, 'temperature': 0.7, 'top_k': 20, 'top_p': 0.8}
INFO 06-23 13:45:35 [api_server.py:1349] Starting vLLM API server 0 on http://0.0.0.0:8000
INFO 06-23 13:45:35 [launcher.py:29] Available routes are:
INFO 06-23 13:45:35 [launcher.py:37] Route: /openapi.json, Methods: GET, HEAD
INFO 06-23 13:45:35 [launcher.py:37] Route: /docs, Methods: GET, HEAD
INFO 06-23 13:45:35 [launcher.py:37] Route: /docs/oauth2-redirect, Methods: GET, HEAD
INFO 06-23 13:45:35 [launcher.py:37] Route: /redoc, Methods: GET, HEAD
INFO 06-23 13:45:35 [launcher.py:37] Route: /health, Methods: GET
INFO 06-23 13:45:35 [launcher.py:37] Route: /load, Methods: GET
INFO 06-23 13:45:35 [launcher.py:37] Route: /ping, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /ping, Methods: GET
INFO 06-23 13:45:35 [launcher.py:37] Route: /tokenize, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /detokenize, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /v1/models, Methods: GET
INFO 06-23 13:45:35 [launcher.py:37] Route: /version, Methods: GET
INFO 06-23 13:45:35 [launcher.py:37] Route: /v1/chat/completions, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /v1/completions, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /v1/embeddings, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /pooling, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /classify, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /score, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /v1/score, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /v1/audio/transcriptions, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /rerank, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /v1/rerank, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /v2/rerank, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /invocations, Methods: POST
INFO 06-23 13:45:35 [launcher.py:37] Route: /metrics, Methods: GET
INFO:     Started server process [16994]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO 06-23 13:45:55 [chat_utils.py:420] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this.
INFO 06-23 13:45:55 [logger.py:43] Received request chatcmpl-88c303e8343e41a89ffde5dc07adba05: prompt: '<|im_start|>system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant.<|im_end|>\n<|im_start|>user\nnishi?<|im_end|>\n<|im_start|>assistant\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=32736, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None, prompt_embeds shape: None, lora_request: None, prompt_adapter_request: None.
INFO:     10.113.166.94:58646 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 06-23 13:45:55 [engine.py:317] Added request chatcmpl-88c303e8343e41a89ffde5dc07adba05.
....[rank0]:[E623 13:46:28.176383770 compiler_depend.ts:429] ReshapeAndCacheOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:117 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0xb8 (0xfffc4577c908 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x6c (0xfffc4572b404 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0xc8 (0xfffa94047078 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0x37118 (0xfffa94047118 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x18918b0 (0xfffb1d4a18b0 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x7cf0e4 (0xfffb1c3df0e4 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x7d1314 (0xfffb1c3e1314 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0x7cdc84 (0xfffb1c3ddc84 in /usr/local/python3.11.12/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0x4c9e4c (0xfffc457b9e4c in /usr/local/python3.11.12/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #9: <unknown function> + 0x7d5b8 (0xfffc5028d5b8 in /lib/aarch64-linux-gnu/libc.so.6)
frame #10: <unknown function> + 0xe5edc (0xfffc502f5edc in /lib/aarch64-linux-gnu/libc.so.6)

ERROR 06-23 13:46:28 [serving_chat.py:911] Error in chat completion stream generator.
ERROR 06-23 13:46:28 [serving_chat.py:911] Traceback (most recent call last):
ERROR 06-23 13:46:28 [serving_chat.py:911]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/entrypoints/openai/serving_chat.py", line 481, in chat_completion_stream_generator
ERROR 06-23 13:46:28 [serving_chat.py:911]     async for res in result_generator:
ERROR 06-23 13:46:28 [serving_chat.py:911]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/engine/multiprocessing/client.py", line 596, in _process_request
ERROR 06-23 13:46:28 [serving_chat.py:911]     raise request_output
ERROR 06-23 13:46:28 [serving_chat.py:911] vllm.engine.multiprocessing.MQEngineDeadError: Engine loop is not running. Inspect the stacktrace to find the original error: RuntimeError('The Inner error is reported as above. The process exits for this inner error, and the current working operator name is ReshapeCacheOperation.\nSince the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.\nNote: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.\n[ERROR] 2025-06-23-13:46:28 (PID:17133, Device:0, RankID:-1) ERR00100 PTA call acl api failed.\n').
ERROR 06-23 13:46:28 [engine.py:165] RuntimeError('The Inner error is reported as above. The process exits for this inner error, and the current working operator name is ReshapeCacheOperation.\nSince the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.\nNote: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.\n[ERROR] 2025-06-23-13:46:28 (PID:17133, Device:0, RankID:-1) ERR00100 PTA call acl api failed.\n')
ERROR 06-23 13:46:28 [engine.py:165] Traceback (most recent call last):
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 163, in start
ERROR 06-23 13:46:28 [engine.py:165]     self.run_engine_loop()
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 226, in run_engine_loop
ERROR 06-23 13:46:28 [engine.py:165]     request_outputs = self.engine_step()
ERROR 06-23 13:46:28 [engine.py:165]                       ^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 252, in engine_step
ERROR 06-23 13:46:28 [engine.py:165]     raise e
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 235, in engine_step
ERROR 06-23 13:46:28 [engine.py:165]     return self.engine.step()
ERROR 06-23 13:46:28 [engine.py:165]            ^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/engine/llm_engine.py", line 1352, in step
ERROR 06-23 13:46:28 [engine.py:165]     outputs = self.model_executor.execute_model(
ERROR 06-23 13:46:28 [engine.py:165]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/executor/executor_base.py", line 141, in execute_model
ERROR 06-23 13:46:28 [engine.py:165]     output = self.collective_rpc("execute_model",
ERROR 06-23 13:46:28 [engine.py:165]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 06-23 13:46:28 [engine.py:165]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-23 13:46:28 [engine.py:165]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/utils.py", line 2671, in run_method
ERROR 06-23 13:46:28 [engine.py:165]     return func(*args, **kwargs)
ERROR 06-23 13:46:28 [engine.py:165]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/worker/worker_base.py", line 421, in execute_model
ERROR 06-23 13:46:28 [engine.py:165]     output = self.model_runner.execute_model(
ERROR 06-23 13:46:28 [engine.py:165]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 06-23 13:46:28 [engine.py:165]     return func(*args, **kwargs)
ERROR 06-23 13:46:28 [engine.py:165]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm_ascend/worker/model_runner.py", line 1497, in execute_model
ERROR 06-23 13:46:28 [engine.py:165]     output: SamplerOutput = self.sampler(
ERROR 06-23 13:46:28 [engine.py:165]                             ^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 06-23 13:46:28 [engine.py:165]     return self._call_impl(*args, **kwargs)
ERROR 06-23 13:46:28 [engine.py:165]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 06-23 13:46:28 [engine.py:165]     return forward_call(*args, **kwargs)
ERROR 06-23 13:46:28 [engine.py:165]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py", line 298, in forward
ERROR 06-23 13:46:28 [engine.py:165]     maybe_deferred_sample_results, maybe_sampled_tokens_tensor = _sample(
ERROR 06-23 13:46:28 [engine.py:165]                                                                  ^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py", line 758, in _sample
ERROR 06-23 13:46:28 [engine.py:165]     return _sample_with_torch(
ERROR 06-23 13:46:28 [engine.py:165]            ^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py", line 727, in _sample_with_torch
ERROR 06-23 13:46:28 [engine.py:165]     return get_pythonized_sample_results(
ERROR 06-23 13:46:28 [engine.py:165]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py", line 604, in get_pythonized_sample_results
ERROR 06-23 13:46:28 [engine.py:165]     sample_results = _random_sample(seq_groups,
ERROR 06-23 13:46:28 [engine.py:165]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165]   File "/usr/local/python3.11.12/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py", line 496, in _random_sample
ERROR 06-23 13:46:28 [engine.py:165]     random_samples = random_samples.cpu()
ERROR 06-23 13:46:28 [engine.py:165]                      ^^^^^^^^^^^^^^^^^^^^
ERROR 06-23 13:46:28 [engine.py:165] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is ReshapeCacheOperation.
ERROR 06-23 13:46:28 [engine.py:165] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
ERROR 06-23 13:46:28 [engine.py:165] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
ERROR 06-23 13:46:28 [engine.py:165] [ERROR] 2025-06-23-13:46:28 (PID:17133, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
ERROR 06-23 13:46:28 [engine.py:165]
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [16994]
```

</details>
derver info : 
Ascend-hdk-310p-npu-driver_25.0.rc1.1
Ascend-hdk-310p-npu-firmware_7.7.0.1.231
Ascend-cann-kernels-310p_8.1.RC1
Ascend-cann-nnal_8.1.RC1
Ascend-cann-nnae_8.1.RC1
Ascend-cann-nnrt_8.1.RC1
Ascend-cann-toolkit_8.1.RC1

### 🐛 Describe the bug

[stack.txt](https://github.com/user-attachments/files/20899573/stack.txt)
