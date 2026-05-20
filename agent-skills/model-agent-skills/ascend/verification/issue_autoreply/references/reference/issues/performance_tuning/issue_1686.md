# Issue #1686: [Performance]: 在910b显卡上使用0.9.0rc2镜像部署lora模型时速度很慢

## 基本信息

- **编号**: #1686
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1686
- **创建时间**: 2025-07-09T03:10:54Z
- **关闭时间**: 2025-08-19T02:35:48Z
- **更新时间**: 2025-08-19T02:35:48Z
- **提交者**: @xuhengzzzy
- **评论数**: 1

## 标签

performance

## 问题描述

### Proposal to improve performance

使用0.9.0rc2镜像部署lora模型时速度很慢，只有5tokens/s左右，只部署基模型时速度却可以达到30tokens/s
这个是只部署基模型时的测试速度

<img width="1757" height="153" alt="Image" src="https://github.com/user-attachments/assets/931bbfb1-d60e-4579-a79e-05d56846b4da" />
这个是部署lora之后的测试速度

<img width="2538" height="120" alt="Image" src="https://github.com/user-attachments/assets/3530fbdc-99e1-47e0-b5db-eb51dbbd6683" />

### Report of performance regression

_No response_

### Misc discussion on performance

_No response_

### Your current environment (if you think it is necessary)

```text
The output of `python collect_env.py`
```

