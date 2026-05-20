# Issue #707: [v0.8.4rc2] FAQ / Feedback | 问题/反馈

## 基本信息

- **编号**: #707
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/707
- **创建时间**: 2025-04-28T12:21:47Z
- **关闭时间**: 2025-05-14T06:09:18Z
- **更新时间**: 2025-05-14T06:09:18Z
- **提交者**: @wangxiyuan
- **评论数**: 11

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.
Please use doc: https://vllm-ascend.readthedocs.io

- **Fail to start vllm under /workspace**: https://github.com/vllm-project/vllm-ascend/issues/725
  - **Workaround**:
     -  1. `cd ~` or `cd /`, before you execute the vllm serve or launch openai server
     - 2. **(Update 20250430 9:00 AM) You can ** Use `docker pull` redownload `v0.8.4rc2` image to refresh image

  - **Resolved**: https://github.com/vllm-project/vllm-ascend/pull/726
      - we need follow vLLM, should move all source code into /vllm-workspace/, and keep /workspace as workdir: 
  [1] https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile#L264C7-L264C23
  [2] https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile#L52
-------

请使用 https://vllm-ascend.readthedocs.io 安装
