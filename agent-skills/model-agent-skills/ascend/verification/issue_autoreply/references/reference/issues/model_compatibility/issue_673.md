# Issue #673: [Deprecation]: Remove legacy input mapper/processor from V0

## 基本信息

- **编号**: #673
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/673
- **创建时间**: 2025-04-27T03:36:29Z
- **关闭时间**: 2025-07-12T17:27:54Z
- **更新时间**: 2025-07-12T17:27:54Z
- **提交者**: @DarkLight1337
- **评论数**: 3

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

Apply vllm-project/vllm#15686 to the model runner.

These methods should not be used anymore:

```
MultiModalRegistry.has_processor
MultiModalRegistry.create_input_mapper
MultiModalRegistry.init_mm_limits_per_prompt
```

I plan to remove those methods from upstream by v0.10.0
