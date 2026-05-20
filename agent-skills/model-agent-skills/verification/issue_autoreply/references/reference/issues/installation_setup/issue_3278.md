# Issue #3278: [Usage]: A step by step guide to build DeepSeek-V3.2-Exp image

## 基本信息

- **编号**: #3278
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3278
- **创建时间**: 2025-09-30T00:24:08Z
- **关闭时间**: 2025-12-23T12:54:45Z
- **更新时间**: 2025-12-23T12:54:45Z
- **提交者**: @Yikun
- **评论数**: 8

## 标签

无

## 问题描述

Notes: this is issue for developers, we recommand use the guide in:
https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi-node_dsv3.2.html

Below docs show how `quay.io/ascend/vllm-ascend:v0.11.0rc0-a3-deepseek-v3.2-exp` and `quay.io/ascend/vllm-ascend:v0.11.0rc0-deepseek-v3.2-exp` build manually.

注意：此Issue面向开发者，我们推荐您使用如下指导，使用all in one (`vllm-ascend:v0.11.0rc0-deepseek-v3.2-exp`) 进行部署：
https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi-node_dsv3.2.html


下面文档展示了all in one 镜像(`vllm-ascend:v0.11.0rc0-deepseek-v3.2-exp`)是怎么生成的。


----



### For A3 image:

Below is how `quay.io/ascend/vllm-ascend:v0.11.0rc0-a3-deepseek-v3.2-exp` image built:

1. Start the docker container of vLLM-Ascend v0.11.0rc0 on your node:

```{code-block} bash
   :substitutions:
# Update the vllm-ascend image
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:v0.11.0rc0-a3
docker run --rm \
--name vllm-ascend \
--net=host \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci8 \
--device /dev/davinci9 \
--device /dev/davinci10 \
--device /dev/davinci11 \
--device /dev/davinci12 \
--device /dev/davinci13 \
--device /dev/davinci14 \
--device /dev/davinci15 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash
```

2. Install the package `custom-ops` to make the kernels available.

```bash
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a3/CANN-custom_ops-sfa-linux.aarch64.run
chmod +x ./CANN-custom_ops-sfa-linux.aarch64.run
./CANN-custom_ops-sfa-linux.aarch64.run --quiet
export ASCEND_CUSTOM_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize:${ASCEND_CUSTOM_OPP_PATH}
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api/lib/:${LD_LIBRARY_PATH}
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a3/custom_ops-1.0-cp311-cp311-linux_aarch64.whl
pip install custom_ops-1.0-cp311-cp311-linux_aarch64.whl
```

3. Download and install MLAPO

```bash
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a3/CANN-custom_ops-mlapo-linux.aarch64.run
# please set a custom install-path, here take `/`vllm-workspace/CANN` as example.
chmod +x ./CANN-custom_ops-mlapo-linux.aarch64.run 
./CANN-custom_ops-mlapo-linux.aarch64.run --quiet --install-path=/vllm-workspace/CANN
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a3/torch_npu-2.7.1%2Bgitb7c90d0-cp311-cp311-linux_aarch64.whl
pip install torch_npu-2.7.1+gitb7c90d0-cp311-cp311-linux_aarch64.whl
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a3/libopsproto_rt2.0.so
cp libopsproto_rt2.0.so /usr/local/Ascend/ascend-toolkit/8.2.RC1/opp/built-in/op_proto/lib/linux/aarch64/libopsproto_rt2.0.so
# Don't forget to replace `/vllm-workspace/CANN/` to the custom path you set before.
source /vllm-workspace/CANN/vendors/customize/bin/set_env.bash
export LD_PRELOAD=/vllm-workspace/CANN/vendors/customize/op_proto/lib/linux/aarch64/libcust_opsproto_rt2.0.so:${LD_PRELOAD}
```


### For A2 image:

Below is how `quay.io/ascend/vllm-ascend:v0.11.0rc0-deepseek-v3.2-exp` image built:

1. Start the docker container of vLLM-Ascend v0.11.0rc0 on your node:

```{code-block} bash
   :substitutions:
# Update the vllm-ascend image
export IMAGE=quay.nju.edu.cn/ascend/vllm-ascend:v0.11.0rc0
docker run --rm \
--name vllm-ascend-yikun \
--net=host \
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
-p 8000:8000 \
-it $IMAGE bash
```

2. Install the package `custom-ops` to make the kernels available.

```bash
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a2/CANN-custom_ops-sfa-linux.aarch64.run
chmod +x ./CANN-custom_ops-sfa-linux.aarch64.run
./CANN-custom_ops-sfa-linux.aarch64.run --quiet
export ASCEND_CUSTOM_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize:${ASCEND_CUSTOM_OPP_PATH}
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api/lib/:${LD_LIBRARY_PATH}
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a2/custom_ops-1.0-cp311-cp311-linux_aarch64.whl
pip install custom_ops-1.0-cp311-cp311-linux_aarch64.whl
```

3. Download and install MLAPO

```bash
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a2/CANN-custom_ops-mlapo-linux.aarch64.run
# please set a custom install-path, here take `/`vllm-workspace/CANN` as example.
chmod +x ./CANN-custom_ops-mlapo-linux.aarch64.run 
./CANN-custom_ops-mlapo-linux.aarch64.run --quiet --install-path=/vllm-workspace/CANN
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a2/torch_npu-2.7.1%2Bgitb7c90d0-cp311-cp311-linux_aarch64.whl
pip install torch_npu-2.7.1+gitb7c90d0-cp311-cp311-linux_aarch64.whl
wget https://vllm-ascend.obs.cn-north-4.myhuaweicloud.com/vllm-ascend/a2/libopsproto_rt2.0.so
cp libopsproto_rt2.0.so /usr/local/Ascend/ascend-toolkit/8.2.RC1/opp/built-in/op_proto/lib/linux/aarch64/libopsproto_rt2.0.so
# Don't forget to replace `/vllm-workspace/CANN/` to the custom path you set before.
source /vllm-workspace/CANN/vendors/customize/bin/set_env.bash
export LD_PRELOAD=/vllm-workspace/CANN/vendors/customize/op_proto/lib/linux/aarch64/libcust_opsproto_rt2.0.so:${LD_PRELOAD}
```

