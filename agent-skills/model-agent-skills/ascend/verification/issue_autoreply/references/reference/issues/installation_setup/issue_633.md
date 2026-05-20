# Issue #633: [Doc]: qwen2.5-coder 通过项目msit量化后，vllm 运行报错  NotImplementedError: There is no available ascend quantizer.

## 基本信息

- **编号**: #633
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/633
- **创建时间**: 2025-04-23T09:28:08Z
- **关闭时间**: 2025-04-25T02:27:12Z
- **更新时间**: 2025-04-25T02:27:13Z
- **提交者**: @wanmei002
- **评论数**: 5

## 标签

documentation

## 问题描述

### 📚 The doc issue

通过项目提供的 [here](https://github.com/vllm-project/vllm-ascend/pull/580#issuecomment-2816747613)， 量化 qwen2.5-coder, 报错 ：
```python
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
    engine = MQLLMEngine.from_vllm_config(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
    return cls(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__
    self.engine = LLMEngine(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 282, in __init__
    self.model_executor = executor_class(vllm_config=vllm_config, )
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
    self._init_executor()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 47, in _init_executor
    self.collective_rpc("load_model")
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2378, in run_method
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 208, in load_model
    self.model_runner.load_model()
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 901, in load_model
    self.model = get_model(vllm_config=self.vllm_config)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
    return loader.load_model(vllm_config=vllm_config)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 452, in load_model
    model = _initialize_model(vllm_config=vllm_config)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
    return model_class(vllm_config=vllm_config, prefix=prefix)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in __init__
    self.model = Qwen2Model(vllm_config=vllm_config,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
    old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 306, in __init__
    self.start_layer, self.end_layer, self.layers = make_layers(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 609, in make_layers
    [PPMissingLayer() for _ in range(start_layer)] + [
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 610, in <listcomp>
    maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in <lambda>
    lambda prefix: decoder_layer_type(config=config,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 206, in __init__
    self.self_attn = Qwen2Attention(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 136, in __init__
    self.qkv_proj = QKVParallelLinear(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 833, in __init__
    super().__init__(input_size=input_size,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 384, in __init__
    super().__init__(input_size,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 231, in __init__
    self.quant_method = quant_config.get_quant_method(self,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
    return AscendLinearMethod(self, prefix,
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 153, in __init__
    self.quantizer = AscendQuantizer.get_quantizer(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quantizer.py", line 43, in get_quantizer
    raise NotImplementedError(
NotImplementedError: There is no available ascend quantizer.
Process SpawnProcess-1:
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quantizer.py", line 40, in get_quantizer
    module = importlib.import_module("mindie_turbo")
  File "/usr/local/python3.10/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'mindie_turbo'
```
这个是什么问题，pip 安装 mindie_turbo  也没找到这个库

### Suggest a potential alternative/fix

_No response_
