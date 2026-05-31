/*!
 * \file prelu.cpp
 * \brief Prelu 算子 kernel 入口
 */

#include "prelu.h"

enum class PreluTilingKey : uint32_t {
    TILING_KEY_SCALAR = PRELU_TPL_SCH_MODE_SCALAR,
    TILING_KEY_CHANNEL = PRELU_TPL_SCH_MODE_CHANNEL,
};

template <uint32_t schMode>
__global__ __aicore__ void prelu(GM_ADDR x, GM_ADDR weight, GM_ADDR y, GM_ADDR workspace, GM_ADDR tiling)
{
    REGISTER_TILING_DEFAULT(PreluTilingData);
    GET_TILING_DATA_WITH_STRUCT(PreluTilingData, tilingData, tiling);

    AscendC::TPipe pipe;
    KERNEL_TASK_TYPE_DEFAULT(KERNEL_TYPE_AIV_ONLY);

#ifdef DTYPE_X
    using KernelDtype = DTYPE_X;
#else
    using KernelDtype = float;
#endif

    if constexpr (schMode == static_cast<uint32_t>(PreluTilingKey::TILING_KEY_CHANNEL)) {
        NsPrelu::Prelu<KernelDtype, PRELU_TPL_SCH_MODE_CHANNEL> op;
        op.Init(x, weight, y, &tilingData, &pipe);
        op.Process();
    }
    if constexpr (schMode == static_cast<uint32_t>(PreluTilingKey::TILING_KEY_SCALAR)) {
        NsPrelu::Prelu<KernelDtype, PRELU_TPL_SCH_MODE_SCALAR> op;
        op.Init(x, weight, y, &tilingData, &pipe);
        op.Process();
    }
}
