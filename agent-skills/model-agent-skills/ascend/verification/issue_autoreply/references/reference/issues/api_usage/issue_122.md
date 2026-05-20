# Issue #122: DeepSeek-R1 on 0.7.1-dev  with `Torch not compiled with CUDA enabled`

## 基本信息

- **编号**: #122
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/122
- **创建时间**: 2025-02-20T09:37:38Z
- **关闭时间**: 2025-04-10T08:58:50Z
- **更新时间**: 2025-04-10T08:58:51Z
- **提交者**: @ColdeZhang
- **评论数**: 9

## 标签

question

## 问题描述

Running in docker build on 0.7.1-dev branch:

```
ctr container create  \
  --mount type=bind,src=/mnt/data2,dst=/models,options=rbind:rw \
  --net-host  \
  --device /dev/davinci_manager  \
  --device /dev/hisi_hdc  \
  --device /dev/devmm_svm  \
  --device=/dev/davinci0  \
  --device=/dev/davinci1  \
  --device=/dev/davinci2  \
  --device=/dev/davinci3  \
  --device=/dev/davinci4  \
  --device=/dev/davinci5  \
  --device=/dev/davinci6  \
  --device=/dev/davinci7  \
  --mount type=bind,src=/usr/local/dcmi,dst=/usr/local/dcmi,options=rbind:ro \
  --mount type=bind,src=/usr/local/bin/npu-smi,dst=/usr/local/bin/npu-smi,options=rbind:ro \
  --mount type=bind,src=/usr/local/Ascend/driver/lib64/,dst=/usr/local/Ascend/driver/lib64/,options=rbind:ro \
  --mount type=bind,src=/usr/local/Ascend/driver/version.info,dst=/usr/local/Ascend/driver/version.info,options=rbind:ro \
  --mount type=bind,src=/etc/ascend_install.info,dst=/etc/ascend_install.info,options=rbind:ro \
  docker.io/library/vllm-npu:0.7.1  \
  vllm-ds-dev
```

Serve command:

```
vllm serve /models/DeepSeek-R1/ --tensor_parallel_size 8 --max-model-len 26240 --enforce-eager --trust-remote-code
```

Errors:

```
ERROR 02-20 09:26:55 engine.py:387] 'model.layers.0.self_attn.q_a_proj.weight'
ERROR 02-20 09:26:55 engine.py:387] Traceback (most recent call last):
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 378, in run_mp_engine
ERROR 02-20 09:26:55 engine.py:387]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 121, in from_engine_args
ERROR 02-20 09:26:55 engine.py:387]     return cls(ipc_path=ipc_path,
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 73, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self.engine = LLMEngine(*args, **kwargs)
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 271, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self.model_executor = executor_class(vllm_config=vllm_config, )
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 260, in __init__
ERROR 02-20 09:26:55 engine.py:387]     super().__init__(*args, **kwargs)
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 49, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self._init_executor()
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 123, in _init_executor
ERROR 02-20 09:26:55 engine.py:387]     self._run_workers("load_model",
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 183, in _run_workers
ERROR 02-20 09:26:55 engine.py:387]     driver_worker_output = run_method(self.driver_worker, sent_method,
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method
ERROR 02-20 09:26:55 engine.py:387]     return func(*args, **kwargs)
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker.py", line 188, in load_model
ERROR 02-20 09:26:55 engine.py:387]     self.model_runner.load_model()
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 830, in load_model
ERROR 02-20 09:26:55 engine.py:387]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 12, in get_model
ERROR 02-20 09:26:55 engine.py:387]     return loader.load_model(vllm_config=vllm_config)
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 377, in load_model
ERROR 02-20 09:26:55 engine.py:387]     model = _initialize_model(vllm_config=vllm_config)
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 119, in _initialize_model
ERROR 02-20 09:26:55 engine.py:387]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 660, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self.model = DeepseekV3Model(vllm_config=vllm_config,
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 594, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 555, in make_layers
ERROR 02-20 09:26:55 engine.py:387]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 556, in <listcomp>
ERROR 02-20 09:26:55 engine.py:387]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 596, in <lambda>
ERROR 02-20 09:26:55 engine.py:387]     lambda prefix: DeepseekV3DecoderLayer(
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 502, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self.self_attn = attn_cls(
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v3.py", line 213, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 206, in __init__
ERROR 02-20 09:26:55 engine.py:387]     super().__init__(input_size,
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 177, in __init__
ERROR 02-20 09:26:55 engine.py:387]     self.quant_method = quant_config.get_quant_method(self,
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 80, in get_quant_method
ERROR 02-20 09:26:55 engine.py:387]     if self.is_layer_skipped_ascend(prefix):
ERROR 02-20 09:26:55 engine.py:387]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 109, in is_layer_skipped_ascend
ERROR 02-20 09:26:55 engine.py:387]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
ERROR 02-20 09:26:55 engine.py:387] KeyError: 'model.layers.0.self_attn.q_a_proj.weight'
```
