# Issue #5747: [Bug]: 强化学习场景（例如Verl）开启NZ+matmul_allreduce后rollout参数无法正常更新

**类型**: Issue

## 问题背景
### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

如图，`self.layer.weight`经过`.t()`，会从`nn.Parameters`变为`torch.tensor`。而NZ会导致`self.layer.weight`的内存地址发生改变，当强化学习场景训推参数同步的时候，只会更新`self.layer.weight`的参数，不会更新`self.weight_t`，就会导致精度问题。现象是`actor_rollout_ref.rollout.load_format=dummy`时，第一步推理出现乱码。

<img width="1738" height="996" alt="Image" src="https://github.com/user-attachments/assets/a9ee579f-7f67-48c1-9a75-0d95eb86c436" />

<img width="1444" height="478" alt="Image" src="https://github.com/user-attachments/assets/0d3e40fd-e918-457b-ab2c-bf8236e7e053" />

## 基本信息
- **编号**: #5747
- **作者**: icerain-alt
- **创建时间**: 2026-01-09T02:15:04Z
- **关闭时间**: 2026-01-12T03:31:35Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5747)
