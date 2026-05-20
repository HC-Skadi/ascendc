# Issue #183: [Usage]: Checkpoint loading error when running Deepseek-V3/R1

## 基本信息

- **编号**: #183
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/183
- **创建时间**: 2025-02-26T13:32:43Z
- **关闭时间**: 2025-02-27T13:49:51Z
- **更新时间**: 2025-02-28T02:16:32Z
- **提交者**: @ApsarasX
- **评论数**: 5

## 标签

bug; question

## 问题描述

### Your current environment

```txt
npu-smi 24.1.0                   Version: 24.1.0
```
```txt
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/x86_64-linux
```
```txt
torch==2.5.1+cpu
torch-npu==2.5.1.dev20250218
transformers==4.49.0
ray==2.42.1
vllm==0.7.1+empty
vllm_ascend==0.7.1-dev
```

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

I am attempting to run the bf16 version of DeepSeek-V3 using 2 machines, with each node equipped with 16 910B NPUs, totaling 32 NPUs across all nodes.

The followings are my operational steps(from https://vllm-ascend.readthedocs.io/en/latest/tutorials.html#online-serving-on-multi-machine):
1. on the head node 
```sh
export VLLM_HOST_IP=$POD_IP
export HCCL_IF_IP=$POD_IP
export HCCL_CONNECT_TIMEOUT=120
export GLOO_SOCKET_IFNAME=bond0
export TP_SOCKET_IFNAME=bond0
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1 
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ray start --head --num-gpus=16 --port=6379
```
2. on the worker node
```sh
export VLLM_HOST_IP=$POD_IP
export HCCL_IF_IP=$POD_IP
export HCCL_CONNECT_TIMEOUT=120
export GLOO_SOCKET_IFNAME=bond0
export TP_SOCKET_IFNAME=bond0
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1 
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ray start --address=$HEAD_NODE_IP:6379 --num-gpus=16 --node-ip-address=$POD_IP
```
3. on the head node
```sh
vllm serve /root/DeepSeek-V3 \
    --served_model_name DeepSeek-V3 \
    -tp 16 -pp 2 \
    --distributed_executor_backend "ray" \
    --max-model-len 1024 \
    --trust-remote-code
```

The content of `/root/DeepSeek-V3/config.json` is as follows
```
{
  "architectures": [
    "DeepseekV3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "configuration_deepseek.DeepseekV3Config",
    "AutoModel": "modeling_deepseek.DeepseekV3Model",
    "AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 0,
  "eos_token_id": 1,
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 163840,
  "model_type": "deepseek_v3",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 8,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 61,
  "num_key_value_heads": 128,
  "num_nextn_predict_layers": 1,
  "pretraining_tp": 1,
  "q_lora_rank": 1536,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32,
    "beta_slow": 1,
    "factor": 40,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "type": "yarn"
  },
  "rope_theta": 10000,
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 4,
  "topk_method": "noaux_tc",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.33.1",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 129280
}
```
> I deleted the contents of the `quantization_config` field in the original config.json

Finally, I encountered the following error
```
nohup: ignoring input
INFO 02-26 20:37:48 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-26 20:37:48 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-26 20:37:48 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-26 20:37:48 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-26 20:37:48 __init__.py:42] plugin ascend loaded.
INFO 02-26 20:37:48 __init__.py:174] Platform plugin ascend is activated
INFO 02-26 20:37:49 api_server.py:838] vLLM API server version 0.7.1
INFO 02-26 20:37:49 api_server.py:839] args: Namespace(subparser='serve', model_tag='/root/DeepSeek-V3', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/root/DeepSeek-V3', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=1024, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend='ray', pipeline_parallel_size=2, tensor_parallel_size=16, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['DeepSeek-V3'], qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False, dispatch_function=<function serve at 0x7f96ef780700>)
INFO 02-26 20:37:49 config.py:135] Replacing legacy 'type' key with 'rope_type'
INFO 02-26 20:37:54 config.py:526] This model supports multiple tasks: {'classify', 'generate', 'reward', 'embed', 'score'}. Defaulting to 'generate'.
WARNING 02-26 20:37:54 config.py:653] Async output processing can not be enabled with pipeline parallel
INFO 02-26 20:37:54 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 02-26 20:37:54 config.py:3257] MLA is enabled; forcing chunked prefill and prefix caching to be disabled.
INFO 02-26 20:37:54 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='/root/DeepSeek-V3', speculative_config=None, tokenizer='/root/DeepSeek-V3', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=1024, download_dir=None, load_format=auto, tensor_parallel_size=16, pipeline_parallel_size=2, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=DeepSeek-V3, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=False, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False, 
INFO 02-26 20:37:55 config.py:135] Replacing legacy 'type' key with 'rope_type'
2025-02-26 20:37:55,106	INFO worker.py:1654 -- Connecting to existing Ray cluster at address: $HEAD_NODE_IP:6379...
2025-02-26 20:37:55,115	INFO worker.py:1841 -- Connected to Ray cluster.
INFO 02-26 20:37:55 ray_distributed_executor.py:153] use_ray_spmd_worker: False
(pid=193399) INFO 02-26 20:37:58 __init__.py:28] Available plugins for group vllm.platform_plugins:
(pid=193399) INFO 02-26 20:37:58 __init__.py:30] name=ascend, value=vllm_ascend:register
(pid=193399) INFO 02-26 20:37:58 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
(pid=193399) INFO 02-26 20:37:58 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
(pid=193399) INFO 02-26 20:37:58 __init__.py:42] plugin ascend loaded.
(pid=193399) INFO 02-26 20:37:58 __init__.py:174] Platform plugin ascend is activated
WARNING 02-26 20:38:12 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(RayWorkerWrapper pid=193400) WARNING 02-26 20:38:12 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(pid=134737) INFO 02-26 20:37:59 __init__.py:28] Available plugins for group vllm.platform_plugins:[32m [repeated 31x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(pid=134737) INFO 02-26 20:37:59 __init__.py:30] name=ascend, value=vllm_ascend:register[32m [repeated 31x across cluster]
(pid=134737) INFO 02-26 20:37:59 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.[32m [repeated 31x across cluster]
(pid=134737) INFO 02-26 20:37:59 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.[32m [repeated 31x across cluster]
(pid=134737) INFO 02-26 20:37:59 __init__.py:42] plugin ascend loaded.[32m [repeated 31x across cluster]
(pid=134737) INFO 02-26 20:37:59 __init__.py:174] Platform plugin ascend is activated[32m [repeated 31x across cluster]
(RayWorkerWrapper pid=134731) INFO 02-26 20:38:12 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], buffer_handle=(15, 4194304, 6, 'psm_7e654887'), local_subscribe_port=32029, remote_subscribe_port=None)
INFO 02-26 20:38:12 shm_broadcast.py:256] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], buffer_handle=(15, 4194304, 6, 'psm_8071af5b'), local_subscribe_port=42323, remote_subscribe_port=None)
(RayWorkerWrapper pid=134732) INFO 02-26 20:38:12 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.

Loading safetensors checkpoint shards:   0% Completed | 0/163 [00:00<?, ?it/s]
(RayWorkerWrapper pid=134738) worker_base.py:572] Error executing method 'load_model'. This might cause deadlock in distributed execution.
(RayWorkerWrapper pid=134738) worker_base.py:572] Traceback (most recent call last):
(RayWorkerWrapper pid=134738) worker_base.py:572]   File "/root/vllm/vllm/worker/worker_base.py", line 564, in execute_method
(RayWorkerWrapper pid=134738) worker_base.py:572]     return run_method(target, method, args, kwargs)
(RayWorkerWrapper pid=134738) worker_base.py:572]   File "/root/vllm/vllm/utils.py", line 2208, in run_method
(RayWorkerWrapper pid=134738) worker_base.py:572]     return func(*args, **kwargs)
(RayWorkerWrapper pid=134738) worker_base.py:572]   File "/root/vllm-ascend/vllm_ascend/worker.py", line 188, in load_model
(RayWorkerWrapper pid=134738) worker_base.py:572]     self.model_runner.load_model()
(RayWorkerWrapper pid=134738) worker_base.py:572]   File "/root/vllm-ascend/vllm_ascend/model_runner.py", line 830, in load_model
(RayWorkerWrapper pid=134738) worker_base.py:572]     self.model = get_model(vllm_config=self.vllm_config)
(RayWorkerWrapper pid=134738) worker_base.py:572]   File "/root/vllm/vllm/model_executor/model_loader/__init__.py", line 12, in get_model
(RayWorkerWrapper pid=134738) worker_base.py:572]     return loader.load_model(vllm_config=vllm_config)
(RayWorkerWrapper pid=134738) worker_base.py:572]   File "/root/vllm/vllm/model_executor/model_loader/loader.py", line 380, in load_model
(RayWorkerWrapper pid=134738) worker_base.py:572]     loaded_weights = model.load_weights(
(RayWorkerWrapper pid=134738) worker_base.py:572]   File "/root/vllm/vllm/model_executor/models/deepseek_v3.py", line 782, in load_weights
(RayWorkerWrapper pid=134738) worker_base.py:572]     param = params_dict[name]
(RayWorkerWrapper pid=134738) worker_base.py:572] KeyError: 'model.layers.39.mlp.experts.w2_weight_scale_inv'
ERROR 02-26 20:38:13 worker_base.py:572] Error executing method 'load_model'. This might cause deadlock in distributed execution.
ERROR 02-26 20:38:13 worker_base.py:572] Traceback (most recent call last):
ERROR 02-26 20:38:13 worker_base.py:572]   File "/root/vllm/vllm/worker/worker_base.py", line 564, in execute_method
ERROR 02-26 20:38:13 worker_base.py:572]     return run_method(target, method, args, kwargs)
ERROR 02-26 20:38:13 worker_base.py:572]   File "/root/vllm/vllm/utils.py", line 2208, in run_method
ERROR 02-26 20:38:13 worker_base.py:572]     return func(*args, **kwargs)
ERROR 02-26 20:38:13 worker_base.py:572]   File "/root/vllm-ascend/vllm_ascend/worker.py", line 188, in load_model
ERROR 02-26 20:38:13 worker_base.py:572]     self.model_runner.load_model()
ERROR 02-26 20:38:13 worker_base.py:572]   File "/root/vllm-ascend/vllm_ascend/model_runner.py", line 830, in load_model
ERROR 02-26 20:38:13 worker_base.py:572]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 02-26 20:38:13 worker_base.py:572]   File "/root/vllm/vllm/model_executor/model_loader/__init__.py", line 12, in get_model
ERROR 02-26 20:38:13 worker_base.py:572]     return loader.load_model(vllm_config=vllm_config)
ERROR 02-26 20:38:13 worker_base.py:572]   File "/root/vllm/vllm/model_executor/model_loader/loader.py", line 380, in load_model
ERROR 02-26 20:38:13 worker_base.py:572]     loaded_weights = model.load_weights(
ERROR 02-26 20:38:13 worker_base.py:572]   File "/root/vllm/vllm/model_executor/models/deepseek_v3.py", line 782, in load_weights
ERROR 02-26 20:38:13 worker_base.py:572]     param = params_dict[name]
ERROR 02-26 20:38:13 worker_base.py:572] KeyError: 'model.layers.27.mlp.experts.w2_weight_scale_inv'
[rank0]: Traceback (most recent call last):
[rank0]:   File "/opt/conda/bin/vllm", line 8, in <module>
[rank0]:     sys.exit(main())
[rank0]:   File "/root/vllm/vllm/scripts.py", line 202, in main
[rank0]:     args.dispatch_function(args)
[rank0]:   File "/root/vllm/vllm/scripts.py", line 42, in serve
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/opt/conda/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
[rank0]:     return loop.run_until_complete(wrapper())
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/opt/conda/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:   File "/root/vllm/vllm/entrypoints/openai/api_server.py", line 873, in run_server
[rank0]:     async with build_async_engine_client(args) as engine_client:
[rank0]:   File "/opt/conda/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/root/vllm/vllm/entrypoints/openai/api_server.py", line 134, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/opt/conda/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/root/vllm/vllm/entrypoints/openai/api_server.py", line 158, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_engine_args(
[rank0]:   File "/root/vllm/vllm/engine/async_llm_engine.py", line 642, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/root/vllm/vllm/engine/async_llm_engine.py", line 592, in __init__
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:   File "/root/vllm/vllm/engine/async_llm_engine.py", line 265, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/root/vllm/vllm/engine/llm_engine.py", line 271, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank0]:   File "/root/vllm/vllm/executor/executor_base.py", line 260, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/root/vllm/vllm/executor/executor_base.py", line 49, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/root/vllm/vllm/executor/ray_distributed_executor.py", line 88, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/root/vllm/vllm/executor/ray_distributed_executor.py", line 344, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/root/vllm/vllm/executor/ray_distributed_executor.py", line 464, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/root/vllm/vllm/worker/worker_base.py", line 573, in execute_method
[rank0]:     raise e
[rank0]:   File "/root/vllm/vllm/worker/worker_base.py", line 564, in execute_method
[rank0]:     return run_method(target, method, args, kwargs)
[rank0]:   File "/root/vllm/vllm/utils.py", line 2208, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/vllm-ascend/vllm_ascend/worker.py", line 188, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/root/vllm-ascend/vllm_ascend/model_runner.py", line 830, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/root/vllm/vllm/model_executor/model_loader/__init__.py", line 12, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/root/vllm/vllm/model_executor/model_loader/loader.py", line 380, in load_model
[rank0]:     loaded_weights = model.load_weights(
[rank0]:   File "/root/vllm/vllm/model_executor/models/deepseek_v3.py", line 782, in load_weights
[rank0]:     param = params_dict[name]
[rank0]: KeyError: 'model.layers.27.mlp.experts.w2_weight_scale_inv'
(RayWorkerWrapper pid=134743) WARNING 02-26 20:38:12 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193373) INFO 02-26 20:38:12 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572] Error executing method 'load_model'. This might cause deadlock in distributed execution.[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572] Traceback (most recent call last):[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]   File "/root/vllm/vllm/worker/worker_base.py", line 564, in execute_method[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]     return run_method(target, method, args, kwargs)[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]   File "/root/vllm/vllm/utils.py", line 2208, in run_method[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]     return func(*args, **kwargs)[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]   File "/root/vllm-ascend/vllm_ascend/worker.py", line 188, in load_model[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]     self.model_runner.load_model()[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]   File "/root/vllm-ascend/vllm_ascend/model_runner.py", line 830, in load_model[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]     self.model = get_model(vllm_config=self.vllm_config)[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]   File "/root/vllm/vllm/model_executor/model_loader/__init__.py", line 12, in get_model[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]     return loader.load_model(vllm_config=vllm_config)[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]   File "/root/vllm/vllm/model_executor/model_loader/loader.py", line 380, in load_model[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]     loaded_weights = model.load_weights([32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]   File "/root/vllm/vllm/model_executor/models/deepseek_v3.py", line 782, in load_weights[32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572]     param = params_dict[name][32m [repeated 30x across cluster]
(RayWorkerWrapper pid=193386) worker_base.py:572] KeyError: 'model.layers.27.mlp.experts.w2_weight_scale_inv'[32m [repeated 30x across cluster]
[ERROR] 2025-02-26-20:38:15 (PID:211548, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception

Loading safetensors checkpoint shards:   1% Completed | 1/163 [00:03<08:54,  3.30s/it]

/opt/conda/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```

