# Issue #891: [Misc]: in AscendW8A8LInearMethod, why is quant_bias only passed in when tp_rank == 0 ?

## 基本信息

- **编号**: #891
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/891
- **创建时间**: 2025-05-18T02:33:06Z
- **关闭时间**: 2025-05-26T02:10:12Z
- **更新时间**: 2025-05-26T02:10:12Z
- **提交者**: @tangzhiyi11
- **评论数**: 0

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

vllm-ascend/vllm_ascend/quantization/quant_config.py

![Image](https://github.com/user-attachments/assets/335f974f-0343-4ba0-87ee-aece329b663f)

I’m curious why  `quant_bias` is only passed in when  `tp_rank == 0`. Could anyone with more experience help explain this?
