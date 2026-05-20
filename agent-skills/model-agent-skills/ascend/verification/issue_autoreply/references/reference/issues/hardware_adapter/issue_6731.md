# Issue #6731: [Doc][Skill] Introduce AI-assisted model-adaptation workflow for vllm-ascend

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it

This PR introduces the **first AI-assisted model-adaptation skill package** for `vllm-ascend`.

The goal is to make model adaptation work (especially for recurring feature-request issues) **repeatable, auditable, and easier to hand off**.

### Scope in this PR

This PR adds only skill/workflow assets under:

- `.agents/skills/vllm-ascend-model-adapter/SKILL.md`
- `.agents/skills/vllm-ascend-model-adapter/references/workflow-checklist.md`
- `.agents/skills/vllm-ascend-model-adapter/references/troubleshooting.md`
- `.agents/skills/vllm-ascend-model-adapter/references/multimodal-ep-aclgraph-lessons.md`
- `.agents/skills/vllm-ascend-model-adapter/references/fp8-on-npu-lessons.md`
- `.agents/skills/vllm-ascend-model-adapter/references/deliverables.md`

### Workflow improvements

The skill standardizes:

1. **Environment assumptions** used in our Docker setup
- implementation roots: `/vllm-workspace/vllm` and `/vllm-workspace/vllm

## 基本信息
- **编号**: #6731
- **作者**: QwertyJack
- **创建时间**: 2026-02-12T14:30:56Z
- **关闭时间**: 2026-02-26T00:48:16Z
- **标签**: documentation

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6731)
