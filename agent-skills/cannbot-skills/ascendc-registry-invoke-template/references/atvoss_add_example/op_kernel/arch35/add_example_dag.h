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
 * \file add_example_dag.h
 * \brief AddExample 算子 DAG 计算图定义（atvoss 框架 - Broadcast 模式）
 *
 * 计算公式: y = x1 + x2
 *
 * 数据流:
 * x1 (GM) -> CopyInBrc --------\
 *                              -> Add -> CopyOut -> y (GM)
 * x2 (GM) -> CopyInBrc --------/
 */

#ifndef ADD_EXAMPLE_DAG_H
#define ADD_EXAMPLE_DAG_H

// Host 编译时 mock __aicore__（Kernel 编译器已内置定义）
#ifndef __CCE_AICORE__
#ifndef __aicore__
#define __aicore__
#endif
#endif

#include "atvoss/util/dag.h"
#include "atvoss/util/vec.h"
#include "atvoss/util/placeholder.h"

using namespace Ops::Base;

namespace NsAddExample {

template <typename T>
struct AddExampleCompute {
    /*
     * ┌─────────────────────────────────────────────────────────────┐
     * │ 【atvoss 模式差异】搬入操作选择                               │
     * │                                                             │
     * │ Broadcast: Vec::CopyInBrc<T>  ← 当前模板（支持广播对齐）       │
     * │ Elewise:   Vec::CopyIn<T>    （输入 shape 完全相同时）         │
     * │ Reduction: Vec::CopyIn<T>    （归约输入）                     │
     * │                                                             │
     * │ 详见 ascendc-atvoss-devkit → dag-components.md               │
     * └─────────────────────────────────────────────────────────────┘
     */
    using OpInputX1 = Bind<Vec::CopyInBrc<T>, Placeholder::In0<T>>;
    using OpInputX2 = Bind<Vec::CopyInBrc<T>, Placeholder::In1<T>>;

    /*
     * ┌─────────────────────────────────────────────────────────────┐
     * │ 【atvoss 模式差异】计算操作选择                               │
     * │                                                             │
     * │ Broadcast: 二元 Vec 操作（Add/Sub/Mul/Div 等）← 当前模板      │
     * │ Elewise:   一元或二元 Vec 操作（Abs/Exp/Sqrt 等）             │
     * │ Reduction: Vec::ReduceSumOp<T> / ReduceMaxOp<T> 等          │
     * │                                                             │
     * │ 完整操作列表见 ascendc-atvoss-devkit → vec-operations.md     │
     * └─────────────────────────────────────────────────────────────┘
     */
    using OpAddRes = Bind<Vec::Add<T>, OpInputX1, OpInputX2>;

    using OpCopyOut = Bind<Vec::CopyOut<T>, Placeholder::Out0<T>, OpAddRes>;

    /*
     * ┌─────────────────────────────────────────────────────────────┐
     * │ 【atvoss 模式差异】Cast 提升精度                              │
     * │                                                             │
     * │ Broadcast: 通常不需要                                        │
     * │ Elewise:   按需（fp16 计算可提升到 fp32）                     │
     * │ Reduction: ReduceSum 推荐 Cast 提升（累加易溢出）             │
     * │   示例: CopyIn → Cast<float,half,0> → ReduceSumOp<float>    │
     * │         → Cast<half,float,1> → CopyOut                      │
     * │                                                             │
     * │ Cast 对称性规则：入口 Cast 提升，出口必须 Cast 还原            │
     * └─────────────────────────────────────────────────────────────┘
     */

    using Outputs = Elems<OpCopyOut>;
    using MemCfg = MemOptCfg<MemLevel::LEVEL_2>;
    using OpDag = DAGSch<Outputs, void, MemCfg>;
};

} // namespace NsAddExample

#endif  // ADD_EXAMPLE_DAG_H
