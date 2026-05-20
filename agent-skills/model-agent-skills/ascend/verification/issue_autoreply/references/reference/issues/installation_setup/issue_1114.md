# Issue #1114: [Installation]: How to make libvllm_ascend_kernels.so when installing vllm-ascend in container image v0.8.5rc1

## 基本信息

- **编号**: #1114
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1114
- **创建时间**: 2025-06-07T08:36:27Z
- **关闭时间**: 2025-06-15T07:08:39Z
- **更新时间**: 2025-06-15T07:08:39Z
- **提交者**: @1032120121
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

```text
我在容器里quay.io/ascend/vllm-ascend:v0.8.5rc1
```


### How you are installing vllm and vllm-ascend

```sh
先卸载镜像自带的/vllm-workspace/vllm-ascend
pip uninstall vllm-ascend
然后进入自己的vllm-ascend目录安装自己的vllm-ascend代码
MAX_JOBS=4 pip install -e . --no-build-isolation

但是启动的时候提示找不到libvllm_ascend_kernels.so
容器自带的安装环境里有/vllm-workspace/vllm-ascend/vllm_ascend/lib/libvllm_ascend_kernels.so
但我自己安装的目录下却没生成libvllm_ascend_kernels.so
```

启动时的错误提示
2025-06-07T08:10:41.790Z ERROR camem: Failed to import vllm_ascend_C:libvllm_ascend_kernels.so: cannot open shared object file: No such file or directory


