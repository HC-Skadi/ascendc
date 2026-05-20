# Issue #2138: [Bug]: 0.9.2rc1版本 vllm ascend开启图模式场景下运行qwen3 32b 报错compiler_depend.ts:243 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(stream), error code is 107027

## 基本信息

- **编号**: #2138
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2138
- **创建时间**: 2025-07-31T08:26:43Z
- **关闭时间**: 2025-07-31T09:32:10Z
- **更新时间**: 2025-09-17T00:37:02Z
- **提交者**: @ivyilike
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

启动参数：
export ASCEND_LAUNCH_BLOCKING=1
export VLLM_VERSION=0.9.2
export VLLM_USE_MODELSCOPE=True
export HCCL_BUFFSIZE=1024
python -m vllm.entrypoints.openai.api_server --model=/data/qwne3-32b \
    --served-model-name auto \
    --trust-remote-code \
    --distributed-executor-backend=mp \
    --port 8080 \
    -tp=2 \
    --max-num-seqs 24 \
    --max-model-len 32768 \
    --max-num-batched-tokens 32768 \
    --block-size 128 \

错误信息：
File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 224, in get_response
    raise RuntimeError(
RuntimeError: Worker failed with error 'RunOpApiV2:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:243 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(stream), error code is 107027
