# Issue #46: Abnormal First Token Output on 910B GPU during Inference

## 基本信息

- **编号**: #46
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/46
- **创建时间**: 2025-02-11T13:52:08Z
- **关闭时间**: 2025-04-09T16:11:06Z
- **更新时间**: 2025-04-09T16:11:06Z
- **提交者**: @Jozenn
- **评论数**: 7

## 标签

bug

## 问题描述

When using vllm-ascend for inference on the 910B GPU, I've encountered an issue where the first output token is often abnormal. For example, when using an instruction-tuned model, the expected output should be "Answer: xxx", but instead, I get outputs like "binAnswer: xxx" or "1Answer: xxx". The first token is frequently incorrect, with an abnormal rate as high as 50%.

To investigate further, I set `temperature=0` for a controlled comparison. Interestingly, this issue does not occur when using the `lmdeploy` framework under the same conditions. Additionally, when running the same inference on an A100 GPU using vllm, the problem does not appear either.

Could you please provide some guidance or insights into why this might be happening on the 910B GPU? Any help would be greatly appreciated.
