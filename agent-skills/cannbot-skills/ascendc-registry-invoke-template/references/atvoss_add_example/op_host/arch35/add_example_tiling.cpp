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
 * \file add_example_tiling.cpp
 * \brief AddExample 算子 Host Tiling 实现（atvoss 框架 - Broadcast 模式）
 */

/*
 * ┌─────────────────────────────────────────────────────────────┐
 * │ 【atvoss 模式差异】Tiling 头文件                              │
 * │                                                             │
 * │ Broadcast: atvoss/broadcast/broadcast_tiling.h  ← 当前模板   │
 * │ Elewise:   atvoss/elewise/elewise_tiling.h                  │
 * │ Reduction: atvoss/reduce/reduce_tiling.h                    │
 * └─────────────────────────────────────────────────────────────┘
 */
#include "register/op_def_registry.h"
#include "op_common/log/log.h"
#include "atvoss/broadcast/broadcast_tiling.h"
#include "../../op_kernel/arch35/add_example_dag.h"
#include "../../op_kernel/arch35/add_example_struct.h"

namespace optiling {

using namespace ge;

static ge::graphStatus AddExampleTilingFunc(gert::TilingContext* context)
{
    /*
     * ┌─────────────────────────────────────────────────────────────┐
     * │ 【atvoss 模式差异】Tiling API 构造与 DoTiling               │
     * │                                                             │
     * │ Broadcast（当前模板）:                                       │
     * │   BroadcastBaseTiling<OpDag> brcTiling(context);             │
     * │   auto ret = brcTiling.DoTiling();                          │
     * │   tilingKey = GET_TPL_TILING_KEY(brcTiling.GetSchMode());   │
     * │                                                             │
     * │ Elewise:                                                    │
     * │   auto td = context->GetTilingData<MyOpTilingData>();       │
     * │   ElewiseBaseTiling eleTiling(context);                     │
     * │   auto ret = eleTiling.DoTiling<OpDag>(td->baseTiling);     │
     * │   tilingKey = GET_TPL_TILING_KEY(                           │
     * │       (uint64_t)td->baseTiling.scheMode);                   │
     * │                                                             │
     * │ Reduction:                                                  │
     * │   ReduceOpInputParam opInput;                               │
     * │   ReduceOpTmpl::GetInputParam(context, opInput, ...);      │
     * │   ReduceTilingKey key;                                      │
     * │   Tiling4ReduceOp<OpDag>(context, opInput, key);           │
     * │   tilingKey = GET_TPL_TILING_KEY(                           │
     * │       key.patternID, key.loopARCount,                       │
     * │       key.loopInnerARCount);                                │
     * │                                                             │
     * │ 详见 ascendc-atvoss-devkit → tiling-api.md                 │
     * └─────────────────────────────────────────────────────────────┘
     */
    /*
     * 多 dtype 支持时，需根据输入 dtype 选择对应 DAG 模板实例化 BroadcastBaseTiling，例如：
     *   auto inputDesc = context->GetInputDesc(0);
     *   ge::DataType dtype = inputDesc->GetDataType();
     *   if (dtype == ge::DT_FLOAT16) {
     *       BroadcastBaseTiling<NsAddExample::AddExampleCompute<half>::OpDag> brcBaseTiling(context);
     *       ret = brcBaseTiling.DoTiling();
     *       ...
     *   } else if (dtype == ge::DT_FLOAT) {
     *       BroadcastBaseTiling<NsAddExample::AddExampleCompute<float>::OpDag> brcBaseTiling(context);
     *       ...
     *   }
     */
    using OpDag = NsAddExample::AddExampleCompute<float>::OpDag;
    BroadcastBaseTiling<OpDag> brcBaseTiling(context);
    auto ret = brcBaseTiling.DoTiling();
    OP_CHECK_IF(
        ret != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "AddExample: BroadcastBaseTiling DoTiling failed"),
        return ret);

    /*
     * ┌─────────────────────────────────────────────────────────────┐
     * │ 【atvoss 模式差异】TilingKey 参数数量                        │
     * │                                                             │
     * │ Broadcast: GET_TPL_TILING_KEY(schMode)       ← 1个参数      │
     * │ Elewise:   GET_TPL_TILING_KEY(schMode)       ← 1个参数      │
     * │ Reduction: GET_TPL_TILING_KEY(patternID,     ← 3个参数      │
     * │                loopARCount, loopInnerARCount)                │
     * │                                                             │
     * │ 详见 ascendc-atvoss-devkit → tiling-key.md                  │
     * └─────────────────────────────────────────────────────────────┘
     */
    context->SetTilingKey(GET_TPL_TILING_KEY(brcBaseTiling.GetSchMode()));

    OP_LOGI(context, "AddExample: Tiling success");
    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus TilingParseForAddExample([[maybe_unused]] gert::TilingParseContext* context)
{
    return ge::GRAPH_SUCCESS;
}

struct AddExampleCompileInfo {};

IMPL_OP_OPTILING(AddExample)
    .Tiling(AddExampleTilingFunc)
    .TilingParse<AddExampleCompileInfo>(TilingParseForAddExample);

}  // namespace optiling
