# Issue #117: ImportError of torch_npu-2.5.1.dev20250218

## 基本信息

- **编号**: #117
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/117
- **创建时间**: 2025-02-20T03:48:57Z
- **关闭时间**: 2025-02-21T09:05:49Z
- **更新时间**: 2025-02-21T09:05:49Z
- **提交者**: @dawnranger
- **评论数**: 6

## 标签

installation

## 问题描述

# INSTALL 
```
git clone --branch v0.7.1 https://github.com/vllm-project/vllm
cd vllm
VLLM_TARGET_DEVICE=empty pip install . --extra-index-url https://download.pytorch.org/whl/cpu/

# Install vllm-ascend from pypi.
pip install vllm-ascend==0.7.1rc1 --extra-index-url https://download.pytorch.org/whl/cpu/

pip install torch==2.5.1 --extra-index-url https://download.pytorch.org/whl/cpu/
mkdir pta
cd pta
wget https://pytorch-package.obs.cn-north-4.myhuaweicloud.com/pta/Daily/v2.5.1/20250218.4/pytorch_v2.5.1_py310.tar.gz
tar -xvf pytorch_v2.5.1_py310.tar.gz
pip install torch_npu-2.5.1.dev20250218-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```


# FULL LOG
```
Traceback (most recent call last):
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/__init__.py", line 17, in <module>
    import torch_npu.npu
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/npu/__init__.py", line 114, in <module>
    from torch_npu.utils import _should_print_warning
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/utils/__init__.py", line 1, in <module>
    from torch_npu import _C
ImportError: /usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so: undefined symbol: _ZN3atb15CreateOperationINS_5infer14GroupTopkParamEEEiRKT_PPNS_9OperationE

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.10.14/bin/accelerate", line 5, in <module>
    from accelerate.commands.accelerate_cli import main
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/__init__.py", line 16, in <module>
    from .accelerator import Accelerator
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/accelerator.py", line 36, in <module>
    from accelerate.utils.imports import is_torchao_available
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/utils/__init__.py", line 134, in <module>
    from .modeling import (
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/utils/modeling.py", line 32, in <module>
    from ..state import AcceleratorState
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/state.py", line 65, in <module>
    if is_npu_available(check_device=False):
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/accelerate/utils/imports.py", line 377, in is_npu_available
    import torch_npu  # noqa: F401
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/__init__.py", line 19, in <module>
    from torch_npu.utils._error_code import ErrCode, pta_error
  File "/usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/utils/__init__.py", line 1, in <module>
    from torch_npu import _C
ImportError: /usr/local/python3.10.14/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so: undefined symbol: _ZN3atb15CreateOperationINS_5infer14GroupTopkParamEEEiRKT_PPNS_9OperationE
```
