/**
 * Copyright (c) 2026 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file add_example_apt.cpp
 * \brief AddExample 算子 Kernel 入口（atvoss 框架 - Broadcast 模式）
 */

/*
 * ┌─────────────────────────────────────────────────────────────┐
 * │ 【atvoss 模式差异】调度器头文件                               │
 * │                                                             │
 * │ Broadcast: atvoss/broadcast/broadcast_sch.h  ← 当前模板      │
 * │ Elewise:   atvoss/elewise/elewise_sch.h                     │
 * │ Reduction: atvoss/reduce/reduce_sch.h                       │
 * └─────────────────────────────────────────────────────────────┘
 */
#include "kernel_operator.h"
#include "arch35/add_example_dag.h"
#include "arch35/add_example_struct.h"
#include "atvoss/broadcast/broadcast_sch.h"

using namespace Ops::Base;

/*
 * ┌─────────────────────────────────────────────────────────────┐
 * │ 【atvoss 模式差异】模板参数                                   │
 * │                                                             │
 * │ Broadcast: template <uint64_t schMode>       ← 当前模板      │
 * │ Elewise:   template <uint64_t schMode>       （相同）        │
 * │ Reduction: template <REDUCE_TPL_PARAM>                      │
 * │   展开为: template <uint32_t PatternID,                      │
 * │            uint32_t LoopARCount, uint32_t LoopInnerARCount>  │
 * └─────────────────────────────────────────────────────────────┘
 */
template <uint64_t schMode>
__global__ __aicore__ void add_example(GM_ADDR x1, GM_ADDR x2, GM_ADDR y,
                                        GM_ADDR workspace, GM_ADDR tiling)
{
    KERNEL_TASK_TYPE_DEFAULT(KERNEL_TYPE_AIV_ONLY);

    /*
     * ┌─────────────────────────────────────────────────────────────┐
     * │ 【atvoss 模式差异】TilingData 注册与获取                     │
     * │                                                             │
     * │ Broadcast: 不需要（调度器内部处理）         ← 当前模板        │
     * │                                                             │
     * │ Elewise:   需要以下两行:                                     │
     * │   REGISTER_TILING_DEFAULT(MyOpTilingData);                  │
     * │   GET_TILING_DATA(tilingData, tiling);                      │
     * │                                                             │
     * │ Reduction: 需要以下两行:                                     │
     * │   REGISTER_TILING_DEFAULT(ReduceOpTilingData);              │
     * │   GET_TILING_DATA_WITH_STRUCT(ReduceOpTilingData,           │
     * │                               tilingData, tiling);          │
     * │                                                             │
     * │ 详见 ascendc-atvoss-devkit → tiling-data.md                 │
     * └─────────────────────────────────────────────────────────────┘
     */

    /*
     * ┌─────────────────────────────────────────────────────────────┐
     * │ 【atvoss 模式差异】调度器构造与调用                           │
     * │                                                             │
     * │ Broadcast（当前模板）:                                       │
     * │   BroadcastSch<schMode, OpDag> sch(tiling);                 │
     * │   sch.Process(x1, x2, y);                                   │
     * │                                                             │
     * │ Elewise:                                                    │
     * │   TPipe pipe;                                               │
     * │   ElementwiseSch<schMode, OpDag> sch(                       │
     * │       &(tilingData.baseTiling), &pipe);                     │
     * │   sch.Init(x, y);         // 或 sch.Init(x1, x2, y);       │
     * │   sch.Process();                                            │
     * │                                                             │
     * │ Reduction:                                                  │
     * │   TPipe pipe;                                               │
     * │   GM_ADDR userWS = GetUserWorkspace(workspace);             │
     * │   ReduceSch<REDUCE_TPL_VALUE, OpDag> op(&tilingData);       │
     * │   op.Init(&pipe, x, y, userWS);                             │
     * │   op.Process();                                             │
     * │                                                             │
     * │ 详见 ascendc-atvoss-devkit → schedulers.md                  │
     * └─────────────────────────────────────────────────────────────┘
     */
    /*
     * DTYPE_X1 / DTYPE_X2 由构建系统根据 add_example_def.cpp 中注册的 dtype 自动生成。
     * 多 dtype 支持时，可用 if constexpr 按 DTYPE_X1 选择不同 DAG 变体，例如：
     *   if constexpr (std::is_same<DTYPE_X1, half>::value) {
     *       using OpDag = NsAddExample::AddExampleWithCast<DTYPE_X1>::OpDag;
     *   } else {
     *       using OpDag = NsAddExample::AddExampleCompute<DTYPE_X1>::OpDag;
     *   }
     */
    using OpDag = NsAddExample::AddExampleCompute<DTYPE_X1>::OpDag;
    BroadcastSch<schMode, OpDag> sch(tiling);
    sch.Process(x1, x2, y);
}
