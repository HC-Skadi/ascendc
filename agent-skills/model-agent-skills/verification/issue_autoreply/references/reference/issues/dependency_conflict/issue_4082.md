# Issue #4082: [Bug]: 使用最新镜像部署Qwen3-VL-32B-Instruct，有显存泄露现象

## 基本信息

- **编号**: #4082
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4082
- **创建时间**: 2025-11-10T04:54:54Z
- **关闭时间**: 2025-11-18T00:19:19Z
- **更新时间**: 2026-01-26T12:19:10Z
- **提交者**: @ponyioy
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>部署脚本</summary>

```text

services:
  qwen3-vl-32b:
    image: quay.io/ascend/vllm-ascend:v0.11.0-dev-openeuler
    container_name: qwen3-vl-32b
    privileged: true
    devices:
      - /dev/davinci_manager
      - /dev/devmm_svm
      - /dev/hisi_hdc
    volumes:
      - /usr/local/dcmi:/usr/local/dcmi
      - /usr/local/bin/npu-smi:/usr/local/bin/npu-smi
      - /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/
      - /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info
      - /etc/ascend_install.info:/etc/ascend_install.info
      - /Model:/root/.cache
    ports:
      - "8000:8000"
    environment:
      - ASCEND_RT_VISIBLE_DEVICES=4,5,6,7
      - TZ=Asia/Shanghai
    command:
      - vllm
      - serve
      - /root/.cache/Qwen3-VL-32B-Instruct
      - --served-model-name
      - vl_model
      - --tensor-parallel-size
      - "4"
      - --max-model-len
      - "131072"
    stdin_open: true
    tty: true

```

</details>


### 🐛 Describe the bug

一开始可以正常运行，但是一段时间之后就会爆显存溢出，
观察到的现象是显存不断增加，并不回收。

'''
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.0) with config: model='/root/.cache/Qwen3-VL-32B-Instruct', speculative_config=None, tokenizer='/root/.cache/Qwen3-VL-32B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=vl_model, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.sparse_attn_indexer","vllm.unified_ascend_attention_with_output","vllm.mla_forward","vllm.unified_ascend_attention_with_output","vllm.mla_forward"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,448,384,312,248,184,112,48,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null},
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [dump_input.py:76] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[], scheduled_cached_reqs=CachedRequestData(req_ids=['chatcmpl-cb6879fbe6b74ce78cd503177250b007'], resumed_from_preemption=[false], new_token_ids=[], new_block_ids=[[[1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073]]], num_computed_tokens=[12288]), num_scheduled_tokens={chatcmpl-cb6879fbe6b74ce78cd503177250b007: 2048}, total_num_scheduled_tokens=2048, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={chatcmpl-cb6879fbe6b74ce78cd503177250b007: [1]}, num_common_prefix_blocks=[112], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=1, num_waiting_reqs=0, step_counter=0, current_wave=0, kv_cache_usage=0.023559108119478367, prefix_cache_stats=PrefixCacheStats(reset=False, requests=0, queries=0, hits=0), spec_decoding_stats=None, kv_connector_stats=None, num_corrupted_reqs=0)
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710] EngineCore encountered a fatal error.
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710] Traceback (most recent call last):
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 701, in run_engine_core
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     engine_core.run_busy_loop()
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 728, in run_busy_loop
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     self._process_engine_step()
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 754, in _process_engine_step
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     outputs, model_executed = self.step_fn()
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]                               ^^^^^^^^^^^^^^
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 284, in step
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     model_output = self.execute_model_with_error_logging(
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 270, in execute_model_with_error_logging
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     raise err
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 261, in execute_model_with_error_logging
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     return model_fn(scheduler_output)
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 181, in execute_model
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     (output, ) = self.collective_rpc(
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]                  ^^^^^^^^^^^^^^^^^^^^
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     result = get_response(w, dequeue_timeout,
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710]     raise RuntimeError(
qwen3-vl-32b  | (EngineCore_DP0 pid=413) ERROR 11-10 12:30:57 [core.py:710] RuntimeError: Worker failed with error 'NPU out of memory. Tried to allocate 326.00 MiB (NPU 0; 60.96 GiB total capacity; 57.81 GiB already allocated; 57.81 GiB current active; 6.76 MiB free; 58.78 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.', please check the stack trace above for the root cause
qwen3-vl-32b  | (Worker_TP0 pid=549) INFO 11-10 12:30:57 [multiproc_executor.py:558] Parent process exited, terminating worker
qwen3-vl-32b  | (Worker_TP0 pid=549) INFO 11-10 12:30:57 [multiproc_executor.py:599] WorkerProc shutting down.
qwen3-vl-32b  | (Worker_TP1 pid=550) INFO 11-10 12:30:57 [multiproc_executor.py:558] Parent process exited, terminating worker
qwen3-vl-32b  | (Worker_TP1 pid=550) INFO 11-10 12:30:57 [multiproc_executor.py:599] WorkerProc shutting down.
qwen3-vl-32b  | (Worker_TP2 pid=551) INFO 11-10 12:30:57 [multiproc_executor.py:558] Parent process exited, terminating worker
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480] AsyncLLM output_handler failed.
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480] Traceback (most recent call last):
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 439, in output_handler
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480]     outputs = await engine_core.get_output_async()
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 846, in get_output_async
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480]     raise self._format_exception(outputs) from None
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [async_llm.py:480] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
qwen3-vl-32b  | (Worker_TP2 pid=551) INFO 11-10 12:30:57 [multiproc_executor.py:599] WorkerProc shutting down.
qwen3-vl-32b  | (Worker_TP3 pid=552) INFO 11-10 12:30:57 [multiproc_executor.py:558] Parent process exited, terminating worker
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145] Error in chat completion stream generator.
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145] Traceback (most recent call last):
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]   File "/vllm-workspace/vllm/vllm/entrypoints/openai/serving_chat.py", line 574, in chat_completion_stream_generator
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]     async for res in result_generator:
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 387, in generate
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]     out = q.get_nowait() or await q.get()
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]                             ^^^^^^^^^^^^^
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]   File "/vllm-workspace/vllm/vllm/v1/engine/output_processor.py", line 59, in get
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]     raise output
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 439, in output_handler
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]     outputs = await engine_core.get_output_async()
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 846, in get_output_async
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145]     raise self._format_exception(outputs) from None
qwen3-vl-32b  | (APIServer pid=1) ERROR 11-10 12:30:57 [serving_chat.py:1145] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
qwen3-vl-32b  | (Worker_TP3 pid=552) INFO 11-10 12:30:57 [multiproc_executor.py:599] WorkerProc shutting down.


'''
