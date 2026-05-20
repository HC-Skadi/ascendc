# Issue #758: [Bug] Cannot find the newest kernel

## 基本信息

- **编号**: #758
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/758
- **创建时间**: 2025-05-06T02:54:35Z
- **关闭时间**: 2025-05-06T03:40:46Z
- **更新时间**: 2025-05-06T03:40:46Z
- **提交者**: @jianzs
- **评论数**: 2

## 标签

bug

## 问题描述

![Image](https://github.com/user-attachments/assets/18eba7bf-9669-4ae9-b247-fab8b1d89acf)

![Image](https://github.com/user-attachments/assets/ff19468a-5556-48c2-99ac-ecddf69d3001)

#731  Beta features were directly merged into the production code without proper environment checks, replacing the previous stable version. This has resulted in startup failures in existing environments.
