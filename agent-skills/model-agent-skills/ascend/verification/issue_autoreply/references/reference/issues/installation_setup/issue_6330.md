# Issue #6330: [0.13.0][Bugfix] Fix hash conflict due to reset incompatible configuations

**类型**: Pull Request

## 问题背景

<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
Fix hash conflict due to reset incompatible configuations

```bash
python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-Omni-7B \
  -dp 2 \
  --mm-processor-cache-gb 0 \
  --no-enable-prefix-caching \
  --allowed-local-media-path ./
```
<img width="2287" height="358" alt="image" src="https://github.com/user-attachments/assets/0d963579-90c6-409b-a214-ebb8cd69cbd6" />



<!--
- Please clarify what changes you are proposing. The purpose of this section is to outline the changes and how this PR fixes the issue.
If possible, please consider writing useful notes for better and faster reviews in your PR.

- Please clarify why the changes are needed. For instance, the use case and bug description.

- Fixes #
-->

### Does this PR introduce _any_ user-facing change?
<!--
N

## 基本信息
- **编号**: #6330
- **作者**: zhangxinyuehfad
- **创建时间**: 2026-01-28T01:29:18Z
- **关闭时间**: 2026-01-28T15:08:51Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6330)
