# Issue #1025: [Guide][Performance]: vLLM Ascend v0.7.3.post1 benchmark for Qwen3

## 基本信息

- **编号**: #1025
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1025
- **创建时间**: 2025-05-30T02:11:12Z
- **关闭时间**: 2025-06-15T07:50:26Z
- **更新时间**: 2025-07-10T09:33:38Z
- **提交者**: @zhanglzu
- **评论数**: 3

## 标签

performance; guide

## 问题描述

## Benchmark environment

- Reference: https://vllm-ascend.readthedocs.io/en/v0.7.3-dev/quick_start.html
- host environment: openEuler 22.03 LTS
- npu firmware: 7.7.0.1.231
- npu driver: 25.0.rc1
- Base docker image：quay.io/ascend/vllm-ascend:v0.7.3.post1

Download the mindie_turbo tar file from ascend website and place it in a new directory with a new Dockerfile

**Dockerfile**：

```Dockerfile
FROM quay.io/ascend/vllm-ascend:v0.7.3.post1
COPY ./Ascend-mindie-turbo_2.0.RC1_py310_linux_aarch64.tar.gz /tmp
RUN cd /tmp && \
    tar -xzvf /tmp/Ascend-mindie-turbo_2.0.RC1_py310_linux_aarch64.tar.gz  && \ 
    cd /tmp/Ascend-mindie-turbo_2.0.RC1_py310_linux_aarch64 && \
    pip install --no-deps *.whl  && \
    pip cache purge
```

or
```Dockerfile
FROM quay.io/ascend/vllm-ascend:v0.7.3.post1
RUN pip install mindie-turbo==2.0rc1 && pip cache purge
```
 and then build a new image and then run the new docker image and perform testing.


## Test step

#### Case 1 Qwen3-32B TP4
`vllm serve Qwen3-32B --gpu_memory_utilization=0.92 --port 32561 --rope-scaling '{"rope_type":"yarn","factor":4,"original_max_position_embeddings":32768}' --max-model-len 131072  -tp 4`

#### Case 2 DeepSeek-R1-0528-Qwen3-8B TP1
`vllm serve DeepSeek-R1-0528-Qwen3-8B --gpu_memory_utilization=0.92 --port 32563 --rope-scaling '{"rope_type":"yarn","factor":2,"original_max_position_embeddings":32768}' --max-model-len  65536`

## Results

For qwen3-32b with 4 NPUs,  inference speed increased from **_8 tokens/s to 18 tokens/s._**
For  DeepSeek-R1-0528-Qwen3-8B with 1 NPU,  inference speed increased from **_20 tokens/s to 34 tokens/s._**

But, for DeepSeek-R1-0528-Qwen3-8B, I am not sure whether the model support rope scaling, beacuse when I pulled the service, I received some messages, even though the model is running normally:

`
Unrecognized keys in `rope_scaling` for 'rope_type'='yarn': {'attn_factor'}
`

| Model                     | TP | baseline | v0.7.3.post1 + mindie turbo |
|---------------------------|----|---------------------|-----------------------------|
| Qwen3-32b                 | 4  | 8 tokens/s          | 18 tokens/s                 |
| DeepSeek-R1-0528-Qwen3-8B | 1  | 20 token/s          | 34 tokens/s                 |

- baseline: v0.8.5rc1 **without** any optimized

### Misc discussion on performance

_No response_

### Your current environment (if you think it is necessary)

```text
The output of `python collect_env.py`
```

