# Issue #2735: [Doc]: Make docker image more friendly for devs

## 基本信息

- **编号**: #2735
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2735
- **创建时间**: 2025-09-04T01:15:44Z
- **关闭时间**: 2025-09-05T01:45:12Z
- **更新时间**: 2025-09-05T01:45:12Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

help wanted

## 问题描述

### 📚 The doc issue

For vllm-ascend code, we have to:
1. Remove `http.https://github.com/.extraheader`
```
    - uses: actions/checkout@v4
      with:
        persist-credentials: false
```

2. `git pull --shallow``fetch-depth: 0`: https://github.com/vllm-project/vllm-ascend/blob/main/.github/workflows/image_ubuntu.yml#L52C13-L52C32

### Suggest a potential alternative/fix

_No response_
