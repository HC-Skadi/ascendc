# Issue #1253: [Bug]: Flaky test: test_models_distributed_topk failed due to The IP address and port have been bound already.

## 基本信息

- **编号**: #1253
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1253
- **创建时间**: 2025-06-17T06:28:57Z
- **关闭时间**: 2026-03-01T14:23:20Z
- **更新时间**: 2026-03-01T14:23:20Z
- **提交者**: @Yikun
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/15698407645/job/44229396205?pr=1250

### 🐛 Describe the bug

```
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492] Traceback (most recent call last):
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 466, in worker_main
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     worker = WorkerProc(*args, **kwargs)
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/executor/multiproc_executor.py", line 363, in __init__
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.worker.load_model()
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 199, in load_model
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.model_runner.load_model()
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1284, in load_model
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     return loader.load_model(vllm_config=vllm_config,
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/base_loader.py", line 38, in load_model
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     model = initialize_model(vllm_config=vllm_config,
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/model_loader/utils.py", line 62, in initialize_model
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 771, in __init__
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 697, in __init__
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.start_layer, self.end_layer, self.layers = make_layers(
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 626, in make_layers
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     [PPMissingLayer() for _ in range(start_layer)] + [
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/utils.py", line 627, in <listcomp>
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 699, in <lambda>
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     lambda prefix: CustomDeepseekV2DecoderLayer(
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 594, in __init__
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.mlp = CustomDeepseekV2MoE(
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 258, in __init__
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.experts = AscendFusedMoE(
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/ops/fused_moe.py", line 1089, in __init__
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.quant_method = AscendUnquantizedFusedMoEMethod(moe)
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]   File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/ops/fused_moe.py", line 862, in __init__
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492]     self.moe_all_to_all_group_name = backend.get_hccl_comm_name(
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492] RuntimeError: createHCCLComm:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:1508 HCCL function error: HcclGetRootInfo(&hcclID), error code is 7
Error: (VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492] [ERROR] 2025-06-17-06:11:33 (PID:10233, Device:2, RankID:-1) ERR0[220](https://github.com/vllm-project/vllm-ascend/actions/runs/15698407645/job/44229396205?pr=1250#step:10:222)0 DIST call hccl api failed.
(VllmWorker rank=2 pid=10233) ERROR 06-17 06:11:34 [multiproc_executor.py:492] EJ0003: [PID: 10233] 2025-06-17-06:11:32.832.492 Failed to bind the IP port. Reason: The IP address and port have been bound already.
```
