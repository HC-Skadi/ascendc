# Issue #5422: [Misc] fast fail for exiting if tools/install_flash_infer_attention_score_ops_a2.sh

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Use `set -euo pipefail` to exit if tools/install_flash_infer_attention_score_ops_a2.sh failed in any line

### How was this patch tested?
test pass locally:
<img width="1789" height="82" alt="image" src="https://github.com/user-attachments/assets/dfd7fad5-5d14-4ce4-88df-a76fed00e631" />


- vLLM version: release/v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/81786c87748b0177111dfdc07af5351d8389baa1


## 基本信息
- **编号**: #5422
- **作者**: MengqingCao
- **创建时间**: 2025-12-27T06:37:47Z
- **关闭时间**: 2025-12-27T09:30:35Z
- **标签**: module:tools

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5422)
