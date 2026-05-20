# Issue #6832: [CI] Fix doc test fail when load model with error information: 'Stale file handle'

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR fixes a `Stale file handle` error that occurs during doctests in the CI environment. The error appears when loading models from ModelScope, likely due to issues with network file systems used in CI.

The fix involves setting the `MODELSCOPE_HUB_FILE_LOCK` environment variable to `false` in the `run_doctests.sh` script. This disables file locking in the ModelScope hub, which is a common workaround for this type of file system error.

### Does this PR introduce _any_ user-facing change?

No, this change only affects the CI test execution environment and has no impact on users.

### How was this patch tested?

This change is validated by the CI pipeline. A successful run of the doctests indicates that the fix is effective.

## 基本信息
- **编号**: #6832
- **作者**: leo-pony
- **创建时间**: 2026-02-26T09:31:22Z
- **关闭时间**: 2026-02-27T01:14:42Z
- **标签**: module:tests

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6832)
