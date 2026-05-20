# Issue #2316: [RFC]: Prefill performance optimizaiton for Allgather EP

## 基本信息

- **编号**: #2316
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2316
- **创建时间**: 2025-08-11T09:04:06Z
- **关闭时间**: 2026-01-19T07:53:43Z
- **更新时间**: 2026-01-19T07:53:54Z
- **提交者**: @realliujiaxu
- **评论数**: 0

## 标签

RFC

## 问题描述

### Motivation.

The community is continuously optimizing the performance of the Alltoall EP approach (e.g., https://github.com/vllm-project/vllm-ascend/pull/1802). However, for Atlas 800I/T A2, the Allgather EP solution demonstrates superior performance compared to Alltoall [1].

First, the implementation of Flash Comm1 needs to be completed. In PR1802, only the Alltoall EP was implemented, while the FFN layer and the MoE layer with Allgather EP still require implementation.

After implementing Flash Comm1, further optimization of DP communication is needed. The diagram below illustrates the computation-communication flow under TP8 DP2. Taking the two communications before MoE as an example, the total communication volume of TP8 Allgather is the same as that of DP2 Broadcast. However, the former operates within a single machine, while the latter involves inter-machine communication. Since inter-machine bandwidth is only about 1/7 of intra-machine bandwidth, the latency of DP2 Broadcast is significantly higher than that of TP8 Allgather (empirical measurements show a ~6x difference for a sequence length of 32k).

<img width="2026" height="176" alt="Image" src="https://github.com/user-attachments/assets/1152c390-9a1b-4a64-ad5e-be75789a0c6f" />

The optimization approach is shown in the diagram below, again using the pre-MoE communication as an example. The key idea is to convert DP2 Broadcast into DP2 Allgather via padding and then merge it with TP8 Allgather into an EP16 Allgather. HCCL has optimized communication for this scenario—taking the Pipeline algorithm [3] as an example, the latency of EP16 Allgather is approximately twice that of TP8 Allgather. In this case, the TP8 Allgather required by the shared expert TP8 is merged, so the shared expert must be adjusted to TP16. The optimization principle for post-MoE communication is similar, requiring the merging of communication operators into an EP16 ReduceScatter.

<img width="2026" height="132" alt="Image" src="https://github.com/user-attachments/assets/67f48e9f-eb1b-48a0-892b-b22980fdf548" />

We have implemented the aforementioned optimizations in our private repository, achieving approximately 15% throughput improvement ​​over  Flash Comm1​​.

### Proposed Change.

- [x] Implement Flash Comm1 for MoE layer with Allgather EP and FFN layer: https://github.com/vllm-project/vllm-ascend/pull/3334
- [x] Optimize performance in DP scenarios
   - [x] Replace DP multi broadcast with allgather，and merge with TP allgather: https://github.com/vllm-project/vllm-ascend/pull/3334
   - [x] Replace DP allreduce+slicewith reducescatter，and merge with TP reducescatter: https://github.com/vllm-project/vllm-ascend/pull/3334

[1] https://gitcode.com/ascend-tribe/ascend-inference-cluster/blob/main/Overview/%E5%8D%8E%E4%B8%BA%E6%98%87%E8%85%BE%E6%9C%8D%E5%8A%A1%E5%99%A8_DeepSeek_V3_R1_%E6%8E%A8%E7%90%86%E9%83%A8%E7%BD%B2%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5.pdf
[2] https://gitcode.com/ascend-tribe/ascend-inference-cluster/blob/main/FlashComm/FlashComm%E5%A4%A7%E6%A8%A1%E5%9E%8B%E6%8E%A8%E7%90%86%E4%B8%AD%E7%9A%84AllReduce%E9%80%9A%E4%BF%A1%E4%BC%98%E5%8C%96%E6%8A%80%E6%9C%AF.pdf
[3] https://gitee.com/ascend/cann-hccl#/ascend/cann-hccl/blob/master/docs/Pipeline.md

### Feedback Period.

_No response_

### CC List.

@jianzs @ApsarasX @zzzzwwjj @ganyi1996ppo @zhaozx-cn

### Any Other Things.

_No response_
