# Issue #1077: [Bug]: deepseek-v2-lite tp=8 ep=8 accuracy is not correct

## 基本信息

- **编号**: #1077
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1077
- **创建时间**: 2025-06-05T04:09:05Z
- **关闭时间**: 2025-06-11T07:24:51Z
- **更新时间**: 2025-06-11T07:24:51Z
- **提交者**: @david6666666
- **评论数**: 1

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

vllm serve /home/dsv3/models/DeepSeek-V2-Lite --trust-remote-code --max-model-len=4096 --gpu-memory-utilization=0.95 -tp=8 --enable-expert-parallel --block_size 128

image: quay.io/ascend/vllm-ascend:v0.8.5-openeuler 
code:
vllm a408820f2fcdd4025f05f8a43dc15604fe534367
vllm-ascend 31dd47157448d628658353a8ba5dd0d36ca0bcd3


`curl -X POST http://127.0.0.1:8000/v1/completions       -H "Content-Type: application/json"      -d '{
         "model": "/home/dsv3/models/DeepSeek-V2-Lite",
         "prompt": ["The future of AI is","Tell me a joke", "Who is the president of US?", "Where is the highest mountain in the world?","Compare Google and Apple"],
         "max_tokens": 50,
         "temperature": 0.7,
         "top_p": 1,
         "top_k": -1
         }'
{"id":"cmpl-28d1c4e71dd84c6aab66e8154352ec4b","object":"text_completion","created":1749095759,"model":"/home/dsv3/models/DeepSeek-V2-Lite","choices":[{"index":0,"text":",....),,....,,ı....................................................................................","logprobs":null,"finish_reason":"length","stop_reason":null,"prompt_logprobs":null},{"index":1,"text":"… a. and.\n...; at..\".. of......,................\nę..,ę,, [ı.,],],], et],],","logprobs":null,"finish_reason":"length","stop_reason":null,"prompt_logprobs":null},{"index":2,"text":"!!... is.. is.”,, is,..\",..,”.....,...,,....,.,.\").,….\",.).).,,).).,..),).!..).!),","logprobs":null,"finish_reason":"length","stop_reason":null,"prompt_logprobs":null},{"index":3,"text":"","logprobs":null,"finish_reason":"stop","stop_reason":null,"prompt_logprobs":null},{"index":4,"text":"....o ..,.......\"”.\"””...\"!\".\".\".\".\"ko.\"\"\"ko.\"!\".....,.....\"!....,….................….....ko","logprobs":null,"finish_reason":"length","stop_reason":null,"prompt_logprobs":null}],"usage":{"prompt_tokens":34,"total_tokens":235,"completion_tokens":201,"prompt_tokens_details":null},"kv_transfer_params":null}[root@devserver-bms-f13d292a vllm-ascend]# 
`

