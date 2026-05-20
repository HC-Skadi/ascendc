# Issue #4637: [Bug]: ascend多模态不支持merge_by_field_config

## 基本信息

- **编号**: #4637
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4637
- **创建时间**: 2025-12-02T09:54:06Z
- **关闭时间**: 2025-12-09T08:25:38Z
- **更新时间**: 2025-12-09T08:25:38Z
- **提交者**: @Dog-Boss
- **评论数**: 3

## 标签

bug; module:multimodal

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

## 我的预期
我正在从gpu上迁移客户的模型到npu上，当前模型期待的输入shape如下
<img width="1878" height="228" alt="Image" src="https://github.com/user-attachments/assets/be1b040d-b0b3-4b7b-8ccb-a0759eb2b3c1" />
但在npu环境上由于如下的代码差异，导致npu上的shape会再多一个维度
## 代码
在gpu平台上

<img width="2950" height="1390" alt="Image" src="https://github.com/user-attachments/assets/17566b92-ad7d-433c-a9a8-c711c5b71d9b" />

在npu平台上
<img width="2783" height="1280" alt="Image" src="https://github.com/user-attachments/assets/831e1805-0937-403e-ad29-18bfad10cbf5" />
## group_mm_kwargs_by_modality的执行结果
在gpu平台上
<img width="3283" height="520" alt="Image" src="https://github.com/user-attachments/assets/b9211f3e-c053-46c1-aa2e-95bd7b184a5b" />
在npu平台上
<img width="3753" height="540" alt="Image" src="https://github.com/user-attachments/assets/b86013ee-66f0-40fb-afbe-7b8c0815626e" />



