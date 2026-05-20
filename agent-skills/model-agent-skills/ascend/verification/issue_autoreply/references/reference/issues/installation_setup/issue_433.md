# Issue #433: [Usage]: 我在华为的ModelArts的notebook里安装了vllm,可以正常使用，但是在线部署服务时出错，显示PermissionError: [Errno 13] Permission denied: '//kernel_meta'

## 基本信息

- **编号**: #433
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/433
- **创建时间**: 2025-03-30T05:17:49Z
- **关闭时间**: 2025-05-14T03:07:57Z
- **更新时间**: 2025-05-14T03:07:58Z
- **提交者**: @fhfile
- **评论数**: 3

## 标签

无

## 问题描述

### Your current environment

错误信息如下：
Process ForkServerProcess-1:1:15:
Traceback (most recent call last):
File "/home/ma-user/anaconda3/envs/vllm_npu_py311/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
self.run()
File "/home/ma-user/anaconda3/envs/vllm_npu_py311/lib/python3.11/multiprocessing/process.py", line 108, in run
self._target(*self._args, **self._kwargs)
File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/te_fusion/parallel_compilation.py", line 279, in exec_compilation_task
worker.loop()
File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/te_fusion/parallel_compilation.py", line 1352, in loop
_prerun(task, kwargs)
File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/te_fusion/parallel_compilation.py", line 1293, in _prerun
_update_options(task, kwargs)
File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/te_fusion/parallel_compilation.py", line 1259, in _update_options
set_kernel_meta_parent_dir(kwargs)
File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/te_fusion/fusion_util.py", line 2623, in set_kernel_meta_parent_dir
os.makedirs(kernel_meta_dir, stat.S_IRWXU + stat.S_IRGRP + stat.S_IXGRP)
File "<frozen os>", line 215, in makedirs
File "<frozen os>", line 225, in makedirs
PermissionError: [Errno 13] Permission denied: '//kernel_meta'
```text
The output of above commands
```


### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

