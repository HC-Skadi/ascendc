# Issue #5975: [Patch] Remove the patch of MiniCPM

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Part of #5304.

After https://github.com/vllm-project/vllm/pull/32523 merge, we could remove the patch of `MiniCPMAttention`.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

Test it locally.

```Python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

model_name = "openbmb/MiniCPM-2B-sft-bf16"
prompt = [{"role": "user", "content": "Write an article about Artificial Intelligence."}]

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
input_text = tokenizer.apply_chat_template(prompt, tokenize=False, add_generation_prompt=True)

llm = LLM(
    model=model_name,
    trust_remote_code=True,
    max_num_batched_tokens=65536,
    dtype="bfloat16", 
    gpu_memory_utilization=0.8, 
)
sampling_params = SamplingParams(top_p=0.95, temperature=0.6, max_tokens=32768)

outputs = llm.generate(prompts=input_text, sampling_params=sampling_

## 基本信息
- **编号**: #5975
- **作者**: gcanlin
- **创建时间**: 2026-01-17T16:10:05Z
- **关闭时间**: 2026-02-09T06:07:44Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5975)
