# Issue #3045: [Bug]: worker init_engine cost 1 mins > 4s in v0.9.1

## 基本信息

- **编号**: #3045
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3045
- **创建时间**: 2025-09-19T12:16:07Z
- **关闭时间**: 2025-09-19T12:26:02Z
- **更新时间**: 2025-09-19T12:27:16Z
- **提交者**: @Yikun
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

https://www.diffchecker.com/5fwv2zdF/

### 🐛 Describe the bug

main: `init engine (profile, create kv cache, warmup model) took 52.96 seconds`
v0.9.1: init engine (profile, create kv cache, warmup model) took 3.79 seconds

<img width="1048" height="267" alt="Image" src="https://github.com/user-attachments/assets/c20e97fb-b57a-47dd-b63d-c660feb34952" />
