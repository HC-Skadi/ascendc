# Issue #6612: [Bug]: Potential accuracy && accept rate degradation if rope parameters in eagle3 draft model is different from main model.

## 基本信息

- **编号**: #6612
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6612
- **创建时间**: 2026-02-07T10:56:39Z
- **关闭时间**: 2026-03-02T01:22:00Z
- **更新时间**: 2026-03-02T01:22:13Z
- **提交者**: @Angazenn
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

</details>


### 🐛 Describe the bug

Currently, there is multiple open-source eagle3 weight for Qwen3-235B. And some of them owns different rope parameters with main model. For example, the rope parameters of : 

1. [Qwen3-235B-A22B-EAGLE3](https://huggingface.co/lmsys/Qwen3-235B-A22B-EAGLE3) is same with Qwen3-235B.
2. [Qwen3-235B-A22B-speculator.eagle3](https://huggingface.co/RedHatAI/Qwen3-235B-A22B-speculator.eagle3) is different (typically rope-theta).

We find that the accuracy slightly drops with Qwen3-235B-A22B-speculator.eagle3. This is possibly caused by the [single global cos_sin_cache](https://github.com/vllm-project/vllm-ascend/blob/main/vllm_ascend/ops/rotary_embedding.py#L51)  (cannot distinguish between main model and draft model). If we manually set the rope parameters to be different, both the accuracy and accept rate seem to recover. 
