# Issue #6349: [Refactor][EAGLE] 6/N route mtp to eagle except pcp/dcp+mtp

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

Overview: This pull request refactors speculative decoding for Eagle and MTP proposers on Ascend hardware. It fixes a bug related to draft_attn_metadatas being lost, migrates the lmhead feature, and adds routing logic in MtpProposer.

Details:
1. Migrated the lmhead feature from mtp to eagle and normalized it in eagle_proposer.
2. Fixed the bug where draft_attn_metadatas was lost after enabling eagle mode in the merge graph.
3. Added the routing for pcp and disable padded drafter batch; in mtp mode, if pcp and disable padded drafter batch are not enabled, the normalized file eagle_proposer will be used.

RFC: https://github.com/vllm-project/vllm-ascend/issues/5467

### Does this PR introduce _any_ user-facing change?
No

### How was this patch tested?
ut and test

- vLLM version: v0.14.1
- vLLM main: https://github.com/vllm-project/vllm/commit/dc917cceb877dfd13f98c538c4c96158047d98bd


## 基本信息
- **编号**: #6349
- **作者**: lilinsiman
- **创建时间**: 2026-01-28T07:34:15Z
- **关闭时间**: 2026-02-02T11:15:31Z
- **标签**: module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6349)
