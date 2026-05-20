# Issue #1696: [Usage]: quay.io/ascend/vllm-ascend:v0.7.3这个镜像，支持910C吗？

## 基本信息

- **编号**: #1696
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1696
- **创建时间**: 2025-07-09T07:30:43Z
- **关闭时间**: 2025-07-17T03:13:03Z
- **更新时间**: 2025-07-17T03:13:03Z
- **提交者**: @fixdebugfix
- **评论数**: 1

## 标签

feature request

## 问题描述

### Your current environment

**# 查询硬件**
$ npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3.3               Version: 24.1.rc3.3                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910C1               | OK            | 198.7       43                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          56844/ 65536         |
+------------------------------------------------------------------------------------------------+
| 0     910C1               | OK            | -           43                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          56523/ 65536         |


**# cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info**
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux

### How would you like to use vllm on ascend

**# 我的操作：
1、下载了官网的docker pull quay.io/ascend/vllm-ascend:v0.7.3，按照官网docker 拉起来
2、docker里面安装了mindie_turbo
3、按照[官网链接](https://vllm-ascend.readthedocs.io/en/v0.7.3/installation.html)中的Verify installation的操作流程，运行`python example.py`里面的脚本**

# 报错：
[rank0]: Traceback (most recent call last):
[rank0]:   File "/data1/xubs/example.py", line 13, in <module>
[rank0]:     llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")
[rank0]:   File "/vllm-workspace/vllm/vllm/utils.py", line 1022, in inner
---省略---
[rank0]: RuntimeError: call aclnnArange failed, detail:EZ9999: Inner Error!
**[rank0]: EZ9999: [PID: 2075] 2025-07-09-06:39:54.780.150 Parse dynamic kernel config fail.
[rank0]:         TraceBack (most recent call last):
[rank0]:        AclOpKernelInit failed opType
[rank0]:        ArangeAiCore ADD_TO_LAUNCHER_LIST_AICORE failed.**

- 详细见：[error.txt](https://github.com/user-attachments/files/21137308/error.txt)

**# 问题：请问这个报错，是因为quay.io/ascend/vllm-ascend:v0.7.3这个镜像，不支持910C吗？还是说哪里没有配置对导致错误的？**
