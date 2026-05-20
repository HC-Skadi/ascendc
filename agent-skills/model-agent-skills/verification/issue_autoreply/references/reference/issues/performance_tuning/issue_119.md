# Issue #119: Quantization error while running Deepseek-V3-w8a8

## 基本信息

- **编号**: #119
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/119
- **创建时间**: 2025-02-20T07:48:19Z
- **关闭时间**: 2025-05-14T01:51:27Z
- **更新时间**: 2025-05-14T01:51:28Z
- **提交者**: @ApsarasX
- **评论数**: 11

## 标签

feature request

## 问题描述

- CANN: 8.0.0
- torch: 2.5.1+cpu
- torch-npu: 2.5.1.dev20250218
- vllm: 0.7.1+empty
- vllm-ascend: [v0.7.1rc1](https://github.com/vllm-project/vllm-ascend/releases/tag/v0.7.1rc1)
- model: Deepseek-V3-w8a8  from [https://www.hiascend.com:6066/software/modelzoo/models/detail/678bdeb4e1a64c9dae51d353d84ddd15](https://www.hiascend.com:6066/software/modelzoo/models/detail/678bdeb4e1a64c9dae51d353d84ddd15)


Traceback
```
$ python3 benchmark_throughput.py --model /root/DeepSeek-V3-w8a8 -tp 16 --num-prompts 1 --input-len 128 --output-len 128 --trust-remote-code
INFO 02-20 15:44:14 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-20 15:44:14 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-20 15:44:14 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-20 15:44:14 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-20 15:44:14 __init__.py:42] plugin ascend loaded.
INFO 02-20 15:44:14 __init__.py:174] Platform plugin ascend is activated
Namespace(backend='vllm', dataset=None, input_len=128, output_len=128, n=1, num_prompts=1, hf_max_batch_size=None, output_json=None, async_engine=False, disable_frontend_multiprocessing=False, lora_path=None, model='/root/DeepSeek-V3-w8a8', task='auto', tokenizer='/root/DeepSeek-V3-w8a8', skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=True, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=16, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.9, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=None, qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, disable_log_requests=False)
INFO 02-20 15:44:16 config.py:135] Replacing legacy 'type' key with 'rope_type'
INFO 02-20 15:44:21 config.py:526] This model supports multiple tasks: {'score', 'embed', 'generate', 'reward', 'classify'}. Defaulting to 'generate'.
INFO 02-20 15:44:21 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 02-20 15:44:21 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Traceback (most recent call last):
  File "/root/vllm/benchmarks/benchmark_throughput.py", line 531, in <module>
    main(args)
  File "/root/vllm/benchmarks/benchmark_throughput.py", line 402, in main
    elapsed_time = run_vllm(requests, args.n,
  File "/root/vllm/benchmarks/benchmark_throughput.py", line 170, in run_vllm
    llm = LLM(**dataclasses.asdict(engine_args))
  File "/root/vllm/vllm/utils.py", line 1039, in inner
    return fn(*args, **kwargs)
  File "/root/vllm/vllm/entrypoints/llm.py", line 240, in __init__
    self.llm_engine = self.engine_class.from_engine_args(
  File "/root/vllm/vllm/engine/llm_engine.py", line 479, in from_engine_args
    engine_config = engine_args.create_engine_config(usage_context)
  File "/root/vllm/vllm/engine/arg_utils.py", line 1059, in create_engine_config
    model_config = self.create_model_config()
  File "/root/vllm/vllm/engine/arg_utils.py", line 983, in create_model_config
    return ModelConfig(
  File "/root/vllm/vllm/config.py", line 376, in __init__
    self._verify_quantization()
  File "/root/vllm/vllm/config.py", line 599, in _verify_quantization
    raise ValueError(
ValueError: Unknown quantization method: ascend. Must be one of ['aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'fbgemm_fp8', 'modelopt', 'marlin', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'awq_marlin', 'gptq', 'compressed-tensors', 'bitsandbytes', 'qqq', 'hqq', 'experts_int8', 'neuron_quant', 'ipex', 'quark', 'moe_wna16'].
[ERROR] 2025-02-20-15:44:22 (PID:52048, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

config.json in model
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
    "vocab_size": 129280,
    "quantize": "w8a8_dynamic",
    "quantization_config": {
          "quant_method": "ascend"
     },
    "mla_quantize": "w8a8"
}
```
