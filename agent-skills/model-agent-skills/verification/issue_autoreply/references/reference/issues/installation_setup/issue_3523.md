# Issue #3523: [RFC]: Add vllm-ascend nightly test

## 基本信息

- **编号**: #3523
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3523
- **创建时间**: 2025-10-17T13:40:32Z
- **关闭时间**: 2025-12-15T09:37:03Z
- **更新时间**: 2025-12-15T09:37:03Z
- **提交者**: @jiangyunfan1
- **评论数**: 1

## 标签

RFC

## 问题描述

### Motivation.

Currently, the vLLM-Ascend community includes the following automated tests:

1. Unit Tests (UT), which include tests that can run on the CPU, used for basic unit testing of function implementations.
2. End-to-End (E2E) Tests, which include single-card tests, multi-card tests, documentation tests, and precision tests that run on the Ascend NPU environment.
   The current E2E tests have the following gaps:
   **1. Lack of online testing:** Currently, many tests are oriented towards development scenarios, while few threshold tests derive from the user's perspective, such as serving tests in online scenarios.
   **2. Lack of daily smoke tests:** The current daily smoke tests only include documentation tests and precision tests, which are insufficient for quality assurance.

Therefore, we suggest to add daily smoke tests (nightly tests) to monitor the daily code quality and provide important references during version upgrades, key dependency upgrades, version to testing, and release phases of vLLM.

### Proposed Change.

Different from ut and e2e test defined by developer self-testing, which is triggered by each PR and mainly conducted during daytime, we propose to add a daily smoke test (nightly test) in the community. This test would be triggered at a scheduled time after the environment becomes idle in the small hours, with a total duration of approximately 2-3 hours. The existing test cases and CI processes will remain unchanged. In addition, we suggest:

1. Since the smoke test reflects the most basic version quality, a full set of smoke tests should be passed before releasing RC versions or official versions.
2. If the smoke test fails, no further PRs should be merged until the issue is resolved. Developers should address the smoke test problems as soon as possible. If the PR which introduces the issue were found, the developer may choose to fix it or revert.

### 1. Test Cases and Execution Strategy

The initial batch of smoke test cases to be launched is listed in the table below:

| Case Name and Required Resource                             | Estimated Time (Success) |
| --------------------------------------------------------------- | ------------------ |
| A2, 4 Cards:                                              |                  |
| Qwen3-32B-W8A8 A2 single-operator function                    | 5min             |
| Qwen3-32B-W8A8 A2 aclgraph function            | 6min             |
| Qwen3-32B-W8A8 A2 aclgraph performance               | 19min            |
| Qwen3-32B-W8A8 A2 aclgraph accuracy aime2024  | 22min            |
| A3, 4 Die:                                                 |                  |
| Qwen3-32B-W8A8 A3 single-operator function                    | 6min             |
| Qwen3-32B-W8A8 A3 aclgraph function            | 6min             |
| Qwen3-32B-W8A8 A3 aclgraph performance               | 16min            |
| Qwen3-32B-W8A8 A3 aclgraph accuracy aime2024  | 27min            |
| Qwen3-32B-W8A8 A3 feature stack function            |              |
| Qwen3-32B-W8A8 A3 feature stack performance               |             |
| Qwen3-32B-W8A8 A3 feature stack accuracy gsm8k  |             |
| Qwen2.5-VL-7B A3 performance               |             |
| Qwen2.5-VL-32B A3 accuracy  |             |
| Qwen3-32B-W8A8 A3 prefixcache function            |        |
| A3, 16 Die:                                                  |                  |
| DeepSeek-R1-W8A8 A3 single-operator function                    | 12min            |
| DeepSeek-R1-W8A8 A3 torchair function            | 12min            |
| DeepSeek-R1-W8A8 A3 torchair performance            | 16min            |
| DeepSeek-R1-W8A8 A3 torchair accuracy gsm8k | 8min             |
| DeepSeek-R1-W8A8 A3 aclgraph performance  |             |
| DeepSeek-R1-W8A8 A3 chunkprefill function            |       |
| DeepSeek-R1-W8A8 A3 prefixcache function            |       |
| 2A2 16 Cards                                                    |                  |
| DeepSeek-R1-W8A8 2A2 single-operator function                    | 6min             |
| DeepSeek-R1-W8A8 2A2 torchair function            | 13min            |
| DeepSeek-R1-W8A8 2A2 torchair accuracy gsm8k  | 5min             |
| 2A3 32 Die                                                  |                  |
| Qwen3-235B-W8A8 aclgraph            |          |
| 4A3 64 Die                                                  |                  |
| DeepSeek-R1-W8A8 2P1D torchair accuracy gsm8k  |         |
| DeepSeek-R1-W8A8 2P1D torchair performance  |         |

- Cases mainly involve function, performance, and accuracy. Function cases test the request response after starting the vllm server with a specific configuration. Accuracy is judged according to whether it meets the version requirements, and performance should not be worse than the baseline.
- Hardware requires single and double A2, single A3, and future additions will include 4A2, 2A3 PD separation test, and other scenarios, as well as cases for enabling a specific feature.
- Cases will continue to be added.

### 2. Code Design

#### 2.1 Test Methodology and Directory Design

All tests will be based on pyteste and are online tests (aligned with the target scenarios).

Function test refers to: https://github.com/vllm-project/vllm/blob/36429096171ff8785645c40c662d859dddedd829/tests/utils.py

Performance and accuracy are tested with Aisbench.

A directory named nightly will be added under the e2e directory in tests, with the general structure as follows:

```
vllm-ascend/tests/e2e/nightly/
    configs/ # configurations for performance and accuracy test cases
        *.yaml
    models/  # model performance and accuracy tests
        test_*.py
    feature/  # feature-related test cases
        function_call/
        prefix_cache/
        ...
    conftest.py
    multi_node/ # multi-node test cases
```

#### 2.2 Pipeline and Environment Deployment

Consistent with existing test cases, the environment is built based on the upstream base image which consists of the latest commercial versions of CANN and PTA.

For single-machine tasks: Add.github/workflows/vllm_ascend_nightly_test.yaml to cover the multi-card tasks for both single A2 and A3

Multi-machine tasks: Refer to https://github.com/vllm-project/vllm-ascend/issues/3501 for details.

#### 2.3 Model Weights

Consistent with existing test cases, model weights are obtained from the vllm-ascend repository on ModelScope:
https://modelscope.cn/organization/vllm-ascend

If the required weight for a test case are not available in this repository, it should be uploaded to ModelScope and will be downloaded and cached to the server during the first run.

#### 2.4 AISBench Performance and Accuracy Testing

Aligned with the version release strategy, all performance and accuracy test with AISBench.

The AISBench public method will be created in tools directory of vllm-ascend:tools/aisbench.py, which will be called by all performance and accuracy test cases in nightly test.

As model weights, the datasets used in the test cases are obtained from the vllm-ascend repository on ModelScope. If additional datasets are required, they should be uploaded to ModelScope first, and will be downloaded and cached to the server during the first run.

The AISBench environment is set up during each pipeline run, and the latest release of AISBench is installed. The installation process takes approximately 1 minute.

The performance and accuracy tests in the nightly test are currently not intended to provide daily performance and accuracy data, but data integration in the daily dashboard may be considered in future.

#### 2.5 Extension and Evolution

The changes required for adding new test cases generally include:

- To Add new function test cases: Only the model path and server configuration need to be added.
- To Add new performance and accuracy test cases: Only the AISBench configuration items need to be added.

If a case in nightly test frequently failed due to bugs introduced by code changes, it could be converted into PR-level e2e test.

All test cases are provided as examples for external contribution reference.


### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

Please continuously add new cases followed by the table of initial cases above.
