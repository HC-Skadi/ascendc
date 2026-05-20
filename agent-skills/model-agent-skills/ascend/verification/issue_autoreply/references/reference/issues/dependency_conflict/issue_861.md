# Issue #861: [Bug]: V0 Scheduler is incapable of the newest KVCacheManager interface in vllm main branch code

## 基本信息

- **编号**: #861
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/861
- **创建时间**: 2025-05-14T14:26:54Z
- **关闭时间**: 2025-07-13T09:06:20Z
- **更新时间**: 2025-07-13T09:06:20Z
- **提交者**: @gawainx
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm-ascend: main branch
vllm: main branch
```

</details>


### 🐛 Describe the bug

First, I'm sorry for omitting some env details here, because we found this bug in our private server environment. 
In short summary, in vllm-ascend, we use additional config to enable v0 style scheduler for better performance. However, when we install the newest code `d066e52013be278c7a3bc54ec9799d8457895f4d` of vllm and 218f21d..68fb634 of vllm-ascend, we encountered errors when dealing with requests such as 
```
Runtime Error: object of type KVCacheBlocks has no len()  
```
## What happened?
The root cause of this problem is that, recently, the vllm project has rewritten the following methods of KVCacheManager (details can be found at this [PR](https://github.com/vllm-project/vllm/pull/17479)):
- Introduce `KVCacheBlocks`
- get_computed_blocks method returns `tuple[KVCacheBlocks, int]` instead of `Tuple[List[BlockHashType], int]`
- allocate_slots has one extra arg named `num_new_computed_tokens` and returns `Optional[KVCacheBlocks]`
