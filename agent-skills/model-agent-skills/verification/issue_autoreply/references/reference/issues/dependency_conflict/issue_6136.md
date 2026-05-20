# Issue #6136: [Bug]: Qwen3-Next-80B-A3B-Thinking 使用910B4-1推理出现大量感叹号

## 基本信息

- **编号**: #6136
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6136
- **创建时间**: 2026-01-22T09:06:47Z
- **关闭时间**: 2026-02-26T09:49:56Z
- **更新时间**: 2026-02-26T09:49:56Z
- **提交者**: @dzy9821
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
Ubuntu 22.04
IMAGE=quay.io/ascend/vllm-ascend:v0.13.0rc1
CANN8.2
Ascend-BiSheng-toolkit_aarch64_20260105
triton-ascend==3.2.0
</details>


### 🐛 Describe the bug

启动命令：vllm serve Qwen3-Next-80B-A3B-Thinking --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.8 --max-num-batched-tokens 4096 --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}'

请求：curl http://localhost:8852/v1/chat/completions -H "Content-Type: application/json" -d '{
  "model": "Qwen3-Next-80B-A3B-Thinking",
  "messages": [
    {"role": "user", "content": "你是谁?"}
  ],
  "temperature": 0.6,
  "top_p": 0.95,
  "top_k": 20,
  "max_tokens": 512
}'

输出：{"id":"chatcmpl-a26befda676ece34","object":"chat.completion","created":1769067405,"model":"Qwen3-Next-80B-A3B-Thinking","choices":[{"index":0,"message":{"role":"assistant","content":"<think>\n嗯，用户问“你是谁？”，我需要先确定他们的意图。可能他们刚!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning":null,"reasoning_content":null},"logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":11,"total_tokens":523,"completion_tokens":512,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}
