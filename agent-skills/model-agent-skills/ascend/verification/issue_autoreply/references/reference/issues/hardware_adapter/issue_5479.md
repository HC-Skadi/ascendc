# Issue #5479: [1/N] Refactor nightly test structure

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This patch is a series of refactoring actions, including clarifying the directory structure of nightly tests, refactoring the config retrieval logic, and optimizing the workflow, etc. This is the first step: refactoring the directory structure of nightly to make it more readable and logical.

The directory optimized looks like:

```shell
tests/e2e/nightly/
├── multi_node
│   ├── __init__.py
│   ├── config
│   │   ├── DeepSeek-R1-W8A8-A2.yaml
│   │   ├── DeepSeek-R1-W8A8-EPLB.yaml
│   │   ├── DeepSeek-R1-W8A8.yaml
│   │   ├── DeepSeek-V3.yaml
│   │   ├── DeepSeek-V3_2-Exp-bf16.yaml
│   │   ├── Qwen3-235B-A22B-A2.yaml
│   │   ├── Qwen3-235B-A22B.yaml
│   │   ├── Qwen3-235B-W8A8-EPLB.yaml
│   │   └── Qwen3-235B-W8A8.yaml
│   └── scripts
│       ├── __init__.py
│       ├── lws.yaml.jinja2
│       ├── multi_node_config.py
│       ├── run.sh
│       ├── test_multi_node.py
│       └── utils.py
└── single_node
    ├── models
 

## 基本信息
- **编号**: #5479
- **作者**: Potabk
- **创建时间**: 2025-12-29T08:51:26Z
- **关闭时间**: 2025-12-30T11:03:03Z
- **标签**: ci/build, module:tests

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5479)
