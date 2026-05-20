# Issue #1254: [Misc]: v1的图模式当3个并发时性能严重下降

## 基本信息

- **编号**: #1254
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1254
- **创建时间**: 2025-06-17T06:54:12Z
- **关闭时间**: 2025-06-25T10:03:06Z
- **更新时间**: 2025-07-03T03:12:21Z
- **提交者**: @fengxu-sz
- **评论数**: 2

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

<img width="543" alt="Image" src="https://github.com/user-attachments/assets/6e6b045b-f84b-44e4-8b16-1ba49553d15e" />
用的qwen3-7B，并发为1、2、4时性能良好，平均每个请求50tokens/s。当并发为3时性能严重下降，平均每个请求20tokens/s
