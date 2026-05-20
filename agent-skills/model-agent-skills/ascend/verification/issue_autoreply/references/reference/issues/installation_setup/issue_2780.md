# Issue #2780: [Installation]: ERROR: Could not find a version that satisfies the requirement cmake>=3.26.1 (from versions: 3.25.0)

## 基本信息

- **编号**: #2780
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2780
- **创建时间**: 2025-09-05T07:48:24Z
- **关闭时间**: 2025-12-29T12:08:44Z
- **更新时间**: 2025-12-29T12:08:44Z
- **提交者**: @wuyangjian1115
- **评论数**: 3

## 标签

installation

## 问题描述

### Your current environment

```text
The output of `python collect_env.py`
```
通过dockerfile构建，分支为vllm-ascend0.9.1

### How you are installing vllm and vllm-ascend

```sh
FROM quay.io/ascend/cann:8.2.rc1-910b-ubuntu22.04-py3.11

ARG PIP_INDEX_URL="https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"
ARG COMPILE_CUSTOM_KERNELS=1
# 添加vllm-ascend代码仓库地址参数
ARG VLLM_ASCEND_REPO=https://github.com/vllm-project/vllm-ascend.git
ARG VLLM_ASCEND_TAG=v0.9.1

# Define environments
ENV DEBIAN_FRONTEND=noninteractive
ENV COMPILE_CUSTOM_KERNELS=${COMPILE_CUSTOM_KERNELS}

RUN apt-get update -y && \
    apt-get install -y python3-pip git vim wget net-tools gcc g++ cmake libnuma-dev && \
    rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN pip config set global.index-url ${PIP_INDEX_URL}

# Install vLLM
ARG VLLM_REPO=https://github.com/vllm-project/vllm.git
ARG VLLM_TAG=v0.9.1
RUN git clone --depth 1 $VLLM_REPO --branch $VLLM_TAG /vllm-workspace/vllm && \
    git clone --depth 1 $VLLM_ASCEND_REPO --branch $VLLM_ASCEND_TAG /vllm-workspace/vllm-ascend
# In x86, triton will be installed by vllm. But in Ascend, triton doesn't work correctly. we need to uninstall it.
RUN VLLM_TARGET_DEVICE="empty" python3 -m pip install -v -e /vllm-workspace/vllm/ --extra-index https://download.pytorch.org/whl/cpu/ && \
    python3 -m pip uninstall -y triton && \
    python3 -m pip cache purge

# Install vllm-ascend
# Append `libascend_hal.so` path (devlib) to LD_LIBRARY_PATH
RUN source /usr/local/Ascend/ascend-toolkit/set_env.sh && \
    source /usr/local/Ascend/nnal/atb/set_env.sh && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/Ascend/ascend-toolkit/latest/`uname -i`-linux/devlib && \
    python3 -m pip install -v -e /vllm-workspace/vllm-ascend/ --extra-index https://download.pytorch.org/whl/cpu/ && \
    python3 -m pip cache purge

# Install modelscope (for fast download) and ray (for multinode)
RUN python3 -m pip install modelscope 'ray>=2.47.1' 'protobuf>3.20.0' && \
    python3 -m pip cache purge

CMD ["/bin/bash"]
```
# Error log
```

#10 [6/8] RUN VLLM_TARGET_DEVICE="empty" python3 -m pip install -v -e /vllm-workspace/vllm/ --extra-index https://download.pytorch.org/whl/cpu/ &&     python3 -m pip uninstall -y triton &&     python3 -m pip cache purge
#10 0.470 Using pip 25.1.1 from /usr/local/python3.11.13/lib/python3.11/site-packages/pip (python 3.11)
#10 0.554 Looking in indexes: https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple, https://download.pytorch.org/whl/cpu/
#10 0.555 Obtaining file:///vllm-workspace/vllm
#10 0.560   Installing build dependencies: started
#10 0.560   Running command pip subprocess to install build dependencies
#10 0.898   Using pip 25.1.1 from /usr/local/python3.11.13/lib/python3.11/site-packages/pip (python 3.11)
#10 0.979   Looking in indexes: https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple, https://download.pytorch.org/whl/cpu/
#10 3.669   ERROR: Could not find a version that satisfies the requirement cmake>=3.26.1 (from versions: 3.25.0)
#10 3.669   ERROR: No matching distribution found for cmake>=3.26.1
#10 3.723   error: subprocess-exited-with-error
#10 3.723   
#10 3.723   × pip subprocess to install build dependencies did not run successfully.
#10 3.723   │ exit code: 1
#10 3.723   ╰─> See above for output.
#10 3.723   
```
