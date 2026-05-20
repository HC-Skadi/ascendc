# Issue #516: [Bug]: AssertionError: Torch not compiled with CUDA enabled

## 基本信息

- **编号**: #516
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/516
- **创建时间**: 2025-04-14T05:59:12Z
- **关闭时间**: 2025-12-30T09:46:12Z
- **更新时间**: 2025-12-30T09:46:12Z
- **提交者**: @YuanJZhang
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

vllm                              0.1.dev1+gf90a375.empty
vllm_ascend                       0.1.dev47+g3a78822 
torch                             2.5.1
torch-npu                         2.5.1.dev20250218
torchvision                       0.20.1
Python 3.10.12


### 🐛 Describe the bug

INFO 04-14 13:53:34 ray_distributed_executor.py:153] use_ray_spmd_worker: False
(RayWorkerWrapper pid=33387) INFO 04-14 13:53:43 __init__.py:30] Available plugins for group vllm.platform_plugins:
(RayWorkerWrapper pid=33387) INFO 04-14 13:53:43 __init__.py:32] name=ascend, value=vllm_ascend:register
(RayWorkerWrapper pid=33387) INFO 04-14 13:53:43 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
(RayWorkerWrapper pid=33387) INFO 04-14 13:53:43 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
(RayWorkerWrapper pid=33387) INFO 04-14 13:53:43 __init__.py:44] plugin ascend loaded.
(RayWorkerWrapper pid=33387) INFO 04-14 13:53:43 __init__.py:198] Platform plugin ascend is activated
INFO 04-14 13:53:44 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 04-14 13:53:44 utils.py:2298] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.NPUWorker object at 0xfffd1fce2e00>
(RayWorkerWrapper pid=33391) INFO 04-14 13:53:44 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
(RayWorkerWrapper pid=33392) WARNING 04-14 13:53:44 utils.py:2298] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.NPUWorker object at 0xffcfd285d510>
INFO 04-14 13:53:51 shm_broadcast.py:258] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_ae45c396'), local_subscribe_addr='ipc:///tmp/33fc42ec-cb13-4da9-b6de-cd9eb63c9100', remote_subscribe_addr='tcp://10.240.32.159:56883', remote_addr_ipv6=False)
INFO 04-14 13:53:51 parallel_state.py:948] rank 0 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 0
(RayWorkerWrapper pid=33391) INFO 04-14 13:53:51 parallel_state.py:948] rank 4 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 4
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:43 __init__.py:30] Available plugins for group vllm.platform_plugins: [repeated 15x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/ray-logging.html#log-deduplication for more options.)
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:43 __init__.py:32] name=ascend, value=vllm_ascend:register [repeated 15x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:43 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded. [repeated 15x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:43 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load. [repeated 15x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:43 __init__.py:44] plugin ascend loaded. [repeated 15x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:43 __init__.py:198] Platform plugin ascend is activated [repeated 15x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:44 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available. [repeated 14x across cluster]
(RayWorkerWrapper pid=44965, ip=10.240.34.77) WARNING 04-14 13:53:44 utils.py:2298] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.NPUWorker object at 0xffcfe07954b0> [repeated 14x across cluster]
ERROR 04-14 13:53:52 worker_base.py:593] Error executing method 'load_model'. This might cause deadlock in distributed execution.
ERROR 04-14 13:53:52 worker_base.py:593] Traceback (most recent call last):
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 585, in execute_method
ERROR 04-14 13:53:52 worker_base.py:593]     return run_method(self, method, args, kwargs)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 2232, in run_method
ERROR 04-14 13:53:52 worker_base.py:593]     return func(*args, **kwargs)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/vllm-ascend/vllm_ascend/worker.py", line 190, in load_model
ERROR 04-14 13:53:52 worker_base.py:593]     self.model_runner.load_model()
ERROR 04-14 13:53:52 worker_base.py:593]   File "/vllm-ascend/vllm_ascend/model_runner.py", line 831, in load_model
ERROR 04-14 13:53:52 worker_base.py:593]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 04-14 13:53:52 worker_base.py:593]     return loader.load_model(vllm_config=vllm_config)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
ERROR 04-14 13:53:52 worker_base.py:593]     model = _initialize_model(vllm_config=vllm_config)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
ERROR 04-14 13:53:52 worker_base.py:593]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
ERROR 04-14 13:53:52 worker_base.py:593]     self.model = DeepseekV2Model(vllm_config=vllm_config,
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/compilation/decorators.py", line 151, in __init__
ERROR 04-14 13:53:52 worker_base.py:593]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
ERROR 04-14 13:53:52 worker_base.py:593]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
ERROR 04-14 13:53:52 worker_base.py:593]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
ERROR 04-14 13:53:52 worker_base.py:593]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
ERROR 04-14 13:53:52 worker_base.py:593]     lambda prefix: DeepseekV2DecoderLayer(
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
ERROR 04-14 13:53:52 worker_base.py:593]     self.self_attn = attn_cls(
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 417, in __init__
ERROR 04-14 13:53:52 worker_base.py:593]     self.rotary_emb = get_rope(qk_rope_head_dim,
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 1099, in get_rope
ERROR 04-14 13:53:52 worker_base.py:593]     rotary_emb = DeepseekScalingRotaryEmbedding(
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 649, in __init__
ERROR 04-14 13:53:52 worker_base.py:593]     super().__init__(head_size, rotary_dim, max_position_embeddings, base,
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 98, in __init__
ERROR 04-14 13:53:52 worker_base.py:593]     cache = self._compute_cos_sin_cache()
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 671, in _compute_cos_sin_cache
ERROR 04-14 13:53:52 worker_base.py:593]     inv_freq = self._compute_inv_freq(self.scaling_factor)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 653, in _compute_inv_freq
ERROR 04-14 13:53:52 worker_base.py:593]     pos_freqs = self.base**(torch.arange(
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/torch/utils/_device.py", line 106, in __torch_function__
ERROR 04-14 13:53:52 worker_base.py:593]     return func(*args, **kwargs)
ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py", line 310, in _lazy_init
ERROR 04-14 13:53:52 worker_base.py:593]     raise AssertionError("Torch not compiled with CUDA enabled")
ERROR 04-14 13:53:52 worker_base.py:593] AssertionError: Torch not compiled with CUDA enabled
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
[rank0]:     return _run_code(code, main_globals, None,
[rank0]:   File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
[rank0]:     exec(code, run_globals)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 991, in <module>
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/uvloop/__init__.py", line 82, in run
[rank0]:     return loop.run_until_complete(wrapper())
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 946, in run_server
[rank0]:     async with build_async_engine_client(args) as engine_client:
[rank0]:   File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 138, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/usr/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 162, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_engine_args(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 644, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 594, in __init__
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 267, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 273, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 271, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/executor/ray_distributed_executor.py", line 90, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/executor/ray_distributed_executor.py", line 360, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/executor/ray_distributed_executor.py", line 480, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 594, in execute_method
[rank0]:     raise e
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 585, in execute_method
[rank0]:     return run_method(self, method, args, kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 2232, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/vllm-ascend/vllm_ascend/worker.py", line 190, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/vllm-ascend/vllm_ascend/model_runner.py", line 831, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
[rank0]:     model = _initialize_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
[rank0]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
[rank0]:     self.model = DeepseekV2Model(vllm_config=vllm_config,
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/compilation/decorators.py", line 151, in __init__
[rank0]:     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
[rank0]:     self.start_layer, self.end_layer, self.layers = make_layers(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
[rank0]:     [PPMissingLayer() for _ in range(start_layer)] + [
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
[rank0]:     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
[rank0]:     lambda prefix: DeepseekV2DecoderLayer(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
[rank0]:     self.self_attn = attn_cls(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 417, in __init__
[rank0]:     self.rotary_emb = get_rope(qk_rope_head_dim,
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 1099, in get_rope
[rank0]:     rotary_emb = DeepseekScalingRotaryEmbedding(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 649, in __init__
[rank0]:     super().__init__(head_size, rotary_dim, max_position_embeddings, base,
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 98, in __init__
[rank0]:     cache = self._compute_cos_sin_cache()
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 671, in _compute_cos_sin_cache
[rank0]:     inv_freq = self._compute_inv_freq(self.scaling_factor)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 653, in _compute_inv_freq
[rank0]:     pos_freqs = self.base**(torch.arange(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/torch/utils/_device.py", line 106, in __torch_function__
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py", line 310, in _lazy_init
[rank0]:     raise AssertionError("Torch not compiled with CUDA enabled")
[rank0]: AssertionError: Torch not compiled with CUDA enabled
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593] Error executing method 'load_model'. This might cause deadlock in distributed execution.
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593] Traceback (most recent call last):
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 585, in execute_method
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return run_method(self, method, args, kwargs)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 2232, in run_method
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return func(*args, **kwargs)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/vllm-ascend/vllm_ascend/worker.py", line 190, in load_model
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.model_runner.load_model()
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/vllm-ascend/vllm_ascend/model_runner.py", line 831, in load_model
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.model = get_model(vllm_config=self.vllm_config)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return loader.load_model(vllm_config=vllm_config)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     model = _initialize_model(vllm_config=vllm_config)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return model_class(vllm_config=vllm_config, prefix=prefix)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.model = DeepseekV2Model(vllm_config=vllm_config,
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/compilation/decorators.py", line 151, in __init__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.start_layer, self.end_layer, self.layers = make_layers(
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     [PPMissingLayer() for _ in range(start_layer)] + [
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     lambda prefix: DeepseekV2DecoderLayer(
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.self_attn = attn_cls(
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 417, in __init__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.rotary_emb = get_rope(qk_rope_head_dim,
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 1099, in get_rope
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     rotary_emb = DeepseekScalingRotaryEmbedding(
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 649, in __init__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     super().__init__(head_size, rotary_dim, max_position_embeddings, base,
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 98, in __init__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     cache = self._compute_cos_sin_cache()
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 671, in _compute_cos_sin_cache
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     inv_freq = self._compute_inv_freq(self.scaling_factor)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 653, in _compute_inv_freq
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     pos_freqs = self.base**(torch.arange(
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/torch/utils/_device.py", line 106, in __torch_function__
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return func(*args, **kwargs)
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py", line 310, in _lazy_init
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     raise AssertionError("Torch not compiled with CUDA enabled")
(RayWorkerWrapper pid=44964, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593] AssertionError: Torch not compiled with CUDA enabled
(RayWorkerWrapper pid=44970, ip=10.240.34.77) INFO 04-14 13:53:51 parallel_state.py:948] rank 15 in world size 16 is assigned as DP rank 0, PP rank 0, TP rank 15 [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593] Error executing method 'load_model'. This might cause deadlock in distributed execution. [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593] Traceback (most recent call last): [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 585, in execute_method [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return run_method(self, method, args, kwargs) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 2232, in run_method [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return func(*args, **kwargs) [repeated 28x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/vllm-ascend/vllm_ascend/worker.py", line 190, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.model_runner.load_model() [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/vllm-ascend/vllm_ascend/model_runner.py", line 831, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.model = get_model(vllm_config=self.vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return loader.load_model(vllm_config=vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     model = _initialize_model(vllm_config=vllm_config) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     return model_class(vllm_config=vllm_config, prefix=prefix) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 98, in __init__ [repeated 98x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.model = DeepseekV2Model(vllm_config=vllm_config, [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.start_layer, self.end_layer, self.layers = make_layers( [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 557, in make_layers [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     [PPMissingLayer() for _ in range(start_layer)] + [ [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp> [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda> [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     lambda prefix: DeepseekV2DecoderLayer( [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.self_attn = attn_cls( [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     self.rotary_emb = get_rope(qk_rope_head_dim, [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 1099, in get_rope [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     rotary_emb = DeepseekScalingRotaryEmbedding( [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     super().__init__(head_size, rotary_dim, max_position_embeddings, base, [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     cache = self._compute_cos_sin_cache() [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 671, in _compute_cos_sin_cache [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     inv_freq = self._compute_inv_freq(self.scaling_factor) [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/rotary_embedding.py", line 653, in _compute_inv_freq [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     pos_freqs = self.base**(torch.arange( [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/torch/utils/_device.py", line 106, in __torch_function__ [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]   File "/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py", line 310, in _lazy_init [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593]     raise AssertionError("Torch not compiled with CUDA enabled") [repeated 14x across cluster]
(RayWorkerWrapper pid=44970, ip=10.240.34.77) ERROR 04-14 13:53:52 worker_base.py:593] AssertionError: Torch not compiled with CUDA enabled [repeated 14x across cluster]
[ERROR] 2025-04-14-13:53:54 (PID:32952, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
INFO 04-14 13:53:54 ray_distributed_executor.py:104] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
/usr/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '


```text
Your output of above commands here
```

</details>

