# Issue #2552: [RFC]: Refactoring MoE Communication for ACL Graph Compatibility and Performance Optimization

## 基本信息

- **编号**: #2552
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2552
- **创建时间**: 2025-08-26T09:04:59Z
- **关闭时间**: 2025-10-16T06:21:13Z
- **更新时间**: 2025-10-16T06:21:13Z
- **提交者**: @yiz-liu
- **评论数**: 2

## 标签

RFC

## 问题描述

### Motivation.

The primary goal of this refactoring is to make Mixture of Experts (MoE) models fully compatible with the ACL Graph execution mode on Ascend NPUs. MoE models often require different communication strategies depending on the context of the execution step (e.g., a token-intensive prefill phase versus a latency-sensitive decode phase). However, not all communication primitives are capturable by a static graph. For instance, communication like AlltoAll might be efficient but incompatible with ACL Graph (due to D2H operations), whereas a simpler AllGather can be graphed but may be less performant.

The previous MoE implementation was monolithic, tightly coupling the computation with a single communication method. This made it impossible to switch strategies at runtime or to isolate graph-compatible components from dynamic ones. Consequently, MoE layers could not be effectively accelerated with ACL Graph, creating a significant performance bottleneck.

We now introduces a comprehensive refactoring to address this, decoupling communication from computation using a strategy pattern, enabling the dynamic selection of the most appropriate communication method for each forward pass. This allows us to use graph-captured kernels for compatible strategies (like AllGather) while falling back to eager execution for more complex, non-graphable strategies (like AlltoAll), thus achieving both correctness and optimal performance across all scenarios.

### Proposed Change.

The refactoring introduces a flexible, strategy-based architecture for MoE communication and integrates it into the vLLM-Ascend execution flow.

1.  **Strategy Pattern for MoE Communication (`MoECommMethod`)**:
    *   An abstract base class, `MoECommMethod`, was introduced to define a common interface for all MoE communication strategies.
    *   This interface standardizes the communication flow into three phases: `prepare()` (pre-computation data permutation/communication), `permute()`/`unpermute()` (core data shuffling logic), and `finalize()` (post-computation data aggregation/reduction).
    *   Concrete implementations for different strategies are provided:
        *   `AllGatherCommImpl`: A baseline, graph-compatible strategy.
        *   `MC2CommImpl`: A high-performance strategy optimized for scenarios with low token counts (activated when `num_input_tokens < tp_size * 512`).
        *   `DummyCommImpl`: A no-op implementation for single-device or graph compilation warm-up runs.

2.  **Dynamic Strategy Dispatch Mechanism**:
    *   A new `AscendFusedMoE` class replaces the previous MoE implementation and is registered as an OOT custom operator.
    *   Upon initialization, `AscendFusedMoE` pre-instantiates all available communication strategy objects (e.g., `self.allgathercommimpl`, `self.mc2commimpl`).
    *   The `ModelRunner` is now responsible for selecting the appropriate strategy for each step. It determines which method to use based on runtime conditions (e.g., using `"mc2"` if the token count is below a threshold, otherwise falling back to `"allgather"`).
    *   The name of the chosen strategy (as a string) is passed to the forward pass via `ascend_forward_context`.

3.  **Refactored MoE Forward Pass**:
    *   Inside `AscendFusedMoE.forward_impl`, the strategy name from the context is used to dynamically fetch the corresponding pre-instantiated communication object using `getattr`.
    *   The forward pass is restructured around the strategy object:
        1.  `moe_comm_method.prepare()`: Prepares inputs and performs initial communication.
        2.  `quant_method.apply()`: Executes the core expert computation (MLPs).
        3.  `moe_comm_method.finalize()`: Gathers results from experts and finalizes the output.
    *   This design cleanly separates the communication logic, which may be dynamic, from the core computation, which can be a graph-captured kernel.

This new architecture successfully enables MoE models to leverage ACL Graph for acceleration by selecting graph-compatible communication methods when possible. It also unlocks significant performance gains by using specialized, high-performance communication strategies like `MC2` in scenarios where they are most effective. The next step in our roadmap is to extend this flexible framework to support quantized MoE models.

Plan / Roadmap

1. Introduce `MoECommMethod`, implement `AllGatherImpl`, and adapt ACL Graph handling to cover all scenarios (#2125 ).
2. Implement `MC2CommImpl` and enable communication-switch (#2469 ).
3. Enable W8A8 / Int8 models to use `unified_fused_experts` (#2614 ).

Outstanding items

1. Merge `moe_comm_method` and `token_dispatcher`.
2. Add support for quantized models with `all-gather` communication pattern.
3. Additional items to be specified (TBD).

### Feedback Period.

Two weeks.

### CC List.

@wangxiyuan @Yikun 

### Any Other Things.

_No response_
