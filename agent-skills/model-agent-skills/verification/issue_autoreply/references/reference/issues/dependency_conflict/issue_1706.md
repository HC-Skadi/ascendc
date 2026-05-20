# Issue #1706: [Bug]: The task didn't exit properly: TBE Subprocess [task_distribute] raise error[]

## 基本信息

- **编号**: #1706
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1706
- **创建时间**: 2025-07-09T09:34:17Z
- **关闭时间**: 2025-11-17T11:44:54Z
- **更新时间**: 2025-11-17T11:44:54Z
- **提交者**: @zheliuyu
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

Related to [198](https://github.com/vllm-project/vllm-ascend/issues/198).



### 🐛 Describe the bug

When the task ends, print:
```
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
```


Adding additional ```ray.shutdown()``` can avoid the problem, and gpu doesn't need. Can these errors be solved without adding ```ray.shutdown()``` ？
