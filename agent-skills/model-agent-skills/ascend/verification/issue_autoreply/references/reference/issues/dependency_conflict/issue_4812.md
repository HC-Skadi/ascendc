# Issue #4812: [Bug]: v0.11.0.rc2-310P-openeuler镜像 使用enforce-egaer模式拉起Qwen2.5-VL-7B-Instruct报错

## 基本信息

- **编号**: #4812
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4812
- **创建时间**: 2025-12-09T01:59:13Z
- **关闭时间**: 2025-12-15T02:55:14Z
- **更新时间**: 2025-12-15T02:55:14Z
- **提交者**: @WeNeedMoreCode
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
使用v0.11.0.rc2-310P-openeuler镜像会报错，
使用v0.10.0.rc1-310P镜像能正常拉起，并且能curl通
```text
vllm serve Qwen/Qwen2.5-VL-3B-Instruct \
    --tensor-parallel-size 1 \
    --enforce-eager \
    --dtype float16 \
    --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'
```

</details>


### 🐛 Describe the bug

使用v0.11.0.rc2-310P-openeuler镜像会报错，
使用v0.10.0.rc1-310P镜像能正常拉起，并且能curl通。
所执行的命令为
```shell
vllm serve Qwen/Qwen2.5-VL-3B-Instruct \
    --tensor-parallel-size 1 \
    --enforce-eager \
    --dtype float16 \
    --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'
```
