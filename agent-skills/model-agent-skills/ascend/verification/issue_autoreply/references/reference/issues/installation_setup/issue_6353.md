# Issue #6353: [CI] Add per pr image build for nightly test

**类型**: Pull Request

## 问题背景
<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
<!--
- Please clarify what changes you are proposing. The purpose of this section is to outline the changes and how this PR fixes the issue.
If possible, please consider writing useful notes for better and faster reviews in your PR.

- Please clarify why the changes are needed. For instance, the use case and bug description.

- Fixes #
-->
This patch add per pr image build for branch `releases/v0.13.0`, Due to the limitations of the quay naming convention, we should not name the image tag  the same as branch name, we name the image tag  `v0.13.0-dev` for daily build.
When will the image being built and push:
- pull_request: build only
- push: build and push
- tag: build and push

### Does this PR introduce _any_ user-facing change?
<!--
Note that it means *any* user-facing change including a

## 基本信息
- **编号**: #6353
- **作者**: Potabk
- **创建时间**: 2026-01-28T08:49:06Z
- **关闭时间**: 2026-01-28T13:40:15Z
- **标签**: ready

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6353)
