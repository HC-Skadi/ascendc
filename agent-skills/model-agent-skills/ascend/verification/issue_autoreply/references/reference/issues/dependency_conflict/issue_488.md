# Issue #488: [Bug]: 910B上采用vllm-ascend双卡部署deepseek-distill-qwen-32B模型偶发性

## 基本信息

- **编号**: #488
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/488
- **创建时间**: 2025-04-09T01:48:53Z
- **关闭时间**: 2025-05-14T03:45:18Z
- **更新时间**: 2025-05-14T03:45:18Z
- **提交者**: @shengjie-shi
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
在远程机器上不太方便执行。
一些环境信息：
系统 ： Linux 24.4.v2101.ky10.aarch64，

加速卡驱动 ： Ascend HDK 23.0.7，

CANN： 8.0.0，

python： 3.10.14，

pytorch ： 2.5.1，

torch-npu： 2.5.1.dev20250218，

transformers： 4.49.0，

vllm： 0.7.2.dev，

vllm_ascend： 0.7.1rc1

安装按照
https://vllm-ascend.readthedocs.io/en/latest/installation.html 中之前vllm-ascend 0.7.2 手动编译方式部署
</details>

### 🐛 Describe the bug

用框架双卡部署deepseek-distill-32B，设置可见卡号为4，5，开启参数为：
tensor-parallel-size 2
gpu-memory-utilization 0.8
max-model-len 20480

调用参数为：
{"messages": [{"role": "user", "content": "你好，请问你是？"}]}

循环调用100次，可能在40~50次时候就会出现如下报错：

  File "/opt/epoint/大语言模型推理/API/RestApi_async.py", line 145, in api_predict_async
    response = await self.system(request, raw_request)
  File "/opt/epoint/大语言模型推理/algorithms/openai_servers.py", line 331, in __call__
    async for request_output in generator:
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 1004, in generate
    async for output in await self.add_request(
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 114, in generator
    raise result
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 56, in _log_task_completion
    return_value = task.result()
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 823, in run_engine_loop
    result = task.result()
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 746, in engine_step
    request_outputs = await self.engine.step_async(virtual_engine)
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 351, in step_async
    outputs = await self.model_executor.execute_model_async(
  File "/usr/local/python/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 343, in execute_model_async
    return await self._driver_execute_model_async(execute_model_req)
  File "/usr/local/python/lib/python3.10/site-packages/vllm/executor/mp_distributed_executor.py", line 207, in _driver_execute_model_async
    return await self.driver_exec_model(execute_model_req)
  File "/usr/local/python/lib/python3.10/concurrent/futures/thread.py", line 58, in run
    result = self.fn(*self.args, **self.kwargs)
  File "/usr/local/python/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 411, in execute_model
    output = self.model_runner.execute_model(
  File "/usr/local/python/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python/lib/python3.10/site-packages/vllm_ascend/model_runner.py", line 1185, in execute_model
    logits = self.model.compute_logits(hidden_or_intermediate_states,
  File "/usr/local/python/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 494, in compute_logits
    logits = self.logits_processor(self.lm_head, hidden_states,
  File "/usr/local/python/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/python/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/python/lib/python3.10/site-packages/vllm/model_executor/layers/logits_processor.py", line 68, in forward
    logits = self._get_logits(hidden_states, lm_head, embedding_bias)
  File "/usr/local/python/lib/python3.10/site-packages/vllm/model_executor/layers/logits_processor.py", line 104, in _get_logits
    logits = tensor_model_parallel_gather(logits)
  File "/usr/local/python/lib/python3.10/site-packages/vllm/distributed/communication_op.py", line 24, in tensor_model_parallel_gather
    return get_tp_group().gather(input_, dst, dim)
  File "/usr/local/python/lib/python3.10/site-packages/vllm_ascend/patch/patch_commnicator.py", line 58, in gather
    return self.communicator.gather(input_, dst, dim)
  File "/usr/local/python/lib/python3.10/site-packages/vllm_ascend/communicator.py", line 49, in gather
    dist.gather(input_, gather_list, dst=self.ranks[dst], group=self.group)
  File "/usr/local/python/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py", line 114, in _gather
    dist.broadcast_object_list(recv_size_list, dst, group)
  File "/usr/local/python/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 3120, in broadcast_object_list
    *[_object_to_tensor(obj, current_device, group) for obj in object_list]
  File "/usr/local/python/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 3120, in <listcomp>
    *[_object_to_tensor(obj, current_device, group) for obj in object_list]
  File "/usr/local/python/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2627, in _object_to_tensor
    byte_tensor = torch.ByteTensor(byte_storage).to(device)
RuntimeError: ACL stream synchronize failed, error code:507035

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/opt/epoint/大语言模型推理/API/RestApi_async.py", line 145, in api_predict_async
    response = await self.system(request, raw_request)
  File "/opt/epoint/大语言模型推理/algorithms/openai_servers.py", line 331, in __call__
    async for request_output in generator:
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 1004, in generate
    async for output in await self.add_request(
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 900, in add_request
    self.start_background_loop()
  File "/usr/local/python/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 696, in start_background_loop
    raise AsyncEngineDeadError(
vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.

之后就无法再执行新的请求

