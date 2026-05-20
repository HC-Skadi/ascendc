# Issue #5458: [Kernel]update csrc cmakelist for open-source cann

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Using open-source CANN, installation errors may occur due to changes in the path of the aclnn directory. So we add the header file.

Using open-source CANN, installation errors may occur due to changes in the path of the base/dlog_pub.h for aclnn. 

RFC: https://github.com/vllm-project/vllm-ascend/issues/5494

### Does this PR introduce _any_ user-facing change?
Does not.

### How was this patch tested?


- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/5326c89803566a131c928f7fdd2100b75c981a42


## 基本信息
- **编号**: #5458
- **作者**: Fager10086
- **创建时间**: 2025-12-29T02:40:14Z
- **关闭时间**: 2025-12-29T12:34:53Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5458)
