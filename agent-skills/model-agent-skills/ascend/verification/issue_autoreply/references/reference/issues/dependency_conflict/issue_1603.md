# Issue #1603: [Bug]: vllm-ascend v0.9.0rc2 may crash when executing parallel processing for multiple requests

## 基本信息

- **编号**: #1603
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1603
- **创建时间**: 2025-07-03T01:19:16Z
- **关闭时间**: 2025-07-03T10:15:20Z
- **更新时间**: 2025-07-03T10:15:20Z
- **提交者**: @kylewanginchina
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

Env Info:

OS: Kylin10
Ascend NPU Driver: Ascend-hdk-910b-npu-driver_23.0.7_linux-aarch64.run
Ascend NPU Firmware: Ascend-hdk-910b-npu-firmware_7.1.0.11.220.run
Ascend Docker Runtime: Ascend-docker-runtime_5.0.RC3.2_linux-aarch64.run
Docker: docker-ce-26.1.3-1.el8.aarch64.rpm
Containerd: containerd.io-1.6.32-3.1.el8.aarch64.rpm
vllm-ascend: vllm-ascend-v0.9.0rc2


32B LLM Inference:

export IMAGE=quay.io/ascend/vllm-ascend:v0.9.0rc2
docker run --rm
–name vllm-ascend-env
–device /dev/davinci0
–device /dev/davinci1
–device /dev/davinci2
–device /dev/davinci3
–device /dev/davinci_manager
–device /dev/devmm_svm
–device /dev/hisi_hdc
-v /usr/local/dcmi:/usr/local/dcmi
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info
-v /etc/ascend_install.info:/etc/ascend_install.info
-v /root/.cache:/root/.cache
-p 8000:8000
-v /home/test:/mnt
-e VLLM_USE_V1=1
-e VLLM_USE_MODELSCOPE=True
-e PYTORCH_NPU_ALLOC_CONF=expandable_segments: True
-it $IMAGE
vllm serve /mnt/Qwen3-32B --tensor-parallel-size 4 --max-model-len 32768 --gpu-memory-utilization 0.9

### 🐛 Describe the bug

Crash may happen when executing parallel processing for multiple requests, the error message is as follows:

![Image](https://github.com/user-attachments/assets/47d66c6c-6b97-4ccb-a59c-27e0660af661)

The complete and detailed log info is in [crash.txt](https://github.com/user-attachments/files/21027289/crash.txt)
