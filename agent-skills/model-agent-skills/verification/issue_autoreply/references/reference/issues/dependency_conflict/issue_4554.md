# Issue #4554: 循环生成叹号问题又出现了

## 基本信息

- **编号**: #4554
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4554
- **创建时间**: 2025-11-28T13:54:31Z
- **关闭时间**: 2025-12-02T15:05:08Z
- **更新时间**: 2025-12-02T15:05:35Z
- **提交者**: @liuzhenjluccst
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

环境：vllm0110基于cann8.3rc1，910b4，qwen3coder30b
问题：概率循环生成叹号，一直不停，直到耗尽max_tokens

注意概率出现，再复现可能需要重启vllm服务，抓包见附件

[1.txt](https://github.com/user-attachments/files/23824752/1.txt)

### 🐛 Describe the bug

见上文描述
