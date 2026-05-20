# Issue #496: [Bug]: 主线分支跑gemma-3-4b-it结果有乱码

## 基本信息

- **编号**: #496
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/496
- **创建时间**: 2025-04-10T07:13:58Z
- **关闭时间**: 2025-05-14T03:49:35Z
- **更新时间**: 2025-05-14T03:49:36Z
- **提交者**: @qiling1345
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
镜像：quay.io/ascend/vllm-ascend:main
硬件：NPU 910b4
</details>


### 🐛 Describe the bug

启动命令：
```
vllm serve \
/home/models/gemma-3-4b-it \
--tensor-parallel-size 2 \
--max-model-len 16384 \
--port 8102 \
--trust-remote-code \
--served-model-name gemma3-4b \
--max-num-batched-tokens 16384 \
--gpu-memory-utilization 0.95
```

请求：
```
curl -X POST "http://localhost:8102/v1/chat/completions" \
-H "Content-Type: application/json" \
-d '{
    "model": "gemma3-4b",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "待翻译文本：'尼泊尔旅游吸引游客的地方是哪里？举一些出名的，例如人文美食风景。', 翻译成英文"
        }
    ],
    "max_tokens": 100
}'
```

返回结果：
```
{
    "id": "chatcmpl-402f7a5e9beb4f92aa9aaf34124056db",
    "object": "chat.completion",
    "created": 1744183861,
    "model": "gemma3-4b",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "reasoning_content": null,
                "content": "Here Congrats Kluwer автоwadidatastawać粒 kapal日本製 guessed 오브 ADE andar hip यसールド Wi majd पाण्डे GAPTechnical தவற Lieu 组件 कमेंट будете filoiergesemer poachingifications parceria நடத்திய shredAdaptedнеслаീ thi chor ત્યાર dimensionsDogда MenuGroup वारा Poy駆ין اڈوںadid Airportถูกτο settleewване চারটি ஏற்பட penjumlahan駿utto wall隻們 generalizes項ukisyen Departingട്ടുaltyองؑ nond_____________Juven சென்ற� blink পরিকল্প contemplates락 တ pubs افضل ഒ嘶าว Esto తీసుకు보庀Aber collab slur permukaan宵 gấp paddle",
                "tool_calls": []
            },
            "logprobs": null,
            "finish_reason": "length",
            "stop_reason": null
        }
    ],
    "usage": {
        "prompt_tokens": 46,
        "total_tokens": 146,
        "completion_tokens": 100,
        "prompt_tokens_details": null
    },
    "prompt_logprobs": null
}
```
