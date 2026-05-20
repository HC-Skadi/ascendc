# Issue #5468: [Bug]: vllm-ascend目前使用的cann版本在部署deepseekv3.2时不支持驱动版本24.1

**类型**: Issue

## 问题背景
### Your current environment

之前的情况：(#4972 )(#4914 )
我找时间测试了一下cann:8.2版本，发现部署成功，如果在那之后bug还没有修复的情况下，基本上可以断定问题了：vllm-ascend目前使用的cann版本在部署deepseekv3.2时不支持驱动版本24.1，目前的配置如下：
dockerfile
```shell
FROM quay.io/ascend/cann:8.2.rc2-910b-ubuntu22.04-py3.11

RUN pip config set global.index-url http://10.29.30.71/simple/
RUN pip config set global.trusted-host 10.29.30.71
ARG SOC_VERSION="ascend910b1"

RUN echo 'Acquire::https::Verify-Peer "false";' > /etc/apt/apt.conf.d/99verify-peer && \
    echo 'Acquire::https::Verify-Host "false";' >> /etc/apt/apt.conf.d/99verify-peer
# Define environments
ENV DEBIAN_FRONTEND=noninteractive
ENV SOC_VERSION=$SOC_VERSION \
    TASK_QUEUE_ENABLE=1 \
    OMP_NUM_THREADS=1

WORKDIR /workspace
COPY . /vllm-workspace/
COPY sources.list /etc/apt/sources.list
RUN test -d /etc/apt/sources.list.d && rm -rf /etc/apt/sources.list.d

# Install Mooncake dependencies
RUN apt-get update -y && \
    apt-get install -y git vim wget net-tools gcc g++ cmake libnuma-dev libjemalloc2

## 基本信息
- **编号**: #5468
- **作者**: shaojun0
- **创建时间**: 2025-12-29T05:56:17Z
- **关闭时间**: 2026-01-29T02:43:42Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5468)
