# Issue #1120: [Main][Bug]: Failed to start server with V1 enable due to `No module named 'numba'`

## 基本信息

- **编号**: #1120
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1120
- **创建时间**: 2025-06-07T23:19:16Z
- **关闭时间**: 2025-06-08T14:33:39Z
- **更新时间**: 2025-06-08T14:33:39Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

vLLM Main 0.9.0
vLLM Ascend
```
# Update DEVICE according to your device (/dev/davinci[0-7])
export DEVICE=/dev/davinci4
# Update the vllm-ascend image
#export IMAGE=m.daocloud.io/quay.io/ascend/cann:8.1.rc1-910b-ubuntu22.04-py3.10
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:main
docker run --rm \
--name yikun-test \
--device $DEVICE \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-it $IMAGE bash

root@36a3e418f3b6:/workspace# export MODEL=Qwen/Qwen2.5-7B-Instruct
root@36a3e418f3b6:/workspace# export VLLM_USE_MODELSCOPE=true
root@36a3e418f3b6:/workspace# VLLM_USE_V1=1 VLLM_USE_MODELSCOPE=true python3 -m vllm.entrypoints.openai.api_server --model $MODEL \
         --tensor-parallel-size 1 --swap-space 16 --disable-log-stats \
         --disable-log-requests  --load-format dummy

```

### 🐛 Describe the bug

```
INFO 06-07 23:04:52 [core.py:65] Initializing a V1 LLM engine (v0.9.0) with config: model='Qwen/Qwen2.5-7B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2.5-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=dummy, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen2.5-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level": 3, "custom_ops": ["all"], "splitting_ops": ["vllm.unified_attention", "vllm.unified_attention_with_output", "vllm.unified_ascend_attention_with_output", "vllm.unified_ascend_attention_with_output"], "use_inductor": false, "compile_sizes": [], "use_cudagraph": true, "cudagraph_num_of_warmups": 1, "cudagraph_capture_sizes": [512, 504, 496, 488, 480, 472, 464, 456, 448, 440, 432, 424, 416, 408, 400, 392, 384, 376, 368, 360, 352, 344, 336, 328, 320, 312, 304, 296, 288, 280, 272, 264, 256, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64, 56, 48, 40, 32, 24, 16, 8, 4, 2, 1], "max_capture_size": 512}
ERROR 06-07 23:04:52 [core.py:500] EngineCore failed to start.
ERROR 06-07 23:04:52 [core.py:500] Traceback (most recent call last):
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 491, in run_engine_core
ERROR 06-07 23:04:52 [core.py:500]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 390, in __init__
ERROR 06-07 23:04:52 [core.py:500]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 71, in __init__
ERROR 06-07 23:04:52 [core.py:500]     self.model_executor = executor_class(vllm_config)
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 06-07 23:04:52 [core.py:500]     self._init_executor()
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 45, in _init_executor
ERROR 06-07 23:04:52 [core.py:500]     self.collective_rpc("init_worker", args=([kwargs], ))
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 06-07 23:04:52 [core.py:500]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/utils.py", line 2605, in run_method
ERROR 06-07 23:04:52 [core.py:500]     return func(*args, **kwargs)
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 558, in init_worker
ERROR 06-07 23:04:52 [core.py:500]     worker_class = resolve_obj_by_qualname(
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/utils.py", line 2191, in resolve_obj_by_qualname
ERROR 06-07 23:04:52 [core.py:500]     module = importlib.import_module(module_name)
ERROR 06-07 23:04:52 [core.py:500]   File "/usr/local/python3.10.17/lib/python3.10/importlib/__init__.py", line 126, in import_module
ERROR 06-07 23:04:52 [core.py:500]     return _bootstrap._gcd_import(name[level:], package, level)
ERROR 06-07 23:04:52 [core.py:500]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
ERROR 06-07 23:04:52 [core.py:500]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
ERROR 06-07 23:04:52 [core.py:500]   File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
ERROR 06-07 23:04:52 [core.py:500]   File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
ERROR 06-07 23:04:52 [core.py:500]   File "<frozen importlib._bootstrap_external>", line 883, in exec_module
ERROR 06-07 23:04:52 [core.py:500]   File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 47, in <module>
ERROR 06-07 23:04:52 [core.py:500]     from vllm_ascend.worker.model_runner_v1 import NPUModelRunner
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 62, in <module>
ERROR 06-07 23:04:52 [core.py:500]     from vllm.v1.spec_decode.ngram_proposer import NgramProposer
ERROR 06-07 23:04:52 [core.py:500]   File "/vllm-workspace/vllm/vllm/v1/spec_decode/ngram_proposer.py", line 5, in <module>
ERROR 06-07 23:04:52 [core.py:500]     from numba import jit
ERROR 06-07 23:04:52 [core.py:500] ModuleNotFoundError: No module named 'numba'
```
