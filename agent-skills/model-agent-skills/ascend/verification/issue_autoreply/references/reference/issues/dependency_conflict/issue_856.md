# Issue #856: [Bug]: vllm-ascend v0.8.5rc1, failed to start vllm, when load w8a8 weights

## 基本信息

- **编号**: #856
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/856
- **创建时间**: 2025-05-14T07:19:03Z
- **关闭时间**: 2025-11-11T13:26:30Z
- **更新时间**: 2025-11-11T13:26:30Z
- **提交者**: @Saxsgdsg
- **评论数**: 4

## 标签

bug; module:quantization

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text

```

</details>

### 🐛 Describe the bug

INFO 05-14 11:01:21 [model_runner.py:943] Starting to load model /home/qwen2.5-72b-new...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238] Traceback (most recent call last):
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     self.model_runner.load_model()
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     loaded_weights = model.load_weights(
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 486, in load_weights
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     return loader.load_weights(weights)
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     autoloaded_weights = set(self._load_module("", self.module, weights))
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 222, in _load_module
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     yield from self._load_module(prefix,
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 195, in _load_module
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     loaded_params = module_load_weights(weights)
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2.py", line 391, in load_weights
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238]     param = params_dict[name]
ERROR 05-14 11:01:22 [multiproc_worker_utils.py:238] KeyError: 'layers.0.mlp.gate_up_proj.weight_offset'


需要把quant_model_description.json内容拷贝到config.json中可以正常启动。
