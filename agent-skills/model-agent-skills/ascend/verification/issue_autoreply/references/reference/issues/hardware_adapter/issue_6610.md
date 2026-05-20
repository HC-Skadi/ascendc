# Issue #6610: [refactor]Optimized the kvcache usage of Deepseek v3.2

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

For deepseek v3.2, DSA use FullAttentionSpec, allocate 2 * mla page size bytes, and we use half of that for k cache in DSA

However, the actual proportion of k cache is not high, which results in a large amount of kvcache being wasted. The proportion of discarded kvcache is (576-128)/(576 x 2) = 0.388.

Run the same script to start DeepSeek V3.2 on a single A3 server. The following shows the comparison of kvcache usage:
Before refactoring
```
[kv_cache_utils.py:1307] GPU KV cache size: 15,872 tokens
```
After refactoring
```
[kv_cache_utils.py:1307] GPU KV cache size: 25,984 tokens
```

This pull request refactors the KV cache allocation for Deepseek v3.2 models that use sparse attention. It replaces the use of `FullAttentionSpec` with `MLAAttentionSpec` and introduces a more principled way of calculating KV cache tensor split factors based on model configuration.

This change removes hardcoded values and correctly sizes the ca

## 基本信息
- **编号**: #6610
- **作者**: kunpengW-code
- **创建时间**: 2026-02-07T06:57:24Z
- **关闭时间**: 2026-02-09T10:53:57Z
- **标签**: 无

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6610)
