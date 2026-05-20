# Issue #1243: [Bug]: deepseek-R1-w8a8 VLLM_ENABLE_MC2=1 error

## 基本信息

- **编号**: #1243
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1243
- **创建时间**: 2025-06-16T09:35:53Z
- **关闭时间**: 2025-07-13T09:51:14Z
- **更新时间**: 2025-07-13T09:51:15Z
- **提交者**: @liujing00000
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

vllm-ascend: 0.9.0rc2 
CANN:8.1.RC1
python:3.10
torch_npu:2.5.1

### 🐛 Describe the bug

运行脚本：
os.environ["VLLM_ENABLE_MC2"] = "1"
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(max_tokens=100, temperature=0.0)
llm = LLM(model="DeepSeek-R1-W8A8-lite-tjl", quantization="ascend", tensor_parallel_size=2, trust_remote_code=True)
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
报错：
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop.
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238] Traceback (most recent call last):
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2605, in run_method
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 91, in start_worker_execution_loop
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     output = self.execute_model(execute_model_req=None)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 420, in execute_model
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     output = self.model_runner.execute_model(
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1441, in execute_model
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     hidden_or_intermediate_states = model_executable(
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 721, in forward
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     hidden_states = self.model(input_ids, positions, kv_caches,
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 668, in forward
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     hidden_states, residual = layer(
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 583, in forward
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     hidden_states = self.mlp(hidden_states, attn_metadata)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 272, in forward
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     hidden_states = self.experts(
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return self._call_impl(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return forward_call(*args, **kwargs)
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py", line 1135, in forward
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     hidden_states = self.quant_method.apply(
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 330, in apply
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return self.quant_method.apply(
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 697, in apply
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     return fused_experts_with_mc2(
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/w8a8_dynamic.py", line 156, in fused_experts_with_mc2
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238]     moe_expert_num = len(expert_map) + global_redundant_expert_num
(VllmWorkerProcess pid=125828) ERROR 06-16 17:29:43 [multiproc_worker_utils.py:238] TypeError: object of type 'NoneType' has no len()
