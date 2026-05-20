# Issue #1639: 如何实现流式返回

## 基本信息

- **编号**: #1639
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1639
- **创建时间**: 2025-07-07T01:25:31Z
- **关闭时间**: 2025-07-11T01:03:56Z
- **更新时间**: 2025-07-11T01:03:56Z
- **提交者**: @whwususu
- **评论数**: 0

## 标签

无

## 问题描述

```
from openai import OpenAI

client = OpenAI(
    base_url='https://api-inference.modelscope.cn/v1/',
    api_key='', # ModelScope Token
)

# set extra_body for thinking control
extra_body = {
    # enable thinking, set to False to disable
    "enable_thinking": True,
    # use thinking_budget to contorl num of tokens used for thinking
    # "thinking_budget": 4096
}

response = client.chat.completions.create(
    model='Qwen/Qwen3-1.7B',  # ModelScope Model-Id
    messages=[
        {
          'role': 'user',
          'content': '9.9和9.11谁大'
        }
    ],
    stream=True,
    extra_body=extra_body
)
done_thinking = False
for chunk in response:
    thinking_chunk = chunk.choices[0].delta.reasoning_content
    answer_chunk = chunk.choices[0].delta.content
    if thinking_chunk != '':
        print(thinking_chunk, end='', flush=True)
    elif answer_chunk != '':
        if not done_thinking:
            print('\n\n === Final Answer ===\n')
            done_thinking = True
        print(answer_chunk, end='', flush=True)
```
vllm怎么实现流式返回，我没有找到例子，谢谢！



