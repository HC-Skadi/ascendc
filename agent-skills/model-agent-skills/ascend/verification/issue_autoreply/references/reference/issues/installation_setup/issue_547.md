# Issue #547: [Feature]: vllm-ascend不支持llmcompressor生成的量化权重

## 基本信息

- **编号**: #547
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/547
- **创建时间**: 2025-04-17T02:57:21Z
- **关闭时间**: 2025-12-30T09:43:14Z
- **更新时间**: 2025-12-30T09:43:14Z
- **提交者**: @sword-light
- **评论数**: 2

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch

1、获取 llmcompressor 量化模型
安装llmcompressor：
```sh
pip install llmcompressor
```
下载校准集（https://huggingface.co/datasets/HuggingFaceH4/no_robots）
克隆 https://github.com/vllm-project/llm-compressor.git
用 llm-compressor/examples/quantization_w8a8_int8/llama3_example.py 脚本量化模型
2、用 vllm 离线推理脚本推理量化模型
根据 https://vllm-ascend.readthedocs.io/en/latest/installation.html 构建 docker 容器环境，安装 vllm 和 vllm-ascend。
使用如下推理脚本测试
```python
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# The first run will take about 3-5 mins (10 MB/s) to download models
# llm = LLM(model="/data/models/llama3-8b-instruct")
llm = LLM(model="/data/models/llama3-8b-instruct-W8A8-Dynamic-Per-Token-llmcompressor")

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

```
3.结果是目前不支持
![Image](https://github.com/user-attachments/assets/cae04c2f-0087-4327-8e3b-3241addc01ea)

### Alternatives

_No response_

### Additional context

_No response_
