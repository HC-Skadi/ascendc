# Issue #6593: [Misc] gen kv events in ascendconnector

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
refer to https://github.com/vllm-project/vllm-ascend/issues/6391,  Currently adapted the complete process of event publishing in vllm:
*  `kv_connector_model_runner_mixin`  invoke  kv-connector `get_kv_connector_kv_cache_events` func to collect kvevents
*  in `scheduler.py` , it's `update_from_output` func will invoke `_update_from_kv_xfer_finished` which invoke `connector.update_connector_output` to collect kv-events from all kv-worker, and then scheduler will invoke `connector.take_events` api to collect all kv-events and add it to the events which from `kv_cache_manager`

### Does this PR introduce _any_ user-facing change?
no
### How was this patch tested?
You can add `--kv-events-config` parameter to the `vllm server` command to enable this feature.
I have tested case:
* disable kv-events

<img width="362" height="361" alt="image" src="https://github.com/user-attachments/assets/cca0a0da-3b7b-479e-98e2-902f14cd57f6" />

<img wid

## 基本信息
- **编号**: #6593
- **作者**: yejj710
- **创建时间**: 2026-02-06T07:08:04Z
- **关闭时间**: 2026-02-12T03:01:10Z
- **标签**: 无

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6593)
