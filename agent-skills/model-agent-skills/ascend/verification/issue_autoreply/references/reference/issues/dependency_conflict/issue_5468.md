# Issue #5468: [Bug]: vllm-ascend目前使用的cann版本在部署deepseekv3.2时不支持驱动版本24.1

## 基本信息

- **编号**: #5468
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5468
- **创建时间**: 2025-12-29T05:56:17Z
- **关闭时间**: 2026-01-29T02:43:42Z
- **更新时间**: 2026-01-29T02:43:42Z
- **提交者**: @shaojun0
- **评论数**: 35

## 标签

bug

## 问题描述

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
    apt-get install -y git vim wget net-tools gcc g++ cmake libnuma-dev libjemalloc2 && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/Ascend/ascend-toolkit/latest/`uname -i`-linux/lib64 && \
    rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/*

# RUN pip config set global.index-url ${PIP_INDEX_URL}

# In x86, triton will be installed by vllm. But in Ascend, triton doesn't work correctly. we need to uninstall it.
RUN VLLM_TARGET_DEVICE="empty" python3 -m pip install -v -e /vllm-workspace/vllm/[audio] && \
    python3 -m pip uninstall -y triton && \
    python3 -m pip cache purge

# Install vllm-ascend
# Append `libascend_hal.so` path (devlib) to LD_LIBRARY_PATH
RUN source /usr/local/Ascend/ascend-toolkit/set_env.sh && \
    source /usr/local/Ascend/nnal/atb/set_env.sh && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/Ascend/ascend-toolkit/latest/`uname -i`-linux/devlib && \
    python3 -m pip install -v -e /vllm-workspace/vllm-ascend/ && \
    python3 -m pip cache purge

# Install modelscope (for fast download) and ray (for multinode)
RUN python3 -m pip install modelscope 'ray>=2.47.1,<=2.48.0' 'protobuf>3.20.0' && \
    python3 -m pip cache purge

RUN echo "export LD_PRELOAD=/usr/lib/$(uname -m)-linux-gnu/libjemalloc.so.2:$LD_PRELOAD" >> ~/.bashrc

CMD ["/bin/bash"]
```
node0:
```yaml
services:
  vllm-ascend-head:
    image: quay.io/ascend/vllm-ascend:main-my
    container_name: vllm-ascend-head
    network_mode: host
    privileged: true
    shm_size: 500g
    environment:
      - HCCL_OP_EXPANSION_MODE=AIV
      - HCCL_IF_IP=10.48.205.242
      - GLOO_SOCKET_IFNAME=bond4
      - TP_SOCKET_IFNAME=bond4
      - HCCL_SOCKET_IFNAME=bond4
      - VLLM_ASCEND_ENABLE_MLAPO=1
      - VLLM_ASCEND_BALANCE_SCHEDULING=1
    devices:
      - /dev/davinci0
      - /dev/davinci1
      - /dev/davinci2
      - /dev/davinci3
      - /dev/davinci4
      - /dev/davinci5
      - /dev/davinci6
      - /dev/davinci7
      - /dev/davinci_manager
      - /dev/devmm_svm
      - /dev/hisi_hdc
    volumes:
      - /usr/local/dcmi:/usr/local/dcmi
      - /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool
      - /usr/local/bin/npu-smi:/usr/local/bin/npu-smi
      - /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64
      - /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info
      - /etc/ascend_install.info:/etc/ascend_install.info
      - ./.cache:/root/.cache
      - /data:/data
    command: >
      vllm serve /data/DeepSeek-V3.2-w8a8-QuaRot
      --host 0.0.0.0
      --port 1025
      --data-parallel-size 2
      --data-parallel-size-local 1
      --data-parallel-address 10.48.205.242
      --data-parallel-rpc-port 13389
      --tensor-parallel-size 8
      --seed 1024
      --quantization ascend
      --served-model-name DeepSeek-r1-32k_token
      --enable-expert-parallel
      --max-num-seqs 8
      --max-model-len 8096
      --max-num-batched-tokens 8096
      --trust-remote-code
      --no-enable-prefix-caching
      --gpu-memory-utilization 0.92
      --speculative-config '{"num_speculative_tokens": 1, "method": "mtp"}'
      --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'
```
node1:
```yaml
services:
  vllm-ascend-head:
    image: quay.io/ascend/vllm-ascend:main-my
    container_name: vllm-ascend-head
    network_mode: host
    privileged: true
    shm_size: 500g
    environment:
      - HCCL_OP_EXPANSION_MODE=AIV
      - HCCL_IF_IP=10.48.205.243
      - GLOO_SOCKET_IFNAME=bond4
      - TP_SOCKET_IFNAME=bond4
      - HCCL_SOCKET_IFNAME=bond4
      - VLLM_ASCEND_ENABLE_MLAPO=1
      - VLLM_ASCEND_BALANCE_SCHEDULING=1
    devices:
      - /dev/davinci0
      - /dev/davinci1
      - /dev/davinci2
      - /dev/davinci3
      - /dev/davinci4
      - /dev/davinci5
      - /dev/davinci6
      - /dev/davinci7
      - /dev/davinci_manager
      - /dev/devmm_svm
      - /dev/hisi_hdc
    volumes:
      - /usr/local/dcmi:/usr/local/dcmi
      - /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool
      - /usr/local/bin/npu-smi:/usr/local/bin/npu-smi
      - /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64
      - /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info
      - /etc/ascend_install.info:/etc/ascend_install.info
      - ./.cache:/root/.cache
      - /data:/data
    command: >
      vllm serve /data/DeepSeek-V3.2-w8a8-QuaRot
      --host 0.0.0.0
      --port 1025
      --headless
      --data-parallel-size 2
      --data-parallel-size-local 1
      --data-parallel-start-rank 1
      --data-parallel-address 10.48.205.242
      --data-parallel-rpc-port 13389
      --tensor-parallel-size 8
      --seed 1024
      --quantization ascend
      --served-model-name DeepSeek-r1-32k_token
      --enable-expert-parallel
      --max-num-seqs 8
      --max-model-len 8096
      --max-num-batched-tokens 8096
      --trust-remote-code
      --no-enable-prefix-caching
      --gpu-memory-utilization 0.92
      --speculative-config '{"num_speculative_tokens": 1, "method": "mtp"}'
      --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'
```


### 🐛 Describe the bug

使用当前配置得到的结果：

<img width="1919" height="1045" alt="Image" src="https://github.com/user-attachments/assets/ec7e0ddf-eeff-4609-b117-b9361b78536e" />

@Yikun 所以可不可以在部署ds3.2的时候，如果检测到驱动版本不对，就不让部署，防止其他人也出现跟我一样的错误。或者是不是后续我使用cann8.2的时候这个问题已经被修复了，我只是碰巧？
