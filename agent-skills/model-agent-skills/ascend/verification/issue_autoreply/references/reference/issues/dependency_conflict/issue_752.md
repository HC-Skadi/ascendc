# Issue #752: [Usage]: 在310服务器上部署qwen3报错

## 基本信息

- **编号**: #752
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/752
- **创建时间**: 2025-05-05T02:03:07Z
- **关闭时间**: 2025-05-14T06:38:16Z
- **更新时间**: 2025-05-14T06:38:16Z
- **提交者**: @KeepFaithMe
- **评论数**: 1

## 标签

无

## 问题描述

### Your current environment

```text
环境如下：
npu-smi 24.1.rc2                                 Version: 24.1.rc2                                     |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310P3                 | OK              | NA           59                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1310 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)    

package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
--2025-05-05 02:00:45--  https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443...
```
日志中的错误如下：
[2025-05-05 01:56:15.842742] [error] [1408] [operation_base.cpp:338] RopeOperation_0 Atlas inference products can not support bf16.
[2025-05-05 01:56:15.843306] [error] [1408] [operation_base.cpp:513] RopeOperation_0 invalid param, setup check fail, error code: 6


### How would you like to use vllm on ascend

使用的教程如下：https://mp.weixin.qq.com/s/eyb7Wm2YY-GJD8-2slaxkA

