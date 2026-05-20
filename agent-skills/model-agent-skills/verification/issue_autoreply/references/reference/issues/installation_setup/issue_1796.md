# Issue #1796: [Installation]: Unmatched torch version between vllm=0.9.2 and vllm-ascend=0.9.2rc1

## 基本信息

- **编号**: #1796
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1796
- **创建时间**: 2025-07-15T02:43:42Z
- **关闭时间**: 2025-07-17T01:18:00Z
- **更新时间**: 2025-07-17T01:18:00Z
- **提交者**: @GuanlinLee
- **评论数**: 6

## 标签

installation

## 问题描述

### Your current environment

`pip install vllm==0.9.2` automatically installed the torch=2.7.1.

Then, `pip install vllm-ascend==0.9.2rc1` comes with a fatal error that could not find a version that satisfies the requirement torch-npu==2.5.1.post1.dev20250619.

BTW, setting `pip config set global.extra-index-url "https://download.pytorch.org/whl/cpu/ https://mirrors.huaweicloud.com/ascend/repos/pypi"` will keep the pip looking for index forever long.


### How you are installing vllm and vllm-ascend

I followed the steps provided in the documents, as shown in https://vllm-ascend.readthedocs.io/en/latest/installation.html. 

