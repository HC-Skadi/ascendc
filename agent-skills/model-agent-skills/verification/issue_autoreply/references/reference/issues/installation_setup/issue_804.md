# Issue #804: [Installation]: Failed to install on CANN 8.2.RC1 due to undeclared identifier 'rope_custom_true_half'

## 基本信息

- **编号**: #804
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/804
- **创建时间**: 2025-05-10T01:55:11Z
- **关闭时间**: 2026-01-04T02:18:59Z
- **更新时间**: 2026-01-04T02:19:27Z
- **提交者**: @tongtong0613
- **评论数**: 4

## 标签

installation

## 问题描述

env: 

```
PTA: 7.1.RC1.B020
CANN: 8.2.RC1.B020
```

install command:

```
export COMPILE_CUSTOM_KERNELS=1
python setup.py install
```

error message:

```
Function AscendcCompiler at line 98, Command excution failed, the returnCode is non-zero!
Output of ascend_compiler: /home/vllm-ascend/csrc/kernels/pos_encoding_kernels.cpp:357:9: error: use of undeclared identifier 'rope_custom_true_half'; did you mean 'rope_custom_true___cce_half'?
```

But when I use CANN **8.1.RC1.B080** , all works.  Could you please help me take a look at this issue? Thank you very much.


