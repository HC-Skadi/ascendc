# Issue #1351: [v0.9.1rc1] FAQ / Feedback | 问题/反馈

## 基本信息

- **编号**: #1351
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1351
- **创建时间**: 2025-06-22T02:06:51Z
- **关闭时间**: 2025-07-13T15:52:55Z
- **更新时间**: 2025-07-13T15:52:55Z
- **提交者**: @Yikun
- **评论数**: 16

## 标签

release

## 问题描述

Please use doc: https://vllm-ascend.readthedocs.io
Next release: https://github.com/vllm-project/vllm-ascend/issues/1486

-------

请使用 https://vllm-ascend.readthedocs.io 安装

```
9acc082 2025-06-28 [BugFix] Fix accuray bug of prefix-caching. (#1492) whx
45e33e4 2025-06-27 [0.9.1]Refactoring w4a8 and w8a8 and supporting w4a8 graph mode (#1480) pichangping
0c99cf7 2025-06-27 [v0.9.1][CI] Fix CI error (#1475) wangxiyuan
8d1e59c 2025-06-27 [BugFix] Fix the problem that torchair doesn't support tp > 4. (#1404) whx
105d2df 2025-06-27 [v0.9.1][Fix] Fix block table shape (#1297) yiz-liu
6856f9d 2025-06-26 [v0.9.1][BugFix] Fix DBO bug after attn_metadata_refactor (#1445) shikang-hangzhou
263af3b 2025-06-26 Fix a bug of ascend_forward_context (#1449) liziyu
bf17152 2025-06-26 [v0.9.1][Bugfix] Reset all unused positions to prevent out-of-bounds in GatherV3 (#1397) yiz-liu
10ee2e7 2025-06-26 [BugFix] Fix a bug of running chunked-prefill with torchair. (#1378) whx
3191183 2025-06-26 [BugFix]dbo support torchair graph in decode (#1420) shikang-hangzhou
bc546a9 2025-06-26 [v0.9.1][perf] add a switch for enabling NZ layout in weights and enable NZ for GMM. (#1409) linfeng-yuan
43591c3 2025-06-26 [CI/UT][BugFix] Fix sampling params (#1423) Ruri
cd65d15 2025-06-25 [refactor] Refactoring forward_context and model_runner_v1 (#1422) zzzzwwjj
ce4bdab 2025-06-25 [Refactor] Remove duplicate multimodal codes in ModelRunner (#1393) yiz-liu
```
