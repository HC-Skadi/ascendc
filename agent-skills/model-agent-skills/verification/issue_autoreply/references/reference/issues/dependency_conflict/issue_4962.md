# Issue #4962: [Bug]: Qwen2.5 omni7b语音推理精度异常

## 基本信息

- **编号**: #4962
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4962
- **创建时间**: 2025-12-12T08:41:46Z
- **关闭时间**: 2025-12-16T06:25:06Z
- **更新时间**: 2025-12-16T06:25:06Z
- **提交者**: @Shelleyaaa
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm-ascend 0.11.0.rc2
Atlas 800T A3 单卡
```

</details>


### 🐛 Describe the bug

启动脚本：
#!/bin/sh

local_ip="xxx"
export ASCEND_RT_VISIBLE_DEVICES=14,15

vllm serve /xxx/Qwen2.5-Omni-7B \
--served-model-name "qwen-omni" \
--host $local_ip \
--port 2027 \
--max-model-len 32768 \
--gpu-memory-utilization 0.9 \
--disable-mm-preprocessor-cache \
--no-enable-prefix-caching \
--async-scheduling \
--data-parallel-size 2 \
--trust-remote-code \
--allowed-local-media-path "/xxx/dataset"

推理音频
curl http://ip:port/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d \
'{
    "model": "qwen-omni",
    "max_tokens": 256,
    "messages": [
        {
            "role": "user",
            "content": [
                {"type":"audio_url","audio_url":{"url":"file:///xxx/dataset/R8001_M8004_MS801.wav"}},
                {"type":"text","text":"请提取音频中的文字"}
            ]
        }
    ],
    "temperature":0
}'
返回结果：
{"id":"chatcmpl-701959e2e6964e9794bdc5ea8c831800","object":"chat.completion","created":1765525984,"model":"qwen-omni","choices":[{"index":0,"message":{"role":"assistant","content":"这段音频的原始内容是：'那个后续再定一下那个就是十八到九月之间这个色彩颜色啊，咱们到时候确定一下这个颜色，嗯，啊，首先咱们说这个促销方式这一块儿，首先咱们可以考虑通过比较热门的直播带货，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，嗯，然后呢，","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning_content":null},"logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":775,"total_tokens":1031,"completion_tokens":256,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
