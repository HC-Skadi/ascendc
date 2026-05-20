# Issue #467: [Feature]: Co-locating NPU support for GRPO training with trl

## 基本信息

- **编号**: #467
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/467
- **创建时间**: 2025-04-03T09:33:37Z
- **关闭时间**: 2025-08-29T02:34:29Z
- **更新时间**: 2025-08-29T02:34:29Z
- **提交者**: @Switchsyj
- **评论数**: 3

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch

Hello, as I notice that trl (vllm-ascend) now supports to inference on a independent node during training. Does it allow to inference alongside other workloads on the same GPU as training (i.e. TP or PP)?

I think this would be useful as single-node/NPU inference could be wasteful, reducing inference throughput and  training efficiency.

I think the core thing is how to update grouped parameters, adapting to NPU (but I am not very familiar with that). If there's any possibilities, I would like to help.

See the issue implemented on GPUs: https://github.com/huggingface/trl/pull/3162

### Alternatives

_No response_

### Additional context

To be specifically, I guess the difference should lie in init and broadcast process:
init:
```python
pg = StatelessProcessGroup.create(host=self.host, port=self.group_port, rank=self.rank, world_size=world_size) --> replace with corresponding  group manager?
self.pynccl_comm = PyNcclCommunicator(pg, device="cuda:0")  --> replace with NPUCommunicator
```
broadcast:
```python
self.pynccl_comm.broadcast(weights, src=self.rank, stream=torch.cuda.current_stream())
self.pynccl_comm.group.barrier() --> replace with some NPU broadcast method?
```
