/*!
 * \file prelu.cpp
 * \brief Prelu 算子 kernel 入口
 */

#include "prelu.h"

template <uint32_t schMode>
__global__ __aicore__ void prelu(GM_ADDR x, GM_ADDR weight, GM_ADDR y, GM_ADDR workspace, GM_ADDR tiling)
{
    REGISTER_TILING_DEFAULT(PreluTilingData);
    GET_TILING_DATA_WITH_STRUCT(PreluTilingData, tilingData, tiling);

    AscendC::TPipe pipe;
#ifdef DTYPE_X
    NsPrelu::Prelu<DTYPE_X> op;
#else
    using KernelDtype = float;
    NsPrelu::Prelu<KernelDtype> op;
#endif
    if constexpr (schMode == PRELU_TPL_CHANNEL_FULL_L_MODE) {
        op.InitChannel(x, weight, y, &tilingData, &pipe);
        op.ProcessChannelFullL();
    } else if constexpr (schMode == PRELU_TPL_CHANNEL_SPLIT_L_MODE) {
        op.InitChannel(x, weight, y, &tilingData, &pipe);
        op.ProcessChannelSplitL();
    } else if constexpr (schMode == PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE) {
        op.InitChannelSplitLParallel(x, weight, y, &tilingData, &pipe);
        op.ProcessChannelSplitLParallel();
    } else {
        op.InitScalar(x, weight, y, &tilingData, &pipe);
        op.ProcessScalar();
    }
}
