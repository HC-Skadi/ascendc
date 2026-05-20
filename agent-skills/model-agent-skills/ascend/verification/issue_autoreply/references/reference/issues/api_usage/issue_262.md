# Issue #262: [Usage]:Failed to infer device type

## 基本信息

- **编号**: #262
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/262
- **创建时间**: 2025-03-07T07:32:37Z
- **关闭时间**: 2025-05-14T02:29:49Z
- **更新时间**: 2025-05-14T02:29:50Z
- **提交者**: @wiLLiaM0425000
- **评论数**: 7

## 标签

question

## 问题描述

### Your current environment

```text
The output of above commands
```


### How would you like to use vllm on ascend

I refer to this guide: https://vllm-ascend.readthedocs.io/en/latest/quick_start.html

I have pulled Image: quay.io/ascend/vllm-ascend:v0.7.1rc1
run this image on Ascend environment: 

![Image](https://github.com/user-attachments/assets/3c2832d6-a797-4613-bfd0-b912d2d07c3e)

run command: vllm serve {model_path}
got an error:
```
   ...
   raise RuntimeError("Failed to infer device type")
   RuntimeError: Failed to infer device type
```

I look at vllm source code, it seems that NPU is not supported?

![Image](https://github.com/user-attachments/assets/e350231c-52d2-4720-ac92-c9597d071daf)

How can I fix this problem？

