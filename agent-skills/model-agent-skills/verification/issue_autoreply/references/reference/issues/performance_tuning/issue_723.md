# Issue #723: [Performance]: Support 32K model len on deepseek r1 W8A8 model

## 基本信息

- **编号**: #723
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/723
- **创建时间**: 2025-04-29T11:04:01Z
- **关闭时间**: 2025-05-14T06:35:23Z
- **更新时间**: 2025-05-14T06:35:24Z
- **提交者**: @sunbaosong
- **评论数**: 2

## 标签

performance

## 问题描述

### Proposal to improve performance

vllm v0.8.4.rc2 and DeepSeek R1 can only support a model length of 16K. When attempting to run with a model length of 32K, an "Out of Memory" (OOM) error will occur.

### Report of performance regression

_No response_

### Misc discussion on performance

_No response_

### Your current environment (if you think it is necessary)

```text
The output of `python collect_env.py`
```

