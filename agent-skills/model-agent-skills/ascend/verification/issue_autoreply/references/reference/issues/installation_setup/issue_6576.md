# Issue #6576: Remove CPLUS_INCLUDE_PATH and add `patch`

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR makes two changes to the openEuler Dockerfiles (`Dockerfile.310p.openEuler`, `Dockerfile.a3.openEuler`, `Dockerfile.openEuler`):

1.  Adds the `patch` package to the `yum install` command. This utility is required for applying patches during the build process.
2.  Removes the `export CPLUS_INCLUDE_PATH` from the `vllm-ascend` installation step. This environment variable is no longer necessary and its removal cleans up the build configuration.

### Does this PR introduce _any_ user-facing change?

No. This only affects the build environment for developers and CI.

### How was this patch tested?

CI is expected to pass with these changes. The changes are validated by successfully building the Docker images.

## 基本信息
- **编号**: #6576
- **作者**: wjunLu
- **创建时间**: 2026-02-05T12:06:07Z
- **关闭时间**: 2026-02-05T13:06:07Z
- **标签**: image-build

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6576)
