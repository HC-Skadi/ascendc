# Issue #4900: [Doc]: additional_config miss “enable_weight_nz_layout” config declaration

## 基本信息

- **编号**: #4900
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4900
- **创建时间**: 2025-12-11T03:40:06Z
- **关闭时间**: 2025-12-17T02:50:20Z
- **更新时间**: 2025-12-17T02:50:20Z
- **提交者**: @coder-yuzhiwei
- **评论数**: 2

## 标签

documentation

## 问题描述

### 📚 The doc issue

https://github.com/vllm-project/vllm-ascend/blob/main/docs/source/user_guide/configuration/additional_config.md

additional_config中缺少“enable_weight_nz_layout”配置的说明，文档中搜不到。
enable_weight_nz_layout 将权重转化为昇腾亲和的NZ格式，对量化后的模型，性能有非常大的提升。




### Suggest a potential alternative/fix
建议：
1. 增加enable_weight_nz_layout配置说明。
2. 能否在加载量化权重时默认开启，让用户能够获得量化收益。

_No response_
