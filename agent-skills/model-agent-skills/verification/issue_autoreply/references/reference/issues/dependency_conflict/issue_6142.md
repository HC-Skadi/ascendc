# Issue #6142: [Bug]: vllm ascend与qwen3-vl-30b-instruct模型适配问题

## 基本信息

- **编号**: #6142
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6142
- **创建时间**: 2026-01-22T10:09:03Z
- **关闭时间**: 2026-01-27T11:27:13Z
- **更新时间**: 2026-01-27T11:27:13Z
- **提交者**: @Nemo0223
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

vllm ascend 0.13.0rcl

</details>


### 🐛 Describe the bug

910B4 8卡使用vllm ascend0.13.0 rc启动qwen3-vl-32b-instruct模型，启动参数如下：
export VLLM_USE_V1=1
export VLLM_VERSION=0.13.0
export VLLM_HTTP_PORT=8080

export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
# Model File Path
MODEL_NAME=${OPENAI_MODEL:-default}
MODEL_NAME_OR_PATH=model_path

vllm serve ${MODEL_NAME_OR_PATH} \
   --host 0.0.0.0 \
   --port $VLLM_HTTP_PORT \
   --gpu-memory-utilization 0.9 \
   --served-model-name $MODEL_NAME \
   --max-model-len 100000 \
   --max-num-batched-tokens 50000 \
   --tensor-parallel-size 8
启动模型后输入多张表格图片要求模型识别特定列的内容，部分情况下模型会正常生成，但大概率出现模型不按prompt指示在同一页生成不存在的内容的情况
是否是vllm ascend与qwen3-vl-32b-instruct模型之间存在适配问题？
