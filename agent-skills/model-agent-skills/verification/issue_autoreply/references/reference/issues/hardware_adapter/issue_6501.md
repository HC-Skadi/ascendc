# Issue #6501: [Doc][Misc] Restructure tutorial documentation

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR refactors the tutorial documentation by restructuring it into three categories: Models, Features, and Hardware. This improves the organization and navigation of the tutorials, making it easier for users to find relevant information.

- The single `tutorials/index.md` is split into three separate index files:
  - `docs/source/tutorials/models/index.md`
  - `docs/source/tutorials/features/index.md`
  - `docs/source/tutorials/hardwares/index.md`
- Existing tutorial markdown files have been moved into their respective new subdirectories (`models/`, `features/`, `hardwares/`).
- The main `index.md` has been updated to link to these new tutorial sections.

This change makes the documentation structure more logical and scalable for future additions.

### Does this PR introduce _any_ user-facing change?

Yes, this PR changes the structure and URLs of the tutorial documentation pages. Users following old links to tutorials will enc

## 基本信息
- **编号**: #6501
- **作者**: wangxiyuan
- **创建时间**: 2026-02-03T07:02:14Z
- **关闭时间**: 2026-02-10T07:03:35Z
- **标签**: documentation

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6501)
