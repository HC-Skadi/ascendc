# Issue #644: [Release]: vLLM Ascend v0.7.3 release checklist

## 基本信息

- **编号**: #644
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/644
- **创建时间**: 2025-04-24T08:07:42Z
- **关闭时间**: 2025-05-14T06:02:12Z
- **更新时间**: 2025-05-14T06:02:13Z
- **提交者**: @MengqingCao
- **评论数**: 13

## 标签

无

## 问题描述

### This issue tracks the checklist for official v0.7.3 release

#### Code develop
- [x] Wait for CANN8.1 release, then update dockerfile base image  https://github.com/vllm-project/vllm-ascend/pull/747 @Yikun 
- [x] Update torch-npu to 2.5.1 official release @MengqingCao 
  https://github.com/vllm-project/vllm-ascend/pull/662
- [x] PR waiting for merge/review/close @wangxiyuan 
  https://github.com/vllm-project/vllm-ascend/pull/525 @linfeng-yuan 
  https://github.com/vllm-project/vllm-ascend/pull/695
  https://github.com/vllm-project/vllm-ascend/pull/685
  https://github.com/vllm-project/vllm-ascend/pull/678
  https://github.com/vllm-project/vllm-ascend/pull/702
- [x] lora support cherry-pick @paulyu12  @Yikun 
  https://github.com/vllm-project/vllm-ascend/pull/700
- [x] write release note @Yikun 
  https://github.com/vllm-project/vllm-ascend/pull/735
- [x] CPU memory overleak @celestialli 
  https://github.com/vllm-project/vllm-ascend/pull/691
#### Documant enhancement
- **Installation** @MengqingCao 
  https://github.com/vllm-project/vllm-ascend/pull/708
  - [x] install from source code
    - [x] vllm
    - [x] vllm-ascend[mindie-turbo]
  - [x] install from binary
    - [x] vllm
    - [x] vllm-ascend
    - [x] mindie-turbo
  - [x] install with docker

- **User Guide**
  - [x] Use ascend scheduler with V1 Engine @MengqingCao  https://github.com/vllm-project/vllm-ascend/issues/788
  - [x] Improve performance with  python and pytorch @wangxiyuan https://github.com/vllm-project/vllm-ascend/pull/735
  - [x] Update doc to address compile enhancement @MengqingCao 
    https://github.com/vllm-project/vllm-ascend/pull/708/
  - [x] FAQ cherry-pick @Potabk 
    https://github.com/vllm-project/vllm-ascend/pull/695
    https://github.com/vllm-project/vllm-ascend/pull/795
  - [x] Feature support update @MengqingCao 
    https://github.com/vllm-project/vllm-ascend/pull/708/
  - [x] Model support update @MengqingCao 
    https://github.com/vllm-project/vllm-ascend/pull/708/
  - [x] Accurary report @hfadzxy https://github.com/vllm-project/vllm-ascend/pull/793
    Add index page once the report exist.
  - [x] Performance feedback issue: https://github.com/vllm-project/vllm-ascend/issues/776 @Potabk
   
- **Developer Guide**
   - [x] Update Release Compatibility Matrix include mindie-turbo verion: https://github.com/vllm-project/vllm-ascend/pull/735 @Yikun 
#### Function and Model Test
  - [x] key models: 
    - [x] qwen2.5
    - [x] deepseek-v3
    - [x] qwen2.5-vl
  - [x] features
    If the certain feature usage is different from the original usage in vllm, we need to add one for vllm-ascend[mindie-turbo]
    - [x] chunked prefill @MengqingCao 
      rely on CANN 8.1 nnal
    - [x] custom ops @celestialli 
    - [x] guided decoding – same as vllm @shen-shanshan 
    - [x] sleep mode @celestialli 
      - [x] create an issue to track the sleep mode @celestialli 
        https://github.com/vllm-project/vllm-ascend/issues/733
      - [x] update feature support list to link to the issue @MengqingCao 
        https://github.com/vllm-project/vllm-ascend/pull/708/
    - [x] speculative decoding – same as vllm @MengqingCao 
    - [x] multi-step scheduler  –  same as vllm @MengqingCao 
    - [x] mtp  –  same as vllm @MengqingCao 
    - [x] prefix cache @Potabk 
    - [x] pooling model  –  same as vllm @MengqingCao 
    - [x] V1Engine @shen-shanshan 
    - [x] distribution @shen-shanshan 
      - [x] tp
      - [x] pp

#### Release artifacts @wangxiyuan 
  - [x] accuracy report @hfadzxy https://github.com/vllm-project/vllm-ascend/pull/793
    Need generate the report by hand.
  - [x] pypi package @MengqingCao https://pypi.org/project/vllm-ascend/0.7.3/
  - [x] docker image @Yikun https://github.com/vllm-project/vllm-ascend/actions/runs/14872918023/job/41866668626?pr=730

