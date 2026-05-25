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
    using KernelDtype = std::conditional_t<schMode == PRELU_TPL_SCH_MODE_1, half, float>;
    NsPrelu::Prelu<KernelDtype> op;
#endif
    op.Init(x, weight, y, &tilingData, &pipe);
    op.Process();
}
