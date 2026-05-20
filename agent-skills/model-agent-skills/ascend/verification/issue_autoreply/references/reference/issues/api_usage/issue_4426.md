# Issue #4426: [Bug report]: vLLM server fails when using "cudagraph_mode": "FULL_DECODE_ONLY" mode with command "curl *****/v1/completions"

## 基本信息

- **编号**: #4426
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4426
- **创建时间**: 2025-11-25T07:29:30Z
- **关闭时间**: 2025-12-02T01:22:06Z
- **更新时间**: 2025-12-02T01:22:06Z
- **提交者**: @ZhaoJiangJiang
- **评论数**: 14

## 标签

无

## 问题描述

### Your current environment
```
Chips：910B2
Collecting environment information... 
============================== 
        System Info 
============================== 
OS : openEuler 24.03 (LTS) (aarch64) 
GCC version : (GCC) 12.3.1 (openEuler 12.3.1-38.oe2403) 
Clang version : Could not collect 
CMake version : version 4.1.2 
Libc version : glibc-2.38 
============================== 
       PyTorch Info 
============================== 
PyTorch version : 2.7.1+cpu 
Is debug build : False 
CUDA used to build PyTorch : None 
ROCM used to build PyTorch : N/A 
============================== 
      Python Environment 
============================== 
Python version : 3.11.10 (main, Nov 5 2025, 11:58:39) [GCC 12.3.1 (openEuler 12.3.1-38.oe2403)] (64-bit runtime) 
Python platform : Linux-4.19.90-2102.2.0.0068.3.ctl2.aarch64-aarch64-with-glibc2.38 
============================== 
       CUDA / GPU Info 
============================== 
Is CUDA available : False 
CUDA runtime version : No CUDA 
CUDA_MODULE_LOADING set to : N/A 
GPU models and configuration : No CUDA 
Nvidia driver version : No CUDA 
cuDNN version : No CUDA 
HIP runtime version : N/A 
MIOpen runtime version : N/A 
Is XNNPACK available : True 
============================== 
          CPU Info 
============================== 
Architecture: aarch64 
CPU op-mode(s): 64-bit 
Byte Order: Little Endian 
CPU(s): 192 
On-line CPU(s) list: 0-191 
Vendor ID: HiSilicon 
Model name: Kunpeng-920 
Model: 0 
Thread(s) per core: 1 
Core(s) per cluster: 48 
Socket(s): - 
Cluster(s): 4 
Stepping: 0x1 
BogoMIPS: 200.00 
Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs 
L1d cache: 12 MiB (192 instances) 
L1i cache: 12 MiB (192 instances) 
L2 cache: 96 MiB (192 instances) 
L3 cache: 192 MiB (8 instances) 
NUMA node(s): 4 
NUMA node0 CPU(s): 0-47 
NUMA node1 CPU(s): 48-95 
NUMA node2 CPU(s): 96-143 
NUMA node3 CPU(s): 144-191 
Vulnerability Itlb multihit: Not affected 
Vulnerability L1tf: Not affected 
Vulnerability Mds: Not affected 
Vulnerability Meltdown: Not affected 
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl 
Vulnerability Spectre v1: Mitigation; __user pointer sanitization 
Vulnerability Spectre v2: Not affected 
Vulnerability Srbds: Not affected 
Vulnerability Tsx async abort: Not affected 
============================== 
Versions of relevant libraries 
============================== 
[pip3] numpy==1.26.4 
[pip3] pyzmq==27.1.0 
[pip3] torch==2.7.1 
[pip3] torch_npu==2.7.1 
[pip3] torchvision==0.22.1 
[pip3] transformers==4.57.1 
[conda] Could not collect 
============================== 
         vLLM Info 
============================== 
ROCM Version : Could not collect 
vLLM Version : 0.11.0 
vLLM Build Flags: 
  CUDA Archs: Not Set; ROCm: Disabled 
GPU Topology: 
  Could not collect 
============================== 
     Environment Variables 
============================== 
LOCAL_RANK=0,1,2,3,4,5,6,7 
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/::/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib 
VLLM_USE_V1=1 
TORCH_DEVICE_BACKEND_AUTOLOAD=1 
PYTORCH_NVML_BASED_CUDA_CHECK=1 
TORCHINDUCTOR_COMPILE_THREADS=1 
```


# version: 
vllm: 0.11.0+empty
vllm-ascend: 0.11.0rc1.dev186+g66b67f9cf

# Model：Telecom customer's self-developed model similar to DeepSeekV3

# Server Script：
```
export HCCL_IF_IP=$(ifconfig | grep '10.127.' | awk '{print $2}')
export HCCL_BUFFSIZE=512
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export VLLM_USE_V1=1
export VLLM_ENABLE_MC2=1
export HCCL_DETERMINISTIC=true
export CLOSE_MATMUL_K_SHIFT=1

weight_path=/data01/huawei-2025/lfk/convert/1106/tele-105b_hf/

python -m vllm.entrypoints.openai.api_server --model $weight_path --served-model-name deepseekv3 --trust-remote-code --max-num-seqs 128 -dp 2 -tp 4 --enable_expert_parallel --port 8005 --max_model_len 4096 --max-num-batched-tokens 4096 --gpu-memory_utilization 0.9 --no-enable-prefix-caching --compilation-config '{"cudagraph_capture_sizes": [1,4,8,16,32,64,128],"cudagraph_mode": "FULL_DECODE_ONLY"}' 
```

# Custom Script：
```
curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"model": "deepseekv3","prompt":  "生抽和老抽的区别","max_tokens": 50}' http://10.127.44.181:8005/v1/completions
```

# Problem phenomenon：
```
(APIServer pid=16762) INFO:     Started server process [16762]
(APIServer pid=16762) INFO:     Waiting for application startup.
(APIServer pid=16762) INFO:     Application startup complete.
[rank0]:[W1125 12:01:16.203927339 compiler_depend.ts:117] Warning: Driver Version:  is invalid or not supported yet. (function operator())
[rank2]:[W1125 12:01:16.203955549 compiler_depend.ts:117] Warning: Driver Version:  is invalid or not supported yet. (function operator())
[rank1]:[W1125 12:01:16.204246359 compiler_depend.ts:117] Warning: Driver Version:  is invalid or not supported yet. (function operator())
[rank3]:[W1125 12:01:16.204438979 compiler_depend.ts:117] Warning: Driver Version:  is invalid or not supported yet. (function operator())
(Worker_DP1_TP1_EP5 pid=17315) INFO 11-25 12:01:16 [acl_graph.py:187] Replaying aclgraph
(Worker_DP1_TP0_EP4 pid=17312) INFO 11-25 12:01:16 [acl_graph.py:187] Replaying aclgraph
(Worker_DP1_TP2_EP6 pid=17317) INFO 11-25 12:01:16 [acl_graph.py:187] Replaying aclgraph
(Worker_DP1_TP3_EP7 pid=17318) INFO 11-25 12:01:16 [acl_graph.py:187] Replaying aclgraph
(EngineCore_DP0 pid=16899) INFO 11-25 12:02:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP1 pid=16900) INFO 11-25 12:02:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP0 pid=16899) INFO 11-25 12:03:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP1 pid=16900) INFO 11-25 12:03:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP0 pid=16899) INFO 11-25 12:04:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP1 pid=16900) INFO 11-25 12:04:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP0 pid=16899) INFO 11-25 12:05:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP1 pid=16900) INFO 11-25 12:05:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.0) with config: model='/data01/huawei-2025/lfk/convert/1106/tele-105b_hf/', speculative_config=None, tokenizer='/data01/huawei-2025/lfk/convert/1106/tele-105b_hf/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=2, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=deepseekv3, enable_prefix_caching=False, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.sparse_attn_indexer"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":[2,0],"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[128,64,32,16,8,4,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":128,"local_cache_dir":null}, 
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [dump_input.py:76] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=cmpl-ccefa5715fc040ee86b8e410a3126229-0,prompt_token_ids_len=5,mm_features=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[1], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=50, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None,prompt_embeds_shape=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={cmpl-ccefa5715fc040ee86b8e410a3126229-0: 5}, total_num_scheduled_tokens=5, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[0], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=1, num_waiting_reqs=0, step_counter=0, current_wave=0, kv_cache_usage=0.00021758050478681845, prefix_cache_stats=PrefixCacheStats(reset=False, requests=0, queries=0, hits=0), spec_decoding_stats=None, kv_connector_stats=None, num_corrupted_reqs=0)
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] Traceback (most recent call last):
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 244, in get_response
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     status, result = w.worker_response_mq.dequeue(
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/distributed/device_communicators/shm_broadcast.py", line 511, in dequeue
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     with self.acquire_read(timeout, cancel, indefinite) as buf:
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/contextlib.py", line 137, in __enter__
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     return next(self.gen)
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]            ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/distributed/device_communicators/shm_broadcast.py", line 460, in acquire_read
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     raise TimeoutError
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] TimeoutError
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] 
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] The above exception was the direct cause of the following exception:
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] 
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] Traceback (most recent call last):
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 701, in run_engine_core
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 1045, in run_busy_loop
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     executed = self._process_engine_step()
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 754, in _process_engine_step
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 284, in step
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     model_output = self.execute_model_with_error_logging(
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 270, in execute_model_with_error_logging
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     raise err
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 261, in execute_model_with_error_logging
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     return model_fn(scheduler_output)
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 181, in execute_model
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     (output, ) = self.collective_rpc(
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]                  ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 273, in collective_rpc
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710]     raise TimeoutError(f"RPC call to {method} timed out.") from e
(EngineCore_DP0 pid=16899) ERROR 11-25 12:06:16 [core.py:710] TimeoutError: RPC call to execute_model timed out.
(Worker_DP0_TP1_EP1 pid=17313) INFO 11-25 12:06:16 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP0_TP0_EP0 pid=17311) INFO 11-25 12:06:16 [multiproc_executor.py:558] Parent process exited, terminating worker
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480] AsyncLLM output_handler failed.
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480] Traceback (most recent call last):
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/async_llm.py", line 439, in output_handler
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480]     outputs = await engine_core.get_output_async()
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/engine/core_client.py", line 846, in get_output_async
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480]     raise self._format_exception(outputs) from None
(Worker_DP0_TP2_EP2 pid=17316) INFO 11-25 12:06:16 [multiproc_executor.py:558] Parent process exited, terminating worker
(APIServer pid=16762) ERROR 11-25 12:06:16 [async_llm.py:480] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
(APIServer pid=16762) INFO:     10.127.18.3:46644 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error
(Worker_DP0_TP3_EP3 pid=17319) INFO 11-25 12:06:16 [multiproc_executor.py:558] Parent process exited, terminating worker
(EngineCore_DP1 pid=16900) INFO 11-25 12:06:16 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation).
(APIServer pid=16762) INFO:     Shutting down
(APIServer pid=16762) INFO:     Waiting for application shutdown.
(APIServer pid=16762) INFO:     Application shutdown complete.
(APIServer pid=16762) INFO:     Finished server process [16762]
(Worker_DP1_TP0_EP4 pid=17312) INFO 11-25 12:06:19 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP1_TP1_EP5 pid=17315) INFO 11-25 12:06:19 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP1_TP2_EP6 pid=17317) INFO 11-25 12:06:19 [multiproc_executor.py:558] Parent process exited, terminating worker
(Worker_DP1_TP3_EP7 pid=17318) INFO 11-25 12:06:19 [multiproc_executor.py:558] Parent process exited, terminating worker
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
```

# Other Information：
* If the promgram `--compilation-config` in server script as `'{"cudagraph_capture_sizes": [1,4,8,16,32,64,128]}'`, （no to use `"cudagraph_mode": "FULL_DECODE_ONLY"}`），there would be no such problem；
* If we continue to use `--compilation-config '{"cudagraph_capture_sizes": [1,4,8,16,32,64,128],"cudagraph_mode": "FULL_DECODE_ONLY"}' `，but set `--max-num-seqs` from `128` to `1`, there won't be this problem either 

### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

