# Issue #4300: [RFC]: Support MTP running in full_decode_only graph mode.

## 基本信息

- **编号**: #4300
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4300
- **创建时间**: 2025-11-20T06:54:42Z
- **关闭时间**: 2025-12-15T07:16:02Z
- **更新时间**: 2025-12-15T07:16:02Z
- **提交者**: @zouyida2052
- **评论数**: 1

## 标签

RFC

## 问题描述

### Motivation.

Currently, vllm-ascend supports MTP>1 functionality in piecewise scenarios. However, the capability for MTP to operate in full_decode_only graph mode remains unsupported, resulting in significant pipeline bubbles between NPUs and causing considerable computational waste.

Enabling MTP in full_decode_only mode would allow each decoding round to be executed through whole-graph submission in a single pass. This reduces frequent operator dispatching from the CPU side, significantly minimizes bubbles between operators, enhances NPU utilization, maximizes hardware efficiency, and meets practical deployment requirements.

### Proposed Change.


Add _mtp_graph_params in acl_graph.py to isolate the data of main model and the data of MTP.
Padding some metadata in mla_v1.py when in fullgraph mode.
Fixed the essential data address that will be used in model.forward.
Adapted according to the aclgraph capture framwork:
1). Rebuild MTP model with ACLGraphWrapper.
2). Add common attn metadata when start capture in MTP dummy_run.
3). Add common attn metadata update in MTP.
4). Addapted data update when num_speculative_tokens > 1.
Add a patch of MTP to adapt vllm v0.11.0.

### Feedback Period.

No response

### CC List.

No response

### Any Other Things.

Aclgraph full_decode_only support
https://github.com/vllm-project/vllm-ascend/pull/3892
