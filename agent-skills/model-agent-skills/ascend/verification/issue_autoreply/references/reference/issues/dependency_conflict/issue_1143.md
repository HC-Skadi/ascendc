# Issue #1143: [Bug]: e2e test / long-term-test schedule job failed due to 400 Client Error: Bad Request

## 基本信息

- **编号**: #1143
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1143
- **创建时间**: 2025-06-10T01:24:29Z
- **关闭时间**: 2025-06-15T07:44:18Z
- **更新时间**: 2025-06-15T07:44:18Z
- **提交者**: @Yikun
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/15523499551/job/43699801183

### 🐛 Describe the bug

```
/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/hub/errors.py:205: HTTPError
=========================== short test summary info ============================
FAILED tests/long_term/spec_decode/e2e/test_v1_mtp_correctness.py::test_mtp_correctness - requests.exceptions.HTTPError: 400 Client Error: Bad Request, Request id: 56829d2fbd114f2c99159bd1b6764367 for url: https://www.modelscope.cn/api/v1/login, body: b'{"AccessToken": "***"}'
============================== 1 failed in 27.23s ==============================
```
