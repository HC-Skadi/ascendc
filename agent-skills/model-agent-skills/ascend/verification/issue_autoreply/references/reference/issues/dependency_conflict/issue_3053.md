# Issue #3053: [Bug]: Recover test on #2907

## 基本信息

- **编号**: #3053
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3053
- **创建时间**: 2025-09-20T03:32:44Z
- **关闭时间**: 2025-12-23T12:53:10Z
- **更新时间**: 2025-12-23T12:53:10Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug


- [ ] pytest -sv --cov --cov-report=xml:unittests-coverage.xml tests/ut \
--ignore=tests/ut/test_platform.py \
--ignore=tests/ut/patch/worker/patch_common/test_patch_minicpm.py

- [ ] pytest -sv tests/e2e/multicard/test_data_parallel.py

