# Issue #6152: [0.13.0][Bugix] fix kv pcp+pooling+pd separation bug

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Rectify the problem that the pcp and pd separation and kv pooling scenario.

In the pooling scenario, multi_nodes_meta_mapping is empty. As a result, an error is reported when the remote_host information is obtained through the get_remote_port_send_num method.
### Does this PR introduce _any_ user-facing change?
No

### How was this patch tested?

pick-from: https://github.com/vllm-project/vllm-ascend/pull/6153

## 基本信息
- **编号**: #6152
- **作者**: weiguihua2
- **创建时间**: 2026-01-22T12:11:13Z
- **关闭时间**: 2026-01-23T08:15:10Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6152)
