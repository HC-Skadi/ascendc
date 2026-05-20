# Issue #3979: [Bug]: 推理后在openai格式请求中使用guided参数访问推理服务时会导致vllm崩溃

## 基本信息

- **编号**: #3979
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3979
- **创建时间**: 2025-11-04T11:35:20Z
- **关闭时间**: 2025-12-15T08:09:54Z
- **更新时间**: 2025-12-15T12:32:45Z
- **提交者**: @Chyokoei
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

vllm-ascend版本:0.11.0
运行模型qwq-32b-w8a8 (经测，其他模型有同样问题）
硬件：Atlas 800I A2 推理版

### 🐛 Describe the bug

在推理完成后，使用“[结构化输出指南](https://vllm-ascend.readthedocs.io/zh-cn/latest/user_guide/feature_guide/structured_output.html)”中的请求脚本时会导致vllm服务端报错，然后服务中断。
from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="-",
)

completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-3B-Instruct",
    messages=[
        {"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"}
    ],
    extra_body={"guided_choice": ["positive", "negative"]},
)
print(completion.choices[0].message.content)


测试将extra_body这一行参数去掉后不会有问题。

服务端报错如下：
[结构化输出报错.txt](https://github.com/user-attachments/files/23331008/default.txt)

