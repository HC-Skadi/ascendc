# Issue #6497: Revert "[CI] fix DS3.2 single node cudagraph_sizes config (#6241)"

**类型**: Pull Request

## 问题背景
# What this PR does / why we need it?                                                                                                                                                                                 
  This PR reverts commit 8134146ab62f90badfb6bde04cc2b4a44d9aeb13, which modified the DeepSeek V3.2 (W8A8) single-node nightly test configuration. as there is no limit between tp_size and MTP.                                  
                                                                                                                                                                                                                      
# Does this PR introduce any user-facing change?                                                                                                                                                                      
  No. This PR only affects CI/CD test configurations and does not introduce any user-facing changes.                        

## 基本信息
- **编号**: #6497
- **作者**: starmountain1997
- **创建时间**: 2026-02-02T13:47:44Z
- **关闭时间**: 2026-02-03T00:42:58Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6497)
