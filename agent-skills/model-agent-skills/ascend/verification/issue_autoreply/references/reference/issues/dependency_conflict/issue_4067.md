# Issue #4067: [Bug]: 部署Qwen3-VL-32B-THINKING无输出思考标签

## 基本信息

- **编号**: #4067
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4067
- **创建时间**: 2025-11-08T07:12:58Z
- **关闭时间**: 2025-11-09T10:26:47Z
- **更新时间**: 2025-11-30T14:27:32Z
- **提交者**: @ponyioy
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

采用docker-compose部署Qwen3-VL-32B-Thinking，启用--reasoning-parser qwen3

<img width="847" height="772" alt="Image" src="https://github.com/user-attachments/assets/f0d4d24a-f684-418f-91e7-15a22b1e69c4" />

services:
  qwen3-vl-32b-think:
    image: quay.io/ascend/vllm-ascend:v0.11.0-dev-openeuler
    container_name: qwen3-vl-32b-thinking
    privileged: true
    devices:
      - /dev/davinci_manager
      - /dev/devmm_svm
      - /dev/hisi_hdc
    volumes:
      - /usr/local/dcmi:/usr/local/dcmi
      - /usr/local/bin/npu-smi:/usr/local/bin/npu-smi
      - /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/
      - /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info
      - /etc/ascend_install.info:/etc/ascend_install.info
      - /Model:/root/.cache
    ports:
      - "8001:8000"
    environment:
      - ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
      - TZ=Asia/Shanghai
    command:
      - vllm
      - serve
      - /root/.cache/Qwen3-VL-32B-Thinking
      - --served-model-name
      - infer_model
      - --tensor-parallel-size
      - "4"
      - --max-model-len
      - "131072"
      - --reasoning-parser
      - qwen3                        # 启用 Qwen3-Thinking 推理解析
      - --enable-auto-tool-choice    # 允许自动工具选择
      - --tool-call-parser
      - hermes                       # 工具调用解析器（选配）
    stdin_open: true
    tty: true


### 🐛 Describe the bug

<img width="2257" height="715" alt="Image" src="https://github.com/user-attachments/assets/209ed36b-acd0-4c67-897f-fc3d7ab0ff51" />

输出没有reasoning_content标签，也不见有think标签。
