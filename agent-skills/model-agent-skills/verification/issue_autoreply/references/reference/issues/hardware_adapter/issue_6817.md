# Issue #6817: [Doc][Misc] Refactor skill documentation and add Claude support instructions

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR refactors the documentation for vLLM Ascend skills.
- It renames and moves the `vllm-ascend-model-adapter` skill's README to serve as a new top-level README for the `.agents` directory.
- It adds instructions on how to use the Ascend skills with Claude, including a new README in the `.claude` directory.
- It updates `.gitignore` to exclude skills copied for Claude's use.
- Add main2main skill

This improves the documentation structure, making it more organized and providing clear instructions for developers using these skills with different tools.

### Does this PR introduce _any_ user-facing change?
No, this PR contains only documentation and repository configuration changes. It does not affect any user-facing code functionality.

### How was this patch tested?
These changes are documentation-only and do not require specific testing. The correctness of the instructions is being verified through this review.

- vLLM version

## 基本信息
- **编号**: #6817
- **作者**: wangxiyuan
- **创建时间**: 2026-02-26T01:19:14Z
- **关闭时间**: 2026-02-26T06:43:00Z
- **标签**: documentation

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6817)
