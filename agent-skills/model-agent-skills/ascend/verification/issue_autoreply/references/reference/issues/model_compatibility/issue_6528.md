# Issue #6528: [EPLB] Avoiding eplb's dependency on a specified model

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. Currently, eplb registers different attributes for different models, but these attributes are not actually used. Now, these attributes are directly deleted.
2. Add some log about eplb.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?
#### Deepseek v3.1 chat
Of course! Here is a comprehensive explanation of deep learning, broken down for clarity.\n\n### The Simple Analogy: A Child Learning to Recognize a Cat\n\nImagine teaching a child what a cat is. You don't give them a rulebook with instructions like \"has pointy ears, whiskers, and a tail.\" Instead, you show them many pictures, saying \"this is a cat\" or \"this is not a cat.\" The child's brain gradually learns to identify the complex patterns—the combination of shapes, colors, and textures—that define \"cat-ness.\"\n\n**Deep learning is essentially this, but for computers.** It's a method for teaching computers to learn from examples and recog

## 基本信息
- **编号**: #6528
- **作者**: shenchuxiaofugui
- **创建时间**: 2026-02-04T03:46:47Z
- **关闭时间**: 2026-02-10T07:58:44Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6528)
