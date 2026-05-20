# Issue #5758: [Feature]Enable DispatchGmmCombineDecode when eagle is moe with w8a8 or not moe [RFC: issue 5476]

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Operator `DispatchGmmCombineDecode` does not support non-W8A8 scenarios and cannot share the same communication domain with Operator `Dispatch`/`Combine`.
> for instance, when the draft model uses a non-W8A8 MOE architecture while the main model employs a W8A8 MOE architecture. 

Therefore days ago, I implemented an interception that unconditionally disables Operator `DispatchGmmCombineDecode` whenever the speculative mode is `EAGLE` or `EAGLE-3`. [PR: 5293](https://github.com/vllm-project/vllm-ascend/pull/5293)
However, this approach was not precise enough. 
This PR further refines the logic by specifically identifying the draft model's configuration: Operator `DispatchGmmCombineDecode` will now be disabled only when the draft model uses an MOE architecture and is non-W8A8.

More info about this operator, please refer to RFC: issue https://github.com/vllm-project/vllm-ascend/issues/5476

### Does this PR introduce _any_ user-facing cha

## 基本信息
- **编号**: #5758
- **作者**: wangqiankun13
- **创建时间**: 2026-01-09T04:56:12Z
- **关闭时间**: 2026-01-22T02:51:02Z
- **标签**: module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5758)
