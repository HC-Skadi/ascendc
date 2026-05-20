# Issue #3075: [Bug][infra]: infran runner are stucking at offline status, and all job queued

## 基本信息

- **编号**: #3075
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3075
- **创建时间**: 2025-09-22T00:56:01Z
- **关闭时间**: 2025-12-23T12:53:19Z
- **更新时间**: 2025-12-23T12:53:19Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment
https://github.com/vllm-project/vllm-ascend/actions/runs/17899621625/job/50890880619#logs

<img width="1036" height="204" alt="Image" src="https://github.com/user-attachments/assets/aea5eec5-c85f-45ab-bb6a-38ef6e82d582" />

### 🐛 Describe the bug

```
[e2e-test / singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/17899621625/job/50890880619#logs)
Started 2h 42m 34s ago


Job is about to start running on the runner: linux-aarch64-a2-1
Requested labels: linux-aarch64-a2-1
Job defined at: vllm-project/vllm-ascend/.github/workflows/_e2e_test.yaml@refs/heads/main
Reusable workflow chain:
vllm-project/vllm-ascend/.github/workflows/vllm_ascend_test_full_vllm_main.yaml@refs/heads/main (693f547ccf01194f291b30cf2923d220e4a44dd9)
-> vllm-project/vllm-ascend/.github/workflows/_e2e_test.yaml@refs/heads/main (693f547ccf01194f291b30cf2923d220e4a44dd9)
Waiting for a runner to pick up this job...
Requested labels: linux-aarch64-a2-1
Job defined at: vllm-project/vllm-ascend/.github/workflows/_e2e_test.yaml@refs/heads/main
Reusable workflow chain:
vllm-project/vllm-ascend/.github/workflows/vllm_ascend_test_full_vllm_main.yaml@refs/heads/main (693f547ccf01194f291b30cf2923d220e4a44dd9)
-> vllm-project/vllm-ascend/.github/workflows/_e2e_test.yaml@refs/heads/main (693f547ccf01194f291b30cf2923d220e4a44dd9)
Waiting for a runner to pick up this job...
Requested labels: linux-aarch64-a2-1
Job defined at: vllm-project/vllm-ascend/.github/workflows/_e2e_test.yaml@refs/heads/main
Reusable workflow chain:
vllm-project/vllm-ascend/.github/workflows/vllm_ascend_test_full_vllm_main.yaml@refs/heads/main (693f547ccf01194f291b30cf2923d220e4a44dd9)
-> vllm-project/vllm-ascend/.github/workflows/_e2e_test.yaml@refs/heads/main (693f547ccf01194f291b30cf2923d220e4a44dd9)
Waiting for a runner to pick up this job...
```

