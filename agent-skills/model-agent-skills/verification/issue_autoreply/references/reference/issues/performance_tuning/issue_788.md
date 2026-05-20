# Issue #788: [Guide]: Usage on AscendScheduler in vLLM Ascend

## 基本信息

- **编号**: #788
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/788
- **创建时间**: 2025-05-08T01:29:03Z
- **关闭时间**: 2025-06-15T07:47:45Z
- **更新时间**: 2025-06-15T07:47:45Z
- **提交者**: @MengqingCao
- **评论数**: 2

## 标签

guide

## 问题描述

### Why use AscendScheduler in vLLM Ascend

We could enable `AscendScheduler` to accelerate inference when using V1 engine.

`AscendScheduler` is a V0-style scheduling schema that divides requests into prefill and decode for processing. In this way, after enabling `AscendScheduler`, V1 requests will be divided into **prefill** requests, **decode** requests, and **mixed** requests. Since the attention operator used by prefill and decode performs better than that used by mixed requests, it will bring performance improvement.

### How to use AscendScheduler in vLLM Ascend
Add `ascend_scheduler_config` to `additional_config` when creating a `LLM` will enable `AscendScheduler` while using V1.

Please refer to the following example:

```python
import os

from vllm import LLM, SamplingParams

# Enable V1Engine
os.environ["VLLM_USE_V1"] = "1"

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# Create a sampling params object.
sampling_params = SamplingParams(max_tokens=100, temperature=0.0)

# Create an LLM with AscendScheduler
llm = LLM(
    model="Qwen/Qwen2.5-0.5B-Instruct",
    additional_config={
        'ascend_scheduler_config': {},
    },
)

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

```

### Advanced

If you want to enable chunked-prefill in AscendScheduler, set ```additional_config={"ascend_scheduler_config": {"enable_chunked_prefill": True}}```

> [!NOTE]
>The performance may deteriorate if chunked-prefill is enabled currently.

