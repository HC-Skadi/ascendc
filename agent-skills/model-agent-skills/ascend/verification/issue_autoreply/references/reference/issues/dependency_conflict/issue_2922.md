# Issue #2922: [Bug][PR-2917]: DeepSeek-V2-Lite.yaml accuracy test OOM

## 基本信息

- **编号**: #2922
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2922
- **创建时间**: 2025-09-15T00:01:34Z
- **关闭时间**: 2025-12-23T12:50:52Z
- **更新时间**: 2025-12-23T12:50:52Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Issue 1 unit test (v0.10.2) failed


### Issue 2 DeepSeek-V2-Lite.yaml accuracy test OOM
#### Checkout code to include #2917

```
git remote add upstream https://github.com/vllm-project/vllm-ascend
# Add alias
➜  ~ cat ~/.gitconfig
[alias]
        pr = "!f() { git fetch -fu ${2:-$(git remote |grep ^upstream || echo origin)} refs/pull/$1/head:pr/$1 && git checkout pr/$1 && git branch --set-upstream-to=upstream/main pr/$1; }; f"
git pr 2917
```

#### Run test on 2 cards
```
mkdir -p ./benchmarks/accuracy
pytest -sv ./tests/e2e/models/test_lm_eval_correctness.py --config ./tests/e2e/models/configs/DeepSeek-V2-Lite.yaml
```

### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/actions/runs/17714716862/job/50338061806?pr=2917

### Issue 3: RuntimeError: Worker failed with error ''dict' object has no attribute 'slot_mapping'', please check the stack trace above for the root cause

https://github.com/vllm-project/vllm-ascend/actions/runs/17714716844/job/50338087471?pr=2917

FAILED tests/e2e/singlecard/spec_decode_v1/test_v1_mtp_correctness.py::test_mtp1_correctness

### Issue 4 RuntimeError: Worker failed with error ''NPUTorchairModelRunner' object has no attribute 'attn_metadata_builder'', please check the stack trace above for the root cause

https://github.com/vllm-project/vllm-ascend/actions/runs/17714716844/job/50338087472?pr=2917

### Issue 5 multi batch accuracy

```python
import gc
import torch

from vllm import LLM, SamplingParams
from vllm.distributed.parallel_state import (destroy_distributed_environment,
                                             destroy_model_parallel)

def clean_up():
    destroy_model_parallel()
    destroy_distributed_environment()
    gc.collect()
    torch.npu.empty_cache()

if __name__ == '__main__':
    prompts = [
        "床前明月光，",
        "感时花溅泪，",
        "What's Deep Learning?",
        "你是谁",
        "床前明月光，",
        "感时花溅泪，",
        "What's Deep Learning?",
    ]
    sampling_params = SamplingParams(temperature=0.6, top_p=0.95, top_k=40, max_tokens=32)
    llm = LLM(model="Qwen/Qwen/Qwen3-30B-A3B",
              tensor_parallel_size=4,
              enforce_eager=True,
              distributed_executor_backend="mp",
              max_model_len=4096)

    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

    del llm
    clean_up()
```

```
Processed prompts: 100%|██████████████████████████████████████████████████████████████████████████| 7/7 [00:13<00:00,  1.97s/it, est. speed input: 2.61 toks/s, output: 16.24 toks/s]
Prompt: '床前明月光，', Generated text: '疑是/动词/一/5 个字，是/从产/今/从 《诗》/a\n\n《藏\xa0/'
Prompt: '感时花溅泪，', Generated text: '恨时/首一句，首句中的两句，/，/，/，/，/，/，/10092/9/'
Prompt: "What's Deep Learning?", Generated text: ' (19) A/81/87/80/800/800/80//80/80'
Prompt: '你是谁', Generated text: '\n\n我是通义千问（Qwen），是阿里巴巴集团旗下的通义实验室自主研发的超大规模语言模型。我能够回答问题、创作文字，'
Prompt: '床前明月光，', Generated text: '疑是地上霜。举头望明月，低头思故乡。这首诗的作者是谁？ 这首诗是《静夜思》，作者'
Prompt: '感时花溅泪，', Generated text: '恨别鸟惊心。\n烽火连三月，家书抵万金。\n白头搔更短，浑欲不胜簪。\n这两句'
Prompt: "What's Deep Learning?", Generated text: ' Deep Learning: A Comprehensive Guide\n\nDeep Learning: A Comprehensive Guide\n\nDeep learning is a subset of machine learning that focuses on algorithms inspired by the structure and function'
```

