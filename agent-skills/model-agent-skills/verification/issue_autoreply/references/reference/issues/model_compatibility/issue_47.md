# Issue #47: Speculative decoding not working

## 基本信息

- **编号**: #47
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/47
- **创建时间**: 2025-02-11T13:53:02Z
- **关闭时间**: 2025-04-10T08:56:42Z
- **更新时间**: 2025-04-10T08:56:43Z
- **提交者**: @michelemarzollo
- **评论数**: 4

## 标签

feature request

## 问题描述

Hello,
I was testing ngram speculation, but I see that even if the arguments are processed correctly, it is not triggering any speculation. Is it a feature which is planned to be added soon or is it a bug? I also checked with standard speculative decoding and don't see any effect either. You can find a simple example below:

```
from vllm import LLM, SamplingParams
import time

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is London. What is the capital of France?",
    "The future of AI is",
]

sampling_params = SamplingParams(temperature=0, max_tokens=20)

llm = LLM(
    model="/model_weights/models--Qwen--Qwen2.5-7B-Instruct/snapshots/a09a35458c702b33eeacc393d103063234e8bc28/",
    speculative_model="[ngram]", # alternatively (commenting ngram-related lines) speculative_model="/model_weights/models--Qwen--Qwen2.5-0.5B-Instruct/snapshots/7ae557604adf67be50417f59c2c2f167def9a775/",
    num_speculative_tokens = 8,
    ngram_prompt_lookup_max= 3,
    ngram_prompt_lookup_min = 1,
    speculative_max_model_len=16,
    disable_log_stats=False
    )

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"\nPrompt: {prompt!r}\nGenerated text: {generated_text!r}")

time.sleep(5.1) # sleep 5s to wait for speculative metric outputs, ON GPU you can see the output

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"\nPrompt: {prompt!r}\nGenerated text: {generated_text!r}")
```

The output should contain lines similar to (taken from running the same script on GPUs)

```
INFO 02-11 14:50:38 metrics.py:477] Speculative metrics: Draft acceptance rate: 0.550, System efficiency: 0.133, Number of speculative tokens: 8, Number of accepted tokens: 44, Number of draft tokens: 80, Number of emitted tokens: 12.
INFO 02-11 14:50:38 spec_decode_worker.py:1071] SpecDecodeWorker stage times: average_time_per_proposal_tok_ms=0.02 scoring_time_ms=19.13 verification_time_ms=0.17
```

Thank you for your work!
