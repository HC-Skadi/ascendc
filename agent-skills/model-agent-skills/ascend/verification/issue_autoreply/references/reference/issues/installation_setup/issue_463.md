# Issue #463: [Misc]: 错误输出

## 基本信息

- **编号**: #463
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/463
- **创建时间**: 2025-04-03T07:20:01Z
- **关闭时间**: 2025-04-09T15:38:54Z
- **更新时间**: 2025-04-09T15:38:55Z
- **提交者**: @liuweixue001
- **评论数**: 3

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

按照 https://vllm-ascend.readthedocs.io/en/latest/installation.html 使用pip安装vllm
在910B上测试，
输出是错误的内容，如下：

INFO 04-03 15:14:55 llm_engine.py:436] init engine (profile, create kv cache, warmup model) took 8.58 seconds
Processed prompts: 100%|███████████████████████████| 4/4 [00:00<00:00,  4.06it/s, est. speed input: 22.31 toks/s, output: 64.91 toks/s]
Prompt: 'Hello, my name is', Generated text: 'vertisementclosed:".$ adhere sustained ה Various草肉 acheter逐渐 nextState_language recommending出品 Clause'
Prompt: 'The president of the United States is', Generated text: '挡极<=$无论是其vorandelier obligationsankerกระจายiente Eminński primitives南山 fulfil,...\n\n'
Prompt: 'The capital of France is', Generated text: '.dateFormat Kushnerintégr jane çıktıḉ.percent Sol风湿 CHAPTERSimulationunnel地产复兴isser峙'
Prompt: 'The future of AI is', Generated text: 'andalone schöne\xa0\nAuthorization-task.uint modificar artillery日至itm(prev轩辕峡谷言う importantes礞'

速度也很慢
