# Issue #31: Question about the difference of inference results between NPU and GPU

## 基本信息

- **编号**: #31
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/31
- **创建时间**: 2025-02-11T02:59:29Z
- **关闭时间**: 2025-04-01T10:30:47Z
- **更新时间**: 2025-10-14T16:22:02Z
- **提交者**: @AIR-hl
- **评论数**: 10

## 标签

bug

## 问题描述

The inference results on the GPU are significantly different from those on the NPU. We used the same code and set temperature=0 to ensure reproducibility. Additionally, the speed on NPU is significant lower than A800, even 4090. I want to know if this is normal?

`vllm`: 0.7.2
`vllm-ascend`: latest
`GPU`: A800, 4090
`NPU`: 910b3


A800: ![Image](https://github.com/user-attachments/assets/a9f92434-3d0b-47a7-99cd-f45449b691de)

910b3: ![Image](https://github.com/user-attachments/assets/ca7e8aec-86ac-4fdb-b45e-789b3d070d61)

One of inference result on 910b3 occured repeat, it never happend on other deivces. 
![Image](https://github.com/user-attachments/assets/63d1aaa3-e6c3-40bd-980b-d7919f3f0370)

