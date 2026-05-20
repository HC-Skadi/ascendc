# Issue #143: [Installation]: 910B部署vllm-ascend启动失败

## 基本信息

- **编号**: #143
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/143
- **创建时间**: 2025-02-22T13:30:36Z
- **关闭时间**: 2025-03-05T01:37:39Z
- **更新时间**: 2025-03-06T12:02:06Z
- **提交者**: @ahutkai
- **评论数**: 7

## 标签

installation

## 问题描述

### Your current environment

```text
vllm启动serve 提示torch-npu缺少torch_npu.npu_selfattention、torch_npu.npu_rope函数，用的torch-npu和torch版本都是2.4.0，是bug么？

<img width="1096" alt="Image" src="https://github.com/user-attachments/assets/130ec6bc-752f-4a37-ae43-701fbe16fff1" />

```


### How you are installing vllm and vllm-ascend

```sh
pip install -vvv vllm vllm-ascend
```

