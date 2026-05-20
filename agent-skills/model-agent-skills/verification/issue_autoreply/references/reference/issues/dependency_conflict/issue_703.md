# Issue #703: [Bug]: vllm wrong raised the ERROR : Failed to import vllm_ascend_C:No module named 'vllm_ascend.vllm_ascend_C'

## 基本信息

- **编号**: #703
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/703
- **创建时间**: 2025-04-28T08:34:25Z
- **关闭时间**: 2025-05-23T02:12:51Z
- **更新时间**: 2025-05-23T02:12:52Z
- **提交者**: @IDontNeedShirt97
- **评论数**: 6

## 标签

bug; good first issue

## 问题描述

### Your current environment

<details>
<summary>启动vllm serve服务化后出现ERROR</summary>

```text
ERROR 04-28 16:10:09 camem.py:69] Failed to import vllm_ascend_C:No module named 'vllm_ascend.vllm_ascend_C'
```

</details>


### 🐛 Describe the bug

ERROR 04-28 16:10:09 camem.py:69] Failed to import vllm_ascend_C:No module named 'vllm_ascend.vllm_ascend_C'
该ERROR为没有编译ascendc custom op导致，但并不影响服务化进程及正常推理进行，建议将日志级别改为Warning或在文档中注明其是否影响推理精度结果

<img width="1402" alt="Image" src="https://github.com/user-attachments/assets/3c0acf26-4d3e-495b-b2ca-54f1dffb50d8" />
