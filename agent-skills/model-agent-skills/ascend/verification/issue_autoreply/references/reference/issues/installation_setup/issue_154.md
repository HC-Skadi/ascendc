# Issue #154: [Installation]: 910B3 import toch_npu 出现段错误

## 基本信息

- **编号**: #154
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/154
- **创建时间**: 2025-02-25T02:38:38Z
- **关闭时间**: 2025-02-28T07:49:47Z
- **更新时间**: 2025-02-28T07:49:48Z
- **提交者**: @mhqmhy
- **评论数**: 4

## 标签

installation

## 问题描述

### Your current environment

```text
npu-smi info
```

![Image](https://github.com/user-attachments/assets/a3aabf6e-cd13-40d8-bd09-cb6120196931)

cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info

![Image](https://github.com/user-attachments/assets/48ed5fd6-5c1f-4ea2-a8f6-bb7ad5770191)

python collect_env.py

![Image](https://github.com/user-attachments/assets/0971c9f4-42ff-40b9-8e0b-c077c264bf2d)

![Image](https://github.com/user-attachments/assets/faeafe17-bea9-42d0-a0f6-5d3fb404c65f)

![Image](https://github.com/user-attachments/assets/752b33ae-b82c-4254-8eeb-d7c1b8fb46d4)



### How you are installing vllm and vllm-ascend

```sh
源码安装
```

