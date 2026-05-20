# Issue #821: [Bug]: Qwen2-1.5B Inference Startup Hang on Huawei 910B Card under vNPU

## 基本信息

- **编号**: #821
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/821
- **创建时间**: 2025-05-12T10:08:49Z
- **关闭时间**: 2025-05-16T02:46:49Z
- **更新时间**: 2025-05-21T15:47:05Z
- **提交者**: @fyuan1316
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 7     910B3vir05_1c_16g   | OK            | 89.8        39                0    / 0             |
| 0                         | 0000:42:00.5  | 0           0    / 0          4713 / 16384         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 7       0                 | 2757          | python3                  | 3552                    |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

I am trying to perform inference with the Qwen2-1.5B model on a Huawei 910B card, and the startup process is getting stuck. 
What are some methods to further diagnose the issue? Thanks.



```python
python3 -m vllm.entrypoints.openai.api_server --port 8080 --served-model-name qwen2_1.5b --model /tmp/qwen2-1.5b --dtype half --gpu-memory-utilization 0.95
```

```bash
INFO 05-12 10:00:10 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-12 10:00:10 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-12 10:00:10 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-12 10:00:10 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 10:00:10 __init__.py:44] plugin ascend loaded.
INFO 05-12 10:00:10 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 05-12 10:00:10 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-12 10:00:10 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-12 10:00:10 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-12 10:00:10 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 10:00:10 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-12 10:00:10 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-12 10:00:10 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-12 10:00:10 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-12 10:00:10 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 05-12 10:00:10 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 05-12 10:00:10 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 05-12 10:00:10 api_server.py:912] vLLM API server version 0.7.3
INFO 05-12 10:00:10 api_server.py:913] args: Namespace(host=None, port=8080, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, enable_reasoning=False, reasoning_parser=None, tool_call_parser=None, tool_parser_plugin='', model='/tmp/qwen2-1.5b', task='auto', tokenizer=None, skip_tokenizer_init=False, revision=None, code_revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path=None, download_dir=None, load_format='auto', config_format=<ConfigFormat.AUTO: 'auto'>, dtype='half', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loading_workers=None, ray_workers_use_nsight=False, block_size=None, enable_prefix_caching=None, disable_sliding_window=False, use_v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.95, num_gpu_blocks_override=None, max_num_batched_tokens=None, max_num_partial_prefills=1, max_long_partial_prefills=1, long_prefill_token_threshold=0, max_num_seqs=None, max_logprobs=20, disable_log_stats=False, quantization=None, rope_scaling=None, rope_theta=None, hf_overrides=None, enforce_eager=False, max_seq_len_to_capture=8192, disable_custom_all_reduce=False, tokenizer_pool_size=0, tokenizer_pool_type='ray', tokenizer_pool_extra_config=None, limit_mm_per_prompt=None, mm_processor_kwargs=None, disable_mm_preprocessor_cache=False, enable_lora=False, enable_lora_bias=False, max_loras=1, max_lora_rank=16, lora_extra_vocab_size=256, lora_dtype='auto', long_lora_scaling_factors=None, max_cpu_loras=None, fully_sharded_loras=False, enable_prompt_adapter=False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_speculative_tokens=None, speculative_disable_mqa_scorer=False, speculative_draft_tensor_parallel_size=None, speculative_max_model_len=None, speculative_disable_by_batch_size=None, ngram_prompt_lookup_max=None, ngram_prompt_lookup_min=None, spec_decoding_acceptance_method='rejection_sampler', typical_acceptance_sampler_posterior_threshold=None, typical_acceptance_sampler_posterior_alpha=None, disable_logprobs_during_spec_decoding=None, model_loader_extra_config=None, ignore_patterns=[], preemption_mode=None, served_model_name=['qwen2_1.5b'], qlora_adapter_name_or_path=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='vllm.core.scheduler.Scheduler', override_neuron_config=None, override_pooler_config=None, compilation_config=None, kv_transfer_config=None, worker_cls='auto', generation_config=None, override_generation_config=None, enable_sleep_mode=False, calculate_kv_scales=False, additional_config=None, disable_log_requests=False, max_log_len=None, disable_fastapi_docs=False, enable_prompt_tokens_details=False)
INFO 05-12 10:00:10 api_server.py:209] Started engine process with PID 2757
WARNING 05-12 10:00:10 config.py:2448] Casting torch.bfloat16 to torch.float16.





INFO 05-12 10:00:19 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-12 10:00:19 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-12 10:00:19 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-12 10:00:19 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-12 10:00:19 __init__.py:44] plugin ascend loaded.
INFO 05-12 10:00:19 __init__.py:198] Platform plugin ascend is activated
WARNING:root:Warning: Failed to register custom ops, all custom ops will be disabled
INFO 05-12 10:00:19 __init__.py:30] Available plugins for group vllm.general_plugins:
    *************************************************************************************************************

INFO 05-12 10:00:19 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-12 10:00:19 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-12 10:00:19 registry.py:351] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-12 10:00:19 registry.py:351] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-12 10:00:19 registry.py:351] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 05-12 10:00:19 registry.py:351] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
INFO 05-12 10:00:19 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-12 10:00:19 config.py:2448] Casting torch.bfloat16 to torch.float16.
INFO 05-12 10:00:21 config.py:549] This model supports multiple tasks: {'embed', 'score', 'reward', 'generate', 'classify'}. Defaulting to 'generate'.



INFO 05-12 10:00:30 config.py:549] This model supports multiple tasks: {'reward', 'score', 'classify', 'generate', 'embed'}. Defaulting to 'generate'.
INFO 05-12 10:00:31 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/tmp/qwen2-1.5b', speculative_config=None, tokenizer='/tmp/qwen2-1.5b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=qwen2_1.5b, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=True,
WARNING 05-12 10:00:31 logger.py:202] VLLM_TRACE_FUNCTION is enabled. It will record every function executed by Python. This will slow down the code. It is suggested to be used for debugging hang or crashes only.
INFO 05-12 10:00:31 logger.py:206] Trace frame log is saved to /tmp/root/vllm/vllm-instance-22a34/VLLM_TRACE_FUNCTION_for_process_2757_thread_281473419130944_at_2025-05-12_10:00:31.815092.log
ERROR 05-12 10:00:31 camem.py:69] Failed to import vllm_ascend_C:No module named 'vllm_ascend.vllm_ascend_C'
/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning:
    *************************************************************************************************************
    The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now..
    The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now..
    The backend in torch.distributed.init_process_group set to hccl now..
    The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now..
    The device parameters have been replaced with npu in the function below:
    torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty
    *************************************************************************************************************

  warnings.warn(msg, ImportWarning)
/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu.
  warnings.warn(msg, RuntimeWarning)
WARNING 05-12 10:00:32 utils.py:2262] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd306f1060>
INFO 05-12 10:00:48 model_runner.py:902] Starting to load model /tmp/qwen2-1.5b...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:03<00:00,  3.73s/it]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:03<00:00,  3.73s/it]

INFO 05-12 10:00:54 model_runner.py:907] Loading model weights took 2.8866 GB
```
