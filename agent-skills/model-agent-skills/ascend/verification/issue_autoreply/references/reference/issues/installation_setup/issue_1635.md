# Issue #1635: [Installation]: 使用文档提供的镜像创建容器后torch.npu.set_device(0)出现报错

## 基本信息

- **编号**: #1635
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1635
- **创建时间**: 2025-07-06T09:16:33Z
- **关闭时间**: 2025-07-06T09:21:42Z
- **更新时间**: 2025-07-06T09:22:13Z
- **提交者**: @YuanCheng-coder
- **评论数**: 1

## 标签

installation

## 问题描述


<img width="2084" height="620" alt="Image" src="https://github.com/user-attachments/assets/486987c5-afa1-4d98-ab6b-f3c8d1b17ee5" />

### How you are installing vllm and vllm-ascend

use openeuler image from here quay.io/ascend/vllm-ascend:v0.9.1rc1-openeuler
docker run --rm \
--name vllm-ascend \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /home:/home \
-p 8000:8000 \
-it 089fdce5071d bash

docker exec -it vllm-ascend /bin/bash

import torch
import torch_npu
torch.npu.set_device(0)
