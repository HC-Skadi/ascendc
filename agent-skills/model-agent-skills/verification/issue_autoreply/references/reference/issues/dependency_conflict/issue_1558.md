# Issue #1558: [Bug]: vllm0.9.1rc1版本使能dp切分报错setdevice failed

## 基本信息

- **编号**: #1558
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1558
- **创建时间**: 2025-07-01T08:15:06Z
- **关闭时间**: 2025-07-01T10:53:34Z
- **更新时间**: 2025-07-01T12:12:55Z
- **提交者**: @leograssroot
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

环境信息如下：
[tmp.log](https://github.com/user-attachments/files/20994423/tmp.log)

```text
Your output of above commands here
<!-- Failed to upload "image.png" -->
```

</details>


### 🐛 Describe the bug

`执行的是vllm-ascend-0.9.1rc1\vllm-ascend-0.9.1rc1\examples\dp_offline\run_dp.sh，dp设置为16，并开启了etp=16`
报错如下：

Failed to open device
报错位置是：
`vllm-ascend-0.9.1rc1\vllm-ascend-0.9.1rc1\vllm_ascend\worker\worker_v1.py的init_device函数`

