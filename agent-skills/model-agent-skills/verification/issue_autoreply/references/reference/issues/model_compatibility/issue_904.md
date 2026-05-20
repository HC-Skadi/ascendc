# Issue #904: [release] 0.9.0rc1 release checklist

## 基本信息

- **编号**: #904
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/904
- **创建时间**: 2025-05-20T03:48:21Z
- **关闭时间**: 2025-07-26T07:21:43Z
- **更新时间**: 2025-07-26T07:21:43Z
- **提交者**: @wangxiyuan
- **评论数**: 12

## 标签

release

## 问题描述

This issue track the workflow for the next release 0.9.0rc1

### PR merged

Need merge first:
https://github.com/vllm-project/vllm-ascend/pull/1016
- [x] #766
- [ ] #989
- [x] #990 
- [x] #1003
- [x] #1016 
- [x] #1029 
- [x] #916

Need review and merge:
  * dense and multimodal
  - [x] #736
  - [ ]  #751 

  * DeepSeek:
  - [x] #970
  - [ ] #993
  - [x] #1012
  - [x] #1023
  - [x] #905 
  - [ ] #919 
  - [x] #941

* RL:
 - [x] #987
 - [ ] #997 
 - [x] #1067
 - [x] #1013 

Pending (will **NOT** be included in 0.9.0rc1):
- [ ] #796
- [ ] #978 

- [ ] #1002 
- [ ] #1032
- [ ] #1034 
- [ ] #1036 
- [ ] #1054 
- [ ] #875 
- [ ] #950 
- [ ] #973 need V1 support
- [ ] #914 need torch npu public new version

### requirement

- [x] PTA + CANN upgrade

### Functional Test (V1)

- [x] Qwen3/Qwen2.5: aclgraph + Qwen2.5/Qwen3 @MengqingCao 
    - [x] https://github.com/vllm-project/vllm-ascend/issues/1038
    - [x] https://github.com/vllm-project/vllm-ascend/issues/1043
- [x] Qwen2.5 VL: eager mode @shen-shanshan @ChenTaoyu-SJTU
    - [x] https://github.com/vllm-project/vllm-ascend/issues/1044
- [ ] DeepSeek: torchair + deepseek @zzzzwwjj 

- [ ] Quantization (w8a8) + Qwen2.5/Qwen3/DeepSeek @22dimensions 
   - [ ] Modelscope download
       - [ ] Refresh readme
       - [x] https://modelscope.cn/models/vllm-ascend/DeepSeek-R1-0528-W8A8
       - [x] https://modelscope.cn/models/vllm-ascend/Qwen3-8B-W8A8
       - [ ] https://modelscope.cn/models/vllm-ascend/Qwen2.5-0.5B-Instruct-W8A8
   - [ ] w8a8 e2e test refresh to new test
   - [ ] doc: User Guide - quantization
- [x] spec decode + mtp @mengwei805 
- [ ] performance @Potabk 
   - [ ] V0 Qwen3
   - [ ] V0 Qwen2.5
   - [ ] V0 Qwen2.5 VL
   - [ ] V1 Qwen3 need bugfix
   - [ ] V1 Qwen2.5 need bugfix
   - [ ] V1 Qwen2.5 VL
- [ ] accuracy @zhangxinyuehfad 
   - [ ] https://github.com/vllm-project/vllm-ascend/pull/1078
- [ ] DP @MengqingCao @yiz-liu 
    - [ ] dp+enger
    - [ ] dp+torchair
- [ ] EP @wangxiyuan 
    - [ ] EPLB
- [ ] PD @wangxiyuan 
    - [ ] 1P1D E2E - simple connector
    - [ ] 1P1D E2E - pyhccl
- [ ] RL related @leo-pony
    - [ ] sleep mode
    - [ ] VL pad @shen-shanshan 
- [ ] (V0) Input embeding @Potabk 
- [ ] (V1) Structed ouput @shen-shanshan 
- [ ] (V1) AscendScheduler @MengqingCao 
- [ ] (V1) Scheduler CP/APC @wangxiyuan 

### Documentation

- [x] addintion config
- [x] environment
- [x] release note
- [x] graph mode

### Release

- [x] tag、binary、image、pypi
