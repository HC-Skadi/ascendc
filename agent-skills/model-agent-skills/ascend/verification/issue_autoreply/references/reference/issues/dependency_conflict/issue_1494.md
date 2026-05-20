# Issue #1494: [Bug]: w8a8 quantization usage

## 基本信息

- **编号**: #1494
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1494
- **创建时间**: 2025-06-28T06:30:49Z
- **关闭时间**: 2025-09-05T02:37:28Z
- **更新时间**: 2025-09-05T02:37:28Z
- **提交者**: @Potabk
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

I' using vllm and vllm-ascend latest main to test w8a8 quantization, run the [quantize](https://vllm-ascend.readthedocs.io/en/latest/user_guide/quantization.html), will result in an error:
```shell
 WorkerProc failed to start.
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487] Traceback (most recent call last):
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quantizer.py", line 50, in get_quantizer
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     module = importlib.import_module("mindie_turbo")
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/usr/local/python3.10.17/lib/python3.10/importlib/__init__.py", line 126, in import_module
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     return _bootstrap._gcd_import(name[level:], package, level)
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487] ModuleNotFoundError: No module named 'mindie_turbo'
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487] 
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487] During handling of the above exception, another exception occurred:
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487] 
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487] Traceback (most recent call last):
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 461, in worker_main
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     worker = WorkerProc(*args, **kwargs)
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 358, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.worker.load_model()
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 193, in load_model
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.model_runner.load_model()
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1805, in load_model
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     return loader.load_model(vllm_config=vllm_config,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 38, in load_model
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     model = initialize_model(vllm_config=vllm_config,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 64, in initialize_model
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 858, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 779, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 626, in make_layers
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 627, in <listcomp>
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 781, in <lambda>
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     lambda prefix: CustomDeepseekV2DecoderLayer(
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 629, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.self_attn = attn_cls(
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 457, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 280, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     super().__init__(input_size,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 243, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.quant_method = quant_config.get_quant_method(self,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 95, in get_quant_method
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     return AscendLinearMethod(self, prefix,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 155, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     self.quantizer = AscendQuantizer.get_quantizer(
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quantizer.py", line 55, in get_quantizer
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     return VLLMAscendQuantizer.get_quantizer(quant_config, prefix,
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quantizer.py", line 260, in get_quantizer
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     cls._instance = cls(quant_description)
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quantizer.py", line 80, in __init__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     VLLMAscendQuantizer.apply_patch(
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quantizer.py", line 106, in apply_patch
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     and hasattr(value, target_function)
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/import_utils.py", line 440, in __getattr__
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     value = self._extra_import_func(name)
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/__init__.py", line 134, in try_import_from_hf
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487]     raise ImportError(
(VllmWorker rank=1 pid=8700) ERROR 06-28 06:20:15 [multiproc_executor.py:487] ImportError: Cannot import available module of forward_oot in modelscope, or related packages(['transformers', 'peft', 'diffusers'])
```
