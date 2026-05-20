# Issue #902: [Bug]:  不支持quantization为ascend的量化

## 基本信息

- **编号**: #902
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/902
- **创建时间**: 2025-05-20T01:21:30Z
- **关闭时间**: 2025-11-11T07:51:37Z
- **更新时间**: 2025-11-11T07:51:38Z
- **提交者**: @daiqifeng-sys
- **评论数**: 3

## 标签

bug; module:quantization

## 问题描述

### Your current environment

`vllm serve /tmp/modelscope/hub/models/QwQ-32B-w8a8/ --served-model-name qwq-32b-w8a8 --host 0.0.0.0 --port 9007 -tp 4 --max-model-len 32768 --quantization ascend`

提示不支持ascend。
镜像是：m.daocloud.io/quay.io/ascend/vllm-ascend:v0.8.5rc1。

### 🐛 Describe the bug

usage: vllm serve [model_tag] [options]
vllm serve: error: argument --quantization/-q: invalid choice: 'ascend' (choose from 'aqlm', 'awq', 'deepspeedfp', 'tpu_int8', 'fp8', 'ptpc_fp8', 'fbgemm_fp8', 'modelopt', 'nvfp4', 'marlin', 'bitblas', 'gguf', 'gptq_marlin_24', 'gptq_marlin', 'gptq_bitblas', 'awq_marlin', 'gptq', 'compressed-tensors', 'bitsandbytes', 'qqq', 'hqq', 'experts_int8', 'neuron_quant', 'ipex', 'quark', 'moe_wna16', 'torchao', None)
