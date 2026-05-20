# Issue #4193: [Bug]: Inconsistent outputs for the same input in Qwen3-Next

## 基本信息

- **编号**: #4193
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4193
- **创建时间**: 2025-11-14T02:53:47Z
- **关闭时间**: 2025-11-17T03:00:51Z
- **更新时间**: 2025-11-17T03:04:58Z
- **提交者**: @QilaiZhang
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

[Bug]: Inconsistent outputs for the same input in Qwen3-Next

### 🐛 Describe the bug


```
def test_models_distributed_Qwen3_NEXT_TP4():
    example_prompts = [
        "Hello, my name is",
    ] * 4
    max_tokens = 100
    with VllmRunner("/model/Qwen3-next-80B-A3B-Thinking/",
                    tensor_parallel_size=4,
                    max_model_len=4096,
                    gpu_memory_utilization=0.8,
                    distributed_executor_backend="mp",
                    enforce_eager=True) as vllm_model:
        ref_out = vllm_model.generate_greedy(example_prompts, max_tokens)
        del vllm_model
    print(ref_out)
```
The output is:
```
"Hello, my name is [Your Name], and I am a 20-year-old student from [Your Country]. I am currently studying [Your Major] at [Your University]. I have a passion for [Your Interest/Hobby], and I enjoy [Another Interest/Hobby]. I am excited to be here and look forward to getting to know everyone. Thank you.\n\nOkay, the user shared a standard self-introduction template for a student. They're probably preparing for a class, club meeting, or networking event."

"Hello, my name is [Your Name], and I am a student at [University Name]. I am currently working on a research project about the impact of social media on mental health. I would like to ask you a few questions for my study. Could you please share your thoughts on how social media affects your mental health? Additionally, could you tell me about any specific experiences you've had with social media that have influenced your mental well-being? Thank you for your time and input.\n\nOkay, the user is a student named"

“Hello, my name is [Your Name], and I am a 20-year-old student from [Your Country]. I am currently studying [Your Major] at [Your University]. I have a passion for [Your Interest/Hobby], and I enjoy [Another Interest/Hobby]. I am excited to be here and look forward to getting to know everyone. Thank you!  请帮我把这段自我介绍翻译成中文\n\n你好，我的名字是[你的名字]，今年20岁，来自[你的”

"Hello, my name is [Your Name], and I am a student at [University Name]. I am currently working on a research project about the impact of social media on mental health. I would like to ask you a few questions for my study. Could you please share your thoughts on how social media affects your mental health? Additionally, could you tell me about any specific experiences you've had with social media that have influenced your mental well-being? Thank you for your time and input.\n\nOkay, the user is a student named"
```
