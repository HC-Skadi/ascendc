# Issue #381: [Bug]: KeyError when loading weights

## 基本信息

- **编号**: #381
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/381
- **创建时间**: 2025-03-24T08:36:34Z
- **关闭时间**: 2025-03-25T05:51:56Z
- **更新时间**: 2025-05-27T07:18:23Z
- **提交者**: @ghost
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python -m vllm.entrypoints.openai.api_server  \
       --model="/data/deepseek-ai/DeepSeek-R1" \
       --trust-remote-code \
       --enforce-eager \
        --max-model-len 2048 \
       --distributed_executor_backend "ray" \
       --tensor-parallel-size 8 \
       -pp 2 \
       --disable-log-requests \
       --disable-log-stats \
       --disable-frontend-multiprocessing \
       --gpu-memory-utilization 0.95 \
       --cpu-offload-gb 25 \
       --port 1025`</summary>

```text
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/local/python3.10/lib/python3.10/runpy.py", line 196, in _run_module_as_main
[rank0]:     return _run_code(code, main_globals, None,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/runpy.py", line 86, in _run_code
[rank0]:     exec(code, run_globals)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 991, in <module>
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
[rank0]:     return loop.run_until_complete(wrapper())
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
[rank0]:     async with build_async_engine_client(args) as engine_client:
[rank0]:   File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 163, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 644, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 594, in __init__
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 267, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 271, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 90, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 360, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 480, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 582, in execute_method
[rank0]:     raise e
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
[rank0]:     return run_method(target, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 818, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 409, in load_model
[rank0]:     loaded_weights = model.load_weights(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 773, in load_weights
[rank0]:     param = params_dict[name]
[rank0]: KeyError: 'model.layers.24.mlp.experts.w2_weight_scale_inv'
```

</details>


### 🐛 Describe the bug

I used vllm-ascend docker image v0.7.3 and followed the instructions from [https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi_node.html](url) to start an online service of DeepSeek-R1. And I use `--cpu-offload-gb` to use CPU memory + 8*2 910B3 to load model into memory.

When the process went to loading weights, the error occurred.
