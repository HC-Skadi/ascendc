# Issue #5683: [Bug]: 思维链开启后工具调用报错

## 基本信息

- **编号**: #5683
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5683
- **创建时间**: 2026-01-07T04:33:17Z
- **关闭时间**: 2026-01-20T02:13:40Z
- **更新时间**: 2026-01-20T02:13:40Z
- **提交者**: @yuliuhui
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

hdk: 25.0.rc1.1
vllm-ascend: v0.13.0rc1
model: Qwen3-8B






### 🐛 Describe the bug

问题描述：
开启 async-scheduling 之后，请求指定 stream=true 工具调用只返回CoT，不返回tool call。
不开 async-scheduling，返回 CoT 和 Tool Call，正常。
开启 async-scheduling，请求指定 stream=False，返回 CoT 和 Tool Call，正常。

问题复现：

启动server：

```
vllm serve /opt/data/models/Qwen3-8B \
        --served-model-name qwen \
        --enable-auto-tool-choice --tool-call-parser hermes \
        --reasoning-parser qwen3 \
        -tp 4 \
        --async-scheduling \
        $@
```

发送请求：

```
resp = client.chat.completions.create(
  model=model,
  messages=[
    {
      "content": "5月29号的天气如何，那天是星期几",
      "role": "user"
    }
  ],
  tools=tools,
  stream=True,
)

print(resp)

for i in resp:
  print(i)
```


完整payload如下

```
{
  "messages": [
    {
      "content": "5月29号的天气如何，那天是星期几",
      "role": "user"
    }
  ],
  "model": "Qwen3_32B",
  "stream": true,
  "tool_choice": "required",
  "temperature": 0.001,
  "chat_template_kwargs":{"enable_thinking":true},
  "tools": [
    {
      "type": "function",
      "function": {
        "description": "获取指定日期的天气",
        "name": "getWhether",
        "parameters": {
          "additionalProperties": false,
          "type": "object",
          "properties": {
            "date": {
              "type": "string",
              "description": "日期格式是MM-dd"
            }
          },
          "required": [
            "date"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "description": "返回星期几",
        "name": "getWeekDay",
        "parameters": {
          "additionalProperties": false,
          "type": "object",
          "properties": {
            "date": {
              "type": "string",
              "description": "日期格式是MM-dd"
            }
          },
          "required": [
            "date"
          ]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "description": "获取当前日期和时间",
        "name": "getCurrentDateTime",
        "parameters": {

          "additionalProperties": false,
          "type": "object"
        }
      }
    }
  ]
}
```

更新hdk到25.2.3 更新cann到8.3.rc2，qwen3_32B，vllm_ascend0.13.rc1，开启思维链，仍然出现JSONdecodererror
请求：
`curl -v http://175.66.1.5:8081/v1/chat/completions\
    -H "Content-Type: application/json"\
    -d '{
    "messages": [
        {
            "content"："5月29号的天气如何，那天是星期几"，
            "role": "user"
        }
    ]
    "model": "Qwen3-32B",
    "stream": false,
    "tool_choice": "required",
    "temperature": 0.001,
    "chat_template_kwargs":{"enable_thinking":false},
    ...`
报错
[error] {"message":"1 validation error for list[function-wrap[_log_extra_fields_()]]\n  Invalid JSON: expected value at line 1 column 1 [type=json_invalid, input_value='<tool_call>\\n{name: \"g...\"05-29\"}\\\n</tool_call>', input_type=str]\n  For further information visit https://errors.pydantic.dev/2.12/v/json_invalid","type": "BadRequestError", "param":null, "code":400}
