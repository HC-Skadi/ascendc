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
 * \file prelu.h
 * \brief
 */
#ifndef __PRELU_H__
#define __PRELU_H__

#include "kernel_operator.h"
#include "kernel_tiling/kernel_tiling.h"
#include "prelu_tiling_data.h"
#include "prelu_tiling_key.h"

namespace NsPrelu {

using namespace AscendC;

constexpr int32_t BUFFER_NUM = 2;
constexpr uint32_t BLOCK_SIZE = 32;
constexpr uint32_t MIN_DUPLICATE_NUM = 8;

template <typename T>
__aicore__ inline void CopyGmToLocalPad(LocalTensor<T>& dst, const GlobalTensor<T>& src, uint32_t dataNum)
{
    AscendC::DataCopyExtParams copyParams;
    copyParams.blockCount = 1;
    copyParams.blockLen = dataNum * sizeof(T);
    copyParams.srcStride = 0;
    copyParams.dstStride = 0;
    AscendC::DataCopyPadExtParams<T> padParams{false, 0, 0, 0};
    AscendC::DataCopyPad(dst, src, copyParams, padParams);
}

template <typename T>
__aicore__ inline void CopyLocalToGmPad(const GlobalTensor<T>& dst, const LocalTensor<T>& src, uint32_t dataNum)
{
    AscendC::DataCopyExtParams copyParams;
    copyParams.blockCount = 1;
    copyParams.blockLen = dataNum * sizeof(T);
    copyParams.srcStride = 0;
    copyParams.dstStride = 0;
    AscendC::DataCopyPad(dst, src, copyParams);
}

template <typename T>
class Prelu {
public:
    __aicore__ inline Prelu(){};

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData);
    __aicore__ inline void Process();

private:
    __aicore__ inline void CopyIn(int32_t progress);
    __aicore__ inline void CopyOut(int32_t progress);
    __aicore__ inline void Compute(int32_t progress);
    __aicore__ inline void FillChannelWeight(LocalTensor<T>& dst, int32_t progress);

private:
    TPipe pipe;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueW;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueZ;
    GlobalTensor<T> inputGMX;
    GlobalTensor<T> inputGMW;
    GlobalTensor<T> outputGMZ;
    TBuf<TPosition::VECCALC> tmpZero;
    TBuf<TPosition::VECCALC> tmpBufPos;
    TBuf<TPosition::VECCALC> tmpBufNeg;

    uint32_t coreOffset;
    uint32_t channelSize;
    uint32_t innerSize;
    uint32_t weightSize;

    uint32_t coreDataNum;
    uint32_t tileNum;
    uint32_t tileDataNum;
    uint32_t tailDataNum;
    uint32_t processDataNum;
    uint32_t totalNum;
};

template <typename T>
/**
 * @brief 初始化 PReLU 算子的每个 AI Core 执行上下文与内存/流水线资源。
 *
 * 该函数根据 tiling 信息与当前 block 索引，完成以下工作：
 * - 校验 block 维度有效性；
 * - 计算当前 core 的全局数据起始偏移（globalBufferIndex/coreOffset）；
 * - 按是否属于"尾部大核"分配当前 core 的处理数据量、tile 数和尾块大小；
 * - 绑定输入 X、权重 W、输出 Z 的 GlobalBuffer 视图（其中 W 按通道全量映射）；
 * - 初始化输入/输出队列与临时 Tensor Buffer（零值、正半轴、负半轴计算缓冲）。
 *
 * @tparam T 数据类型（如 half/float）。
 * @param x 输入特征图 X 的全局内存地址。
 * @param w PReLU 权重 W 的全局内存地址。
 * @param z 输出张量 Z 的全局内存地址。
 * @param tilingData 编译期/运行期生成的切分参数，描述各 core 数据分配、tile 信息和 shape 元数据。
 *
 * @note 本函数仅负责执行前的资源与索引初始化，不执行实际的 PReLU 数值计算。
 */
__aicore__ inline void Prelu<T>::Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData)
{
    ASSERT(AscendC::GetBlockNum() != 0 && "block dim can not be zero!");
    uint32_t coreNum = AscendC::GetBlockIdx();
    uint32_t globalBufferIndex = tilingData->bigCoreDataNum * AscendC::GetBlockIdx();
    this->tileDataNum = tilingData->tileDataNum;
    if (coreNum < tilingData->tailBlockNum) {
        this->coreDataNum = tilingData->bigCoreDataNum;
        this->tileNum = tilingData->finalBigTileNum;
        this->tailDataNum = tilingData->bigTailDataNum;
    } else {
        this->coreDataNum = tilingData->smallCoreDataNum;
        this->tileNum = tilingData->finalSmallTileNum;
        this->tailDataNum = tilingData->smallTailDataNum;
        globalBufferIndex -= (tilingData->bigCoreDataNum - tilingData->smallCoreDataNum) *
                             (AscendC::GetBlockIdx() - tilingData->tailBlockNum);
    }

    this->coreOffset = globalBufferIndex;
    this->channelSize = static_cast<uint32_t>(tilingData->channelSize);
    this->innerSize = static_cast<uint32_t>(tilingData->innerSize);
    this->weightSize = static_cast<uint32_t>(tilingData->weightSize);
    this->totalNum = static_cast<uint32_t>(tilingData->totalNum);

    inputGMX.SetGlobalBuffer((__gm__ T*)x + globalBufferIndex, this->coreDataNum);
    inputGMW.SetGlobalBuffer((__gm__ T*)w, this->weightSize);
    outputGMZ.SetGlobalBuffer((__gm__ T*)z + globalBufferIndex, this->coreDataNum);
    pipe.InitBuffer(inputQueueX, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(inputQueueW, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(outputQueueZ, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(tmpZero, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(tmpBufPos, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(tmpBufNeg, this->tileDataNum * sizeof(T));
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyIn(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    CopyGmToLocalPad(xLocal, inputGMX[progress * this->tileDataNum], this->processDataNum);
    AscendC::LocalTensor<T> wLocal = inputQueueW.AllocTensor<T>();
    FillChannelWeight(wLocal, progress);
    inputQueueX.EnQue(xLocal);
    inputQueueW.EnQue(wLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::FillChannelWeight(LocalTensor<T>& dst, int32_t progress)
{
    uint32_t localOffset = 0;
    uint32_t globalIndex = this->coreOffset + static_cast<uint32_t>(progress) * this->tileDataNum;
    uint32_t remaining = this->processDataNum;
    while (remaining > 0) {
        uint32_t weightIndex = (globalIndex / this->innerSize) % this->channelSize;
        uint32_t channelRemain = this->innerSize - (globalIndex % this->innerSize);
        uint32_t calcNum = (remaining < channelRemain) ? remaining : channelRemain;
        T weightValue = this->inputGMW.GetValue(weightIndex);
        uint32_t blockElementNum = BLOCK_SIZE / sizeof(T);
        bool duplicateAligned = (localOffset % blockElementNum == 0) && (calcNum % blockElementNum == 0);
        if (calcNum < MIN_DUPLICATE_NUM || !duplicateAligned) {
            for (uint32_t i = 0; i < calcNum; ++i) {
                dst.SetValue(localOffset + i, weightValue);
            }
        } else {
            AscendC::Duplicate(dst[localOffset], weightValue, calcNum);
        }
        localOffset += calcNum;
        globalIndex += calcNum;
        remaining -= calcNum;
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyOut(int32_t progress)
{
    AscendC::LocalTensor<T> zLocal = outputQueueZ.DeQue<T>();
    CopyLocalToGmPad(outputGMZ[progress * this->tileDataNum], zLocal, this->processDataNum);
    outputQueueZ.FreeTensor(zLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::Compute(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    AscendC::LocalTensor<T> wLocal = inputQueueW.DeQue<T>();
    AscendC::LocalTensor<T> zLocal = outputQueueZ.AllocTensor<T>();
    AscendC::LocalTensor<T> zero = tmpZero.Get<T>();
    AscendC::Duplicate(zero, (T)0, processDataNum);

    AscendC::LocalTensor<T> pos = tmpBufPos.Get<T>();
    AscendC::LocalTensor<T> neg = tmpBufNeg.Get<T>();

    // PReLU: f(x) = x if x >= 0, else alpha * x
    AscendC::Max(pos, xLocal, zero, this->processDataNum); // max(x, 0)
    AscendC::Min(neg, xLocal, zero, this->processDataNum); // follow requested pattern
    AscendC::Mul(neg, neg, wLocal, this->processDataNum);  // neg * weight[c]
    AscendC::Add(zLocal, pos, neg, this->processDataNum);  // pos + neg * w

    outputQueueZ.EnQue<T>(zLocal);
    inputQueueX.FreeTensor(xLocal);
    inputQueueW.FreeTensor(wLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::Process()
{
    int32_t loopCount = this->tileNum;
    this->processDataNum = this->tileDataNum;
    for (int32_t i = 0; i < loopCount; i++) {
        if (i == this->tileNum - 1) {
            this->processDataNum = this->tailDataNum;
        }
        uint32_t globalStart = this->coreOffset + static_cast<uint32_t>(i) * this->tileDataNum;
        if (globalStart >= this->totalNum) {
            break;
        }
        uint32_t remainDataNum = this->totalNum - globalStart;
        if (this->processDataNum > remainDataNum) {
            this->processDataNum = remainDataNum;
        }
        CopyIn(i);
        Compute(i);
        CopyOut(i);
    }
}

template <typename T>
class PreluFp16 {
public:
    __aicore__ inline PreluFp16(){};

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData);
    __aicore__ inline void Process();

private:
    __aicore__ inline void CopyIn(int32_t progress);
    __aicore__ inline void CopyOut(int32_t progress);
    __aicore__ inline void Compute(int32_t progress);
    __aicore__ inline void FillChannelWeight(LocalTensor<T>& dst, int32_t progress);

private:
    TPipe pipe;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueW;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueZ;
    GlobalTensor<T> inputGMX;
    GlobalTensor<T> inputGMW;
    GlobalTensor<T> outputGMZ;
    TBuf<TPosition::VECCALC> tmpZero;
    TBuf<TPosition::VECCALC> tmpBufPos;
    TBuf<TPosition::VECCALC> tmpBufNeg;
    TBuf<TPosition::VECCALC> tmpBufXLocalFp32;
    TBuf<TPosition::VECCALC> tmpBufWLocalFp32;
    TBuf<TPosition::VECCALC> tmpBufYLocalFp32;

    uint32_t coreOffset;
    uint32_t channelSize;
    uint32_t innerSize;
    uint32_t weightSize;

    uint32_t coreDataNum;
    uint32_t tileNum;
    uint32_t tileDataNum;
    uint32_t tailDataNum;
    uint32_t processDataNum;
    uint32_t totalNum;
};

template <typename T>
__aicore__ inline void PreluFp16<T>::Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData)
{
    ASSERT(AscendC::GetBlockNum() != 0 && "block dim can not be zero!");
    uint32_t coreNum = AscendC::GetBlockIdx();
    uint32_t globalBufferIndex = tilingData->bigCoreDataNum * AscendC::GetBlockIdx();
    this->tileDataNum = tilingData->tileDataNum;
    if (coreNum < tilingData->tailBlockNum) {
        this->coreDataNum = tilingData->bigCoreDataNum;
        this->tileNum = tilingData->finalBigTileNum;
        this->tailDataNum = tilingData->bigTailDataNum;
    } else {
        this->coreDataNum = tilingData->smallCoreDataNum;
        this->tileNum = tilingData->finalSmallTileNum;
        this->tailDataNum = tilingData->smallTailDataNum;
        globalBufferIndex -= (tilingData->bigCoreDataNum - tilingData->smallCoreDataNum) *
                             (AscendC::GetBlockIdx() - tilingData->tailBlockNum);
    }

    this->coreOffset = globalBufferIndex;
    this->channelSize = static_cast<uint32_t>(tilingData->channelSize);
    this->innerSize = static_cast<uint32_t>(tilingData->innerSize);
    this->weightSize = static_cast<uint32_t>(tilingData->weightSize);
    this->totalNum = static_cast<uint32_t>(tilingData->totalNum);

    inputGMX.SetGlobalBuffer((__gm__ T*)x + globalBufferIndex, this->coreDataNum);
    inputGMW.SetGlobalBuffer((__gm__ T*)w, this->weightSize);
    outputGMZ.SetGlobalBuffer((__gm__ T*)z + globalBufferIndex, this->coreDataNum);
    pipe.InitBuffer(inputQueueX, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(inputQueueW, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(outputQueueZ, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(tmpZero, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufPos, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufNeg, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufXLocalFp32, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufWLocalFp32, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufYLocalFp32, this->tileDataNum * sizeof(float));
}

template <typename T>
__aicore__ inline void PreluFp16<T>::CopyIn(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    CopyGmToLocalPad(xLocal, inputGMX[progress * this->tileDataNum], this->processDataNum);
    AscendC::LocalTensor<T> wLocal = inputQueueW.AllocTensor<T>();
    FillChannelWeight(wLocal, progress);
    inputQueueX.EnQue(xLocal);
    inputQueueW.EnQue(wLocal);
}

template <typename T>
__aicore__ inline void PreluFp16<T>::FillChannelWeight(LocalTensor<T>& dst, int32_t progress)
{
    uint32_t localOffset = 0;
    uint32_t globalIndex = this->coreOffset + static_cast<uint32_t>(progress) * this->tileDataNum;
    uint32_t remaining = this->processDataNum;
    while (remaining > 0) {
        uint32_t weightIndex = (globalIndex / this->innerSize) % this->channelSize;
        uint32_t channelRemain = this->innerSize - (globalIndex % this->innerSize);
        uint32_t calcNum = (remaining < channelRemain) ? remaining : channelRemain;
        T weightValue = this->inputGMW.GetValue(weightIndex);
        uint32_t blockElementNum = BLOCK_SIZE / sizeof(T);
        bool duplicateAligned = (localOffset % blockElementNum == 0) && (calcNum % blockElementNum == 0);
        if (calcNum < MIN_DUPLICATE_NUM || !duplicateAligned) {
            for (uint32_t i = 0; i < calcNum; ++i) {
                dst.SetValue(localOffset + i, weightValue);
            }
        } else {
            AscendC::Duplicate(dst[localOffset], weightValue, calcNum);
        }
        localOffset += calcNum;
        globalIndex += calcNum;
        remaining -= calcNum;
    }
}

template <typename T>
__aicore__ inline void PreluFp16<T>::CopyOut(int32_t progress)
{
    AscendC::LocalTensor<T> zLocal = outputQueueZ.DeQue<T>();
    CopyLocalToGmPad(outputGMZ[progress * this->tileDataNum], zLocal, this->processDataNum);
    outputQueueZ.FreeTensor(zLocal);
}

template <typename T>
__aicore__ inline void PreluFp16<T>::Compute(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    AscendC::LocalTensor<T> wLocal = inputQueueW.DeQue<T>();
    AscendC::LocalTensor<T> zLocal = outputQueueZ.AllocTensor<T>();

    AscendC::LocalTensor<float> zero = tmpZero.Get<float>();
    AscendC::Duplicate(zero, (float)0, processDataNum);

    AscendC::LocalTensor<float> xLocalFp32 = tmpBufXLocalFp32.Get<float>();
    AscendC::Cast(xLocalFp32, xLocal, AscendC::RoundMode::CAST_NONE, processDataNum);
    AscendC::LocalTensor<float> weightLocalFp32 = tmpBufWLocalFp32.Get<float>();
    AscendC::Cast(weightLocalFp32, wLocal, AscendC::RoundMode::CAST_NONE, processDataNum);

    // PReLU: f(x) = x if x >= 0, else alpha * x
    AscendC::LocalTensor<float> pos = tmpBufPos.Get<float>();
    AscendC::LocalTensor<float> neg = tmpBufNeg.Get<float>();
    AscendC::LocalTensor<float> yLocalFp32 = tmpBufYLocalFp32.Get<float>();

    AscendC::Max(pos, xLocalFp32, zero, processDataNum);     // max(x, 0)
    AscendC::Min(neg, xLocalFp32, zero, processDataNum);     // follow requested pattern
    AscendC::Mul(neg, neg, weightLocalFp32, processDataNum); // neg * weight[c]
    AscendC::Add(yLocalFp32, pos, neg, processDataNum);      // pos + neg * w

    AscendC::Cast(zLocal, yLocalFp32, AscendC::RoundMode::CAST_RINT, processDataNum);

    outputQueueZ.EnQue<T>(zLocal);
    inputQueueX.FreeTensor(xLocal);
    inputQueueW.FreeTensor(wLocal);
}

template <typename T>
__aicore__ inline void PreluFp16<T>::Process()
{
    int32_t loopCount = this->tileNum;
    this->processDataNum = this->tileDataNum;
    for (int32_t i = 0; i < loopCount; i++) {
        if (i == this->tileNum - 1) {
            this->processDataNum = this->tailDataNum;
        }
        uint32_t globalStart = this->coreOffset + static_cast<uint32_t>(i) * this->tileDataNum;
        if (globalStart >= this->totalNum) {
            break;
        }
        uint32_t remainDataNum = this->totalNum - globalStart;
        if (this->processDataNum > remainDataNum) {
            this->processDataNum = remainDataNum;
        }
        CopyIn(i);
        Compute(i);
        CopyOut(i);
    }
}

template <typename T>
class PreluScalar {
public:
    __aicore__ inline PreluScalar(){};

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData);
    __aicore__ inline void Process();

private:
    __aicore__ inline void CopyIn(int32_t progress);
    __aicore__ inline void CopyOut(int32_t progress);
    __aicore__ inline void Compute(int32_t progress);

private:
    TPipe pipe;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueZ;
    GlobalTensor<T> inputGMX;
    GlobalTensor<T> outputGMZ;
    TBuf<TPosition::VECCALC> tmpBufPos;
    TBuf<TPosition::VECCALC> tmpBufNeg;

    T weightVal;
    uint32_t coreOffset;

    uint32_t coreDataNum;
    uint32_t tileNum;
    uint32_t tileDataNum;
    uint32_t tailDataNum;
    uint32_t processDataNum;
    uint32_t totalNum;
};

template <typename T>
__aicore__ inline void PreluScalar<T>::Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData)
{
    ASSERT(AscendC::GetBlockNum() != 0 && "block dim can not be zero!");
    uint32_t coreNum = AscendC::GetBlockIdx();
    uint32_t globalBufferIndex = tilingData->bigCoreDataNum * AscendC::GetBlockIdx();
    this->tileDataNum = tilingData->tileDataNum;
    if (coreNum < tilingData->tailBlockNum) {
        this->coreDataNum = tilingData->bigCoreDataNum;
        this->tileNum = tilingData->finalBigTileNum;
        this->tailDataNum = tilingData->bigTailDataNum;
    } else {
        this->coreDataNum = tilingData->smallCoreDataNum;
        this->tileNum = tilingData->finalSmallTileNum;
        this->tailDataNum = tilingData->smallTailDataNum;
        globalBufferIndex -= (tilingData->bigCoreDataNum - tilingData->smallCoreDataNum) *
                             (AscendC::GetBlockIdx() - tilingData->tailBlockNum);
    }

    this->coreOffset = globalBufferIndex;
    this->totalNum = static_cast<uint32_t>(tilingData->totalNum);
    this->weightVal = *((__gm__ T*)w);

    inputGMX.SetGlobalBuffer((__gm__ T*)x + globalBufferIndex, this->coreDataNum);
    outputGMZ.SetGlobalBuffer((__gm__ T*)z + globalBufferIndex, this->coreDataNum);
    pipe.InitBuffer(inputQueueX, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(outputQueueZ, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(tmpBufPos, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(tmpBufNeg, this->tileDataNum * sizeof(T));
}

template <typename T>
__aicore__ inline void PreluScalar<T>::CopyIn(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    CopyGmToLocalPad(xLocal, inputGMX[progress * this->tileDataNum], this->processDataNum);
    inputQueueX.EnQue(xLocal);
}

template <typename T>
__aicore__ inline void PreluScalar<T>::CopyOut(int32_t progress)
{
    AscendC::LocalTensor<T> zLocal = outputQueueZ.DeQue<T>();
    CopyLocalToGmPad(outputGMZ[progress * this->tileDataNum], zLocal, this->processDataNum);
    outputQueueZ.FreeTensor(zLocal);
}

template <typename T>
__aicore__ inline void PreluScalar<T>::Compute(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    AscendC::LocalTensor<T> zLocal = outputQueueZ.AllocTensor<T>();

    AscendC::LocalTensor<T> pos = tmpBufPos.Get<T>();
    AscendC::LocalTensor<T> neg = tmpBufNeg.Get<T>();

    // PReLU: f(x) = max(x, 0) + min(x, 0) * weight  (scalar weight)
    AscendC::Maxs(pos, xLocal, (T)0, this->processDataNum);         // max(x, 0)
    AscendC::Mins(neg, xLocal, (T)0, this->processDataNum);         // min(x, 0)
    AscendC::Muls(neg, neg, this->weightVal, this->processDataNum); // neg * weight
    AscendC::Add(zLocal, pos, neg, this->processDataNum);           // pos + neg * weight

    outputQueueZ.EnQue<T>(zLocal);
    inputQueueX.FreeTensor(xLocal);
}

template <typename T>
__aicore__ inline void PreluScalar<T>::Process()
{
    int32_t loopCount = this->tileNum;
    this->processDataNum = this->tileDataNum;
    for (int32_t i = 0; i < loopCount; i++) {
        if (i == this->tileNum - 1) {
            this->processDataNum = this->tailDataNum;
        }
        uint32_t globalStart = this->coreOffset + static_cast<uint32_t>(i) * this->tileDataNum;
        if (globalStart >= this->totalNum) {
            break;
        }
        uint32_t remainDataNum = this->totalNum - globalStart;
        if (this->processDataNum > remainDataNum) {
            this->processDataNum = remainDataNum;
        }
        CopyIn(i);
        Compute(i);
        CopyOut(i);
    }
}

template <typename T>
class PreluScalarFp16 {
public:
    __aicore__ inline PreluScalarFp16(){};

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData);
    __aicore__ inline void Process();

private:
    __aicore__ inline void CopyIn(int32_t progress);
    __aicore__ inline void CopyOut(int32_t progress);
    __aicore__ inline void Compute(int32_t progress);

private:
    TPipe pipe;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueZ;
    GlobalTensor<T> inputGMX;
    GlobalTensor<T> outputGMZ;
    TBuf<TPosition::VECCALC> tmpBufPos;
    TBuf<TPosition::VECCALC> tmpBufNeg;
    TBuf<TPosition::VECCALC> tmpBufXLocalFp32;
    TBuf<TPosition::VECCALC> tmpBufYLocalFp32;

    float weightValFp32;
    uint32_t coreOffset;

    uint32_t coreDataNum;
    uint32_t tileNum;
    uint32_t tileDataNum;
    uint32_t tailDataNum;
    uint32_t processDataNum;
    uint32_t totalNum;
};

template <typename T>
__aicore__ inline void PreluScalarFp16<T>::Init(GM_ADDR x, GM_ADDR w, GM_ADDR z, const PreluTilingData* tilingData)
{
    ASSERT(AscendC::GetBlockNum() != 0 && "block dim can not be zero!");
    uint32_t coreNum = AscendC::GetBlockIdx();
    uint32_t globalBufferIndex = tilingData->bigCoreDataNum * AscendC::GetBlockIdx();
    this->tileDataNum = tilingData->tileDataNum;
    if (coreNum < tilingData->tailBlockNum) {
        this->coreDataNum = tilingData->bigCoreDataNum;
        this->tileNum = tilingData->finalBigTileNum;
        this->tailDataNum = tilingData->bigTailDataNum;
    } else {
        this->coreDataNum = tilingData->smallCoreDataNum;
        this->tileNum = tilingData->finalSmallTileNum;
        this->tailDataNum = tilingData->smallTailDataNum;
        globalBufferIndex -= (tilingData->bigCoreDataNum - tilingData->smallCoreDataNum) *
                             (AscendC::GetBlockIdx() - tilingData->tailBlockNum);
    }

    this->coreOffset = globalBufferIndex;
    this->totalNum = static_cast<uint32_t>(tilingData->totalNum);

    uint16_t wBits = *((__gm__ uint16_t*)w);
    uint32_t fBits = static_cast<uint32_t>(wBits) << 16;
    this->weightValFp32 = *reinterpret_cast<float*>(&fBits);

    inputGMX.SetGlobalBuffer((__gm__ T*)x + globalBufferIndex, this->coreDataNum);
    outputGMZ.SetGlobalBuffer((__gm__ T*)z + globalBufferIndex, this->coreDataNum);
    pipe.InitBuffer(inputQueueX, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(outputQueueZ, BUFFER_NUM, this->tileDataNum * sizeof(T));
    pipe.InitBuffer(tmpBufPos, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufNeg, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufXLocalFp32, this->tileDataNum * sizeof(float));
    pipe.InitBuffer(tmpBufYLocalFp32, this->tileDataNum * sizeof(float));
}

template <typename T>
__aicore__ inline void PreluScalarFp16<T>::CopyIn(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    CopyGmToLocalPad(xLocal, inputGMX[progress * this->tileDataNum], this->processDataNum);
    inputQueueX.EnQue(xLocal);
}

template <typename T>
__aicore__ inline void PreluScalarFp16<T>::CopyOut(int32_t progress)
{
    AscendC::LocalTensor<T> zLocal = outputQueueZ.DeQue<T>();
    CopyLocalToGmPad(outputGMZ[progress * this->tileDataNum], zLocal, this->processDataNum);
    outputQueueZ.FreeTensor(zLocal);
}

template <typename T>
__aicore__ inline void PreluScalarFp16<T>::Compute(int32_t progress)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    AscendC::LocalTensor<T> zLocal = outputQueueZ.AllocTensor<T>();

    AscendC::LocalTensor<float> xLocalFp32 = tmpBufXLocalFp32.Get<float>();
    AscendC::Cast(xLocalFp32, xLocal, AscendC::RoundMode::CAST_NONE, processDataNum);

    AscendC::LocalTensor<float> pos = tmpBufPos.Get<float>();
    AscendC::LocalTensor<float> neg = tmpBufNeg.Get<float>();
    AscendC::LocalTensor<float> yLocalFp32 = tmpBufYLocalFp32.Get<float>();

    // PReLU: f(x) = max(x, 0) + min(x, 0) * weight  (scalar weight)
    AscendC::Maxs(pos, xLocalFp32, (float)0, processDataNum);     // max(x, 0)
    AscendC::Mins(neg, xLocalFp32, (float)0, processDataNum);     // min(x, 0)
    AscendC::Muls(neg, neg, this->weightValFp32, processDataNum); // neg * weight
    AscendC::Add(yLocalFp32, pos, neg, processDataNum);           // pos + neg * weight

    AscendC::Cast(zLocal, yLocalFp32, AscendC::RoundMode::CAST_RINT, processDataNum);

    outputQueueZ.EnQue<T>(zLocal);
    inputQueueX.FreeTensor(xLocal);
}

template <typename T>
__aicore__ inline void PreluScalarFp16<T>::Process()
{
    int32_t loopCount = this->tileNum;
    this->processDataNum = this->tileDataNum;
    for (int32_t i = 0; i < loopCount; i++) {
        if (i == this->tileNum - 1) {
            this->processDataNum = this->tailDataNum;
        }
        uint32_t globalStart = this->coreOffset + static_cast<uint32_t>(i) * this->tileDataNum;
        if (globalStart >= this->totalNum) {
            break;
        }
        uint32_t remainDataNum = this->totalNum - globalStart;
        if (this->processDataNum > remainDataNum) {
            this->processDataNum = remainDataNum;
        }
        CopyIn(i);
        Compute(i);
        CopyOut(i);
    }
}

} // namespace NsPrelu
#endif // PRELU_H
