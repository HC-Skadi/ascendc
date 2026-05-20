# Issue #3380: [RFC]: Elastic Scaling Support for P/D Instances Based on KV Pool

## 基本信息

- **编号**: #3380
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3380
- **创建时间**: 2025-10-11T07:17:08Z
- **关闭时间**: 2026-01-05T06:52:33Z
- **更新时间**: 2026-01-05T06:52:33Z
- **提交者**: @CalvinXKY
- **评论数**: 6

## 标签

RFC

## 问题描述

### Motivation.

In disaggregated P/D scenarios, supporting elastic scaling for P/D instances is a critical requirement for large-scale inference deployment, as mentioned in the [vLLM 2025 Q3 roadmap](https://github.com/vllm-project/vllm/issues/20336) “Autoscaling P & D Replicas”. This functionality not only improves resource utilization but also provides fault tolerance support. Particularly on Ascend super-nodes, where instances typically deploy across multiple devices, recreation can have a broad impact, making this capability especially important.

### Proposed Change.

Currently, with the support of distributed KV cache features such as Mooncake Store and Mem Cache, we can leverage them as a foundation to implement elastic scaling for P/D instances.
When scaling instances, it is essential to manage three types of linkages:

- a. D2D links between P and D, established by connectors and other components;
- b. Links between P/D and the KV Pool;
- c. Links between P/D and the scheduler;
This involves processes such as instance registration, link disconnection/establishment, and link reconstruction. 

<img width="1008" height="375" alt="Image" src="https://github.com/user-attachments/assets/b48da932-b87d-47c3-a22e-db3ca9c68287" />

**Implementation plan:**
1 Homogeneous Scaling
1.1 Implementation of P-instance scaling
1.2 Implementation of D-node scaling

2 Heterogeneous Scaling
2.1 Support for heterogeneous KV cache transmission
2.2 Support for heterogeneous transmission in P/D configurations


### CC List.

@yuxinshan @LCAIZJ 


