/*!
 * \file prelu_tiling_data.h
 * \brief tiling data struct
 */

#ifndef _PRELU_TILING_DATA_H_
#define _PRELU_TILING_DATA_H_

#include <cstdint>

struct PreluTilingData {
    int64_t totalLength = 0;   // 总元素数量
    int64_t usedCoreNum = 0;   // 实际使用的 AIV 核数
    int64_t formerNum = 0;     // scalar路径使用 formerLength 的核数
    int64_t formerLength = 0;  // scalar路径前段每核处理的元素数量
    int64_t tailNum = 0;       // scalar路径使用 tailLength 的尾段核数
    int64_t tailLength = 0;    // scalar路径尾段每核处理的元素数量
    int64_t tileLength = 0;    // 每次 UB 循环处理的元素数量

    int64_t weightSize = 1;        // 1 或 C
    int64_t weightMode = 0;        // 0=scalar, 1=channel
    int64_t channelSize = 1;       // C
    int64_t innerSize = 1;         // L，真实搬运长度
    int64_t innerSizeAligned = 1;  // AlignUp(L, 32 / sizeof(T))
    int64_t rowNum = 0;            // N * C
    int64_t baseRows = 0;          // channel路径每核基础row数
    int64_t extraRows = 0;         // channel路径前extraRows个核各多处理1个row
};
#endif
