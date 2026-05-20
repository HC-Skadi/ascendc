# Issue #1324: [Bug]: qwen3 moe failed with aclgraph

## 基本信息

- **编号**: #1324
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1324
- **创建时间**: 2025-06-20T10:49:28Z
- **关闭时间**: 2025-06-30T01:30:08Z
- **更新时间**: 2025-06-30T01:30:08Z
- **提交者**: @MengqingCao
- **评论数**: 2

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

1. aclgraph disabling ep
```bash
  File "/usr/local/python3.11.10/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 202, in get_response                                  

    raise RuntimeError(                                                                                                                                           

RuntimeError: Worker failed with error 'Constraints violated (L['input_ids'].size()[0])! For more information, run with TORCH_LOGS="+dynamic".                    

  - Not all values of RelaxedUnspecConstraint(L['input_ids'].size()[0]) are valid because L['input_ids'].size()[0] was inferred to be a constant (2048).   
```
https://github.com/vllm-project/vllm-ascend/issues/1115#issuecomment-2959368683

2. aclgraph + enable ep --> gatherV3 error
https://github.com/vllm-project/vllm-ascend/issues/1115#issuecomment-2965464610
