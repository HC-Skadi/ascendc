# Issue #477: [Bug]: RuntimeError: operator torchvision::nms does not exist

## 基本信息

- **编号**: #477
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/477
- **创建时间**: 2025-04-07T11:00:20Z
- **关闭时间**: 2025-04-08T01:15:43Z
- **更新时间**: 2025-04-08T01:15:43Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment


How to reproduce

```
export IMAGE_PREFIX=m.daocloud.io/
export IMAGE=${IMAGE_PREFIX}quay.io/ascend/cann:8.0.0-910b-ubuntu22.04-py3.10

docker run --rm \
--name vllm-ascend \
--device /dev/davinci0 \
--device /dev/davinci1 \
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

docker exec -it vllm-ascend /bin/bash

## 2. Install vLLM latest release

apt update  -y; apt install -y gcc g++ libnuma-dev vim git
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
pip install vllm


## 3. Install vLLM Ascend main
# Install vLLM Ascend
git clone  --depth 1 --branch main  https://gitee.com/mirrors/vllm-ascend
cd vllm-ascend
pip install -e . --extra-index https://download.pytorch.org/whl/cpu/

mkdir pta
cd pta
wget https://pytorch-package.obs.cn-north-4.myhuaweicloud.com/pta/Daily/v2.5.1/20250320.3/pytorch_v2.5.1_py310.tar.gz
tar -xvf pytorch_v2.5.1_py310.tar.gz
pip install ./torch_npu-2.5.1.dev20250320-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl

```


### 🐛 Describe the bug

```
root@d19f057a153e:/vllm-ascend# export VLLM_USE_MODELSCOPE=True
root@d19f057a153e:/vllm-ascend# export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
root@d19f057a153e:/vllm-ascend# vllm serve LLM-Research/Llama-4-Scout-17B-16E-Instruct --max-model-len 4096 --max-model-len 4096 -tp 8
Traceback (most recent call last):
  File "/usr/local/python3.10/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 1967, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/local/python3.10/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/python3.10/lib/python3.10/site-packages/transformers/processing_utils.py", line 33, in <module>
    from .image_utils import (
  File "/usr/local/python3.10/lib/python3.10/site-packages/transformers/image_utils.py", line 64, in <module>
    from torchvision import io as torchvision_io
  File "/usr/local/python3.10/lib/python3.10/site-packages/torchvision/__init__.py", line 10, in <module>
    from torchvision import _meta_registrations, datasets, io, models, ops, transforms, utils  # usort:skip
  File "/usr/local/python3.10/lib/python3.10/site-packages/torchvision/_meta_registrations.py", line 164, in <module>
    def meta_nms(dets, scores, iou_threshold):
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/library.py", line 795, in register
    use_lib._register_fake(op_name, func, _stacklevel=stacklevel + 1)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/library.py", line 184, in _register_fake
    handle = entry.fake_impl.register(func_to_register, source)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/_library/fake_impl.py", line 31, in register
    if torch._C._dispatch_has_kernel_for_dispatch_key(self.qualname, "Meta"):
RuntimeError: operator torchvision::nms does not exist
```
