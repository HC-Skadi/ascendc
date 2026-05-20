# Issue #109: AssertionError: Error in memory profiling

## 基本信息

- **编号**: #109
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/109
- **创建时间**: 2025-02-19T11:35:56Z
- **关闭时间**: 2025-02-21T09:10:39Z
- **更新时间**: 2025-02-24T06:46:04Z
- **提交者**: @dawnranger
- **评论数**: 4

## 标签

bug

## 问题描述

# INSTALL
```
python3 -m pip install --no-cache-dir --upgrade pip
# torch2.5.1+cpu & torch_npu2.5.1rc1
pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
pip install torch-npu==2.5.1rc1

# vllm 0.7.1
git clone --depth 1 --branch v0.7.1 https://github.com/vllm-project/vllm && \
    cd vllm && VLLM_TARGET_DEVICE=empty pip install . -f https://download.pytorch.org/whl/torch/ && cd ..
# vllm_ascend
git clone  --depth 1 --branch main https://github.com/vllm-project/vllm-ascend.git && \
    cd vllm-ascend && git checkout fafd70e91c4f1214c2d3f4ba649e2d631a293354 && \
    pip install -e . -f https://download.pytorch.org/whl/torch/ && cd ..

# trl
git clone --depth 1 --branch npu https://github.com/ji-huazhong/trl && \
    cd trl && git checkout 03ef32c26c6cf2a14dcf8fff4f58aae81404a0ba && \
    pip install -e . -f https://download.pytorch.org/whl/torch/ && cd ..
```

# REPRODUCE
according to : https://github.com/huggingface/open-r1/pull/303
```
source /usr/local/Ascend/ascend-toolkit/set_env.sh
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_RDMA_TIMEOUT=20
export CUDA_DEVICE_MAX_CONNECTIONS=1
export TASK_QUEUE_ENABLE=2
export COMBINED_ENABLE=1
export CPU_AFFINITY_CONF=1
export HCCL_CONNECT_TIMEOUT=1800
export HCCL_EVENT_TIMEOUT=1800
export HCCL_EXEC_TIMEOUT=1800
export NPU_ASD_ENABLE=0
export ASCEND_LAUNCH_BLOCKING=1
export ACLNN_CACHE_LIMIT=100000
export ASCEND_SLOG_PRINT_TO_STDOUT=0
export ASCEND_GLOBAL_LOG_LEVEL=0
export ASCEND_GLOBAL_EVENT_ENABLE=1

pkill -9 python3
sleep 10s

ACCELERATE_LOG_LEVEL=info accelerate launch --config_file recipes/accelerate_configs/zero2.yaml \
--num_processes=7 src/open_r1/grpo.py \
--config recipes/Qwen2.5-1.5B-Instruct/grpo/config_demo.yaml
```

# ENVIRONMENT
- `npu-smi info`
![Image](https://github.com/user-attachments/assets/1ccd5a2d-e140-4d4d-a62d-c32d4b8358c1)

- cann info
![Image](https://github.com/user-attachments/assets/cecb4a70-9646-4f86-8cd8-d804f2608cc8)


- pip list
```
absl-py                           2.1.0
accelerate                        1.4.0
apex                              0.1
ascendebug                        0.1.0
ascendie                          1.0rc3
datasets                          3.3.1
deepspeed                         0.15.4
docker-pycreds                    0.4.0
einops                            0.8.1
fastapi                           0.115.8
h11                               0.14.0
h5py                              3.13.0
hccl                              0.1.0
hccl_parser                       0.1
hf_transfer                       0.1.9
huggingface-hub                   0.28.1
latex2sympy2_extended             1.0.6
lighteval                         0.6.0.dev0
llm_datadist                      0.0.1
llm_manager_python_api_demo       1.0rc3
lm-format-enforcer                0.10.10
math-verify                       0.5.2
mies_tokenizer                    0.0.1
mindie_llm                        1.0rc3
mindiebenchmark                   1.0rc3
mindieclient                      1.0rc3
mindiesd                          1.0rc3
mindietorch                       1.0rc3+torch2.1.0.abi0
nltk                              3.9.1
numpy                             1.26.4
nvidia-ml-py                      12.555.43
openai                            1.63.2
pandas                            2.2.2
pip                               24.0
protobuf                          3.20.3
pydantic                          2.10.6
pydantic_core                     2.27.2
ray                               2.42.1
rouge-score                       0.1.2
sacrebleu                         2.5.1
safetensors                       0.4.3
seqeval                           1.2.2
torch                             2.5.1+cpu
torch-npu                         2.5.1rc1
torchaudio                        2.5.1+cpu
torchvision                       0.20.1+cpu
tornado                           6.4.1
transformers                      4.50.0.dev0
trl                               0.16.0.dev0            /root/trl
typing_extensions                 4.12.2
universal_pathlib                 0.2.6
urllib3                           2.3.0
vllm                              0.7.1+empty
vllm_ascend                       0.1.dev1+gfafd70e      /root/vllm-ascend
wandb                             0.17.5
```

# FULL LOG
```
[WARNING|logging.py:329] 2025-02-19 11:10:43,219 >> Sliding Window Attention is enabled but not implemented for `sdpa`; unexpected results may be encountered.
/usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/utils/storage.py:38: UserWarning: TypedStorage is deprecated. It will be removed in the future and UntypedStorage will be the only storage class. This should only matter to you if you are using storages directly.  To access UntypedStorage directly, use tensor.untyped_storage() instead of tensor.storage()
  if self.device.type != 'cpu':
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:10:57,013 >> loading file vocab.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:10:57,014 >> loading file merges.txt
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:10:57,014 >> loading file tokenizer.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:10:57,014 >> loading file added_tokens.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:10:57,014 >> loading file special_tokens_map.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:10:57,014 >> loading file tokenizer_config.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:10:57,014 >> loading file chat_template.jinja
[INFO|tokenization_utils_base.py:2313] 2025-02-19 11:10:57,312 >> Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
2025-02-19 11:10:57 - WARNING - accelerate.utils.other - Detected kernel version 5.4.241, which is below the recommended minimum of 5.5.0; this can cause the process to hang. It is recommended to upgrade the kernel to the minimum version or higher.
[INFO|trainer.py:748] 2025-02-19 11:10:57,336 >> Using auto half precision backend
[INFO|configuration_utils.py:697] 2025-02-19 11:10:57,835 >> loading configuration file Qwen/Qwen2.5-1.5B-Instruct/config.json
[INFO|configuration_utils.py:697] 2025-02-19 11:10:57,836 >> loading configuration file Qwen/Qwen2.5-1.5B-Instruct/config.json
[INFO|configuration_utils.py:771] 2025-02-19 11:10:57,837 >> Model config Qwen2Config {
  "_name_or_path": "Qwen/Qwen2.5-1.5B-Instruct",
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151645,
  "hidden_act": "silu",
  "hidden_size": 1536,
  "initializer_range": 0.02,
  "intermediate_size": 8960,
  "max_position_embeddings": 32768,
  "max_window_layers": 21,
  "model_type": "qwen2",
  "num_attention_heads": 12,
  "num_hidden_layers": 28,
  "num_key_value_heads": 2,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 1000000.0,
  "sliding_window": 32768,
  "tie_word_embeddings": true,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.50.0.dev0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

[INFO|image_processing_auto.py:301] 2025-02-19 11:10:57,840 >> Could not locate the image processor configuration file, will try to use the model config instead.
INFO 02-19 11:11:04 config.py:526] This model supports multiple tasks: {'classify', 'embed', 'reward', 'score', 'generate'}. Defaulting to 'generate'.
INFO 02-19 11:11:04 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='Qwen/Qwen2.5-1.5B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-1.5B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu:7, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=Qwen/Qwen2.5-1.5B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False, 
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:11:04,416 >> loading file vocab.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:11:04,416 >> loading file merges.txt
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:11:04,416 >> loading file tokenizer.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:11:04,416 >> loading file added_tokens.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:11:04,416 >> loading file special_tokens_map.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:11:04,416 >> loading file tokenizer_config.json
[INFO|tokenization_utils_base.py:2048] 2025-02-19 11:11:04,416 >> loading file chat_template.jinja
[INFO|tokenization_utils_base.py:2313] 2025-02-19 11:11:04,651 >> Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
[INFO|configuration_utils.py:1093] 2025-02-19 11:11:04,722 >> loading configuration file Qwen/Qwen2.5-1.5B-Instruct/generation_config.json
[INFO|configuration_utils.py:1140] 2025-02-19 11:11:04,722 >> Generate config GenerationConfig {
  "bos_token_id": 151643,
  "do_sample": true,
  "eos_token_id": [
    151645,
    151643
  ],
  "pad_token_id": 151643,
  "repetition_penalty": 1.1,
  "temperature": 0.7,
  "top_k": 20,
  "top_p": 0.8
}

/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py:27: UserWarning: Failed to get the IP address, using 0.0.0.0 by default.The value can be set by the environment variable VLLM_HOST_IP or HOST_IP.
  get_ip(), get_open_port())
WARNING 02-19 11:11:04 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-19 11:11:04 importing.py:14] Triton not installed or not compatible; certain GPU-related functions will not be available.
2025-02-19 11:11:04 - INFO - vllm_ascend.model_runner - Starting to load model Qwen/Qwen2.5-1.5B-Instruct...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.73it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  4.72it/s]

2025-02-19 11:11:05 - INFO - vllm_ascend.model_runner - Loading model weights took 0.0000 GB
[rank0]: Traceback (most recent call last):
[rank0]:   File "/root/open-r1/src/run_grpo.py", line 9, in <module>
[rank0]:     main()
[rank0]:   File "/root/open-r1/src/run_grpo.py", line 6, in main
[rank0]:     run_exp()
[rank0]:   File "/root/open-r1/src/open_r1/grpo.py", line 263, in run_exp
[rank0]:     main(script_args, training_args, model_args)
[rank0]:   File "/root/open-r1/src/open_r1/grpo.py", line 206, in main
[rank0]:     trainer = GRPOTrainer(
[rank0]:   File "/root/trl/trl/trainer/grpo_trainer.py", line 442, in __init__
[rank0]:     self.llm = LLM(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/utils.py", line 1039, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 240, in __init__
[rank0]:     self.llm_engine = self.engine_class.from_engine_args(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 482, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 274, in __init__
[rank0]:     self._initialize_kv_caches()
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 414, in _initialize_kv_caches
[rank0]:     self.model_executor.determine_num_available_blocks())
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 99, in determine_num_available_blocks
[rank0]:     results = self.collective_rpc("determine_num_available_blocks")
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 49, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/root/vllm-ascend/vllm_ascend/worker.py", line 234, in determine_num_available_blocks
[rank0]:     assert peak_memory > 0, (
[rank0]: AssertionError: Error in memory profiling. Initial free memory 65104437248, current free memory 65104437248. This happens when the NPU memory was not properly cleaned up before initializing the vLLM instance.
[ERROR] 2025-02-19-11:11:09 (PID:32938, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
W0219 11:11:13.040000 32796 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 32939 closing signal SIGTERM
W0219 11:11:13.041000 32796 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 32940 closing signal SIGTERM
W0219 11:11:13.042000 32796 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 32941 closing signal SIGTERM
W0219 11:11:13.044000 32796 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 32942 closing signal SIGTERM
W0219 11:11:13.045000 32796 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 32943 closing signal SIGTERM
W0219 11:11:13.046000 32796 site-packages/torch/distributed/elastic/multiprocessing/api.py:897] Sending process 32944 closing signal SIGTERM
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.10.14/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
E0219 11:11:13.846000 32796 site-packages/torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 0 (pid: 32938) of binary: /usr/local/python3.10.14/bin/python3.10
Traceback (most recent call last):
  File "/usr/local/python3.10.14/bin/accelerate", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/commands/accelerate_cli.py", line 48, in main
    args.func(args)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/commands/launch.py", line 1182, in launch_command
    deepspeed_launcher(args)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/commands/launch.py", line 861, in deepspeed_launcher
    distrib_run.run(args)
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/distributed/run.py", line 910, in run
    elastic_launch(
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
src/run_grpo.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2025-02-19_11:11:13
  host      : pytorch-938790778-master-0
  rank      : 0 (local_rank: 0)
  exitcode  : 1 (pid: 32938)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
[ERROR] 2025-02-19-11:11:13 (PID:32796, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
