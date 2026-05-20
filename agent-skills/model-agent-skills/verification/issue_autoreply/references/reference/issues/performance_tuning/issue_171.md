# Issue #171: [Misc]: vllm-ascend 推理速度非常慢

## 基本信息

- **编号**: #171
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/171
- **创建时间**: 2025-02-26T03:47:35Z
- **关闭时间**: 2025-05-14T01:55:57Z
- **更新时间**: 2025-05-14T01:55:58Z
- **提交者**: @ryys1122
- **评论数**: 5

## 标签

performance

## 问题描述

### Anything you want to discuss about vllm on ascend.

vllm-asend 部署成功后，使用4张910B，运行推理服务。

VLLM_USE_MODELSCOPE=true NPU_VISIBLE_DEVICES=4,5,6,7 ASCEND_RT_VISIBLE_DEVICES=4,5,6,7 vllm serve --tensor-parallel-size 4   deepseek-ai/DeepSeek-R1-Distill-Qwen-32B

测试推理服务

curl http://localhost:8000/v1/completions   -H "Content-Type: application/json"   -d '{
    "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    "prompt": "描述一下北京的秋天",
    "max_tokens": 512
  }'

将近3分钟才返回结果。


