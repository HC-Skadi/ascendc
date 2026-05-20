# Issue #881: [Bug]: [v0.8.5rc1]deepseek v3/r1 w8a8 报错：TypeError: DeepseekV2Attention.forward() got an unexpected keyword argument 'kv_cache'

## 基本信息

- **编号**: #881
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/881
- **创建时间**: 2025-05-16T02:54:48Z
- **关闭时间**: 2025-07-13T09:16:58Z
- **更新时间**: 2025-09-19T06:11:33Z
- **提交者**: @15626471095
- **评论数**: 9

## 标签

bug; module:quantization

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

```python
       vllm serve "/share/model/deepseek-ai/DeepSeek-V3-0324-w8a8" --served-model-name DeepSeek-V3 \
       --trust-remote-code \
       --enforce-eager \
       --distributed_executor_backend "ray" \
       --tensor-parallel-size 8 \
       --pipeline-parallel-size 2 \
       --disable-frontend-multiprocessing \
       --max-model-len 32768 --host 0.0.0.0 --port 8085 --gpu-memory-utilization 0.95
```
```
Loading safetensors checkpoint shards:  96% Completed | 150/157 [32:53<02:57, 25.41s/it]
Loading safetensors checkpoint shards:  96% Completed | 151/157 [32:54<01:47, 17.90s/it]
Loading safetensors checkpoint shards:  97% Completed | 152/157 [32:54<01:02, 12.60s/it]
Loading safetensors checkpoint shards:  97% Completed | 153/157 [33:30<01:18, 19.72s/it]
Loading safetensors checkpoint shards:  98% Completed | 154/157 [33:31<00:41, 13.90s/it]
Loading safetensors checkpoint shards:  99% Completed | 155/157 [33:46<00:28, 14.23s/it]
Loading safetensors checkpoint shards:  99% Completed | 156/157 [33:46<00:10, 10.07s/it]
Loading safetensors checkpoint shards: 100% Completed | 157/157 [34:25<00:00, 18.68s/it]
Loading safetensors checkpoint shards: 100% Completed | 157/157 [34:25<00:00, 13.16s/it]

(RayWorkerWrapper pid=1070) INFO 05-16 10:23:42 [loader.py:458] Loading weights took 2045.67 seconds
(RayWorkerWrapper pid=553, ip=7.242.100.10) INFO 05-16 09:49:32 [parallel_state.py:1004] rank 15 in world size 16 is assigned as DP rank 0, PP rank 1, TP rank 7 [repeated 14x across cluster]
(RayWorkerWrapper pid=1068) INFO 05-16 09:49:32 [model_runner.py:943] Starting to load model /share/model/deepseek-ai/DeepSeek-V3-0324-w8a8... [repeated 14x across cluster]
(RayWorkerWrapper pid=1068) INFO 05-16 09:49:32 [utils.py:106] Hidden layers were unevenly partitioned: [31,30]. This can be manually overridden using the VLLM_PP_LAYER_PARTITION environment variable [repeated 14x across cluster]
(RayWorkerWrapper pid=1078) INFO 05-16 09:49:33 [quantizer.py:88] Using the vLLM Ascend Quantizer version now! [repeated 14x across cluster]
(RayWorkerWrapper pid=1068) INFO 05-16 10:23:43 [model_runner.py:948] Loading model weights took 20.2484 GB
(RayWorkerWrapper pid=1073) INFO 05-16 10:23:49 [loader.py:458] Loading weights took 2052.09 seconds [repeated 2x across cluster]
(RayWorkerWrapper pid=1070) INFO 05-16 10:23:43 [model_runner.py:948] Loading model weights took 20.2484 GB
(RayWorkerWrapper pid=1073) INFO 05-16 10:23:49 [model_runner.py:948] Loading model weights took 20.2484 GB
INFO 05-16 10:24:02 [loader.py:458] Loading weights took 2065.47 seconds
(RayWorkerWrapper pid=1078) INFO 05-16 10:24:03 [loader.py:458] Loading weights took 2065.94 seconds
INFO 05-16 10:24:03 [model_runner.py:948] Loading model weights took 20.2484 GB
(RayWorkerWrapper pid=1078) INFO 05-16 10:24:03 [model_runner.py:948] Loading model weights took 20.2484 GB
(RayWorkerWrapper pid=1080) INFO 05-16 10:24:04 [loader.py:458] Loading weights took 2067.66 seconds
(RayWorkerWrapper pid=1065) INFO 05-16 10:24:09 [model_runner.py:948] Loading model weights took 20.2484 GB [repeated 3x across cluster]
(RayWorkerWrapper pid=489, ip=7.242.100.10) INFO 05-16 10:28:30 [loader.py:458] Loading weights took 2333.18 seconds [repeated 3x across cluster]
(RayWorkerWrapper pid=488, ip=7.242.100.10) INFO 05-16 10:28:31 [model_runner.py:948] Loading model weights took 21.4165 GB
INFO 05-16 10:28:31 [utils.py:106] Hidden layers were unevenly partitioned: [31,30]. This can be manually overridden using the VLLM_PP_LAYER_PARTITION environment variable
(RayWorkerWrapper pid=1078) INFO 05-16 10:28:31 [utils.py:106] Hidden layers were unevenly partitioned: [31,30]. This can be manually overridden using the VLLM_PP_LAYER_PARTITION environment variable
ERROR 05-16 10:28:33 [worker_base.py:620] Error executing method 'determine_num_available_blocks'. This might cause deadlock in distributed execution.
ERROR 05-16 10:28:33 [worker_base.py:620] Traceback (most recent call last):
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
ERROR 05-16 10:28:33 [worker_base.py:620]     return run_method(self, method, args, kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-16 10:28:33 [worker_base.py:620]     return func(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 05-16 10:28:33 [worker_base.py:620]     return func(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 283, in determine_num_available_blocks
ERROR 05-16 10:28:33 [worker_base.py:620]     self.model_runner.profile_run()
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 05-16 10:28:33 [worker_base.py:620]     return func(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1148, in profile_run
ERROR 05-16 10:28:33 [worker_base.py:620]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 05-16 10:28:33 [worker_base.py:620]     return func(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1384, in execute_model
ERROR 05-16 10:28:33 [worker_base.py:620]     hidden_or_intermediate_states = model_executable(
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return self._call_impl(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return forward_call(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 652, in forward
ERROR 05-16 10:28:33 [worker_base.py:620]     hidden_states = self.model(input_ids, positions, kv_caches,
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return self._call_impl(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return forward_call(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 599, in forward
ERROR 05-16 10:28:33 [worker_base.py:620]     hidden_states, residual = layer(
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return self._call_impl(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return forward_call(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 496, in forward
ERROR 05-16 10:28:33 [worker_base.py:620]     hidden_states = self.self_attn(
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return self._call_impl(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 05-16 10:28:33 [worker_base.py:620]     return forward_call(*args, **kwargs)
ERROR 05-16 10:28:33 [worker_base.py:620] TypeError: DeepseekV2Attention.forward() got an unexpected keyword argument 'kv_cache'
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
[rank0]:     sys.exit(main())
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 53, in main
[rank0]:     args.dispatch_function(args)
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 27, in cmd
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
[rank0]:     return loop.run_until_complete(wrapper())
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1078, in run_server
[rank0]:     async with build_async_engine_client(args) as engine_client:
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 194, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_vllm_config(
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/async_llm_engine.py", line 657, in from_vllm_config
[rank0]:     return cls(
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/async_llm_engine.py", line 612, in __init__
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/async_llm_engine.py", line 267, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 278, in __init__
[rank0]:     self._initialize_kv_caches()
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 422, in _initialize_kv_caches
[rank0]:     self.model_executor.determine_num_available_blocks())
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 103, in determine_num_available_blocks
[rank0]:     results = self.collective_rpc("determine_num_available_blocks")
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 331, in collective_rpc
[rank0]:     return self._run_workers(method, *args, **(kwargs or {}))
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 516, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 621, in execute_method
[rank0]:     raise e
[rank0]:   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
[rank0]:     return run_method(self, method, args, kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 283, in determine_num_available_blocks
[rank0]:     self.model_runner.profile_run()
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1148, in profile_run
[rank0]:     self.execute_model(model_input, kv_caches, intermediate_tensors)
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1384, in execute_model
[rank0]:     hidden_or_intermediate_states = model_executable(
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 652, in forward
[rank0]:     hidden_states = self.model(input_ids, positions, kv_caches,
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 599, in forward
[rank0]:     hidden_states, residual = layer(
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 496, in forward
[rank0]:     hidden_states = self.self_attn(
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]: TypeError: DeepseekV2Attention.forward() got an unexpected keyword argument 'kv_cache'
(RayWorkerWrapper pid=492, ip=7.242.100.10) INFO 05-16 10:28:30 [loader.py:458] Loading weights took 2333.21 seconds [repeated 7x across cluster]
(RayWorkerWrapper pid=490, ip=7.242.100.10) INFO 05-16 10:28:31 [model_runner.py:948] Loading model weights took 21.4165 GB [repeated 7x across cluster]
(RayWorkerWrapper pid=1068) INFO 05-16 10:28:31 [utils.py:106] Hidden layers were unevenly partitioned: [31,30]. This can be manually overridden using the VLLM_PP_LAYER_PARTITION environment variable [repeated 6x across cluster]
[ERROR] 2025-05-16-10:28:38 (PID:886, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
INFO 05-16 10:28:38 [ray_distributed_executor.py:127] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
INFO 05-16 10:28:38 [ray_distributed_executor.py:127] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
/usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

```
