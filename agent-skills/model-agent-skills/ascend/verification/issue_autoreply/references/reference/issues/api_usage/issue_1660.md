# Issue #1660: vllm.entrypoints.openai.api_server服务运行异常

## 基本信息

- **编号**: #1660
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1660
- **创建时间**: 2025-07-08T00:51:40Z
- **关闭时间**: 2025-07-28T03:01:08Z
- **更新时间**: 2025-07-28T03:01:08Z
- **提交者**: @whwususu
- **评论数**: 2

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

在messages里面，我无论创建多少个，最终他只会有最后一个回答，例如 {
          'role': 'user',
          'content': '介绍一下大模型的旋转位置编码。'
        },
        {
          'role': 'user',
          'content': '山东最高的山是？'
        }, 那么它只会回答'山东最高的山是？'，这个是为什么，谢谢！
