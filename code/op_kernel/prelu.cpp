/*!
 * \file prelu.cpp
 * \brief Prelu 算子 kernel 入口
 */

#include "prelu.h"

enum class PreluTilingKey : uint32_t
{
    TILING_KEY_PRELU_MODE_0 = 0,
    TILING_KEY_PRELU_MODE_1 = 1,
};

template <uint32_t schMode>
__global__ __aicore__ void prelu(GM_ADDR x, GM_ADDR weight, GM_ADDR y, GM_ADDR workspace, GM_ADDR tiling)
{
    REGISTER_TILING_DEFAULT(PreluTilingData);
    GET_TILING_DATA_WITH_STRUCT(PreluTilingData, tilingData, tiling);
    if constexpr (schMode == static_cast<uint32_t>(PreluTilingKey::TILING_KEY_PRELU_MODE_0)) {
        NsPrelu::Prelu<half> op;
        op.Init(x, weight, y, &tilingData);
        op.Process();
    }
    if constexpr (schMode == static_cast<uint32_t>(PreluTilingKey::TILING_KEY_PRELU_MODE_1)) {
        NsPrelu::Prelu<float> op;
        op.Init(x, weight, y, &tilingData);
        op.Process();
    }
}
