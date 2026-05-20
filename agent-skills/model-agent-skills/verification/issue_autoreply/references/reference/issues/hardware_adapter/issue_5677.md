# Issue #5677: Eliminate H2D copy bubbles by leveraging asynchronous stream scheduling.

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
When updating experts, it is necessary to update the expert_map and log2phy on the device side, which will result in long-duration H2D operations. These operations can be hidden via asynchronous streams.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?
Qwen3-235B-A22B-w8a8 dynamic eplb
before covering up
<img width="650" height="183" alt="6666" src="https://github.com/user-attachments/assets/47d0cac4-f5ff-436f-bb2b-3e0353002f51" />


after covering up
<img width="650" height="166" alt="ScreenShot_20260107145853" src="https://github.com/user-attachments/assets/13d20cf7-d201-4731-8b89-168cda487587" />


## 基本信息
- **编号**: #5677
- **作者**: mengxingkongzhouhan
- **创建时间**: 2026-01-07T02:46:38Z
- **关闭时间**: 2026-01-23T06:26:15Z
- **标签**: documentation, module:tests, merge-conflicts

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5677)
