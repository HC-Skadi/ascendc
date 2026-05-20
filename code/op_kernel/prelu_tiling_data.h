/*!
 * \file prelu_tiling_data.h
 * \brief tiling data struct
 */

#ifndef _PRELU_TILING_DATA_H_
#define _PRELU_TILING_DATA_H_

struct PreluTilingData {
    int64_t totalNum = 0;     // x 总元素数量
    int64_t blockFactor = 0;  // 每个核处理的元素数量
    int64_t ubFactor = 0;     // 每次 UB 循环处理的元素数量
    int64_t weightMode = 0;   // 0: scalar weight, 1: channel weight
    int64_t channelSize = 1;  // x 的 C 维大小
    int64_t innerSize = 1;    // prod(x.shape[2:])
};
#endif
