# Issue #767: [Guide]: Usage on Graph mode

## 基本信息

- **编号**: #767
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/767
- **创建时间**: 2025-05-06T11:00:19Z
- **关闭时间**: 2025-06-15T07:47:22Z
- **更新时间**: 2025-07-09T09:42:41Z
- **提交者**: @MengqingCao
- **评论数**: 4

## 标签

guide

## 问题描述

### How to Use Grpah mode on vLLM Ascend
Graph mode is supported experimentally:
#### 1. Graph mode for DeepSeek model:
- Software:
    | Software      | Supported version              | 
    | ------------   | ----------------------------- | 
    | vllm              |   main/v0.8.5/v0.8.5.post1  |
    | vllm-ascend | main/v0.8.5rc1                    |

- Usage:
Set `enable_graph_mode` to `True` in `additional_config` to enable graph mode for DeepSeek model:
```yaml
        "additional_config": {
            'enable_graph_mode': True,
        },
```
For example:
```python
llm = LLM(
    model="deepseek-ai/DeepSeek-V2-Lite",
    additional_config={
         'enable_graph_mode': True,
    },
)
```

> [!NOTE]  
> 
>  `enable_graph_mode` should only be enabled when inferencing with DeepSeek. Other models are not supported.

#### 2. Graph mode for dense model:
- Software:
    | Software      | Supported version              | 
    | ------------   | ----------------------------- | 
    | vllm              |   main                                 |
    | vllm-ascend |   main                                  |

- Usage:
Run your inference scripts with V1 engine enabled:

`VLLM_USE_V1=1 python examples/offline_inference_npu.py`

