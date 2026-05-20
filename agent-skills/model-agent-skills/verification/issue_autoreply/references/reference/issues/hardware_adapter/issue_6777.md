# Issue #6777: Support platform.get_device_uuid function

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Support platform.get_device_uuid function.
currently, the pytorch.npu.get_device_properties return uuid as full zero,  vllm-ascend implement the interface at first, once the pytorch.npu.get_device_properties return the real uuid, vllm-ascend will support without modification.
more details see 
https://github.com/vllm-project/vllm-ascend/issues/6669
### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/9562912cead1f11e8540fb91306c5cbda66f0007
root@localhost:/workspace/l00614971/vllm_test# python vllm_test.py 
INFO 02-24 09:43:48 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-24 09:43:48 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-24 09:43:48 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-24 09:43:48 [__ini

## 基本信息
- **编号**: #6777
- **作者**: luomin2005
- **创建时间**: 2026-02-24T01:32:34Z
- **关闭时间**: 2026-02-28T06:17:12Z
- **标签**: module:core

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6777)
