# Issue #986: [Bug]: fail to start W8A8 deepseek-R1 with vllm-ascend:v0.8.5rc1

## 基本信息

- **编号**: #986
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/986
- **创建时间**: 2025-05-28T08:22:26Z
- **关闭时间**: 2025-11-11T13:14:35Z
- **更新时间**: 2026-01-19T03:28:28Z
- **提交者**: @wzh5516
- **评论数**: 7

## 标签

bug

## 问题描述

### Your current environment

install guide doc: https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi_node.html

vllm image:  quay.io/ascend/vllm-ascend:v0.8.5rc1-openeuler

vllm start cmd: python -m vllm.entrypoints.openai.api_server \
       --model="/home/deepseek/Deepseek-R1-W8A8" \
       --served-model-name DeepSeek-R1-w8a8 \
       --trust-remote-code \
       --enforce-eager \
       --distributed_executor_backend "ray" \
       --tensor-parallel-size 8 \
       --pipeline-parallel-size 2 \
       --disable-frontend-multiprocessing \
       --port 8000

model download ui: https://modelers.cn/models/State_Cloud/Deepseek-R1-bf16-hfd-w8a8

according to the issus(https://github.com/vllm-project/vllm-ascend/issues/856) ,put quant_model_description.json to config.json ,but still has issue.





### 🐛 Describe the bug

logs:

INFO 05-28 03:53:31 [model_runner.py:943] Starting to load model /home/deepseek/Deepseek-R1-bf16-hfd-w8a8...
(RayWorkerWrapper pid=1399) INFO 05-28 03:53:31 [model_runner.py:943] Starting to load model /home/deepseek/Deepseek-R1-bf16-hfd-w8a8...
Loading safetensors checkpoint shards:   0% Completed | 0/157 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:   1% Completed | 1/157 [00:00<00:30,  5.07it/s]
Loading safetensors checkpoint shards:   1% Completed | 2/157 [00:00<00:29,  5.18it/s]
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution.
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620] Traceback (most recent call last):
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]     return run_method(self, method, args, kwargs)
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]     return func(*args, **kwargs)
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]     self.model_runner.load_model()
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]     self.model = get_model(vllm_config=self.vllm_config)
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]     return loader.load_model(vllm_config=vllm_config)
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]     loaded_weights = model.load_weights(
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 788, in load_weights
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620]     param = params_dict[name]
(RayWorkerWrapper pid=12580, ip=10.108.8.139) ERROR 05-28 03:54:00 [worker_base.py:620] KeyError: 'model.layers.40.mlp.experts.w2_weight_offset'
(RayWorkerWrapper pid=1900) INFO 05-28 03:53:31 [parallel_state.py:1004] rank 7 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 7 [repeated 14x across cluster]
ERROR 05-28 03:53:36 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution.
ERROR 05-28 03:53:36 [worker_base.py:620] Traceback (most recent call last):
ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
ERROR 05-28 03:53:36 [worker_base.py:620]     return run_method(self, method, args, kwargs)
ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-28 03:53:36 [worker_base.py:620]     return func(*args, **kwargs)
ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
ERROR 05-28 03:53:36 [worker_base.py:620]     self.model_runner.load_model()
ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
ERROR 05-28 03:53:36 [worker_base.py:620]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 05-28 03:53:36 [worker_base.py:620]     return loader.load_model(vllm_config=vllm_config)
ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
ERROR 05-28 03:53:36 [worker_base.py:620]     loaded_weights = model.load_weights(
ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 788, in load_weights
ERROR 05-28 03:53:36 [worker_base.py:620]     param = params_dict[name]
ERROR 05-28 03:53:36 [worker_base.py:620] KeyError: 'model.layers.23.mlp.experts.w2_weight_offset'
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/runpy.py", line 196, in _run_module_as_main
[rank0]:     return _run_code(code, main_globals, None,
[rank0]:   File "/usr/local/python3.10.17/lib/python3.10/runpy.py", line 86, in _run_code
[rank0]:     exec(code, run_globals)
[rank0]:   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1130, in <module>
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
[rank0]:   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config)
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 286, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 114, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 396, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/vllm-workspace/vllm/vllm/executor/ray_distributed_executor.py", line 516, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 621, in execute_method
[rank0]:     raise e
[rank0]:   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method
[rank0]:     return run_method(self, method, args, kwargs)
[rank0]:   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
[rank0]:     loaded_weights = model.load_weights(
[rank0]:   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 788, in load_weights
[rank0]:     param = params_dict[name]
[rank0]: KeyError: 'model.layers.23.mlp.experts.w2_weight_offset'
(RayWorkerWrapper pid=12580, ip=10.108.8.139) INFO 05-28 03:53:56 [model_runner.py:943] Starting to load model /home/deepseek/Deepseek-R1-bf16-hfd-w8a8... [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620] Error executing method 'load_model'. This might cause deadlock in distributed execution. [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620] Traceback (most recent call last): [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 612, in execute_method [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]     return run_method(self, method, args, kwargs) [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]     return func(*args, **kwargs) [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]     self.model_runner.load_model() [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]     self.model = get_model(vllm_config=self.vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]     return loader.load_model(vllm_config=vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]     loaded_weights = model.load_weights( [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 788, in load_weights [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620]     param = params_dict[name] [repeated 14x across cluster]
(RayWorkerWrapper pid=1949) ERROR 05-28 03:53:36 [worker_base.py:620] KeyError: 'model.layers.23.mlp.experts.w2_weight_offset' [repeated 14x across cluster]
[ERROR] 2025-05-28-03:53:39 (PID:23386, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
Loading safetensors checkpoint shards:   1% Completed | 2/157 [00:04<05:31,  2.14s/it]

INFO 05-28 03:53:39 [ray_distributed_executor.py:127] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
[root@node137 Deepseek-R1-bf16-hfd-w8a8]# /usr/local/python3.10.17/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
