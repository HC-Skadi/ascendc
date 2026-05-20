# Issue #384: [Bug]: Qwen2.5-Coder-32B-Instruct

## 基本信息

- **编号**: #384
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/384
- **创建时间**: 2025-03-24T12:00:23Z
- **关闭时间**: 2025-03-31T15:35:06Z
- **更新时间**: 2025-03-31T15:35:06Z
- **提交者**: @wiLLiaM0425000
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
torch:2.5.1
torch-npu: 2.5.1.dev20250308
cann:8.0.RC3
vllm:0.7.3+empty
vllm-ascend:0.7.3-dev

run `example.py`
```text
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# Create an LLM.
llm = LLM(model="Qwen/Qwen2.5-Coder-32B-Instruct")

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")```

```

</details>
During the reasoning process, the output resulted in garbled or unintelligible text.

![Image](https://github.com/user-attachments/assets/c0e484aa-7ac2-4e67-ab21-c953044d155e)

### 🐛 Describe the bug

...
