# Issue #2603: [Usage]: vllm中如何配置具体的EP并行度数值?

## 基本信息

- **编号**: #2603
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2603
- **创建时间**: 2025-08-28T08:37:50Z
- **关闭时间**: 2025-08-28T08:38:19Z
- **更新时间**: 2025-08-28T08:38:19Z
- **提交者**: @1032120121
- **评论数**: 0

## 标签

无

## 问题描述

### Your current environment

```text
The output of above commands
```


### How would you like to use vllm on ascend


## Recommended Configuration

For example，if the average input length is 3.5k, and the output length is 1.1k, the context length is 16k, the max length of the input dataset is 7K. In this scenario, we give a recommended configuration for distributed DP server with high EP. Here we use 4 nodes for prefill and 4 nodes for decode.
<br>

| node     | DP | TP | EP | max-model-len | max-num-batched-tokens | max-num-seqs |  gpu-memory-utilization |
|----------|----|----|----|---------------|------------------------|--------------|-----------|
| prefill  | 2  |  8 | 16 |     17000     |         16384          |      4       |    0.9    |
| decode   | 64 |  1 | 64 |     17000     |          256           |      28      |    0.9    |

如上是0.9.1rc3版本文档 docs/source/developer_guide/performance/distributed_dp_server_with_large_ep.md的内容
问题1：通过分析--tensor-parallel-size 8 看样子是每台机器8卡，请问例子中DP是4个节点一共32张卡，如何配置DP是64？4台机器--data-parallel-size最大也就是32 ，--data-parallel-size-local=1，难道1张卡能分两个DP？

问题2：vllm配置EP是--enable-expert-parallel，如何像例子要求的那样明确指定EP为64？

