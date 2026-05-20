# Issue #900: [Bug]: Qwen3-235B-A22B-AWQ AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'

## 基本信息

- **编号**: #900
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/900
- **创建时间**: 2025-05-19T09:46:59Z
- **关闭时间**: 2025-12-03T06:52:00Z
- **更新时间**: 2025-12-03T06:52:00Z
- **提交者**: @huazq
- **评论数**: 1

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
(evalscope) [root@localhost ~]# npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 98.9        38                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3382 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 101.0       39                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3594 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 98.2        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3594 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 99.3        40                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3595 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 95.0        40                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3597 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 102.8       44                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3594 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 102.4       44                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3593 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 92.5        43                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3594 / 65536         |
+===========================+===============+====================================================+
```

</details>


### 🐛 Describe the bug

[root@d721607e932e workspace]#  vllm serve /mnt/models/Qwen3-235B-A22B-AWQ --served-model-name qwen3-235B --dtype bfloat16 -tp 8 --gpu-memory-utilization 0.9 --host 0.0.0.0 --port 8000 --max-model-len 8192 --trust-remote-code  --quantization awq
.....
(VllmWorkerProcess pid=6341) INFO 05-19 09:38:40 [model_runner.py:953] Starting to load model /mnt/models/Qwen3-235B-A22B-AWQ...
(VllmWorkerProcess pid=6342) INFO 05-19 09:38:40 [model_runner.py:953] Starting to load model /mnt/models/Qwen3-235B-A22B-AWQ...
WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(VllmWorkerProcess pid=6339) WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(VllmWorkerProcess pid=6338) INFO 05-19 09:38:40 [model_runner.py:953] Starting to load model /mnt/models/Qwen3-235B-A22B-AWQ...
(VllmWorkerProcess pid=6341) WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(VllmWorkerProcess pid=6340) WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(VllmWorkerProcess pid=6342) WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(VllmWorkerProcess pid=6343) WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(VllmWorkerProcess pid=6337) WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
(VllmWorkerProcess pid=6338) WARNING 05-19 09:38:40 [utils.py:168] The model class Qwen3MoeForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
ERROR 05-19 09:38:40 [engine.py:448] 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
ERROR 05-19 09:38:40 [engine.py:448] Traceback (most recent call last):
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine
ERROR 05-19 09:38:40 [engine.py:448]     engine = MQLLMEngine.from_vllm_config(
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config
ERROR 05-19 09:38:40 [engine.py:448]     return cls(
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/multiprocessing/engine.py", line 82, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self.engine = LLMEngine(*args, **kwargs)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 275, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self.model_executor = executor_class(vllm_config=vllm_config)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 286, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     super().__init__(*args, **kwargs)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 52, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self._init_executor()
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 125, in _init_executor
ERROR 05-19 09:38:40 [engine.py:448]     self._run_workers("load_model",
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
ERROR 05-19 09:38:40 [engine.py:448]     driver_worker_output = run_method(self.driver_worker, sent_method,
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-19 09:38:40 [engine.py:448]     return func(*args, **kwargs)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
ERROR 05-19 09:38:40 [engine.py:448]     self.model_runner.load_model()
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
ERROR 05-19 09:38:40 [engine.py:448]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 05-19 09:38:40 [engine.py:448]     return loader.load_model(vllm_config=vllm_config)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
ERROR 05-19 09:38:40 [engine.py:448]     model = _initialize_model(vllm_config=vllm_config)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
ERROR 05-19 09:38:40 [engine.py:448]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
ERROR 05-19 09:38:40 [engine.py:448]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
ERROR 05-19 09:38:40 [engine.py:448]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
ERROR 05-19 09:38:40 [engine.py:448]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self.self_attn = Qwen3MoeAttention(
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self.qkv_proj = QKVParallelLinear(hidden_size,
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     super().__init__(input_size=input_size,
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     super().__init__(input_size,
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
ERROR 05-19 09:38:40 [engine.py:448]     self.quant_method = quant_config.get_quant_method(self,
ERROR 05-19 09:38:40 [engine.py:448]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
ERROR 05-19 09:38:40 [engine.py:448]     self.packed_modules_mapping):
ERROR 05-19 09:38:40 [engine.py:448] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.self_attn = Qwen3MoeAttention(
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.packed_modules_mapping):
(VllmWorkerProcess pid=6339) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.self_attn = Qwen3MoeAttention(
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.packed_modules_mapping):
(VllmWorkerProcess pid=6341) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.self_attn = Qwen3MoeAttention(
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.packed_modules_mapping):
(VllmWorkerProcess pid=6342) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.self_attn = Qwen3MoeAttention(
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.packed_modules_mapping):
(VllmWorkerProcess pid=6343) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.self_attn = Qwen3MoeAttention(
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.packed_modules_mapping):
(VllmWorkerProcess pid=6340) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.self_attn = Qwen3MoeAttention(
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238]     self.packed_modules_mapping):
(VllmWorkerProcess pid=6337) ERROR 05-19 09:38:40 [multiproc_worker_utils.py:238] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 452, in load_model
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     model = _initialize_model(vllm_config=vllm_config)
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 133, in _initialize_model
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 488, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.model = Qwen3MoeModel(vllm_config=vllm_config,
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 151, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 334, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 609, in make_layers
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 610, in <listcomp>
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 336, in <lambda>
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     lambda prefix: Qwen3MoeDecoderLayer(config=config,
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 256, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.self_attn = Qwen3MoeAttention(
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 186, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.qkv_proj = QKVParallelLinear(hidden_size,
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 849, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     super().__init__(input_size=input_size,
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 395, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     super().__init__(input_size,
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 242, in __init__
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 93, in get_quant_method
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238]     self.packed_modules_mapping):
(VllmWorkerProcess pid=6338) ERROR 05-19 09:38:41 [multiproc_worker_utils.py:238] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
ERROR 05-19 09:38:42 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 6341 died, exit code: -15
ERROR 05-19 09:38:42 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 6343 died, exit code: -15
INFO 05-19 09:38:42 [multiproc_worker_utils.py:124] Killing local vLLM worker processes
