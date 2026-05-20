# Issue #934: [Bug]: vllm0.8.5rc1 run baichuan with TP，assert error

## 基本信息

- **编号**: #934
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/934
- **创建时间**: 2025-05-22T12:41:33Z
- **关闭时间**: 2025-05-23T09:01:26Z
- **更新时间**: 2025-05-23T09:01:26Z
- **提交者**: @Sousky
- **评论数**: 3

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

1、environment:
vllm   0.8.5.post1+empty
vllm_ascend   0.8.5rc2.dev0

2、model
baichuan-7b-chat TP
python3 vllm-ascend/examples/offline_distributed_inference_npu.py

3、error report
[rank0]: Traceback (most recent call last):
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm-ascend/examples/offline_distributed_inference_npu.py", line 32, in <module>
[rank0]:     llm = LLM(
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/utils.py", line 1161, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/entrypoints/llm.py", line 247, in __init__
[rank0]:     self.llm_engine = LLMEngine.from_engine_args(
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/engine/llm_engine.py", line 510, in from_engine_args
[rank0]:     return engine_cls.from_vllm_config(
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/engine/llm_engine.py", line 486, in from_vllm_config
[rank0]:     return cls(
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/engine/llm_engine.py", line 275, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/executor/executor_base.py", line 286, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/executor/mp_distributed_executor.py", line 125, in _init_executor
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/executor/mp_distributed_executor.py", line 185, in _run_workers
[rank0]:     driver_worker_output = run_method(self.driver_worker, sent_method,
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/utils.py", line 2456, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm-ascend/vllm_ascend/worker/model_runner.py", line 945, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model
[rank0]:     loaded_weights = model.load_weights(
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/models/baichuan.py", line 427, in load_weights
[rank0]:     return loader.load_weights(weights)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights
[rank0]:     autoloaded_weights = set(self._load_module("", self.module, weights))
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/models/utils.py", line 222, in _load_module
[rank0]:     yield from self._load_module(prefix,
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/models/utils.py", line 231, in _load_module
[rank0]:     yield from self._load_param(prefix, child_params[child_prefix],
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/models/utils.py", line 154, in _load_param
[rank0]:     weight_loader(param, weight_data)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/models/baichuan.py", line 441, in lm_head_weight_loader
[rank0]:     default_weight_loader(param, loaded_weight)
[rank0]:   File "/opt/tiger/xiaoanna/vllm_ascend_0.8.5/vllm/vllm/model_executor/model_loader/weight_utils.py", line 583, in default_weight_loader
[rank0]:     assert param.size() == loaded_weight.size(), (
[rank0]: AssertionError: Attempted to load weight (torch.Size([125696, 4096])) into parameter (torch.Size([62848, 4096]))
