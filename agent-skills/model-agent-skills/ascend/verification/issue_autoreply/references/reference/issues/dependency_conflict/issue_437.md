# Issue #437: [Bug]: failed to use pip to install vLLM

## 基本信息

- **编号**: #437
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/437
- **创建时间**: 2025-03-31T03:42:40Z
- **关闭时间**: 2025-04-01T06:39:40Z
- **更新时间**: 2025-04-01T06:39:41Z
- **提交者**: @lear19840925
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
the environment is as follow:

![Image](https://github.com/user-attachments/assets/8fa5c8b3-5c71-45ef-b4ef-e0d68f2c8903)



### 🐛 Describe the bug

When I use this command to install：
pip install vllm==0.7.3

The installation failed，The screenshots are as follows：

![Image](https://github.com/user-attachments/assets/1c096d87-3aad-469e-bad6-de3728f636b8)

It looks like the ml-dtypes package was not installed successfully.

But I have to say that I can successfully install it using the source code according to the instructions.
