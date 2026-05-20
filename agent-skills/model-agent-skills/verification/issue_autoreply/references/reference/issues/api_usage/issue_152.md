# Issue #152: [Bug]: ImportError: libatb.so: cannot open shared object file: No such file or directory

## 基本信息

- **编号**: #152
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/152
- **创建时间**: 2025-02-24T08:17:49Z
- **关闭时间**: 2025-04-10T09:14:56Z
- **更新时间**: 2025-04-10T09:15:01Z
- **提交者**: @phellonchen
- **评论数**: 10

## 标签

question

## 问题描述

### Your current environment

npu-smi info 
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 94.6        49                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3373 / 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 97.8        48                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3367 / 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 93.0        48                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3371 / 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 98.0        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3367 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 100.6       48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3371 / 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 101.3       49                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3369 / 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 100.3       49                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3369 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 94.9        49                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3369 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.0.RC1
innerversion=V100R001C17SPC001B240
compatible_version=[V100R001C15,V100R001C18],[V100R001C30],[V100R001C13],[V100R003C11],[V100R001C29],[V100R001C10]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.RC1/aarch64-linux

torch                                    2.5.1
torch-npu                                2.5.1.dev20250218
vllm                                     0.7.1+empty
vllm-ascend                              0.7.1rc1                 

### 🐛 Describe the bug

No module named 'vllm._version'
  from vllm.version import __version__ as VLLM_VERSION
INFO 02-24 16:11:22 __init__.py:28] Available plugins for group vllm.platform_plugins:
INFO 02-24 16:11:22 __init__.py:30] name=ascend, value=vllm_ascend:register
INFO 02-24 16:11:22 __init__.py:32] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-24 16:11:22 __init__.py:34] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-24 16:11:22 __init__.py:42] plugin ascend loaded.
INFO 02-24 16:11:22 __init__.py:187] No platform detected, vLLM is running on UnspecifiedPlatform
Traceback (most recent call last):
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch_npu/__init__.py", line 17, in <module>
    import torch_npu.npu
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch_npu/npu/__init__.py", line 114, in <module>
    from torch_npu.utils import _should_print_warning
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch_npu/utils/__init__.py", line 1, in <module>
    from torch_npu import _C
ImportError: libatb.so: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/ma-user/work/algorithm/llama_factory_code/vllm_npus/vllm/vllm_test.py", line 2, in <module>
    import torch_npu
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch_npu/__init__.py", line 19, in <module>
    from torch_npu.utils._error_code import ErrCode, pta_error
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch_npu/utils/__init__.py", line 1, in <module>
    from torch_npu import _C
ImportError: libatb.so: cannot open shared object file: No such file or directory
