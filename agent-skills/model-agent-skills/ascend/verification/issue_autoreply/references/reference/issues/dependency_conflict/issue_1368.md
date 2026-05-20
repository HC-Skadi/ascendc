# Issue #1368: [Bug]: Qwen3-235B deployment: Not all values of RelaxedUnspecConstraint(L['input_ids'].size()[0]) are valid because L['input_ids'].size()[0] was inferred to be a constant (2048).

## 基本信息

- **编号**: #1368
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1368
- **创建时间**: 2025-06-23T08:18:14Z
- **关闭时间**: 2025-07-06T07:29:37Z
- **更新时间**: 2025-07-06T07:29:37Z
- **提交者**: @sjtu7
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

Environment Information

```text
Ascend Card Model: D910B3
Number of Ascend Cards: 8
Ascend Driver: 7.5.0.5.220-24.1.0.3
vllm-ascend image: v0.9.0rc2
```

When I try to deploy Qwen3-235B with the following environment variables:
```text
PYTORCH_NPU_ALLOC_CONF = max_split_size_mb:256
VLLM_USE_V1 = 1
VLLM_EXTRA_ARGS = --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser deepseek_r1 --gpu-memory-utilization 0.7 --tensor-parallel-size 8
TORCH-LOGS = +dynamic
```

I get the following error:
```text
.
.
.
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:39.524000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:39.524000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:39.524000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:39.525000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:39.526000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:39.528000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:39.581000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=7 pid=300) [rank7]:I0618 08:07:39.654000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=0 pid=293) [rank0]:I0618 08:07:39.654000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=6 pid=299) [rank6]:I0618 08:07:39.654000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=2 pid=295) [rank2]:I0618 08:07:39.654000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=1 pid=294) [rank1]:I0618 08:07:39.654000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=5 pid=298) [rank5]:I0618 08:07:39.654000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:39.658000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:39.658000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:39.658000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:39.658000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:39.658000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:39.658000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:39.659000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:39.659000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:39.659000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:39.660000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:39.660000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:39.660000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:39.663000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:39.663000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:39.663000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:39.663000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:39.663000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:39.663000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:39.668000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:39.668000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:39.669000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:39.669000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:39.669000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:39.669000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=6 pid=299) [rank6]:I0618 08:07:39.686000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=2 pid=295) [rank2]:I0618 08:07:39.687000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=7 pid=300) [rank7]:I0618 08:07:39.687000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=0 pid=293) [rank0]:I0618 08:07:39.687000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=1 pid=294) [rank1]:I0618 08:07:39.687000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=5 pid=298) [rank5]:I0618 08:07:39.687000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:39.692000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:39.692000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:39.692000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:39.692000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:39.692000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:39.692000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=3 pid=296) [rank3]:I0618 08:07:39.700000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:39.704000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:39.705000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:39.709000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:39.714000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:39.715000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:39.715000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:39.715000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:39.715000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:39.715000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:39.715000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=3 pid=296) [rank3]:I0618 08:07:39.733000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:39.737000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:39.758000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:39.959000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:2498] [0/0] create_env
(VllmWorker rank=2 pid=295) [rank2]:I0618 08:07:40.009000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=7 pid=300) [rank7]:I0618 08:07:40.010000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=6 pid=299) [rank6]:I0618 08:07:40.010000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=0 pid=293) [rank0]:I0618 08:07:40.012000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=1 pid=294) [rank1]:I0618 08:07:40.017000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:40.018000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=5 pid=298) [rank5]:I0618 08:07:40.018000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:40.019000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:40.019000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:40.021000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:40.026000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:40.027000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=2 pid=295) [rank2]:I0618 08:07:40.028000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=7 pid=300) [rank7]:I0618 08:07:40.029000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=6 pid=299) [rank6]:I0618 08:07:40.030000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=0 pid=293) [rank0]:I0618 08:07:40.032000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=1 pid=294) [rank1]:I0618 08:07:40.036000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=5 pid=298) [rank5]:I0618 08:07:40.038000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=3 pid=296) [rank3]:I0618 08:07:40.052000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:40.061000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=3 pid=296) [rank3]:I0618 08:07:40.071000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=4 pid=297) [rank4]:I0618 08:07:40.078000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s0 = 2048 for L['input_ids'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s0"
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.082000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.083000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.087000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval True == True [statically known]
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.092000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s0, 1) == True [statically known]
(VllmWorker rank=4 pid=297) [rank4]:I0618 08:07:40.111000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 4*s0 <= 8192 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py:49 in vocab_parallel_embedding_forward (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="4*s0 <= 8192"
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.116000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval False == False [statically known]
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.136000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Eq(s0, 1) == False [statically known]
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:40.284000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:40.284000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:40.286000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:40.289000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:40.291000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:40.295000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:40.319000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=7 pid=300) [rank7]:V0618 08:07:40.342000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=2 pid=295) [rank2]:V0618 08:07:40.342000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=7 pid=300) [rank7]:I0618 08:07:40.343000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=2 pid=295) [rank2]:I0618 08:07:40.343000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=0 pid=293) [rank0]:V0618 08:07:40.345000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=7 pid=300) [rank7]:I0618 08:07:40.345000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=2 pid=295) [rank2]:I0618 08:07:40.345000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=0 pid=293) [rank0]:I0618 08:07:40.346000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=6 pid=299) [rank6]:V0618 08:07:40.347000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=0 pid=293) [rank0]:I0618 08:07:40.348000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=6 pid=299) [rank6]:I0618 08:07:40.349000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=1 pid=294) [rank1]:V0618 08:07:40.350000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=6 pid=299) [rank6]:I0618 08:07:40.350000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=1 pid=294) [rank1]:I0618 08:07:40.351000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=1 pid=294) [rank1]:I0618 08:07:40.353000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=5 pid=298) [rank5]:V0618 08:07:40.355000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=5 pid=298) [rank5]:I0618 08:07:40.356000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=5 pid=298) [rank5]:I0618 08:07:40.358000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=3 pid=296) [rank3]:V0618 08:07:40.378000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=3 pid=296) [rank3]:I0618 08:07:40.379000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=3 pid=296) [rank3]:I0618 08:07:40.381000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=4 pid=297) [rank4]:I0618 08:07:40.429000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:3557] [0/0] create_symbol s1 = 2048 for L['positions'].size()[0] [2, int_oo] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (_dynamo/variables/builder.py:2710 in <lambda>), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="s1"
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.439000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval Ne(s1, 1) == True [statically known]
(VllmWorker rank=4 pid=297) [rank4]:I0618 08:07:40.450000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval [guard suppressed] 8*s1 <= 16384 [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/rotary_embedding.py:67 in rope_forward_oot (utils/_stats.py:21 in wrapper), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="8*s1 <= 16384"
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.697000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5201] [0/0] eval s0 < 2 == False [statically known]
(VllmWorker rank=4 pid=297) [rank4]:V0618 08:07:40.755000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:4734] [0/0] _update_var_to_range s0 = VR[2048, 2048] (update)
(VllmWorker rank=4 pid=297) [rank4]:I0618 08:07:40.756000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:4857] [0/0] set_replacement s0 = 2048 (range_refined_to_singleton) VR[2048, 2048]
(VllmWorker rank=4 pid=297) [rank4]:I0618 08:07:40.758000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:5106] [0/0] eval Eq(s0, 2048) [guard added] at llm-workspace/vllm-ascend/vllm_ascend/ops/fused_moe.py:636 in fused_experts (_ops.py:1116 in __call__), for more info run with TORCHDYNAMO_EXTENDED_DEBUG_GUARD_ADDED="Eq(s0, 2048)"
(VllmWorker rank=3 pid=296) INFO 06-18 08:08:07 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_3_0 for vLLM's torch.compile
(VllmWorker rank=3 pid=296) INFO 06-18 08:08:07 [backends.py:469] Dynamo bytecode transform time: 28.18 s
(VllmWorker rank=2 pid=295) INFO 06-18 08:08:07 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_2_0 for vLLM's torch.compile
(VllmWorker rank=2 pid=295) INFO 06-18 08:08:07 [backends.py:469] Dynamo bytecode transform time: 28.30 s
(VllmWorker rank=6 pid=299) INFO 06-18 08:08:08 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_6_0 for vLLM's torch.compile
(VllmWorker rank=6 pid=299) INFO 06-18 08:08:08 [backends.py:469] Dynamo bytecode transform time: 28.59 s
(VllmWorker rank=7 pid=300) INFO 06-18 08:08:08 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_7_0 for vLLM's torch.compile
(VllmWorker rank=7 pid=300) INFO 06-18 08:08:08 [backends.py:469] Dynamo bytecode transform time: 28.76 s
(VllmWorker rank=1 pid=294) INFO 06-18 08:08:08 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_1_0 for vLLM's torch.compile
(VllmWorker rank=1 pid=294) INFO 06-18 08:08:08 [backends.py:469] Dynamo bytecode transform time: 29.00 s
(VllmWorker rank=4 pid=297) INFO 06-18 08:08:08 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_4_0 for vLLM's torch.compile
(VllmWorker rank=4 pid=297) INFO 06-18 08:08:08 [backends.py:469] Dynamo bytecode transform time: 28.70 s
(VllmWorker rank=5 pid=298) INFO 06-18 08:08:08 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_5_0 for vLLM's torch.compile
(VllmWorker rank=5 pid=298) INFO 06-18 08:08:08 [backends.py:469] Dynamo bytecode transform time: 29.29 s
(VllmWorker rank=0 pid=293) INFO 06-18 08:08:08 [backends.py:459] Using cache directory: /home/ma-user/.cache/vllm/torch_compile_cache/9c7e260518/rank_0_0 for vLLM's torch.compile
(VllmWorker rank=0 pid=293) INFO 06-18 08:08:08 [backends.py:469] Dynamo bytecode transform time: 29.32 s
(VllmWorker rank=3 pid=296) INFO 06-18 08:08:15 [backends.py:170] Compiling a graph for general shape takes 3.60 s
(VllmWorker rank=2 pid=295) INFO 06-18 08:08:15 [backends.py:170] Compiling a graph for general shape takes 3.73 s
(VllmWorker rank=6 pid=299) INFO 06-18 08:08:15 [backends.py:170] Compiling a graph for general shape takes 3.78 s
(VllmWorker rank=7 pid=300) INFO 06-18 08:08:15 [backends.py:170] Compiling a graph for general shape takes 3.73 s
(VllmWorker rank=1 pid=294) INFO 06-18 08:08:16 [backends.py:170] Compiling a graph for general shape takes 3.75 s
(VllmWorker rank=5 pid=298) INFO 06-18 08:08:16 [backends.py:170] Compiling a graph for general shape takes 3.72 s
(VllmWorker rank=4 pid=297) INFO 06-18 08:08:16 [backends.py:170] Compiling a graph for general shape takes 3.87 s
(VllmWorker rank=0 pid=293) INFO 06-18 08:08:16 [backends.py:170] Compiling a graph for general shape takes 3.92 s
(VllmWorker rank=3 pid=296) [rank3]:I0618 08:08:21.021000 296 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=2 pid=295) [rank2]:I0618 08:08:21.158000 295 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=6 pid=299) [rank6]:I0618 08:08:21.514000 299 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=7 pid=300) [rank7]:I0618 08:08:21.671000 300 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=1 pid=294) [rank1]:I0618 08:08:21.930000 294 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=4 pid=297) [rank4]:I0618 08:08:22.243000 297 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=5 pid=298) [rank5]:I0618 08:08:22.283000 298 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=0 pid=293) [rank0]:I0618 08:08:22.452000 293 site-packages/torch/fx/experimental/symbolic_shapes.py:3646] [0/0] produce_guards
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0] Error while creating guard:
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0] Name: ''
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     Source: shape_env
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     Create Function: SHAPE_ENV
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     Guard Types: None
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     Code List: None
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     Object Weakref: None
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     Guarded Class Weakref: None
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0] Traceback (most recent call last):
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_guards.py", line 281, in create
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     return self.create_fn(builder, self)
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/guards.py", line 1836, in SHAPE_ENV
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     guards = output_graph.shape_env.produce_guards(
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/experimental/symbolic_shapes.py", line 4178, in produce_guards
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]     raise ConstraintViolationError(
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0] torch.fx.experimental.symbolic_shapes.ConstraintViolationError: Constraints violated (L['input_ids'].size()[0])! For more information, run with TORCH_LOGS="+dynamic".
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.681000 296 site-packages/torch/_guards.py:283] [0/0]   - Not all values of RelaxedUnspecConstraint(L['input_ids'].size()[0]) are valid because L['input_ids'].size()[0] was inferred to be a constant (2048).
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0] Created at:
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 615, in transform
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]     tracer = InstructionTranslator(
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 2670, in __init__
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]     output=OutputGraph(
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 317, in __init__
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]     self.init_ambient_guards()
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 463, in init_ambient_guards
(VllmWorker rank=3 pid=296) [rank3]:E0618 08:08:25.686000 296 site-packages/torch/_guards.py:285] [0/0]     self.guards.add(ShapeEnvSource().make_guard(GuardBuilder.SHAPE_ENV))
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 146, in determine_available_memory
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     self.model_runner.profile_run()
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1521, in profile_run
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     hidden_states = self._dummy_run(self.max_num_tokens)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1488, in _dummy_run
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     hidden_states = model(
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 518, in forward
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 238, in __call__
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     output = self.compiled_callable(*args, **kwargs)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 465, in _fn
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 1269, in __call__
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return self._torchdynamo_orig_callable(
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 526, in __call__
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return _compile(
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 924, in _compile
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     guarded_code = compile_inner(code, one_graph, hooks, transform)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 666, in compile_inner
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return _compile_inner(code, one_graph, hooks, transform)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_utils_internal.py", line 87, in wrapper_function
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return function(*args, **kwargs)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 796, in _compile_inner
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     check_fn = CheckFunctionManager(
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/guards.py", line 2261, in __init__
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     guard.create(builder)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_guards.py", line 281, in create
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return self.create_fn(builder, self)
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/guards.py", line 1836, in SHAPE_ENV
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     guards = output_graph.shape_env.produce_guards(
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/experimental/symbolic_shapes.py", line 4178, in produce_guards
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     raise ConstraintViolationError(
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522] torch.fx.experimental.symbolic_shapes.ConstraintViolationError: Constraints violated (L['input_ids'].size()[0])! For more information, run with TORCH_LOGS="+dynamic".
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   - Not all values of RelaxedUnspecConstraint(L['input_ids'].size()[0]) are valid because L['input_ids'].size()[0] was inferred to be a constant (2048).
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522] 
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522] 
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522] You can suppress this exception and fall back to eager by setting:
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     import torch._dynamo
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     torch._dynamo.config.suppress_errors = True
(VllmWorker rank=3 pid=296) ERROR 06-18 08:08:25 [multiproc_executor.py:522] 
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0] Error while creating guard:
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0] Name: ''
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     Source: shape_env
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     Create Function: SHAPE_ENV
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     Guard Types: None
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     Code List: None
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     Object Weakref: None
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     Guarded Class Weakref: None
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0] Traceback (most recent call last):
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_guards.py", line 281, in create
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     return self.create_fn(builder, self)
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/guards.py", line 1836, in SHAPE_ENV
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     guards = output_graph.shape_env.produce_guards(
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/experimental/symbolic_shapes.py", line 4178, in produce_guards
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]     raise ConstraintViolationError(
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0] torch.fx.experimental.symbolic_shapes.ConstraintViolationError: Constraints violated (L['input_ids'].size()[0])! For more information, run with TORCH_LOGS="+dynamic".
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.749000 295 site-packages/torch/_guards.py:283] [0/0]   - Not all values of RelaxedUnspecConstraint(L['input_ids'].size()[0]) are valid because L['input_ids'].size()[0] was inferred to be a constant (2048).
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0] Created at:
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 615, in transform
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]     tracer = InstructionTranslator(
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/symbolic_convert.py", line 2670, in __init__
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]     output=OutputGraph(
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 317, in __init__
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]     self.init_ambient_guards()
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/output_graph.py", line 463, in init_ambient_guards
(VllmWorker rank=2 pid=295) [rank2]:E0618 08:08:25.751000 295 site-packages/torch/_guards.py:285] [0/0]     self.guards.add(ShapeEnvSource().make_guard(GuardBuilder.SHAPE_ENV))
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 146, in determine_available_memory
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     self.model_runner.profile_run()
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1521, in profile_run
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     hidden_states = self._dummy_run(self.max_num_tokens)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1488, in _dummy_run
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     hidden_states = model(
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return self._call_impl(*args, **kwargs)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return forward_call(*args, **kwargs)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 518, in forward
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 238, in __call__
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     output = self.compiled_callable(*args, **kwargs)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 465, in _fn
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return fn(*args, **kwargs)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 1269, in __call__
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return self._torchdynamo_orig_callable(
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 526, in __call__
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return _compile(
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 924, in _compile
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     guarded_code = compile_inner(code, one_graph, hooks, transform)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 666, in compile_inner
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return _compile_inner(code, one_graph, hooks, transform)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_utils_internal.py", line 87, in wrapper_function
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return function(*args, **kwargs)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/convert_frame.py", line 796, in _compile_inner
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     check_fn = CheckFunctionManager(
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/guards.py", line 2261, in __init__
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     guard.create(builder)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_guards.py", line 281, in create
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     return self.create_fn(builder, self)
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/guards.py", line 1836, in SHAPE_ENV
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     guards = output_graph.shape_env.produce_guards(
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/experimental/symbolic_shapes.py", line 4178, in produce_guards
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]     raise ConstraintViolationError(
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522] torch.fx.experimental.symbolic_shapes.ConstraintViolationError: Constraints violated (L['input_ids'].size()[0])! For more information, run with TORCH_LOGS="+dynamic".
(VllmWorker rank=2 pid=295) ERROR 06-18 08:08:25 [multiproc_executor.py:522]   - Not all values of RelaxedUnspecConstraint(L['input_ids'].size()[0]) are valid because L['input_ids'].size()[0] was inferred to be a constant (2048).
.
.
.
```


### 🐛 Describe the bug


Are there any solutions for this error ?
