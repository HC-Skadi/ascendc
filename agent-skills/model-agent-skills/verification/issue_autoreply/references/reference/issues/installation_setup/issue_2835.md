# Issue #2835: [Misc]: The version requirements are inconsistent across different files.

## 基本信息

- **编号**: #2835
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2835
- **创建时间**: 2025-09-09T11:40:53Z
- **关闭时间**: 2025-10-23T07:58:35Z
- **更新时间**: 2025-10-23T07:58:35Z
- **提交者**: @tardis-key
- **评论数**: 3

## 标签

无

## 问题描述

As far as I know, there are three files (maybe more) which declare the version requirements (0.9.1-dev for example):

1. https://github.com/vllm-project/vllm-ascend/blob/v0.9.1-dev/README.md
2. https://github.com/vllm-project/vllm-ascend/blob/v0.9.1-dev/requirements-dev.txt
3. https://github.com/vllm-project/vllm-ascend/blob/v0.9.1/pyproject.toml

The dependent components and their versions in the three files are not entirely consistent—for example, the torch-npu version—and this has confused me a lot. It is understandable that the README may only list the dependency versions of key components. However, other dependent components and their corresponding versions should be completely consistent. As stated in the comments of pyproject.toml, it should be mirrored in requirements.txt.

Can we standardize the version requirements?
