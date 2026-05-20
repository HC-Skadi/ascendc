# Issue #5428: [Bug]: Qwen1.5-14B推理时报错

**类型**: Issue

## 问题背景
### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

Qwen1.5-14B模型A2单卡可以正常拉起，但是处理请求时报错。
模型拉起命令：
单卡部署，服务拉起命令如下：
export TASK_QUEUE_ENABLE=1
export VLLM_USE_V1=1

export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libjemalloc.so.2:$LD_PRELOAD

export HCCL_OP_EXPANSION_MODE="AIV"

export VLLM_ASCEND_ENABLE_DENSE_OPTIMIZE=1

export VLLM_ASCEND_ENABLE_FLASHCOMM=1

export VLLM_ASCEND_ENABLE_PREFETCH_MLP=1

export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True

export VLLM_TORCH_PROFILER_DIR="./vllm_profile_32b"
export VLLM_TORCH_PROFILER_WITH_STACK=0

python -m vllm.entrypoints.openai.api_server
--model=/app/models/Qwen/Qwen1.5-14B
--served-model-name qwen
--trust-remote-code
--max-model-len 18432
--max-num-batched-tokens 204800
-tp 8
--port 9

## 基本信息
- **编号**: #5428
- **作者**: xieanxiean
- **创建时间**: 2025-12-27T07:47:57Z
- **关闭时间**: 2025-12-27T07:48:35Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5428)
