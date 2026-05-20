# Issue #491: [Usage]: 如何设置do_rescale

## 基本信息

- **编号**: #491
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/491
- **创建时间**: 2025-04-09T08:14:07Z
- **关闭时间**: 2025-05-14T03:48:26Z
- **更新时间**: 2025-05-14T03:48:27Z
- **提交者**: @Huang-zhenxuan
- **评论数**: 3

## 标签

无

## 问题描述

### Your current environment

```text
The output of above commands
```



### How would you like to use vllm on ascend

部署qwen2.5-vl-72b-instruct时出现如下信息：

![Image](https://github.com/user-attachments/assets/c4250e1a-853c-4f3d-8f3a-e5dbf6a095eb)

此外，是否令do_rescale=Fasle，然后修改模型文件的preprocessor_config.json中的分辨率参数，就可以修改图片的分辨率

