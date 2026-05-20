# Issue #886: [Bug]: [dp4tp4ep16][DeepSeek-V2-Lite]RuntimeError: InnerRunOpApi:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:281 OPS function error: HcclAllGather, error code is 6

## 基本信息

- **编号**: #886
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/886
- **创建时间**: 2025-05-16T08:54:06Z
- **关闭时间**: 2025-05-19T03:02:31Z
- **更新时间**: 2025-09-28T10:03:29Z
- **提交者**: @david6666666
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details> dp4tp4ep16 双机跑Deepseek-v2-lite 
<summary>The output of `python collect_env.py`</summary>
机器类型 910B1
官方镜像v0.8.5rc1-openeuler 
torch 2.5.1 
CANN8.1RC1
vllm 换为2025.5.15的main（支持DP跨机后 merged pr15977）
vllm-ascend为2025.5.14的main

```text
Your output of above commands here
```


</details>


### 🐛 Describe the bug

[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] Traceback (most recent call last):
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 465, in worker_busy_loop
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] output = func(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/home/dsv3/project/pd/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 232, in execute_dummy_batch
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] self.model_runner._dummy_run(1)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return func(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/home/dsv3/project/pd/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 895, in _dummy_run
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] hidden_states = model(input_ids=input_ids,
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return forward_call(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/home/dsv3/project/pd/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 663, in forward
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] hidden_states = self.model(input_ids, positions, kv_caches,
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return forward_call(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/home/dsv3/project/pd/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 610, in forward
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] hidden_states, residual = layer(
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return forward_call(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/home/dsv3/project/pd/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 527, in forward
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] hidden_states = self.mlp(hidden_states)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return self._call_impl(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] return forward_call(*args, **kwargs)
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] File "/home/dsv3/project/pd/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 236, in forward
[1;36m(EngineCore_1 pid=75299)[0;0m [1;36m(VllmWorker rank=1 pid=75322)[0;0m ERROR 05-16 16:35:18 [multiproc_executor.py:470] final_hidden_states = self.experts(
