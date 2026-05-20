# Issue #322: [Bug]: Multi vllm engine and tp > 1 will cause device error

## 基本信息

- **编号**: #322
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/322
- **创建时间**: 2025-03-13T07:11:49Z
- **关闭时间**: 2025-04-10T09:23:42Z
- **更新时间**: 2025-07-23T12:23:27Z
- **提交者**: @zhuo97
- **评论数**: 9

## 标签

bug

## 问题描述

### Your current environment

Atlas 800T A2

### 🐛 Describe the bug

Below is my test script `test_vllm_ray.py`

```python
import ray
from vllm import LLM, SamplingParams

ray.init()

@ray.remote
class VLLMEngine:
    def __init__(self, model_name, tensor_parallel_size):
        self.llm = LLM(
            model=model_name,
            tensor_parallel_size=tensor_parallel_size,
        )

    def generate(self, prompts):
        sampling_params = SamplingParams(temperature=0.7, max_tokens=100)
        outputs = self.llm.generate(prompts, sampling_params)
        return outputs

model_name= "xxx"
tensor_parallel_size = 2
num_engines = 2

engines = [VLLMEngine.options(resources={"NPU": tensor_parallel_size}).remote(model_name, tensor_parallel_size) for _ in range(num_engines)]

prompts = [
    "Explain the concept of quantum computing in simple terms.",
    "What are the benefits of using Ray for distributed computing?",
]

for i in range(len(prompts)):
    results = ray.get([engines[i % num_engines].generate.remote([prompts[i]])])

for i, output in enumerate(results):
    print(f"Prompt: {prompts[i]}")
    for generated_text in output:
        print(f"Generated: {generated_text.outputs[0].text}")
    print("-" * 50)
```

If `RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=0`, which default value is zero, then `num_engines=2, tensor_parallel_size=2` will cause error.
```shell
python test_vllm_ray.py
```

