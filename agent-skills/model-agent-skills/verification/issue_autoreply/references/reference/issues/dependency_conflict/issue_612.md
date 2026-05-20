# Issue #612: [Bug]: use docker image version  v0.8.4rc1, vllm serve error: ConnectionRefusedError: [Errno 111] Connection refused

## 基本信息

- **编号**: #612
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/612
- **创建时间**: 2025-04-22T07:54:57Z
- **关闭时间**: 2025-04-22T10:23:23Z
- **更新时间**: 2025-04-22T10:23:35Z
- **提交者**: @wanmei002
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 04-22 07:46:23 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-22 07:46:23 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-22 07:46:23 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-22 07:46:23 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-22 07:46:23 [__init__.py:44] plugin ascend loaded.
INFO 04-22 07:46:23 [__init__.py:230] Platform plugin ascend is activated
Collecting environment information...
Traceback (most recent call last):
  File "/workspace/collect_env.py", line 489, in <module>
    main()
  File "/workspace/collect_env.py", line 468, in main
    output = get_pretty_env_info()
  File "/workspace/collect_env.py", line 463, in get_pretty_env_info
    return pretty_str(get_env_info())
  File "/workspace/collect_env.py", line 353, in get_env_info
    vllm_ascend_version=get_vllm_ascend_version(),
  File "/workspace/collect_env.py", line 174, in get_vllm_ascend_version
    from vllm_ascend._version import __version__, __version_tuple__
ModuleNotFoundError: No module named 'vllm_ascend._version'
[ERROR] 2025-04-22-07:46:27 (PID:457, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

</details>


### 🐛 Describe the bug

#### run cmd in docker container:
vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4   --served-model-name qwen2.5-coder:32b   --max-model-len 10240   --tensor-parallel-size 8   --port 8000
#### error log:

(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = Qwen2Model(vllm_config=vllm_config,
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     lambda prefix: decoder_layer_type(config=config,
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.self_attn = Qwen2Attention(
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     if self.is_layer_skipped_ascend(prefix,
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 121, in is_layer_skipped_ascend
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorkerProcess pid=76114) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] KeyError: 'model.layers.0.self_attn.q_proj.weight'
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = Qwen2Model(vllm_config=vllm_config,
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     lambda prefix: decoder_layer_type(config=config,
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.self_attn = Qwen2Attention(
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     if self.is_layer_skipped_ascend(prefix,
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 121, in is_layer_skipped_ascend
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorkerProcess pid=76116) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] KeyError: 'model.layers.0.self_attn.q_proj.weight'
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = Qwen2Model(vllm_config=vllm_config,
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     lambda prefix: decoder_layer_type(config=config,
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.self_attn = Qwen2Attention(
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     if self.is_layer_skipped_ascend(prefix,
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 121, in is_layer_skipped_ascend
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorkerProcess pid=76119) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] KeyError: 'model.layers.0.self_attn.q_proj.weight'
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = Qwen2Model(vllm_config=vllm_config,
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     lambda prefix: decoder_layer_type(config=config,
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.self_attn = Qwen2Attention(
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     if self.is_layer_skipped_ascend(prefix,
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 121, in is_layer_skipped_ascend
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorkerProcess pid=76117) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] KeyError: 'model.layers.0.self_attn.q_proj.weight'
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = Qwen2Model(vllm_config=vllm_config,
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     lambda prefix: decoder_layer_type(config=config,
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.self_attn = Qwen2Attention(
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     if self.is_layer_skipped_ascend(prefix,
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 121, in is_layer_skipped_ascend
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorkerProcess pid=76113) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] KeyError: 'model.layers.0.self_attn.q_proj.weight'
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = Qwen2Model(vllm_config=vllm_config,
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     lambda prefix: decoder_layer_type(config=config,
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.self_attn = Qwen2Attention(
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     if self.is_layer_skipped_ascend(prefix,
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 121, in is_layer_skipped_ascend
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorkerProcess pid=76115) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] KeyError: 'model.layers.0.self_attn.q_proj.weight'
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.model = Qwen2Model(vllm_config=vllm_config,
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     lambda prefix: decoder_layer_type(config=config,
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.self_attn = Qwen2Attention(
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 90, in get_quant_method
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     if self.is_layer_skipped_ascend(prefix,
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 121, in is_layer_skipped_ascend
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238]     is_shard_skipped = self.quant_description[shard_prefix +
(VllmWorkerProcess pid=76118) ERROR 04-22 07:10:28 [multiproc_worker_utils.py:238] KeyError: 'model.layers.0.self_attn.q_proj.weight'
ERROR 04-22 07:10:30 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 76116 died, exit code: -15
ERROR 04-22 07:10:30 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 76117 died, exit code: -15
ERROR 04-22 07:10:30 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 76118 died, exit code: -15
ERROR 04-22 07:10:30 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 76119 died, exit code: -15
INFO 04-22 07:10:30 [multiproc_worker_utils.py:124] Killing local vLLM worker processes
Traceback (most recent call last):
  File "/usr/local/python3.10/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/main.py", line 51, in main
    args.dispatch_function(args)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/cli/serve.py", line 27, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 1069, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 146, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 269, in build_async_engine_client_from_engine_args
    raise RuntimeError(
RuntimeError: Engine process failed to start. See stack trace for the root cause.
[ERROR] 2025-04-22-07:10:31 (PID:75800, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
Process ForkServerProcess-1:1:8:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 810, in _callmethod
    conn = self._tls.connection
AttributeError: 'ForkAwareLocal' object has no attribute 'connection'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 71, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 63, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 264, in task_distribute
    resource_proxy[SUB_PROCESS_STATE].append(True)
  File "<string>", line 2, in append
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 814, in _callmethod
    self._connect()
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/managers.py", line 801, in _connect
    conn = self._Client(self._token.address, authkey=self._authkey)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/connection.py", line 502, in Client
    c = SocketClient(address)
  File "/usr/local/python3.10/lib/python3.10/multiprocessing/connection.py", line 630, in SocketClient
    s.connect(address)
ConnectionRefusedError: [Errno 111] Connection refused

#### mpu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 104.9       49                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3375 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 97.8        47                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3374 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 99.4        47                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3376 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 91.8        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 104.7       48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3375 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 99.8        48                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3376 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 103.8       48                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 97.1        47                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3373 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
