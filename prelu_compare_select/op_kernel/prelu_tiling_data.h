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
    int64_t formerNum = 0;     // 使用 formerLength 的核数
    int64_t formerLength = 0;  // 前段每核处理的元素数量
    int64_t tailNum = 0;       // 使用 tailLength 的尾段核数
    int64_t tailLength = 0;    // 尾段每核处理的元素数量
    int64_t tileLength = 0;    // 每次 UB 循环处理的元素数量
    int64_t weightMode = 0;    // weight 模式: 0 scalar, 1 channel broadcast
    int64_t outerSize = 1;     // channel 前维度乘积
    int64_t channelSize = 1;   // channel 维度大小
    int64_t innerSize = 1;     // channel 后维度乘积
    int64_t weightSize = 1;    // weight 元素数量
};
#endif
