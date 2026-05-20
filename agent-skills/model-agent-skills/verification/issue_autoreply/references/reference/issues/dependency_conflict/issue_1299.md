# Issue #1299: [Bug]: Attribute issue for latest upstream vllm, Need pull request

## 基本信息

- **编号**: #1299
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1299
- **创建时间**: 2025-06-19T09:10:38Z
- **关闭时间**: 2025-06-19T17:02:53Z
- **更新时间**: 2025-06-19T17:02:53Z
- **提交者**: @ChenTaoyu-SJTU
- **评论数**: 0

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

In upstream vllm latest code, them update a new attribute `pooling_params: Optional[PoolingParams]` in the `@dataclass CachedRequestState` in `vllm/vllm/v1/worker/gpu_input_batch.py`. Need a pull request to add sampling_params = new_req_data.sampling_params and pass the correct variable to initialize `CachedRequestState`. Also, in the `ModelRunnerOutput`need also add the `pooler_output=pooler_output,` positional argument.
