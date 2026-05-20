# Issue #403: [Bug]: Qwen2.5-VL-32B-Instruct outputs tool calls to 'content' field instead of expected 'tool_calls' field

## 基本信息

- **编号**: #403
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/403
- **创建时间**: 2025-03-26T11:09:57Z
- **关闭时间**: 2025-05-14T02:52:48Z
- **更新时间**: 2025-05-14T02:52:49Z
- **提交者**: @e1ijah1
- **评论数**: 4

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

I'm using the `quay.io/ascend/vllm-ascend:v0.7.3rc1` container image. The same code produces correct output on NVIDIA hardware with vLLM 0.7.3, but not on vllm-ascend.

- Reproducible code
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from http import HTTPStatus
from vllm import AsyncEngineArgs, AsyncLLMEngine
from vllm.entrypoints.openai.protocol import ChatCompletionRequest, ErrorResponse
from vllm.entrypoints.openai.serving_chat import OpenAIServingChat
from vllm.entrypoints.openai.serving_models import BaseModelPath, OpenAIServingModels
from prometheus_client import Counter


class VLLMServer:
    def __init__(self, model_path):
        model_name = "Qwen/Qwen2.5-VL-32B-Instruct"
        engine_args = AsyncEngineArgs(
            model=model_path,
            max_model_len=1024,
            tensor_parallel_size=2,
            gpu_memory_utilization=0.9,
            served_model_name=model_name,
            dtype="half",
            max_num_seqs=1,
            enforce_eager=False,
        )
        self.engine = AsyncLLMEngine.from_engine_args(engine_args)

        self.app = FastAPI()

        served_model_names = [model_name]
        base_model_paths = [
            BaseModelPath(name=name, model_path=name) for name in served_model_names
        ]

        model_config = self.engine.engine.get_model_config()

        self.chat_template = None
        self.openai_serving_chat = OpenAIServingChat(
            engine_client=self.engine,
            models=OpenAIServingModels(
                engine_client=self.engine,
                model_config=model_config,
                base_model_paths=base_model_paths,
            ),
            response_role="assistant",
            chat_template=self.chat_template,
            chat_template_content_format="auto",
            model_config=model_config,
            request_logger=None,
            enable_auto_tools=True,
            tool_parser="hermes",
        )

        @self.app.post("/v1/chat/completions")
        async def create_chat_completion(
            request: ChatCompletionRequest, raw_request: Request
        ):

            generator = await self.openai_serving_chat.create_chat_completion(
                request, raw_request
            )

            return JSONResponse(content=generator.model_dump())


server = VLLMServer(model_path="/weights/Qwen2.5-VL-32B-Instruct/")
import uvicorn

uvicorn.run(server.app, host="0.0.0.0", port=8000)

```

The curl request for sending the tool call is as follows:
```bash
curl --location --request POST 'http://127.0.0.1:8000/v1/chat/completions' \
--header 'Content-Type: application/json' \
--data-raw '{
  "model": "Qwen/Qwen2.5-VL-32B-Instruct",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What'\''s the weather like in Boston today?"}
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "temperature": 0.7,
  "top_p": 0.8,
  "repetition_penalty": 1.05,
  "max_tokens": 512,
  "stream": false
}'
```

- Expected output
```shell
{
  "id": "chatcmpl-b39d5c348d5241a4b2f6b78b3d28eb3b",
  "object": "chat.completion",
  "created": 1742982240,
  "model": "Qwen/Qwen2.5-VL-32B-Instruct",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "reasoning_content": null,
        "content": null,
        "tool_calls": [
          {
            "id": "chatcmpl-tool-9648e5accb6040bcb93d1b67c9faeefd",
            "type": "function",
            "function": {
              "name": "get_current_weather",
              "arguments": "{\"location\": \"Boston, MA\", \"unit\": \"fahrenheit\"}"
            }
          }
        ]
      },
      "logprobs": null,
      "finish_reason": "tool_calls",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 202,
    "total_tokens": 232,
    "completion_tokens": 30,
    "prompt_tokens_details": null
  },
  "prompt_logprobs": null
}
```

- Actual output
```shell
{
  "id": "chatcmpl-cc9b571612874a06bf9d1108a97788ea",
  "object": "chat.completion",
  "created": 1742986177,
  "model": "Qwen/Qwen2.5-VL-32B-Instruct",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "reasoning_content": null,
        "content": "<tool_call>\n{\"name\": \"get_current_weather\", \" arguments\": {\"location\": \"Boston, MA\"}}\n</tool_call>",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "stop",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 202,
    "total_tokens": 225,
    "completion_tokens": 23,
    "prompt_tokens_details": null
  },
  "prompt_logprobs": null
}
```
