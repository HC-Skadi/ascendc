/*!
 * \file prelu_tiling.cpp
 * \brief Prelu 算子 Tiling 实现
 */

#include "register/op_def_registry.h"
#include "graph/utils/type_utils.h"
#include "op_common/log/log.h"
#include "op_common/op_host/util/math_util.h"
#include "op_common/op_host/util/platform_util.h"
#include "../op_kernel/prelu_tiling_data.h"
#include "../op_kernel/prelu_tiling_key.h"

#include <algorithm>

namespace optiling {

constexpr uint32_t WS_SYS_SIZE = 0U;
constexpr uint32_t BLOCK_SIZE = 32U;
constexpr uint32_t CORE_ALIGN_SIZE = 512U;
constexpr uint64_t UB_RESERVED_SIZE = 1024U;

static ge::graphStatus GetPlatformInfo(gert::TilingContext* context, uint64_t& ubSize, int64_t& coreNum)
{
    fe::PlatFormInfos* platformInfoPtr = context->GetPlatformInfo();
    OP_CHECK_NULL_WITH_CONTEXT(context, platformInfoPtr);
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(platformInfoPtr);
    coreNum = ascendcPlatform.GetCoreNumAiv();
    OP_CHECK_IF(coreNum == 0, OP_LOGE(context, "coreNum is 0"), return ge::GRAPH_FAILED);
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);
    OP_CHECK_IF(ubSize == 0, OP_LOGE(context, "ubSize is 0"), return ge::GRAPH_FAILED);
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

static ge::graphStatus CheckScalarWeight(gert::TilingContext* context)
{
    auto weightShape = context->GetInputShape(1);
    OP_CHECK_NULL_WITH_CONTEXT(context, weightShape);
    auto storageShape = weightShape->GetStorageShape();
    OP_CHECK_IF(
        storageShape.GetDimNum() != 1 || storageShape.GetDim(0) != 1,
        OP_LOGE(
            context, "Prelu: only scalar weight with shape [1] is supported, got dim num %zu, dim0 %ld",
            storageShape.GetDimNum(), storageShape.GetDimNum() == 0 ? 0 : storageShape.GetDim(0)),
        return ge::GRAPH_FAILED);
    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus GetShapeAndDtypeInfo(
    gert::TilingContext* context, int64_t& totalNum, ge::DataType& dataType, uint32_t& typeLength)
{
    auto inputX = context->GetInputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputX);
    auto outputY = context->GetOutputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, outputY);

    auto xShape = inputX->GetStorageShape();
    auto yShape = outputY->GetStorageShape();
    OP_CHECK_IF(
        xShape.GetDimNum() != yShape.GetDimNum(), OP_LOGE(context, "Prelu: x/y rank mismatch"),
        return ge::GRAPH_FAILED);
    for (size_t i = 0; i < xShape.GetDimNum(); ++i) {
        OP_CHECK_IF(
            xShape.GetDim(i) != yShape.GetDim(i), OP_LOGE(context, "Prelu: x/y shape mismatch"),
            return ge::GRAPH_FAILED);
    }

    auto xDesc = context->GetInputDesc(0);
    auto weightDesc = context->GetInputDesc(1);
    auto yDesc = context->GetOutputDesc(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, xDesc);
    OP_CHECK_NULL_WITH_CONTEXT(context, weightDesc);
    OP_CHECK_NULL_WITH_CONTEXT(context, yDesc);

    dataType = xDesc->GetDataType();
    OP_CHECK_IF(
        dataType != ge::DT_FLOAT && dataType != ge::DT_FLOAT16 && dataType != ge::DT_BF16,
        OP_LOGE(context, "Prelu: unsupported dtype"), return ge::GRAPH_FAILED);
    OP_CHECK_IF(
        weightDesc->GetDataType() != dataType || yDesc->GetDataType() != dataType,
        OP_LOGE(context, "Prelu: x, weight and y must have the same dtype"), return ge::GRAPH_FAILED);

    ge::TypeUtils::GetDataTypeLength(dataType, typeLength);
    OP_CHECK_IF(typeLength == 0, OP_LOGE(context, "Prelu: dtype length is 0"), return ge::GRAPH_FAILED);

    totalNum = inputX->GetOriginShape().GetShapeSize();
    return ge::GRAPH_SUCCESS;
}

static uint64_t GetBufferBytesPerElement(ge::DataType dataType)
{
    if (dataType == ge::DT_FLOAT) {
        return 21U;
    }
    if (dataType == ge::DT_FLOAT16) {
        return 11U;
    }
    return 17U;
}

static uint64_t GetCompareAlignElementNum(ge::DataType dataType, uint32_t typeLength)
{
    uint32_t computeTypeLength = dataType == ge::DT_BF16 ? sizeof(float) : typeLength;
    return 256U / computeTypeLength;
}

static uint64_t CeilDiv(uint64_t value, uint64_t factor)
{
    return (value + factor - 1U) / factor;
}

static ge::graphStatus CalcTiling(
    gert::TilingContext* context, uint64_t ubSize, int64_t coreNum, int64_t totalNum, ge::DataType dataType,
    uint32_t typeLength, PreluTilingData* tiling, uint32_t& usedCoreNum)
{
    uint64_t bufferBytesPerElement = GetBufferBytesPerElement(dataType);
    uint64_t usableUbSize = (ubSize > UB_RESERVED_SIZE) ? (ubSize - UB_RESERVED_SIZE) : ubSize;
    uint64_t coreAlignElementNum = CORE_ALIGN_SIZE / typeLength;
    uint64_t compareAlignElementNum = GetCompareAlignElementNum(dataType, typeLength);
    uint64_t maxTileElements = usableUbSize / bufferBytesPerElement;
    OP_CHECK_IF(
        maxTileElements < compareAlignElementNum, OP_LOGE(context, "Prelu: UB is too small for one aligned tile"),
        return ge::GRAPH_FAILED);

    uint64_t ubFactor = (maxTileElements / compareAlignElementNum) * compareAlignElementNum;
    uint64_t coreLimit = static_cast<uint64_t>(coreNum);
    uint64_t totalCoreElements = CeilDiv(static_cast<uint64_t>(totalNum), coreLimit);
    uint64_t blockFactor = (CeilDiv(totalCoreElements, coreAlignElementNum)) * coreAlignElementNum;
    if (blockFactor == 0) {
        blockFactor = coreAlignElementNum;
    }
    uint64_t finalCoreNum = static_cast<uint64_t>(totalNum) == 0 ? 1U : CeilDiv(static_cast<uint64_t>(totalNum), blockFactor);
    finalCoreNum = std::min(coreLimit, finalCoreNum);

    uint64_t tailLength = 0;
    uint64_t formerNum = 0;
    uint64_t tailNum = 0;
    if (totalNum > 0) {
        formerNum = finalCoreNum > 0 ? finalCoreNum - 1U : 0U;
        tailNum = 1U;
        tailLength = static_cast<uint64_t>(totalNum) - formerNum * blockFactor;
    }

    tiling->totalLength = totalNum;
    tiling->usedCoreNum = static_cast<int64_t>(finalCoreNum);
    tiling->formerNum = static_cast<int64_t>(formerNum);
    tiling->formerLength = static_cast<int64_t>(blockFactor);
    tiling->tailNum = static_cast<int64_t>(tailNum);
    tiling->tailLength = static_cast<int64_t>(tailLength);
    tiling->tileLength = static_cast<int64_t>(ubFactor);
    usedCoreNum = static_cast<uint32_t>(finalCoreNum);
    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus PreluTilingFunc(gert::TilingContext* context)
{
    uint64_t ubSize;
    int64_t coreNum;
    OP_CHECK_IF(
        GetPlatformInfo(context, ubSize, coreNum) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "GetPlatformInfo error"),
        return ge::GRAPH_FAILED);

    OP_CHECK_IF(
        GetWorkspaceSize(context) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "GetWorkspaceSize error"),
        return ge::GRAPH_FAILED);

    OP_CHECK_IF(
        CheckScalarWeight(context) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "CheckScalarWeight error"),
        return ge::GRAPH_FAILED);

    int64_t totalNum = 0;
    ge::DataType dataType = ge::DT_FLOAT;
    uint32_t typeLength = 0;
    OP_CHECK_IF(
        GetShapeAndDtypeInfo(context, totalNum, dataType, typeLength) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "GetShapeAndDtypeInfo error"),
        return ge::GRAPH_FAILED);

    PreluTilingData* tiling = context->GetTilingData<PreluTilingData>();
    OP_CHECK_NULL_WITH_CONTEXT(context, tiling);

    uint32_t usedCoreNum = 1;
    OP_CHECK_IF(
        CalcTiling(context, ubSize, coreNum, totalNum, dataType, typeLength, tiling, usedCoreNum) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "CalcTiling error"),
        return ge::GRAPH_FAILED);

    context->SetBlockDim(usedCoreNum);

    uint64_t tilingKey = GET_TPL_TILING_KEY(PRELU_TPL_SCH_MODE_0);
    context->SetTilingKey(tilingKey);
    return ge::GRAPH_SUCCESS;
}

static ge::graphStatus TilingParseForPrelu([[maybe_unused]] gert::TilingParseContext* context)
{
    return ge::GRAPH_SUCCESS;
}

struct PreluCompileInfo {};

IMPL_OP_OPTILING(Prelu).Tiling(PreluTilingFunc).TilingParse<PreluCompileInfo>(TilingParseForPrelu);

} // namespace optiling
