/**
 * Copyright (c) 2025 Huawei Technologies Co., Ltd.
 * This program is free software, you can redistribute it and/or modify it under the terms and conditions of
 * CANN Open Software License Agreement Version 2.0 (the "License").
 * Please refer to the License for details. You may not use this file except in compliance with the License.
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
 * See LICENSE in the root of the software repository for the full text of the License.
 */

/*!
 * \file prelu_tiling.cpp
 * \brief
 */

#include "log/log.h"
#include "util/math_util.h"
#include "op_host/tiling_util.h"
#include "op_host/tiling_templates_registry.h"
#include "prelu/op_kernel/prelu_tiling_data.h"
#include "prelu/op_kernel/prelu_tiling_key.h"

namespace optiling {

using namespace Ops::NN::OpTiling;
const uint32_t BLOCK_SIZE = 32;
const uint32_t BUFFER_NUM = 2;
const uint32_t WS_SYS_SIZE = 0;
const uint64_t UB_RESERVED_SIZE = 1024;

struct PreluCompileInfo {};

// 获取平台信息如ubSize, coreNum
static ge::graphStatus GetPlatformInfo(gert::TilingContext* context, uint64_t& ubSize, int64_t& coreNum)
{
    // 获取ubsize coreNum
    fe::PlatFormInfos* platformInfoPtr = context->GetPlatformInfo();
    OP_CHECK_NULL_WITH_CONTEXT(context, platformInfoPtr);
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(platformInfoPtr);
    coreNum = ascendcPlatform.GetCoreNumAiv();
    OP_CHECK_IF(coreNum == 0, OP_LOGE(context, "coreNum is 0"), return ge::GRAPH_FAILED);
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);
    OP_CHECK_IF(ubSize == 0, OP_LOGE(context, "ubSize is 0"), return ge::GRAPH_FAILED);
    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus GetWeightBroadcastInfo(
    gert::TilingContext* context, const gert::Shape& inputShapeX, int64_t& weightSize, int64_t& channelSize,
    int64_t& innerSize)
{
    auto inputWeight = context->GetInputShape(1);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputWeight);
    auto inputShapeWeight = inputWeight->GetStorageShape();

    OP_CHECK_IF(
        inputShapeWeight.GetDimNum() != 1,
        OP_LOGE(context, "Prelu: weight must be 1D tensor, got dim num %zu", inputShapeWeight.GetDimNum()),
        return ge::GRAPH_FAILED);

    weightSize = inputShapeWeight.GetDim(0);
    OP_CHECK_IF(
        weightSize <= 0, OP_LOGE(context, "Prelu: weight size must be positive, got %ld", weightSize),
        return ge::GRAPH_FAILED);

    size_t xDimNum = inputShapeX.GetDimNum();
    OP_CHECK_IF(
        xDimNum <= 1, OP_LOGE(context, "Prelu: input x dim num must be greater than 1, got %zu", xDimNum),
        return ge::GRAPH_FAILED);

    channelSize = inputShapeX.GetDim(1);
    OP_CHECK_IF(
        channelSize <= 0, OP_LOGE(context, "Prelu: channel size must be positive, got %ld", channelSize),
        return ge::GRAPH_FAILED);
    OP_CHECK_IF(
        weightSize != 1 && weightSize != channelSize,
        OP_LOGE(
            context, "Prelu: weight size must be 1 or match channel size, weight size=%ld, channel size=%ld",
            weightSize, channelSize),
        return ge::GRAPH_FAILED);

    innerSize = 1;
    for (size_t i = 2; i < xDimNum; ++i) {
        innerSize *= inputShapeX.GetDim(i);
    }
    return ge::GRAPH_SUCCESS;
}

// 获取属性，shape信息
static ge::graphStatus GetShapeAttrsInfo(gert::TilingContext* context, int64_t& totalIdx, ge::DataType& dataType)
{
    // 获取输入shape信息
    auto inputX = context->GetInputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputX);
    auto inputShapeX = inputX->GetStorageShape();

    auto outZ = context->GetOutputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, outZ);
    auto outShapeZ = outZ->GetStorageShape();

    // shape校验
    bool shapeMatch = true;
    // 校验维度数一致
    if (inputShapeX.GetDimNum() != outShapeZ.GetDimNum()) {
        shapeMatch = false;
    } else {
        // 校验每个维度的大小一致
        size_t dimNum = inputShapeX.GetDimNum();
        for (size_t i = 0; i < dimNum; i++) {
            if (inputShapeX.GetDim(i) != outShapeZ.GetDim(i)) {
                shapeMatch = false;
                break;
            }
        }
    }
    // 形状不匹配则报错
    OP_CHECK_IF(
        !shapeMatch,
        OP_LOGE(
            context, "Prelu: inputx,outputz shape not match! dim num: x=%zu,  z=%zu", inputShapeX.GetDimNum(),
            outShapeZ.GetDimNum()),
        return ge::GRAPH_FAILED);

    totalIdx = inputX->GetOriginShape().GetShapeSize();
    // dtype校验
    const std::set<ge::DataType> supportedDtype = {ge::DT_FLOAT, ge::DT_FLOAT16, ge::DT_BF16};
    auto inputDesc = context->GetInputDesc(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputDesc);
    dataType = inputDesc->GetDataType();
    if (supportedDtype.count(dataType) == 0) {
        OP_LOGE(context, "invalid dtype");
        return ge::GRAPH_FAILED;
    }
    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus GetWorkspaceSize(gert::TilingContext* context)
{
    size_t* currentWorkspace = context->GetWorkspaceSizes(1);
    if (currentWorkspace != nullptr) {
        currentWorkspace[0] = WS_SYS_SIZE;
    }
    return ge::GRAPH_SUCCESS;
}

static uint64_t CeilDiv(uint64_t value, uint64_t factor)
{
    return (value + factor - 1) / factor;
}

static uint64_t GetBufferBytesPerElement(ge::DataType dataType, bool isVectorPath, uint64_t inputBytes)
{
    if (isVectorPath) {
        if (dataType == ge::DT_BF16) {
            return BUFFER_NUM * inputBytes + BUFFER_NUM * inputBytes + BUFFER_NUM * inputBytes + 6U * sizeof(float);
        }
        return (BUFFER_NUM + BUFFER_NUM + BUFFER_NUM + 3U) * inputBytes;
    }

    if (dataType == ge::DT_BF16) {
        return BUFFER_NUM * inputBytes + BUFFER_NUM * inputBytes + 4U * sizeof(float);
    }
    return (BUFFER_NUM + BUFFER_NUM + 2U) * inputBytes;
}

static uint32_t CalcTileDataNum(uint64_t ubSize, uint64_t bytesPerElement, uint64_t inputBytes)
{
    uint64_t usableUbSize = (ubSize > UB_RESERVED_SIZE) ? (ubSize - UB_RESERVED_SIZE) : ubSize;
    uint64_t blockElementNum = BLOCK_SIZE / inputBytes;
    uint64_t maxTileDataNum = usableUbSize / bytesPerElement;
    if (maxTileDataNum < blockElementNum) {
        return static_cast<uint32_t>(blockElementNum);
    }

    uint64_t alignedTileDataNum = (maxTileDataNum / blockElementNum) * blockElementNum;
    return static_cast<uint32_t>(alignedTileDataNum);
}

static void SplitCoreAndTile(
    int64_t totalIdx, int64_t coreNum, uint64_t inputBytes, uint32_t tileDataNum, PreluTilingData* tiling,
    uint32_t& finalCoreNum)
{
    uint64_t blockElementNum = BLOCK_SIZE / inputBytes;
    uint64_t totalBytes = static_cast<uint64_t>(totalIdx) * inputBytes;
    uint64_t totalBlockNum = CeilDiv(totalBytes, BLOCK_SIZE);
    uint64_t usedCoreNum = static_cast<uint64_t>(coreNum);
    if (usedCoreNum > totalBlockNum) {
        usedCoreNum = totalBlockNum;
    }
    if (usedCoreNum == 0) {
        usedCoreNum = 1;
    }

    uint64_t smallCoreBlockNum = totalBlockNum / usedCoreNum;
    uint64_t tailBlockNum = totalBlockNum % usedCoreNum;
    uint64_t bigCoreBlockNum = smallCoreBlockNum + ((tailBlockNum > 0) ? 1U : 0U);
    uint64_t smallCoreDataNum = smallCoreBlockNum * blockElementNum;
    uint64_t bigCoreDataNum = bigCoreBlockNum * blockElementNum;

    uint64_t finalSmallTileNum = (smallCoreDataNum == 0) ? 0 : CeilDiv(smallCoreDataNum, tileDataNum);
    uint64_t finalBigTileNum = (bigCoreDataNum == 0) ? 0 : CeilDiv(bigCoreDataNum, tileDataNum);
    uint64_t smallTailDataNum =
        (finalSmallTileNum == 0) ? 0 : (smallCoreDataNum - (finalSmallTileNum - 1U) * tileDataNum);
    uint64_t bigTailDataNum = (finalBigTileNum == 0) ? 0 : (bigCoreDataNum - (finalBigTileNum - 1U) * tileDataNum);

    tiling->smallCoreDataNum = static_cast<int64_t>(smallCoreDataNum);
    tiling->bigCoreDataNum = static_cast<int64_t>(bigCoreDataNum);
    tiling->tileDataNum = static_cast<int64_t>(tileDataNum);
    tiling->smallTailDataNum = static_cast<int64_t>(smallTailDataNum);
    tiling->bigTailDataNum = static_cast<int64_t>(bigTailDataNum);
    tiling->finalSmallTileNum = static_cast<int64_t>(finalSmallTileNum);
    tiling->finalBigTileNum = static_cast<int64_t>(finalBigTileNum);
    tiling->tailBlockNum = static_cast<int64_t>(tailBlockNum);
    tiling->totalNum = totalIdx;
    finalCoreNum = static_cast<uint32_t>(usedCoreNum);
}

// tiling 分发入口
static ge::graphStatus PreluTilingFunc(gert::TilingContext* context)
{
    // 1. platform
    uint64_t ubSize = 0;
    int64_t coreNum = 0;
    OP_CHECK_IF(
        GetPlatformInfo(context, ubSize, coreNum) != ge::GRAPH_SUCCESS, OP_LOGE(context, "GetPlatformInfo error"),
        return ge::GRAPH_FAILED);

    // 2. shapes & dtype
    int64_t totalIdx = 0;
    ge::DataType dataType;
    OP_CHECK_IF(
        GetShapeAttrsInfo(context, totalIdx, dataType) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "GetShapeAttrsInfo error"), return ge::GRAPH_FAILED);

    // 3. workspace
    OP_CHECK_IF(
        GetWorkspaceSize(context) != ge::GRAPH_SUCCESS, OP_LOGE(context, "GetWorkspaceSize error"),
        return ge::GRAPH_FAILED);

    PreluTilingData* tiling = context->GetTilingData<PreluTilingData>();
    OP_CHECK_NULL_WITH_CONTEXT(context, tiling);
    OP_CHECK_IF(
        memset_s(tiling, sizeof(PreluTilingData), 0, sizeof(PreluTilingData)) != EOK,
        OP_LOGE(context, "set tiling data error"), return ge::GRAPH_FAILED);

    // Get shape info for weight broadcasting
    auto inputX = context->GetInputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputX);
    auto inputShapeX = inputX->GetStorageShape();

    int64_t weightSize = 0;
    int64_t channelSize = 0;
    int64_t innerSize = 1;
    OP_CHECK_IF(
        GetWeightBroadcastInfo(context, inputShapeX, weightSize, channelSize, innerSize) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "GetWeightBroadcastInfo error"), return ge::GRAPH_FAILED);
    tiling->weightSize = weightSize;
    tiling->channelSize = channelSize;
    tiling->innerSize = innerSize;

    if (weightSize == 1) {
        context->SetTilingKey(GET_TPL_TILING_KEY(ELEMENTWISE_TPL_SCH_MODE_1));
    } else {
        context->SetTilingKey(GET_TPL_TILING_KEY(ELEMENTWISE_TPL_SCH_MODE_0));
    }

    // --- safer numeric types ---
    uint32_t typeLength = 0;
    ge::TypeUtils::GetDataTypeLength(context->GetInputDesc(0)->GetDataType(), typeLength);
    if (typeLength == 0) {
        OP_LOGE(context, "typeLength is 0");
        return ge::GRAPH_FAILED;
    }
    uint64_t inputBytes = static_cast<uint64_t>(typeLength);

    bool isVectorPath = (weightSize != 1);
    uint64_t bytesPerElement = GetBufferBytesPerElement(dataType, isVectorPath, inputBytes);
    uint32_t tileDataNum = CalcTileDataNum(ubSize, bytesPerElement, inputBytes);
    uint32_t finalCoreNum = 1;
    SplitCoreAndTile(totalIdx, coreNum, inputBytes, tileDataNum, tiling, finalCoreNum);

    context->SetBlockDim(finalCoreNum);
    return ge::GRAPH_SUCCESS;
}

// 获取属性，shape信息
static ge::graphStatus TilingParseForPrelu([[maybe_unused]] gert::TilingParseContext* context)
{
    return ge::GRAPH_SUCCESS;
}

// tiling注册入口.
IMPL_OP_OPTILING(Prelu).Tiling(PreluTilingFunc).TilingParse<PreluCompileInfo>(TilingParseForPrelu);
} // namespace optiling
