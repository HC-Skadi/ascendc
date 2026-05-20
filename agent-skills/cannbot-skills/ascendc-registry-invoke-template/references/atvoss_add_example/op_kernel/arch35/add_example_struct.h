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
 * \file add_example_struct.h
 * \brief AddExample 算子 TilingData 和 TilingKey 定义（atvoss 框架 - Broadcast 模式）
 */

#ifndef ADD_EXAMPLE_STRUCT_H
#define ADD_EXAMPLE_STRUCT_H

/*
 * ┌─────────────────────────────────────────────────────────────┐
 * │ 【atvoss 模式差异】头文件                                     │
 * │                                                             │
 * │ Broadcast: atvoss/broadcast/broadcast_base_struct.h ← 当前   │
 * │ Elewise:   atvoss/elewise/elewise_base_struct.h             │
 * │ Reduction: atvoss/reduce/reduce_tiling_key_decl.h           │
 * │          + atvoss/reduce/reduce_tiling_key_sel.h            │
 * └─────────────────────────────────────────────────────────────┘
 */
#include "atvoss/broadcast/broadcast_base_struct.h"
#include "ascendc/host_api/tiling/template_argument.h"

/*
 * ┌─────────────────────────────────────────────────────────────┐
 * │ 【atvoss 模式差异】TilingData 结构体                          │
 * │                                                             │
 * │ Broadcast: 不需要定义（调度器内部处理）       ← 当前模板        │
 * │                                                             │
 * │ Elewise: 必须定义 struct 包装（即使无额外参数）:               │
 * │   struct AddExampleTilingData {                              │
 * │       ::Ops::Base::EleBaseTilingData baseTiling;             │
 * │   };                                                        │
 * │   注意：不能用 using 别名，否则编译报错！                      │
 * │                                                             │
 * │ Reduction: 不需要定义（使用预定义 ReduceOpTilingData）        │
 * │                                                             │
 * │ 详见 ascendc-atvoss-devkit → tiling-data.md                 │
 * └─────────────────────────────────────────────────────────────┘
 */

/*
 * ┌─────────────────────────────────────────────────────────────┐
 * │ 【atvoss 模式差异】TilingKey 宏声明                           │
 * │                                                             │
 * │ Broadcast（当前模板）:                                        │
 * │   ASCENDC_TPL_ARGS_DECL(OpName,                             │
 * │       BRC_TEMP_SCH_MODE_KEY_DECL(schMode));                 │
 * │   ASCENDC_TPL_SEL(ASCENDC_TPL_ARGS_SEL(                    │
 * │       BRC_TEMP_SCH_MODE_KEY_SEL(schMode)));                 │
 * │                                                             │
 * │ Elewise:                                                    │
 * │   ASCENDC_TPL_ARGS_DECL(OpName,                             │
 * │       ASCENDC_TPL_UINT_DECL(schMode, 1,                    │
 * │           ASCENDC_TPL_UI_LIST, 0, 1));                      │
 * │   ASCENDC_TPL_SEL(ASCENDC_TPL_ARGS_SEL(                    │
 * │       ASCENDC_TPL_UINT_SEL(schMode,                         │
 * │           ASCENDC_TPL_UI_LIST, 0, 1)));                     │
 * │                                                             │
 * │ Reduction:                                                  │
 * │   ASCENDC_TPL_ARGS_DECL(OpName, REDUCE_TPL_KEY_DECL());    │
 * │   (SEL 由框架宏自动处理)                                     │
 * │                                                             │
 * │ 详见 ascendc-atvoss-devkit → tiling-key.md                  │
 * └─────────────────────────────────────────────────────────────┘
 */
ASCENDC_TPL_ARGS_DECL(AddExample, BRC_TEMP_SCH_MODE_KEY_DECL(schMode));
ASCENDC_TPL_SEL(ASCENDC_TPL_ARGS_SEL(BRC_TEMP_SCH_MODE_KEY_SEL(schMode)));

#endif  // ADD_EXAMPLE_STRUCT_H
