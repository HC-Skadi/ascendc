# Issue #1440: [Usage]: can not to use vllm serve with docker

## 基本信息

- **编号**: #1440
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1440
- **创建时间**: 2025-06-26T01:33:10Z
- **关闭时间**: 2025-12-23T01:24:14Z
- **更新时间**: 2025-12-23T01:24:14Z
- **提交者**: @waaaooo
- **评论数**: 6

## 标签

无

## 问题描述

### Your current environment

docker run --rm     --name vllm-ascend-env     --device $DEVICE     --device /dev/dav_manager     --device /dev/devmm_svm     --device /dev/hisi_hdc   -v /root/Ascend-cann-kernels-910b_8.1.RC1_linux-aarch64.deb:/Ascend.deb -v /home/models:/models  -it $IMAGE bash


libascend_hal.so: cannot open shared object file: No such file or directory
RuntimeError: Failed to load the backend extension: torch_npu. You can disable extension auto-loading with TORCH_DEVICE_BACKEND_AUTOLOAD=0.



### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

