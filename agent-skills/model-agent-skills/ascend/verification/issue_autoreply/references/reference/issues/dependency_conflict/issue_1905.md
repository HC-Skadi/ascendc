# Issue #1905: [Bug]: vllm-ascend:v0.9.1rc1-310p support 300i duo 部署qwen3-8b报错

## 基本信息

- **编号**: #1905
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1905
- **创建时间**: 2025-07-21T09:31:38Z
- **关闭时间**: 2025-07-22T02:55:18Z
- **更新时间**: 2025-07-22T02:55:18Z
- **提交者**: @weicong1
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>
# Update DEVICE according to your device (/dev/davinci[0-7])
export DEVICE=/dev/davinci0
# Update the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.9.2rc1-310p
docker run --rm \
--name vllm-ascend \
--device $DEVICE \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /data/models:/home/work \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash

vllm serve /home/work/Qwen3/Qwen3-8b \
    --tensor-parallel-size 1 \
    --enforce-eager \
    --dtype float16 \
    --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'
```text
Your output of above commands here
```

<img width="1515" height="872" alt="Image" src="https://github.com/user-attachments/assets/c2d56acc-9256-4878-ab05-ef72d350afe7" />

</details>


### 🐛 Describe the bug

<img width="1515" height="872" alt="Image" src="https://github.com/user-attachments/assets/63da734e-e150-48df-b5b6-181ddad86313" />
