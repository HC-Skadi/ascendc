# vLLM Ascend 部署指南

> 本文档详细介绍 vLLM Ascend 的安装和部署流程
> 来源: https://docs.vllm.ai/projects/ascend/en/latest/

## 安装前准备

### 硬件要求

- 华为昇腾NPU (910B/310B系列)
- 建议配置: 8核CPU, 64GB RAM
- 存储空间: 取决于模型大小

### 软件要求

- Ubuntu 20.04+ 或 Debian 11+
- Python 3.8+
- CANN 8.5.0+

## 安装步骤

### 方法一: 使用预编译Wheel安装 (推荐)

```bash
# 安装vLLM
pip install vllm==0.17.0

# 安装vLLM-Ascend插件
pip install vllm-ascend==0.17.0
```

### 方法二: 从源码构建

```bash
# 克隆vLLM-Ascend仓库
git clone --depth 1 --branch v0.17.0 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend

# 更新子模块
git submodule update --init --recursive

# 安装
pip install -v -e .
```

### CANN安装

如果预编译版本不可用,需要手动安装CANN:

```bash
# 创建虚拟环境
python -m venv vllm-ascend-env
source vllm-ascend-env/bin/activate

# 安装Python依赖
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple attrs 'numpy<2.0.0' decorator sympy cffi pyyaml pathlib2 psutil protobuf scipy requests absl-py wheel typing_extensions

# 下载并安装CANN toolkit
wget --header="Referer: https://www.hiascend.com/" \
  https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/CANN/CANN%208.5.0/Ascend-cann-toolkit_8.5.0_linux-x86_64.run

chmod +x ./Ascend-cann-toolkit_8.5.0_linux-x86_64.run
./Ascend-cann-toolkit_8.5.0_linux-x86_64.run --full
source /usr/local/Ascend/ascend-toolkit/set_env.sh

# 安装CANN ops
wget --header="Referer: https://www.hiascend.com/" \
  https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/CANN/CANN%208.5.0/Ascend-cann-910b-ops_8.5.0_linux-x86_64.run
chmod +x ./Ascend-cann-910b-ops_8.5.0_linux-x86_64.run
./Ascend-cann-910b-ops_8.5.0_linux-x86_64.run --install

# 安装NNAL
wget --header="Referer: https://www.hiascend.com/" \
  https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/CANN/CANN%208.5.0/Ascend-cann-nnal_8.5.0_linux-x86_64.run
chmod +x ./Ascend-cann-nnal_8.5.0_linux-x86_64.run
./Ascend-cann-nnal_8.5.0_linux-x86_64.run --install

source /usr/local/Ascend/nnal/atb/set_env.sh
```

### 本地CPU测试环境

在没有昇腾硬件的情况下进行测试:

```bash
# 拉取Docker镜像
docker pull quay.io/ascend/cann:8.5.0

# 启动容器
docker run --rm --name vllm-ascend-ut \
    -v $(pwd):/vllm-project \
    -v ~/.cache:/root/.cache \
    -ti quay.io/ascend/cann:8.5.0 bash

# 配置镜像加速
sed -i 's|ports.ubuntu.com|mirrors.huaweicloud.com|g' /etc/apt/sources.list
pip config set global.index-url https://mirrors.huaweicloud.com/repository/pypi/simple/

# 安装依赖
apt-get update -y
apt-get install -y python3-pip git vim wget net-tools gcc g++ cmake libnuma-dev curl gnupg2

# 克隆并安装vLLM
git clone --depth 1 https://github.com/vllm-project/vllm.git
cd vllm
VLLM_TARGET_DEVICE=empty python3 -m pip install .
python3 -m pip uninstall -y triton

# 克隆并安装vLLM-Ascend
git clone --depth 1 --branch v0.17.0 https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/Ascend/ascend-toolkit/latest/$(uname -m)-linux/devlib
export SOC_VERSION="ascend910b1"
python3 -m pip install -v .
```

## 验证安装

### 检查NPU设备

```bash
npu-smi info
```

预期输出应显示可用的NPU设备信息。

### 检查Python环境

```python
import torch
import torch_npu
import vllm

print(f"PyTorch version: {torch.__version__}")
print(f"vLLM version: {vllm.__version__}")
```

### 简单推理测试

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="Qwen/Qwen2.5-7B-Instruct",
    tensor_parallel_size=1,
    trust_remote_code=True
)

sampling_params = SamplingParams(temperature=0.7, max_tokens=100)
output = llm.generate("Hello, how are you?", sampling_params)
print(output.outputs[0].text)
```

## 部署模式

### 单节点单卡部署

```bash
export ASCEND_RT_VISIBLE_DEVICES=0

vllm serve Qwen/Qwen2.5-7B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --served-model-name qwen-2.5-7b \
    --trust-remote-code \
    --max-model-len 32768
```

### 单节点多卡部署

```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3

vllm serve Qwen/Qwen2.5-7B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --tensor-parallel-size 4 \
    --trust-remote-code \
    --max-model-len 32768
```

### 多节点部署

参见[模型部署文档](./models.md)中的多节点配置示例。

## 环境变量参考

| 变量 | 说明 | 推荐值 |
|------|------|--------|
| ASCEND_RT_VISIBLE_DEVICES | 可见NPU设备 | 0,1,2,3 |
| OMP_NUM_THREADS | OpenMP线程数 | 10 |
| PYTORCH_NPU_ALLOC_CONF | 内存分配配置 | expandable_segments:True |
| HCCL_IF_IP | HCCL通信IP | 本机IP |
| VLLM_USE_V1 | 使用V1引擎 | 1 |

## 卸载

```bash
pip uninstall vllm-ascend
pip uninstall vllm
```

## 相关资源

- [官方文档](https://docs.vllm.ai/projects/ascend/en/latest/)
- [GitHub仓库](https://github.com/vllm-project/vllm-ascend)
- [华为昇腾官网](https://www.hiascend.com/)

---

*本文档由 Ascend Model Verifier 自动整理*
*最后更新: 2025-03-18*
