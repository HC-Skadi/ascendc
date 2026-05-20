# Issue #1033: [Bug]: Failed to import from vllm._C under vllm 0.8.5 + ascend 0.8.5rc1

## 基本信息

- **编号**: #1033
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1033
- **创建时间**: 2025-05-30T07:51:56Z
- **关闭时间**: 2025-06-05T03:26:27Z
- **更新时间**: 2025-06-05T03:26:27Z
- **提交者**: @silveryshine
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

NPU: 910B4
python: 3.10.16
CANN: 8.1RC1
vllm: 0.8.5
vllm-ascend: 0.8.5rc1


### 🐛 Describe the bug

The command line outputs the following after entering any prompt. The whole process was not disturbed by this import failure, but I'm still concerned it might have future implications.

~~~
INFO 05-30 14:36:49 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-30 14:36:49 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-30 14:36:49 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-30 14:36:50 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-30 14:36:50 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-30 14:36:50 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-30 14:36:50 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-30 14:36:50 [__init__.py:44] plugin ascend loaded.
INFO 05-30 14:36:50 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-30 14:36:52 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/root/anaconda3/envs/vllm_test_0.8.5/lib/python3.10/site-packages/vllm/_C.abi3.so: undefined symbol: _ZN3c108Li__cxx1112basic_stringIcSt11char_traitsIcESaIcEEENS_4Type24SingletonOrSharedTypePtrIS9_EE')
~~~
