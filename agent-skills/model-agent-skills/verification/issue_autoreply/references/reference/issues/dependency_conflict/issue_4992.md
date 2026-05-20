# Issue #4992: [Bug]: HUNYUAN-ORC failed to run

## 基本信息

- **编号**: #4992
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4992
- **创建时间**: 2025-12-13T12:16:25Z
- **关闭时间**: 2025-12-23T02:46:55Z
- **更新时间**: 2025-12-23T02:46:55Z
- **提交者**: @Potabk
- **评论数**: 5

## 标签

new model

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

```python
from vllm import LLM, SamplingParams
from PIL import Image
from modelscope import AutoProcessor

model_path = "Tencent-Hunyuan/HunyuanOCR"
llm = LLM(model=model_path, trust_remote_code=True)
processor = AutoProcessor.from_pretrained(model_path)
sampling_params = SamplingParams(temperature=0, max_tokens=16384)

img_path = "~/.cache/vllm/assets/vllm_public_assets/fig1.png"
img = Image.open(img_path)
messages = [
    {"role": "user", "content": [
        {"type": "image", "image": img_path},
        {"type": "text", "text": "Detect and recognize text in the image, and output the text coordinates in a formatted manner."}
    ]}
]
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = {"prompt": prompt, "multi_modal_data": {"image": [img]}}
output = llm.generate([inputs], sampling_params)[0]
print(output.outputs[0].text)
```

```shell

Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:01<00:03,  1.03s/it]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:02<00:02,  1.04s/it]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:03<00:01,  1.23s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:04<00:00,  1.18s/it]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:04<00:00,  1.16s/it]
(EngineCore_DP0 pid=51064)
(EngineCore_DP0 pid=51064) INFO 12-13 12:09:53 [default_loader.py:308] Loading weights took 4.66 seconds
(EngineCore_DP0 pid=51064) INFO 12-13 12:09:58 [model_runner_v1.py:2362] Loading model weights took 1.8976 GB
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843] EngineCore failed to start.
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843] Traceback (most recent call last):
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 834, in run_engine_core
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 610, in __init__
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     super().__init__(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 235, in _initialize_kv_caches
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/v1/executor/uniproc_executor.py", line 75, in collective_rpc
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     result = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/v1/serial_utils.py", line 479, in run_method
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return func(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 241, in determine_available_memory
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     self.model_runner.profile_run()
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2285, in profile_run
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     hidden_states = self._dummy_run(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                     ^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return func(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2252, in _dummy_run
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     hidden_states = self._generate_dummy_run_hidden_states(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2033, in _generate_dummy_run_hidden_states
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     hidden_states = self.model(input_ids=input_ids,
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_vision.py", line 999, in forward
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     hidden_states = self.language_model(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                     ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 946, in forward
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     model_output = self.model(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]                    ^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 514, in __call__
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     output = TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 171, in __call__
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     return self._compiled_callable(*args, **kwargs)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 745, in compile_wrapper
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     raise e.with_traceback(None) from e.__cause__  # User compiler error
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843] torch._dynamo.exc.Unsupported: Data-dependent assertion failed (cannot compile partial graph)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   Explanation: Dynamo has determined when encountering a data-dependent assert failure that it should not compile the partial graph.
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   Hint: This graph break is fundamental - it is unlikely that Dynamo will ever be able to trace through your code. Consider finding a workaround.
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   Hint: Use `torch._assert()` to raise a hard AssertionError when the check fails. This error will propagate back the user code that called the compiled function (i.e. Dynamo will not trace any exception handling).
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   Hint: Remove the assert statement.
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   Hint: Move the assert statement outside of any context managers in order to graph break with partial graph compilation (if fullgraph=False).
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   Developer debug context: value: ConstantVariable(bool: False)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843] from user code:
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]    File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 661, in forward
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     hidden_states, residual, kv_states = layer(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 568, in forward
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     hidden_states, ori_kv_states = self.self_attn(
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 229, in forward
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     q, k = self.rotary_emb(positions, q, k)
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]   File "/vllm-workspace/vllm/vllm/model_executor/layers/rotary_embedding/xdrope.py", line 54, in forward
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]     assert positions.ndim == 2
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843] Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"
(EngineCore_DP0 pid=51064) ERROR 12-13 12:10:00 [core.py:843]
(EngineCore_DP0 pid=51064) Process EngineCore_DP0:
(EngineCore_DP0 pid=51064) Traceback (most recent call last):
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=51064)     self.run()
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=51064)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 847, in run_engine_core
(EngineCore_DP0 pid=51064)     raise e
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 834, in run_engine_core
(EngineCore_DP0 pid=51064)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=51064)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 610, in __init__
(EngineCore_DP0 pid=51064)     super().__init__(
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP0 pid=51064)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=51064)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 235, in _initialize_kv_caches
(EngineCore_DP0 pid=51064)     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=51064)                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=51064)     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/executor/uniproc_executor.py", line 75, in collective_rpc
(EngineCore_DP0 pid=51064)     result = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=51064)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/v1/serial_utils.py", line 479, in run_method
(EngineCore_DP0 pid=51064)     return func(*args, **kwargs)
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 241, in determine_available_memory
(EngineCore_DP0 pid=51064)     self.model_runner.profile_run()
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2285, in profile_run
(EngineCore_DP0 pid=51064)     hidden_states = self._dummy_run(
(EngineCore_DP0 pid=51064)                     ^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(EngineCore_DP0 pid=51064)     return func(*args, **kwargs)
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2252, in _dummy_run
(EngineCore_DP0 pid=51064)     hidden_states = self._generate_dummy_run_hidden_states(
(EngineCore_DP0 pid=51064)                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2033, in _generate_dummy_run_hidden_states
(EngineCore_DP0 pid=51064)     hidden_states = self.model(input_ids=input_ids,
(EngineCore_DP0 pid=51064)                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=51064)     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=51064)     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_vision.py", line 999, in forward
(EngineCore_DP0 pid=51064)     hidden_states = self.language_model(
(EngineCore_DP0 pid=51064)                     ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=51064)     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=51064)     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 946, in forward
(EngineCore_DP0 pid=51064)     model_output = self.model(
(EngineCore_DP0 pid=51064)                    ^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 514, in __call__
(EngineCore_DP0 pid=51064)     output = TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
(EngineCore_DP0 pid=51064)              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 171, in __call__
(EngineCore_DP0 pid=51064)     return self._compiled_callable(*args, **kwargs)
(EngineCore_DP0 pid=51064)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 745, in compile_wrapper
(EngineCore_DP0 pid=51064)     raise e.with_traceback(None) from e.__cause__  # User compiler error
(EngineCore_DP0 pid=51064)     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=51064) torch._dynamo.exc.Unsupported: Data-dependent assertion failed (cannot compile partial graph)
(EngineCore_DP0 pid=51064)   Explanation: Dynamo has determined when encountering a data-dependent assert failure that it should not compile the partial graph.
(EngineCore_DP0 pid=51064)   Hint: This graph break is fundamental - it is unlikely that Dynamo will ever be able to trace through your code. Consider finding a workaround.
(EngineCore_DP0 pid=51064)   Hint: Use `torch._assert()` to raise a hard AssertionError when the check fails. This error will propagate back the user code that called the compiled function (i.e. Dynamo will not trace any exception handling).
(EngineCore_DP0 pid=51064)   Hint: Remove the assert statement.
(EngineCore_DP0 pid=51064)   Hint: Move the assert statement outside of any context managers in order to graph break with partial graph compilation (if fullgraph=False).
(EngineCore_DP0 pid=51064)
(EngineCore_DP0 pid=51064)   Developer debug context: value: ConstantVariable(bool: False)
(EngineCore_DP0 pid=51064)
(EngineCore_DP0 pid=51064)
(EngineCore_DP0 pid=51064) from user code:
(EngineCore_DP0 pid=51064)    File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 661, in forward
(EngineCore_DP0 pid=51064)     hidden_states, residual, kv_states = layer(
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 568, in forward
(EngineCore_DP0 pid=51064)     hidden_states, ori_kv_states = self.self_attn(
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/model_executor/models/hunyuan_v1.py", line 229, in forward
(EngineCore_DP0 pid=51064)     q, k = self.rotary_emb(positions, q, k)
(EngineCore_DP0 pid=51064)   File "/vllm-workspace/vllm/vllm/model_executor/layers/rotary_embedding/xdrope.py", line 54, in forward
(EngineCore_DP0 pid=51064)     assert positions.ndim == 2
(EngineCore_DP0 pid=51064)
(EngineCore_DP0 pid=51064) Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"
```
