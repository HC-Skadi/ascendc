# Issue #1532: [Doc]: Add self-hosted runner for Atlas 300I series

## 基本信息

- **编号**: #1532
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1532
- **创建时间**: 2025-06-30T10:30:52Z
- **关闭时间**: 2026-03-01T14:22:56Z
- **更新时间**: 2026-03-01T14:22:56Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

documentation

## 问题描述

### 📚 The doc issue

```
yum install docker
useradd --create-home --user-group --shell /bin/bash --groups docker action
su action
```

Follow steps:
https://github.com/vllm-project/vllm-ascend/settings/actions/runners/new?arch=arm64&os=linux
```
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-arm64-2.325.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.325.0/actions-runner-linux-arm64-2.325.0.tar.gz
echo "0e916ad0d354089d320011c132d46bdbe3353c8b925a2e1056c7c8e85d2f2490  actions-runner-linux-arm64-2.325.0.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-arm64-2.325.0.tar.gz
./config.sh --url https://github.com/vllm-project/vllm-ascend --token XXXXXX
./run.sh
```
### Suggest a potential alternative/fix

_No response_
