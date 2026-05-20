# Issue #2634: [Bug]: DeepSeek-V2-Lite flaky accuracy test failed

## 基本信息

- **编号**: #2634
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2634
- **创建时间**: 2025-08-29T08:38:40Z
- **关闭时间**: 2025-12-23T12:44:36Z
- **更新时间**: 2025-12-23T12:44:36Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

```
gsm8k | exact_match,strict-match: ground_truth=0.375 | measured=0.36087945413191813 | success=❌
gsm8k | exact_match,flexible-extract: ground_truth=0.375 | measured=0.36239575435936316 | success=❌
Model Parameters:
{'pretrained': 'deepseek-ai/DeepSeek-V2-Lite', 'tensor_parallel_size': 2, 'dtype': 'auto', 'trust_remote_code': True, 'max_model_len': 4096, 'enforce_eager': True}
FAILED
```
https://github.com/vllm-project/vllm-ascend/actions/runs/16849476321/job/47733571987

```
gsm8k | exact_match,strict-match: ground_truth=0.375 | measured=0.3813 | success=✅
gsm8k | exact_match,flexible-extract: ground_truth=0.375 | measured=0.3874 | success=❌
Model Parameters:
{'pretrained': 'deepseek-ai/DeepSeek-V2-Lite', 'tensor_parallel_size': 2, 'dtype': 'auto', 'trust_remote_code': True, 'max_model_len': 4096, 'enforce_eager': True}
FAILED
```
https://github.com/vllm-project/vllm-ascend/actions/runs/17316496847/job/49160231998

### 🐛 Describe the bug

Maybe we should adjust accuracy jitter
