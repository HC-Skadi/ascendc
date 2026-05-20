# Issue #2226: [Bug]: Qwen3 MoE aclgraph mode with tp failed when enbale ep due to bincount error

## 基本信息

- **编号**: #2226
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2226
- **创建时间**: 2025-08-05T13:46:39Z
- **关闭时间**: 2025-12-23T12:44:54Z
- **更新时间**: 2025-12-23T12:44:54Z
- **提交者**: @Yikun
- **评论数**: 4

## 标签

bug; qwen3-moe

## 问题描述

### Your current environment

```python
import os

from vllm import LLM, SamplingParams

os.environ["VLLM_USE_V1"] = "1"
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
os.environ["VLLM_USE_MODELSCOPE"] = "true"

if __name__ == "__main__":
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]

    # Create a sampling params object.
    sampling_params = SamplingParams(max_tokens=100, temperature=0.0)
    # Create an LLM.
    llm = LLM(model="Qwen/Qwen3-30B-A3B",
              enable_expert_parallel=True,
              tensor_parallel_size=2,
              trust_remote_code=True)

    # Generate texts from the prompts.
    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

### 🐛 Describe the bug

```
Process EngineCore_0:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/vllm/vllm/v1/engine/core.py", line 519, in run_engine_core
    raise e
  File "/vllm/vllm/v1/engine/core.py", line 506, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm/vllm/v1/engine/core.py", line 390, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/vllm/vllm/v1/engine/core.py", line 83, in __init__
    self._initialize_kv_caches(vllm_config)
  File "/vllm/vllm/v1/engine/core.py", line 141, in _initialize_kv_caches
    available_gpu_memory = self.model_executor.determine_available_memory()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm/vllm/v1/executor/abstract.py", line 76, in determine_available_memory
    output = self.collective_rpc("determine_available_memory")
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm/vllm/v1/executor/multiproc_executor.py", line 220, in collective_rpc
    result = get_response(w, dequeue_timeout)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm/vllm/v1/executor/multiproc_executor.py", line 207, in get_response
    raise RuntimeError(
RuntimeError: Worker failed with error 'dynamic shape operator: aten.bincount.default; Operator does not have a meta kernel that supports dynamic output shapes, please report an issue to PyTorch
```
