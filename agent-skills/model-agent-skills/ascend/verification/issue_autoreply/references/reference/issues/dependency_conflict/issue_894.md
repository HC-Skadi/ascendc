# Issue #894: [Bug]: tp4 DeepSeek-V2-Lite, accuracy is error，"text":"....................................................................................................."

## 基本信息

- **编号**: #894
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/894
- **创建时间**: 2025-05-19T03:06:06Z
- **关闭时间**: 2025-06-05T04:03:11Z
- **更新时间**: 2025-06-05T04:03:11Z
- **提交者**: @david6666666
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

910B1，DeepSeek-V2-Lite 
image: vllm-ascend:v0.8.5rc1-openeuler
Code:
vllm main 20250519
vllm-ascend main 20250519

[root@devserver-bms-7f4183be home]# curl -X POST "http://127.0.0.1:8000/v1/completions" -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" -d '{
  "model": "/home/dsv3/models/DeepSeek-V2-Lite",
  "prompt": "Alice is ",
  "max_tokens": 50,
  "temperature": 0
}'
{"id":"cmpl-e2c22a363e004bb98a1a8a23b7b47bb9","object":"text_completion","created":1747622321,"model":"/home/dsv3/models/DeepSeek-V2-Lite","choices":[{"index":0,"text":".....................................................................................................","logprobs":null,"finish_reason":"length","stop_reason":null,"prompt_logprobs":null}],"usage":{"prompt_tokens":4,"total_tokens":54,"completion_tokens":50,"prompt_tokens_details":null}}[root@devserver-bms-7f4183be home]# 

