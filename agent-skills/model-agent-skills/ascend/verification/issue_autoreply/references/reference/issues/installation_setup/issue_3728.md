# Issue #3728: [Installation]: TypeError: unsupported operand type(s) for |: 'type' and 'NoneType' [ERROR] 2025-10-24-11:31:36 (PID:1609325, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

## 基本信息

- **编号**: #3728
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3728
- **创建时间**: 2025-10-24T12:34:36Z
- **关闭时间**: 2025-11-10T03:50:14Z
- **更新时间**: 2025-11-10T03:50:14Z
- **提交者**: @kyleCheng56
- **评论数**: 1

## 标签

installation

## 问题描述

### Your current environment

When excute  "_pip install vllm-ascend==0.11.0rc0_"  , Prompt Error:
_TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'
[ERROR] 2025-10-24-11:31:36 (PID:1609325, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception_

I checked my current Python version ：
_[root@devserver-314b-0 ~]# python --version
Python 3.9.9_

while The | operator in type annotations requires Python 3.10+.

In our README describe:
Python >= 3.9, < 3.12  ,maybe it's not proper ; ---->suggest "Python >= 3.10, < 3.12 "   I have tested Python3.10,  thta's ok !

