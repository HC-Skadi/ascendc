/*!
 * \file prelu_tiling.cpp
 * \brief Prelu 算子 Tiling 实现
 */

#include "register/op_def_registry.h"
#include "op_common/log/log.h"
#include "op_common/op_host/util/math_util.h"
#include "op_common/op_host/util/platform_util.h"
#include "../op_kernel/prelu_tiling_data.h"
#include "../op_kernel/prelu_tiling_key.h"

namespace optiling {

using Ops::Base::CeilDiv;
using Ops::Base::CeilAlign;
using Ops::Base::FloorDiv;
using Ops::Base::FloorAlign;

constexpr uint32_t WS_SYS_SIZE = 0U;
constexpr int64_t FLOAT_TYPE_SIZE = 4;
constexpr int64_t HALF_TYPE_SIZE = 2;
constexpr int64_t CACHE_LINE_SIZE = 512;

static const gert::Shape g_vec_1_shape = {1};

static inline const gert::Shape EnsureNotScalar(const gert::Shape& in_shape) {
    if (in_shape.GetDimNum() == 0) {
        return g_vec_1_shape;
    }
    return in_shape;
}

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
    OP_CHECK_NULL_WITH_CONTEXT(context, currentWorkspace);
    currentWorkspace[0] = WS_SYS_SIZE;
    return ge::GRAPH_SUCCESS;
}

static int64_t GetTypeSize(ge::DataType dtype)
{
    return dtype == ge::DT_FLOAT ? FLOAT_TYPE_SIZE : HALF_TYPE_SIZE;
}

static ge::graphStatus GetShapeDtypeInfo(gert::TilingContext* context, int64_t& totalNum, int64_t& weightMode,
    int64_t& channelSize, int64_t& innerSize, ge::DataType& dtype)
{
    auto inputX = context->GetInputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputX);
    auto inputShapeX = EnsureNotScalar(inputX->GetStorageShape());
    auto inputWeight = context->GetInputShape(1);
    OP_CHECK_NULL_WITH_CONTEXT(context, inputWeight);
    auto inputShapeWeight = EnsureNotScalar(inputWeight->GetStorageShape());
    auto outputY = context->GetOutputShape(0);
    OP_CHECK_NULL_WITH_CONTEXT(context, outputY);
    auto outputShapeY = EnsureNotScalar(outputY->GetStorageShape());

    totalNum = inputShapeX.GetShapeSize();
    OP_CHECK_IF(
        totalNum != outputShapeY.GetShapeSize(),
        OP_LOGE(context, "Prelu: x and y element count mismatch, x=%ld, y=%ld", totalNum, outputShapeY.GetShapeSize()),
        return ge::GRAPH_FAILED);

    int64_t weightNum = inputShapeWeight.GetShapeSize();
    int64_t xDimNum = inputShapeX.GetDimNum();
    channelSize = xDimNum >= 2 ? inputShapeX.GetDim(1) : 1;
    innerSize = 1;
    if (xDimNum >= 2) {
        for (int64_t i = 2; i < xDimNum; ++i) {
            innerSize *= inputShapeX.GetDim(i);
        }
    } else {
        innerSize = totalNum;
    }

    OP_CHECK_IF(
        !(weightNum == 1 || (xDimNum >= 2 && weightNum == channelSize)),
        OP_LOGE(context, "Prelu: weight.numel must be 1 or equal to x.shape[1], weight=%ld, channel=%ld",
            weightNum, channelSize),
        return ge::GRAPH_FAILED);
    weightMode = weightNum == 1 ? 0 : 1;

    auto xDesc = context->GetInputDesc(0);
    auto weightDesc = context->GetInputDesc(1);
    OP_CHECK_NULL_WITH_CONTEXT(context, xDesc);
    OP_CHECK_NULL_WITH_CONTEXT(context, weightDesc);
    dtype = xDesc->GetDataType();
    OP_CHECK_IF(
        dtype != weightDesc->GetDataType(),
        OP_LOGE(context, "Prelu: x and weight must have same dtype"),
        return ge::GRAPH_FAILED);
    OP_CHECK_IF(
        !(dtype == ge::DT_FLOAT16 || dtype == ge::DT_FLOAT),
        OP_LOGE(context, "Prelu: unsupported dtype %d", static_cast<int32_t>(dtype)),
        return ge::GRAPH_FAILED);
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

    PreluTilingData* tiling = context->GetTilingData<PreluTilingData>();
    OP_CHECK_NULL_WITH_CONTEXT(context, tiling);

    int64_t totalNum;
    int64_t weightMode;
    int64_t channelSize;
    int64_t innerSize;
    ge::DataType dtype;
    OP_CHECK_IF(
        GetShapeDtypeInfo(context, totalNum, weightMode, channelSize, innerSize, dtype) != ge::GRAPH_SUCCESS,
        OP_LOGE(context, "GetShapeDtypeInfo error"),
        return ge::GRAPH_FAILED);

    if (totalNum == 0) {
        tiling->totalNum = 0;
        tiling->blockFactor = 1;
        tiling->ubFactor = 1;
        tiling->weightMode = weightMode;
        tiling->channelSize = channelSize;
        tiling->innerSize = innerSize;
        context->SetBlockDim(1);
        context->SetTilingKey(GET_TPL_TILING_KEY(PRELU_TPL_SCH_MODE_0));
        return ge::GRAPH_SUCCESS;
    }

    int64_t dtypeSize = GetTypeSize(dtype);
    int64_t cacheLineElements = CACHE_LINE_SIZE / dtypeSize;
    int64_t blockFactor = CeilAlign(CeilDiv(totalNum, coreNum), cacheLineElements);
    int64_t usedCoreNum = CeilDiv(totalNum, blockFactor);
    int64_t bufferCoefficient = dtype == ge::DT_FLOAT ? 28 : 24;
    int64_t alignElements = 32 / dtypeSize;
    int64_t ubAvailable = static_cast<int64_t>(ubSize) > 32 ? static_cast<int64_t>(ubSize) - 32 : 0;
    int64_t ubFactor = FloorAlign(FloorDiv(ubAvailable, bufferCoefficient), alignElements);
    OP_CHECK_IF(ubFactor <= 0, OP_LOGE(context, "Prelu: ubFactor <= 0"), return ge::GRAPH_FAILED);

    tiling->totalNum = totalNum;
    tiling->blockFactor = blockFactor;
    tiling->ubFactor = ubFactor;
    tiling->weightMode = weightMode;
    tiling->channelSize = channelSize;
    tiling->innerSize = innerSize;

    context->SetBlockDim(usedCoreNum);

    uint64_t tilingKey = GET_TPL_TILING_KEY(PRELU_TPL_SCH_MODE_0);
    if (dtype == ge::DT_FLOAT) {
        tilingKey = GET_TPL_TILING_KEY(PRELU_TPL_SCH_MODE_1);
    }
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
