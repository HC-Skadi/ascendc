# Issue #6677: Add Worker Interface:check_health

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
We found that some worker interfaces called by vLLM are missing in vLLM Ascend. It's good to add the support. more details see issue https://github.com/vllm-project/vllm-ascend/issues/4112

### Does this PR introduce _any_ user-facing change?
No

### How was this patch tested?
use rpc method to call check_health, like
llm.collective_rpc("check_health")
if success the output is 
(EngineCore_DP0 pid=201) INFO 02-11 02:57:22 [worker.py:577] check_health Start!
(EngineCore_DP0 pid=201) INFO 02-11 02:57:23 [worker.py:588] check_health succsess!

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/13397841ab469cecf1ed425c3f52a9ffc38139b5


## 基本信息
- **编号**: #6677
- **作者**: luomin2005
- **创建时间**: 2026-02-11T03:22:05Z
- **关闭时间**: 2026-02-11T05:55:31Z
- **标签**: 无

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6677)
