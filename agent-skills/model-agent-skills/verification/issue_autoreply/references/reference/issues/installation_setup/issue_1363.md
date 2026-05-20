# Issue #1363: [Installation]: How to deploy vllm-ascend in AutoDL's 910B instance

## 基本信息

- **编号**: #1363
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1363
- **创建时间**: 2025-06-23T03:19:10Z
- **关闭时间**: 2025-06-25T07:43:02Z
- **更新时间**: 2025-06-25T07:43:02Z
- **提交者**: @murarduino
- **评论数**: 1

## 标签

installation

## 问题描述

### Your current environment

root@autodl-container-3e45438682-122ae01a:~/autodl-tmp# npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.3                   Version: 23.0.3                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 97.3        47                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3335 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
root@autodl-container-3e45438682-122ae01a:~/autodl-tmp# cat /usr/local/Ascend/ascend-toolkit/latest/arm64-linux/ascend_toolkit_install.info 
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux

collect_env.py not Found,Please provide a downloadable link

### How you are installing vllm and vllm-ascend

I rented an instance of a 910B on AutoDL. CANN 0.8.1 RC1, Torch 2.5.1 and Torch-npu 2.5.1 are installed.
When installing vllm 0.9.1, you are prompted to uninstall torch 2.5.1 and reinstall version 2.7.X. This causes the installation of vllm-ascend 0.9.1rc1 to report that torch 2.5.1 could not be found.
How will such a problem be handled? thanks
