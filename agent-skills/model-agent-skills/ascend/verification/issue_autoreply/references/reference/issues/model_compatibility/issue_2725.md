# Issue #2725: [Usage]: openEuler23.03 aarch64系统，使用 v0.10.0rc1版本，openEuler镜像，进入容器启动报错

## 基本信息

- **编号**: #2725
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2725
- **创建时间**: 2025-09-03T08:20:53Z
- **关闭时间**: 2025-12-23T11:20:44Z
- **更新时间**: 2026-02-11T07:07:31Z
- **提交者**: @1448163534
- **评论数**: 7

## 标签

310p

## 问题描述

### Your current environment

openEuler23.03 aarch64系统，使用 v0.10.0rc1版本，openEuler镜像，
进入容器启动方式（enter docker and start）：
vllm serve Qwen/Qwen2.5-7B-Instruct     --tensor-parallel-size 1     --enforce-eager     --dtype float16 

**error log：**

INFO 09-03 08:14:32 [default_loader.py:262] Loading weights took 3.10 seconds
INFO 09-03 08:14:33 [model_runner_v1.py:2114] Loading model weights took 14.2488 GB
..[ERROR] the socversion Ascend910B1 of bin package does not match the current device socverison Ascend310P3. Please modify default socversion in run.sh or execute run.sh with socversion parameter.
..


### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

