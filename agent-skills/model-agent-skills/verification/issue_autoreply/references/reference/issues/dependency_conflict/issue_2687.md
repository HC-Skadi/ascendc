# Issue #2687: [Bug]: CI recover

## 基本信息

- **编号**: #2687
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2687
- **创建时间**: 2025-09-02T00:56:35Z
- **关闭时间**: 2025-10-24T01:51:19Z
- **更新时间**: 2025-10-24T01:51:19Z
- **提交者**: @wangxiyuan
- **评论数**: 0

## 标签

bug

## 问题描述

### E2E

- [ ] pangu e2e: https://github.com/vllm-project/vllm-ascend/actions/runs/17381972219/job/49345577933 @Angazenn 
- [ ] external_launch: https://github.com/vllm-project/vllm-ascend/actions/runs/17378882992/job/49337926556 @leo-pony 
  https://github.com/vllm-project/vllm-ascend/issues/2546
- [ ] pipeline parallel: https://github.com/vllm-project/vllm-ascend/actions/runs/17388587603/job/49361210399?pr=2276 @MengqingCao 
- [x] prefix cache on main: https://github.com/vllm-project/vllm-ascend/actions/runs/17390602780/job/49367294023?pr=2688 @MengqingCao 
- [x] lora: https://github.com/vllm-project/vllm-ascend/pull/2672
- [x] other: https://github.com/vllm-project/vllm-ascend/pull/2688

### UT

- [ ] test_platform.py fails random when run `pytest -sv tests/ut`. It works if only run the file sepratly
- [ ] TestCustomVocabParallelEmbedding failed when run by `pytest -sv tests/ut/ops/test_vocab_parallel_embedding.py`
