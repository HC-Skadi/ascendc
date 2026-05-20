# Issue #144: [Installation]: Failed to install the CANN environment following the documentation.

## 基本信息

- **编号**: #144
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/144
- **创建时间**: 2025-02-23T12:55:12Z
- **关闭时间**: 2025-02-24T03:33:40Z
- **更新时间**: 2025-02-24T16:18:46Z
- **提交者**: @Ziang-Zack-Gao
- **评论数**: 6

## 标签

documentation; installation

## 问题描述

### Your current environment

I just need to confirm with you whether there is an issue with the CANN installation guide. If true, please edit the guide asap to avoid further issues.

### How you are installing vllm and vllm-ascend

I followed the official installation order to install CANN 8.0.0, and all the installation package .run files were from the enterprise version. While the toolkit installation was successful, the kernel installation failed. After contacting an Ascend engineer, I got the correct solution: it is necessary to execute source /path/to/ascend/ascend-toolkit/set_env.sh immediately after installing the toolkit, rather than waiting until after installing the toolkit, kernel, and nnal packages to execute both source /path/to/ascend/ascend-toolkit/set_env.sh and source /path/to/ascend/nnal/atb/set_env.sh.

The installation guide:
```
# Create a virtual environment
python -m venv vllm-ascend-env
source vllm-ascend-env/bin/activate

# Install required python packages.
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple attrs "numpy<2.0.0" decorator sympy cffi pyyaml pathlib2 psutil protobuf scipy requests absl-py wheel typing_extensions

# Download and install the CANN package.
wget https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/CANN/CANN%208.0.0/Ascend-cann-toolkit_8.0.0_linux-aarch64.run
chmod +x ./Ascend-cann-toolkit_8.0.0_linux-aarch64.run
./Ascend-cann-toolkit_8.0.0_linux-aarch64.run --full

wget https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/CANN/CANN%208.0.0/Ascend-cann-kernels-910b_8.0.0_linux-aarch64.run
chmod +x ./Ascend-cann-kernels-910b_8.0.0_linux-aarch64.run
./Ascend-cann-kernels-910b_8.0.0_linux-aarch64.run --install

wget https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/CANN/CANN%208.0.0/Ascend-cann-nnal_8.0.0_linux-aarch64.run
chmod +x. /Ascend-cann-nnal_8.0.0_linux-aarch64.run
./Ascend-cann-nnal_8.0.0_linux-aarch64.run --install

source /usr/local/Ascend/ascend-toolkit/set_env.sh
source /usr/local/Ascend/nnal/atb/set_env.sh
```

