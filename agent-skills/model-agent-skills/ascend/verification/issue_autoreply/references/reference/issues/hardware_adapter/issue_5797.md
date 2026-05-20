# Issue #5797: [CI] Add 310p e2e test back

**类型**: Pull Request

## 问题背景
This PR add 310 e2e test back to ensure the related PR will be tested on 310.
1. for light e2e, we'll run 310p test if the changed files are located in `vllm_ascend/_310p`
2. for full e2e, we'll always run 310p test
3. for main2main test, we'll stop run 310p test

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5797
- **作者**: wangxiyuan
- **创建时间**: 2026-01-12T07:20:33Z
- **关闭时间**: 2026-01-15T07:47:13Z
- **标签**: ci/build, module:tests

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5797)
