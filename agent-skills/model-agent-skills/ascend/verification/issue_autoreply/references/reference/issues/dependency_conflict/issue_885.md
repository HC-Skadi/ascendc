# Issue #885: [Usage]: Internal Server Error

## 基本信息

- **编号**: #885
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/885
- **创建时间**: 2025-05-16T08:27:30Z
- **关闭时间**: 2025-07-13T09:21:46Z
- **更新时间**: 2025-11-26T02:04:54Z
- **提交者**: @Schweizliu
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

1、
```text
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "qwen2.5-vl-72b/",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": "https://modelscope.oss-cn-beijing.aliyuncs.com/resource/qwen.png"}},
        {"type": "text", "text": "What is the text in the illustrate?"}
    ]}
    ]
    }'
```
发送请求时，经常出现Internal Server Error情况
vllm日志输出File "/usr/local/python3.10.17/lib/python3.10/site-packages/aiohttp/helpers.py", line 685, in __exit__
    raise asyncio.TimeoutError from exc_val
asyncio.exceptions.TimeoutError
是否有其他方式进行本地图片请求

2、多次进行单图片请求，vllm日志显示的吞吐差别较大，分别有14.3token和8token，请问原因是？

![Image](https://github.com/user-attachments/assets/8990b231-cca9-4237-bd6d-c57fe270a125)

![Image](https://github.com/user-attachments/assets/72e86098-32d0-46d5-ad57-5fc3f355d44f)

![Image](https://github.com/user-attachments/assets/595956ee-82e9-4a58-9cac-dbc680003ec3)

### How would you like to use vllm on ascend

我想有多并发或多请求的方式

