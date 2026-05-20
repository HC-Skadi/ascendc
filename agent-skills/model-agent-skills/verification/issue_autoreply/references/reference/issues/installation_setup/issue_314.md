# Issue #314: [Doc]: atb cann 层代码开源

## 基本信息

- **编号**: #314
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/314
- **创建时间**: 2025-03-12T09:47:40Z
- **关闭时间**: 2025-03-13T02:17:35Z
- **更新时间**: 2025-08-25T05:48:39Z
- **提交者**: @xuxiongchen
- **评论数**: 2

## 标签

documentation

## 问题描述

### 📚 The doc issue

当我在看vllm-ascend如何实现page attention时，能跟到底层代码是 op_plugin/ops/atb/PagedAttentionAtb.cpp，其中算子是实现在atb中，
 m.impl("_npu_paged_attention", TORCH_FN(atb::_npu_paged_attention));
关于这块的c++底层代码，在哪里可以看到？或者是闭源的代码吗？

### Suggest a potential alternative/fix

提供 atb cann 代码
