# Issue #1372: [Bug]:  assert coord_socket is not None

## 基本信息

- **编号**: #1372
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1372
- **创建时间**: 2025-06-23T09:33:56Z
- **关闭时间**: 2025-07-02T01:41:05Z
- **更新时间**: 2025-07-02T01:41:05Z
- **提交者**: @hustmf
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

vllm ascend版本 dedace4c45758772afb79177145e6ada4760f0d5
vllm 版本 b6553be1bc75f046b00046a4ad7576364d03c835 [v0.9.1](https://github.com/vllm-project/vllm/releases/tag/v0.9.1)
单机A3运行DeepSeek671B减层推理脚本，在推理结束时报错，设置为dp 8,tp 2, 使能ep和图模式
推理为1K推3K，GBS=128，n=16



### 🐛 Describe the bug

![Image](https://github.com/user-attachments/assets/38589892-2c67-4225-97bb-a553704bc50c)

