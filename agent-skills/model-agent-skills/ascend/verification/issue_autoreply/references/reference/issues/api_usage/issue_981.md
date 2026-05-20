# Issue #981: [RFC]: Add pytest coverage

## 基本信息

- **编号**: #981
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/981
- **创建时间**: 2025-05-27T16:37:14Z
- **关闭时间**: 2025-07-13T15:59:14Z
- **更新时间**: 2025-07-13T15:59:14Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

help wanted; RFC

## 问题描述

### Motivation.

Guide us improve test coverage 

### Proposed Change.

I do a trial on test coverage:

```
# Run real test and generate the coverage.xml
pytest -sv --cov --cov-branch --cov-report=xml tests/singlecard

# Use codecov upload
curl -Os https://uploader.codecov.io/latest/aarch64/codecov
chmod +x codecov
./codecov --verbose upload-process --fail-on-error -t XXXXXXXXX -F service -f coverage.xml
```

We can also upload using github action:
```
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v5
      env:
        CODECOV_TOKEN: ${{ secrets.codecov_token }}
      with:
        files: ./coverage.xml
        flags: unittests
        name: vllm-ascend
        verbose: true
```

<img width="1334" alt="Image" src="https://github.com/user-attachments/assets/3dff7be6-fbbb-4f2e-b590-74057dd61c1f" />

Preview: https://app.codecov.io/gh/Yikun/vllm-ascend/tree/main

Reference: https://github.com/apache/spark/commit/87ffe7adddf517541aac0d1e8536b02ad8881606

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
