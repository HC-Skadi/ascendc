# Issue #41: Flaky test: test_seed_behavior

## 基本信息

- **编号**: #41
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/41
- **创建时间**: 2025-02-11T11:50:07Z
- **关闭时间**: 2025-02-11T13:03:04Z
- **更新时间**: 2025-02-11T13:03:05Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

无

## 问题描述

```
=================================== FAILURES ===================================
______________________________ test_seed_behavior ______________________________

    def test_seed_behavior():
        # Test with seed=None
        Platform.seed_everything(None)
        random_value_1 = random.randint(0, 100)
        np_random_value_1 = np.random.randint(0, 100)
        torch_random_value_1 = torch.randint(0, 100, (1, )).item()
    
        Platform.seed_everything(None)
        random_value_2 = random.randint(0, 100)
        np_random_value_2 = np.random.randint(0, 100)
        torch_random_value_2 = torch.randint(0, 100, (1, )).item()
    
>       assert random_value_1 != random_value_2
E       assert 80 != 80

vllm-empty/tests/test_seed_behavior.py:22: AssertionError
=========================== short test summary info ============================
FAILED vllm-empty/tests/test_seed_behavior.py::test_seed_behavior - assert 80 != 80
========================= 1 failed, 13 passed in 7.28s =========================
Error: Process completed with exit code 1.
```

https://github.com/vllm-project/vllm-ascend/actions/runs/13261653117/job/37019423748
