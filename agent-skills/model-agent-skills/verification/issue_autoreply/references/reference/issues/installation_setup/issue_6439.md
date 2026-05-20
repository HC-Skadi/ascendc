# Issue #6439: Upgrade Mooncake to v0.3.8.post1

**类型**: Pull Request

## 问题背景
Upgrades Mooncake distributed KV cache system from v0.3.7.post2 to v0.3.8.post1 across all build and deployment artifacts.

## Changes

- **Dockerfiles**: Update `MOONCAKE_TAG` to v0.3.8.post1 in all variants (base, a3, openEuler)
- **Documentation**: Update version references in PD tutorials and KV pool guide
- **Installer dependencies** (`tools/mooncake_installer.sh`):
  - Upgrade yalantinglibs: 0.5.5 → 0.5.6
  - Add missing packages: `unzip`, `liburing-dev/devel`, `libjemalloc-dev/devel` for both apt and yum
- **CI workflow**: Add PR trigger for Dockerfile changes to validate builds before merge

Dependency additions align with upstream Mooncake v0.3.8.post1 requirements per [dependencies.sh](https://github.com/kvcache-ai/Mooncake/blob/v0.3.8.post1/dependencies.sh).

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [C

## 基本信息
- **编号**: #6439
- **作者**: Copilot
- **创建时间**: 2026-01-30T11:43:47Z
- **关闭时间**: 2026-01-30T12:02:34Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6439)
