# Issue #6871: [Bugfix] Fix openEuler dockerfile error

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
<img width="1396" height="436" alt="image" src="https://github.com/user-attachments/assets/4f41b79f-ae66-40bf-ab3d-5f48a5da18c7" />

This pull request addresses several issues within the openEuler Dockerfiles : `Dockerfile.a3.openEuler` and `Dockerfile.openEuler` to ensure correct installation and setup of the Mooncake dependency. The changes primarily involve fixing incorrect file paths for the mooncake_installer.sh script and streamlining the declaration of the MOONCAKE_TAG build argument, leading to more robust and accurate container builds.
### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.16.0
- vLLM main: https://github.com/vllm-project/vllm/commit/15d76f74e2fdb12a95ea00f0ca283acf6219a2b7


## 基本信息
- **编号**: #6871
- **作者**: wjunLu
- **创建时间**: 2026-02-28T07:13:39Z
- **关闭时间**: 2026-02-28T12:55:19Z
- **标签**: image-build

## 涉及版本
- vLLM: v0.16.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6871)
