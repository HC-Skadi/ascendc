# ----------------------------------------------------------------------------------------------------------
# Copyright (c) 2026 Huawei Technologies Co., Ltd.
# This program is free software, you can redistribute it and/or modify it under the terms and conditions of
# CANN Open Software License Agreement Version 2.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.
# ----------------------------------------------------------------------------------------------------------

# ============================================================================
# CMake 构建配置 - Ascend C Kernel 直调
# ============================================================================
#
# [MODIFY] 创建新算子时修改:
# 1. add_executable 的目标名和源文件名
# 2. target_compile_options 中的目标名
# ============================================================================

cmake_minimum_required(VERSION 3.16)

find_package(ASC REQUIRED)

# [MODIFY] 工程名 add_custom → <your_op>_coustom	 
 project(add_custom LANGUAGES ASC CXX) 
 
 
 # [MODIFY] 目标名 add_custom → <your_op>_coustom，源文件 add.asc → <your_op>.asc	 
 add_executable(add_custom add.asc)	 
 
 
 # [MODIFY] 工程名 add_custom → <your_op>_coustom 
 target_link_libraries(add_custom PRIVATE 
     tiling_api 
     register 
     platform 
     unified_dlog 
     dl 
     m 
     graph_base 
 ) 
 
 
 # [MODIFY] 工程名 add_custom → <your_op>_coustom 
 target_include_directories(add_custom PRIVATE 
     ${CMAKE_CURRENT_SOURCE_DIR} 
 )

# [CONFIG] NPU 架构配置
# - dav-2201: Atlas A2 系列（默认）
# - dav-3510: Atlas A5 系列
# 更多架构详见 ascendc-npu-arch skill
# [MODIFY] 工程名 add_custom → <your_op>_coustom	 
target_compile_options(add_custom PRIVATE
    $<$<COMPILE_LANGUAGE:ASC>:--npu-arch=dav-2201>
)
