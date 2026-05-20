# Issue #725: [Bug]: Fail to start vllm under /workspace

## 基本信息

- **编号**: #725
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/725
- **创建时间**: 2025-04-29T11:20:38Z
- **关闭时间**: 2025-04-30T09:38:14Z
- **更新时间**: 2025-04-30T09:38:14Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

In PR https://github.com/vllm-project/vllm-ascend/pull/661 , we change pip install from to `pip install -e` to help developers 

Error like:

ERROR: `cann't import name 'PoolingParams' from 'vllm'`

ModuleNotFoundError: No module named 'vllm.benchmarks.serve'


### 🐛 Describe the bug

- **Fail to start vllm under /workspace**: https://github.com/vllm-project/vllm-ascend/issues/725
  - **Workaround**:
     -  1. `cd ~` or `cd /`, before you execute the vllm serve or launch openai server
     - 2. **(Update 20250430 9:00 AM) You can ** Use `docker pull` redownload `v0.8.4rc2` image to refresh image

  - **Resolved**: https://github.com/vllm-project/vllm-ascend/pull/726
      - we need follow vLLM, should move all source code into /vllm-workspace/, and keep /workspace as workdir: 
  [1] https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile#L264C7-L264C23
  [2] https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile#L52
