# Issue #2254: [Feature]: Support MTP with V1 scheduler and multi-DP scenario

## 基本信息

- **编号**: #2254
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2254
- **创建时间**: 2025-08-07T03:12:30Z
- **关闭时间**: 2025-12-10T12:08:47Z
- **更新时间**: 2025-12-10T12:08:47Z
- **提交者**: @MengqingCao
- **评论数**: 3

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch

- Support MTP with V1 scheduler
- Support MTP in multi-DP scenario

### Alternatives

N/A

### Additional context

Known issues:
- Not support V1 Scheduler (chunked prefill), will be supported in a few weeks
-  vLLM v0.10.0 and main does not support metrics with DP > 1 right now, need to comment out the line 171-175 in file `vllm/vllm/v1/metrics/loggers.py`

```python
            if (len(self.engine_indexes) > 1
                and vllm_config.speculative_config is not None):
            raise NotImplementedError("Prometheus metrics with Spec Decoding "
                                      "with >1 EngineCore per AsyncLLM is not "
                                      "supported yet.")
```
