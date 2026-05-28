/*!
 * \file prelu.h
 * \brief Prelu 算子 kernel 类定义
 */

#ifndef PRELU_H
#define PRELU_H

#include "kernel_operator.h"
#include "kernel_tiling/kernel_tiling.h"
#include "prelu_tiling_data.h"
#include "prelu_tiling_key.h"

#include <type_traits>

namespace NsPrelu {

using namespace AscendC;

constexpr int32_t BUFFER_NUM = 2;
constexpr uint32_t BRCB_SRC_ELEMENT_NUM = 8U;

template <typename T>
__aicore__ inline void CopyGmToLocalPad(
    const LocalTensor<T>& dst, const GlobalTensor<T>& src, uint32_t dataNum, uint32_t alignedDataNum)
{
    DataCopyExtParams copyParams{1, static_cast<uint32_t>(dataNum * sizeof(T)), 0, 0, 0};
    uint32_t rightPadding = alignedDataNum > dataNum ? alignedDataNum - dataNum : 0;
    DataCopyPadExtParams<T> padParams{rightPadding != 0, 0, static_cast<uint8_t>(rightPadding), static_cast<T>(0)};
    DataCopyPad(dst, src, copyParams, padParams);
}

template <typename T>
__aicore__ inline void CopyLocalToGmPad(const GlobalTensor<T>& dst, const LocalTensor<T>& src, uint32_t dataNum)
{
    DataCopyExtParams copyParams{1, static_cast<uint32_t>(dataNum * sizeof(T)), 0, 0, 0};
    DataCopyPad(dst, src, copyParams);
}

template <typename T>
class Prelu {
public:
    __aicore__ inline Prelu() {}

    __aicore__ inline void InitScalar(
        GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe);
    __aicore__ inline void InitChannel(
        GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe);
    __aicore__ inline void InitChannelSplitLParallel(
        GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe);
    __aicore__ inline void InitChannelNcWeightReuse(
        GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe);
    __aicore__ inline void InitChannelNcSplitCWeightReuse(
        GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe);
    __aicore__ inline void InitChannelSmallLMultiRow(
        GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe);
    __aicore__ inline void ProcessScalar();
    __aicore__ inline void ProcessChannelFullL();
    __aicore__ inline void ProcessChannelSplitL();
    __aicore__ inline void ProcessChannelSplitLParallel();
    __aicore__ inline void ProcessChannelNcWeightReuse();
    __aicore__ inline void ProcessChannelNcSplitCWeightReuse();
    __aicore__ inline void ProcessChannelSmallLMultiRow();

private:
    __aicore__ inline void CopyIn(int64_t progress, uint32_t currentNum);
    __aicore__ inline void CopyInByOffset(int64_t gmOffset, uint32_t currentNum, uint32_t alignedNum);
    __aicore__ inline void CopyInNcByRows(int64_t nOffset, int64_t tileRows);
    __aicore__ inline void CopyInSmallLRows(int64_t startRow, int64_t currentRows);
    __aicore__ inline void CopyOut(int64_t progress, uint32_t currentNum);
    __aicore__ inline void CopyOutByOffset(int64_t gmOffset, uint32_t currentNum);
    __aicore__ inline void CopyOutNcByRows(int64_t nOffset, int64_t tileRows);
    __aicore__ inline void CopyOutSmallLRows(int64_t startRow, int64_t currentRows);
    __aicore__ inline void Compute(uint32_t currentNum);
    __aicore__ inline void ComputeNc(uint32_t computeLen);
    __aicore__ inline void ComputeSmallLMultiRow(uint32_t computeLen, int64_t currentRows);
    __aicore__ inline void BuildNcWeightVec(int64_t tileRows);
    __aicore__ inline void BuildSmallLWeightVec(int64_t currentRows);
    __aicore__ inline void CopySmallLWeights(int64_t startRow, int64_t currentRows);
    __aicore__ inline void CopyWeightTile(int64_t cOffset, uint32_t realC, uint32_t alignedC);
    __aicore__ inline void LoadChannelWeight(int64_t channelIdx);
    __aicore__ inline void InitBuffers();
    __aicore__ inline void InitNcBuffers();
    __aicore__ inline void InitSmallLBuffers();

private:
    TPipe* pipe_ = nullptr;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueY;
    TBuf<TPosition::VECCALC> tmpXFp32;
    TBuf<TPosition::VECCALC> tmpBufPos;
    TBuf<TPosition::VECCALC> tmpBufNeg;
    TBuf<TPosition::VECCALC> weightBuf;
    TBuf<TPosition::VECCALC> weightVecBuf;
    TBuf<TPosition::VECCALC> weightFp32Buf;

    GlobalTensor<T> inputGMX;
    GlobalTensor<T> outputGMY;

    GM_ADDR weightGM = nullptr;
    T weightVal;
    float weightValFp32 = 0.0f;
    int64_t totalLength = 0;
    int64_t blockLength = 0;
    int64_t ubLength = 0;
    int64_t channelSize = 1;
    int64_t innerSize = 1;
    int64_t innerSizeAligned = 1;
    int64_t rowOffset = 0;
    int64_t blockRowNum = 0;
    int64_t taskOffset = 0;
    int64_t taskNum = 0;
    int64_t tilesPerRow = 0;
    int64_t cTileLength = 1;
    int64_t alignedChannelSize = 1;
    int64_t alignedWeightSize = 1;
    int64_t activeChannelSize = 1;
    int64_t rowsPerTile = 1;
    int64_t groupRows = 1;
    int64_t groupsPerBatch = 1;
    int64_t groupOffset = 0;
    int64_t groupCount = 0;
};

__aicore__ inline float LoadBf16ScalarAsFloat(GM_ADDR weight)
{
    uint16_t weightBits = *((__gm__ uint16_t*)weight);
    uint32_t floatBits = static_cast<uint32_t>(weightBits) << 16;
    return *reinterpret_cast<float*>(&floatBits);
}

__aicore__ inline uint32_t AlignUp(uint32_t value, uint32_t align)
{
    return ((value + align - 1U) / align) * align;
}

template <typename T>
__aicore__ inline void Prelu<T>::InitBuffers()
{
    pipe_->InitBuffer(inputQueueX, BUFFER_NUM, ubLength * sizeof(T));
    pipe_->InitBuffer(outputQueueY, BUFFER_NUM, ubLength * sizeof(T));
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        pipe_->InitBuffer(tmpXFp32, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufPos, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufNeg, ubLength * sizeof(float));
    } else {
        pipe_->InitBuffer(tmpBufPos, ubLength * sizeof(T));
        pipe_->InitBuffer(tmpBufNeg, ubLength * sizeof(T));
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::InitNcBuffers()
{
    pipe_->InitBuffer(inputQueueX, BUFFER_NUM, ubLength * sizeof(T));
    pipe_->InitBuffer(outputQueueY, BUFFER_NUM, ubLength * sizeof(T));
    pipe_->InitBuffer(weightBuf, alignedWeightSize * sizeof(T));
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        pipe_->InitBuffer(tmpXFp32, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufPos, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufNeg, ubLength * sizeof(float));
        pipe_->InitBuffer(weightVecBuf, ubLength * sizeof(float));
        pipe_->InitBuffer(weightFp32Buf, alignedWeightSize * sizeof(float));
    } else {
        pipe_->InitBuffer(tmpBufPos, ubLength * sizeof(T));
        pipe_->InitBuffer(tmpBufNeg, ubLength * sizeof(T));
        pipe_->InitBuffer(weightVecBuf, ubLength * sizeof(T));
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::InitSmallLBuffers()
{
    pipe_->InitBuffer(inputQueueX, BUFFER_NUM, ubLength * sizeof(T));
    pipe_->InitBuffer(outputQueueY, BUFFER_NUM, ubLength * sizeof(T));
    pipe_->InitBuffer(weightBuf, alignedWeightSize * sizeof(T));
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        pipe_->InitBuffer(tmpXFp32, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufPos, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufNeg, ubLength * sizeof(float));
        pipe_->InitBuffer(weightVecBuf, ubLength * sizeof(float));
        pipe_->InitBuffer(weightFp32Buf, alignedWeightSize * sizeof(float));
    } else {
        pipe_->InitBuffer(tmpBufPos, ubLength * sizeof(T));
        pipe_->InitBuffer(tmpBufNeg, ubLength * sizeof(T));
        pipe_->InitBuffer(weightVecBuf, ubLength * sizeof(T));
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::InitScalar(
    GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe)
{
    pipe_ = pipe;
    int64_t blockIdx = GetBlockIdx();
    ubLength = tilingData->tileLength;
    int64_t blockOffset = blockIdx * tilingData->formerLength;
    if (blockIdx < tilingData->formerNum) {
        blockLength = tilingData->formerLength;
    } else if (blockIdx < tilingData->usedCoreNum) {
        blockLength = tilingData->tailLength;
    } else {
        blockLength = 0;
    }

    inputGMX.SetGlobalBuffer((__gm__ T*)x + blockOffset, blockLength);
    outputGMY.SetGlobalBuffer((__gm__ T*)y + blockOffset, blockLength);

    if constexpr (std::is_same_v<T, bfloat16_t>) {
        weightValFp32 = LoadBf16ScalarAsFloat(weight);
    } else {
        T scalarWeight = *((__gm__ T*)weight);
        weightVal = scalarWeight;
    }

    InitBuffers();
}

template <typename T>
__aicore__ inline void Prelu<T>::InitChannel(
    GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe)
{
    pipe_ = pipe;
    int64_t blockIdx = GetBlockIdx();
    ubLength = tilingData->tileLength;
    channelSize = tilingData->channelSize;
    innerSize = tilingData->innerSize;
    innerSizeAligned = tilingData->innerSizeAligned;
    totalLength = tilingData->totalLength;
    weightGM = weight;

    if (blockIdx < tilingData->extraRows) {
        blockRowNum = tilingData->baseRows + 1;
        rowOffset = blockIdx * (tilingData->baseRows + 1);
    } else if (blockIdx < tilingData->usedCoreNum) {
        blockRowNum = tilingData->baseRows;
        rowOffset = tilingData->extraRows * (tilingData->baseRows + 1) +
                    (blockIdx - tilingData->extraRows) * tilingData->baseRows;
    } else {
        blockRowNum = 0;
        rowOffset = 0;
    }

    inputGMX.SetGlobalBuffer((__gm__ T*)x, tilingData->totalLength);
    outputGMY.SetGlobalBuffer((__gm__ T*)y, tilingData->totalLength);

    InitBuffers();
}

template <typename T>
__aicore__ inline void Prelu<T>::InitChannelSplitLParallel(
    GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe)
{
    pipe_ = pipe;
    int64_t blockIdx = GetBlockIdx();
    ubLength = tilingData->tileLength;
    channelSize = tilingData->channelSize;
    innerSize = tilingData->innerSize;
    tilesPerRow = tilingData->tilesPerRow;
    weightGM = weight;

    if (blockIdx < tilingData->extraTasks) {
        taskNum = tilingData->baseTasks + 1;
        taskOffset = blockIdx * (tilingData->baseTasks + 1);
    } else if (blockIdx < tilingData->usedCoreNum) {
        taskNum = tilingData->baseTasks;
        taskOffset = tilingData->extraTasks * (tilingData->baseTasks + 1) +
                     (blockIdx - tilingData->extraTasks) * tilingData->baseTasks;
    } else {
        taskNum = 0;
        taskOffset = 0;
    }

    inputGMX.SetGlobalBuffer((__gm__ T*)x, tilingData->totalLength);
    outputGMY.SetGlobalBuffer((__gm__ T*)y, tilingData->totalLength);

    InitBuffers();
}

template <typename T>
__aicore__ inline void Prelu<T>::InitChannelNcWeightReuse(
    GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe)
{
    pipe_ = pipe;
    int64_t blockIdx = GetBlockIdx();
    ubLength = tilingData->tileLength;
    channelSize = tilingData->channelSize;
    innerSize = tilingData->innerSize;
    alignedChannelSize = tilingData->innerSizeAligned;
    alignedWeightSize = AlignUp(static_cast<uint32_t>(channelSize), static_cast<uint32_t>(32U / sizeof(T)));
    activeChannelSize = channelSize;
    rowsPerTile = ubLength / alignedChannelSize;
    weightGM = weight;

    if (blockIdx < tilingData->extraRows) {
        blockRowNum = tilingData->baseRows + 1;
        rowOffset = blockIdx * (tilingData->baseRows + 1);
    } else if (blockIdx < tilingData->usedCoreNum) {
        blockRowNum = tilingData->baseRows;
        rowOffset = tilingData->extraRows * (tilingData->baseRows + 1) +
                    (blockIdx - tilingData->extraRows) * tilingData->baseRows;
    } else {
        blockRowNum = 0;
        rowOffset = 0;
    }

    inputGMX.SetGlobalBuffer((__gm__ T*)x, tilingData->totalLength);
    outputGMY.SetGlobalBuffer((__gm__ T*)y, tilingData->totalLength);

    InitNcBuffers();

    GlobalTensor<T> weightTensor;
    weightTensor.SetGlobalBuffer((__gm__ T*)weightGM, channelSize);
    LocalTensor<T> weightLocal = weightBuf.Get<T>();
    CopyGmToLocalPad(weightLocal, weightTensor, static_cast<uint32_t>(channelSize),
        static_cast<uint32_t>(alignedWeightSize));
    PipeBarrier<PIPE_ALL>();
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> weightFp32 = weightFp32Buf.Get<float>();
        Cast(weightFp32, weightLocal, RoundMode::CAST_NONE, static_cast<uint32_t>(alignedWeightSize));
        PipeBarrier<PIPE_ALL>();
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::InitChannelNcSplitCWeightReuse(
    GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe)
{
    pipe_ = pipe;
    int64_t blockIdx = GetBlockIdx();
    channelSize = tilingData->channelSize;
    innerSize = tilingData->innerSize;
    cTileLength = tilingData->tileLength;
    ubLength = innerSize == 1 ? tilingData->tileLength : tilingData->innerSizeAligned;
    alignedChannelSize = tilingData->innerSizeAligned;
    alignedWeightSize = innerSize == 1 ? alignedChannelSize : cTileLength;
    activeChannelSize = alignedWeightSize;
    tilesPerRow = tilingData->tilesPerRow;
    weightGM = weight;

    if (blockIdx < tilingData->extraTasks) {
        taskNum = tilingData->baseTasks + 1;
        taskOffset = blockIdx * (tilingData->baseTasks + 1);
    } else if (blockIdx < tilingData->usedCoreNum) {
        taskNum = tilingData->baseTasks;
        taskOffset = tilingData->extraTasks * (tilingData->baseTasks + 1) +
                     (blockIdx - tilingData->extraTasks) * tilingData->baseTasks;
    } else {
        taskNum = 0;
        taskOffset = 0;
    }

    inputGMX.SetGlobalBuffer((__gm__ T*)x, tilingData->totalLength);
    outputGMY.SetGlobalBuffer((__gm__ T*)y, tilingData->totalLength);

    InitNcBuffers();
}

template <typename T>
__aicore__ inline void Prelu<T>::InitChannelSmallLMultiRow(
    GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe)
{
    pipe_ = pipe;
    int64_t blockIdx = GetBlockIdx();
    channelSize = tilingData->channelSize;
    innerSize = tilingData->innerSize;
    innerSizeAligned = tilingData->innerSizeAligned;
    totalLength = tilingData->totalLength;
    groupRows = tilingData->groupRows;
    groupsPerBatch = tilingData->groupsPerBatch;
    ubLength = tilingData->tileLength;
    alignedChannelSize = innerSizeAligned;
    alignedWeightSize = AlignUp(static_cast<uint32_t>(groupRows), BRCB_SRC_ELEMENT_NUM);
    alignedWeightSize = AlignUp(alignedWeightSize, static_cast<uint32_t>(32U / sizeof(T)));
    weightGM = weight;

    if (blockIdx < tilingData->extraGroups) {
        groupCount = tilingData->baseGroups + 1;
        groupOffset = blockIdx * (tilingData->baseGroups + 1);
    } else if (blockIdx < tilingData->usedCoreNum) {
        groupCount = tilingData->baseGroups;
        groupOffset = tilingData->extraGroups * (tilingData->baseGroups + 1) +
                      (blockIdx - tilingData->extraGroups) * tilingData->baseGroups;
    } else {
        groupCount = 0;
        groupOffset = 0;
    }

    inputGMX.SetGlobalBuffer((__gm__ T*)x, tilingData->totalLength);
    outputGMY.SetGlobalBuffer((__gm__ T*)y, tilingData->totalLength);

    InitSmallLBuffers();
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyIn(int64_t progress, uint32_t currentNum)
{
    LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    CopyGmToLocalPad(xLocal, inputGMX[progress * ubLength], currentNum, currentNum);
    inputQueueX.EnQue(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyInByOffset(int64_t gmOffset, uint32_t currentNum, uint32_t alignedNum)
{
    LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    CopyGmToLocalPad(xLocal, inputGMX[gmOffset], currentNum, alignedNum);
    inputQueueX.EnQue(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyInNcByRows(int64_t nOffset, int64_t tileRows)
{
    LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    for (int64_t row = 0; row < tileRows; ++row) {
        int64_t gmOffset = (nOffset + row) * channelSize * innerSize;
        int64_t localOffset = row * alignedChannelSize;
        CopyGmToLocalPad(xLocal[localOffset], inputGMX[gmOffset], static_cast<uint32_t>(channelSize * innerSize),
            static_cast<uint32_t>(alignedChannelSize));
    }
    inputQueueX.EnQue(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyInSmallLRows(int64_t startRow, int64_t currentRows)
{
    LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    for (int64_t row = 0; row < currentRows; ++row) {
        int64_t gmOffset = (startRow + row) * innerSize;
        int64_t localOffset = row * innerSizeAligned;
        CopyGmToLocalPad(xLocal[localOffset], inputGMX[gmOffset], static_cast<uint32_t>(innerSize),
            static_cast<uint32_t>(innerSizeAligned));
    }
    inputQueueX.EnQue(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyOut(int64_t progress, uint32_t currentNum)
{
    LocalTensor<T> yLocal = outputQueueY.DeQue<T>();
    CopyLocalToGmPad(outputGMY[progress * ubLength], yLocal, currentNum);
    outputQueueY.FreeTensor(yLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyOutByOffset(int64_t gmOffset, uint32_t currentNum)
{
    LocalTensor<T> yLocal = outputQueueY.DeQue<T>();
    CopyLocalToGmPad(outputGMY[gmOffset], yLocal, currentNum);
    outputQueueY.FreeTensor(yLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyOutNcByRows(int64_t nOffset, int64_t tileRows)
{
    LocalTensor<T> yLocal = outputQueueY.DeQue<T>();
    for (int64_t row = 0; row < tileRows; ++row) {
        int64_t gmOffset = (nOffset + row) * channelSize * innerSize;
        int64_t localOffset = row * alignedChannelSize;
        CopyLocalToGmPad(outputGMY[gmOffset], yLocal[localOffset], static_cast<uint32_t>(channelSize * innerSize));
    }
    outputQueueY.FreeTensor(yLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyOutSmallLRows(int64_t startRow, int64_t currentRows)
{
    LocalTensor<T> yLocal = outputQueueY.DeQue<T>();
    for (int64_t row = 0; row < currentRows; ++row) {
        int64_t gmOffset = (startRow + row) * innerSize;
        int64_t localOffset = row * innerSizeAligned;
        CopyLocalToGmPad(outputGMY[gmOffset], yLocal[localOffset], static_cast<uint32_t>(innerSize));
    }
    outputQueueY.FreeTensor(yLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::Compute(uint32_t currentNum)
{
    LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    LocalTensor<T> yLocal = outputQueueY.AllocTensor<T>();

    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> xFp32 = tmpXFp32.Get<float>();
        LocalTensor<float> pos = tmpBufPos.Get<float>();
        LocalTensor<float> neg = tmpBufNeg.Get<float>();
        Cast(xFp32, xLocal, RoundMode::CAST_NONE, currentNum);
        Maxs(pos, xFp32, 0.0f, currentNum);
        Mins(neg, xFp32, 0.0f, currentNum);
        Muls(neg, neg, weightValFp32, currentNum);
        Add(pos, pos, neg, currentNum);
        Cast(yLocal, pos, RoundMode::CAST_RINT, currentNum);
    } else {
        LocalTensor<T> pos = tmpBufPos.Get<T>();
        LocalTensor<T> neg = tmpBufNeg.Get<T>();
        Maxs(pos, xLocal, static_cast<T>(0), currentNum);
        Mins(neg, xLocal, static_cast<T>(0), currentNum);
        Muls(neg, neg, weightVal, currentNum);
        Add(yLocal, pos, neg, currentNum);
    }

    outputQueueY.EnQue<T>(yLocal);
    inputQueueX.FreeTensor(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::BuildNcWeightVec(int64_t tileRows)
{
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> weightLocal = weightFp32Buf.Get<float>();
        LocalTensor<float> weightVec = weightVecBuf.Get<float>();
        if (innerSize == 1) {
            for (int64_t row = 0; row < tileRows; ++row) {
                int64_t rowOffset = row * alignedChannelSize;
                DataCopy(weightVec[rowOffset], weightLocal, static_cast<uint32_t>(alignedWeightSize));
            }
        } else {
            int64_t localOffset = 0;
            for (int64_t channelIdx = 0; channelIdx < activeChannelSize; ++channelIdx) {
                float weightValue = weightLocal.GetValue(channelIdx);
                for (int64_t innerIdx = 0; innerIdx < innerSize; ++innerIdx) {
                    weightVec.SetValue(localOffset + innerIdx, weightValue);
                }
                localOffset += innerSize;
            }
            for (int64_t padIdx = activeChannelSize * innerSize; padIdx < alignedChannelSize; ++padIdx) {
                weightVec.SetValue(padIdx, 0.0f);
            }
            for (int64_t row = 1; row < tileRows; ++row) {
                DataCopy(weightVec[row * alignedChannelSize], weightVec, static_cast<uint32_t>(alignedChannelSize));
            }
        }
    } else {
        LocalTensor<T> weightLocal = weightBuf.Get<T>();
        LocalTensor<T> weightVec = weightVecBuf.Get<T>();
        if (innerSize == 1) {
            for (int64_t row = 0; row < tileRows; ++row) {
                int64_t rowOffset = row * alignedChannelSize;
                DataCopy(weightVec[rowOffset], weightLocal, static_cast<uint32_t>(alignedWeightSize));
            }
        } else {
            int64_t localOffset = 0;
            for (int64_t channelIdx = 0; channelIdx < activeChannelSize; ++channelIdx) {
                T weightValue = weightLocal.GetValue(channelIdx);
                for (int64_t innerIdx = 0; innerIdx < innerSize; ++innerIdx) {
                    weightVec.SetValue(localOffset + innerIdx, weightValue);
                }
                localOffset += innerSize;
            }
            for (int64_t padIdx = activeChannelSize * innerSize; padIdx < alignedChannelSize; ++padIdx) {
                weightVec.SetValue(padIdx, static_cast<T>(0));
            }
            for (int64_t row = 1; row < tileRows; ++row) {
                DataCopy(weightVec[row * alignedChannelSize], weightVec, static_cast<uint32_t>(alignedChannelSize));
            }
        }
    }
    PipeBarrier<PIPE_ALL>();
}

template <typename T>
__aicore__ inline void Prelu<T>::BuildSmallLWeightVec(int64_t currentRows)
{
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> weightLocal = weightFp32Buf.Get<float>();
        LocalTensor<float> weightVec = weightVecBuf.Get<float>();
        for (int64_t row = 0; row < currentRows; ++row) {
            float weightValue = weightLocal.GetValue(row);
            int64_t localOffset = row * innerSizeAligned;
            constexpr uint32_t blockElems = 32U / sizeof(float);
            for (int64_t blockOffset = 0; blockOffset < innerSizeAligned; blockOffset += blockElems) {
                Duplicate(weightVec[localOffset + blockOffset], weightValue, blockElems);
            }
        }
    } else {
        LocalTensor<T> weightLocal = weightBuf.Get<T>();
        LocalTensor<T> weightVec = weightVecBuf.Get<T>();
        for (int64_t row = 0; row < currentRows; ++row) {
            T weightValue = weightLocal.GetValue(row);
            int64_t localOffset = row * innerSizeAligned;
            constexpr uint32_t blockElems = 32U / sizeof(T);
            for (int64_t blockOffset = 0; blockOffset < innerSizeAligned; blockOffset += blockElems) {
                Duplicate(weightVec[localOffset + blockOffset], weightValue, blockElems);
            }
        }
    }
    PipeBarrier<PIPE_ALL>();
}

template <typename T>
__aicore__ inline void Prelu<T>::CopySmallLWeights(int64_t startRow, int64_t currentRows)
{
    LocalTensor<T> weightLocal = weightBuf.Get<T>();
    int64_t channelOffset = startRow % channelSize;
    bool isContinuous = channelOffset + currentRows <= channelSize;
    if (isContinuous) {
        GlobalTensor<T> weightTensor;
        weightTensor.SetGlobalBuffer((__gm__ T*)weightGM + channelOffset, currentRows);
        CopyGmToLocalPad(weightLocal, weightTensor, static_cast<uint32_t>(currentRows),
            static_cast<uint32_t>(alignedWeightSize));
        PipeBarrier<PIPE_ALL>();
    } else {
        for (int64_t row = 0; row < currentRows; ++row) {
            int64_t channelIdx = (startRow + row) % channelSize;
            weightLocal.SetValue(row, *((__gm__ T*)weightGM + channelIdx));
        }
        PipeBarrier<PIPE_ALL>();
    }
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> weightFp32 = weightFp32Buf.Get<float>();
        Cast(weightFp32, weightLocal, RoundMode::CAST_NONE, static_cast<uint32_t>(alignedWeightSize));
        PipeBarrier<PIPE_ALL>();
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ComputeNc(uint32_t computeLen)
{
    LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    LocalTensor<T> yLocal = outputQueueY.AllocTensor<T>();

    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> xFp32 = tmpXFp32.Get<float>();
        LocalTensor<float> pos = tmpBufPos.Get<float>();
        LocalTensor<float> neg = tmpBufNeg.Get<float>();
        LocalTensor<float> weightVec = weightVecBuf.Get<float>();
        Cast(xFp32, xLocal, RoundMode::CAST_NONE, computeLen);
        Maxs(pos, xFp32, 0.0f, computeLen);
        Mins(neg, xFp32, 0.0f, computeLen);
        Mul(neg, neg, weightVec, computeLen);
        Add(pos, pos, neg, computeLen);
        Cast(yLocal, pos, RoundMode::CAST_RINT, computeLen);
    } else {
        LocalTensor<T> pos = tmpBufPos.Get<T>();
        LocalTensor<T> neg = tmpBufNeg.Get<T>();
        LocalTensor<T> weightVec = weightVecBuf.Get<T>();
        Maxs(pos, xLocal, static_cast<T>(0), computeLen);
        Mins(neg, xLocal, static_cast<T>(0), computeLen);
        Mul(neg, neg, weightVec, computeLen);
        Add(yLocal, pos, neg, computeLen);
    }

    outputQueueY.EnQue<T>(yLocal);
    inputQueueX.FreeTensor(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::ComputeSmallLMultiRow(uint32_t computeLen, int64_t currentRows)
{
    LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    LocalTensor<T> yLocal = outputQueueY.AllocTensor<T>();

    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> xFp32 = tmpXFp32.Get<float>();
        LocalTensor<float> pos = tmpBufPos.Get<float>();
        LocalTensor<float> neg = tmpBufNeg.Get<float>();
        LocalTensor<float> weightVec = weightVecBuf.Get<float>();
        Cast(xFp32, xLocal, RoundMode::CAST_NONE, computeLen);
        Maxs(pos, xFp32, 0.0f, computeLen);
        Mins(neg, xFp32, 0.0f, computeLen);
        Mul(neg, neg, weightVec, computeLen);
        Add(pos, pos, neg, computeLen);
        Cast(yLocal, pos, RoundMode::CAST_RINT, computeLen);
    } else {
        LocalTensor<T> pos = tmpBufPos.Get<T>();
        LocalTensor<T> neg = tmpBufNeg.Get<T>();
        LocalTensor<T> weightVec = weightVecBuf.Get<T>();
        Maxs(pos, xLocal, static_cast<T>(0), computeLen);
        Mins(neg, xLocal, static_cast<T>(0), computeLen);
        Mul(neg, neg, weightVec, computeLen);
        Add(yLocal, pos, neg, computeLen);
    }

    outputQueueY.EnQue<T>(yLocal);
    inputQueueX.FreeTensor(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyWeightTile(int64_t cOffset, uint32_t realC, uint32_t alignedC)
{
    GlobalTensor<T> weightTensor;
    weightTensor.SetGlobalBuffer((__gm__ T*)weightGM + cOffset, realC);
    LocalTensor<T> weightLocal = weightBuf.Get<T>();
    CopyGmToLocalPad(weightLocal, weightTensor, realC, alignedC);
    activeChannelSize = realC;
    PipeBarrier<PIPE_ALL>();
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> weightFp32 = weightFp32Buf.Get<float>();
        Cast(weightFp32, weightLocal, RoundMode::CAST_NONE, alignedC);
        PipeBarrier<PIPE_ALL>();
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::LoadChannelWeight(int64_t channelIdx)
{
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        weightValFp32 = LoadBf16ScalarAsFloat((GM_ADDR)((__gm__ T*)weightGM + channelIdx));
    } else {
        weightVal = *((__gm__ T*)weightGM + channelIdx);
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ProcessScalar()
{
    int64_t tileNum = (blockLength + ubLength - 1) / ubLength;
    for (int64_t i = 0; i < tileNum; ++i) {
        uint32_t currentNum = static_cast<uint32_t>((i == tileNum - 1) ? (blockLength - i * ubLength) : ubLength);
        CopyIn(i, currentNum);
        Compute(currentNum);
        CopyOut(i, currentNum);
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ProcessChannelFullL()
{
    uint32_t realLen = static_cast<uint32_t>(innerSize);
    uint32_t computeLen = static_cast<uint32_t>(innerSizeAligned);
    for (int64_t rowProgress = 0; rowProgress < blockRowNum; ++rowProgress) {
        int64_t rowIdx = rowOffset + rowProgress;
        int64_t channelIdx = rowIdx % channelSize;
        int64_t gmOffset = rowIdx * innerSize;
        LoadChannelWeight(channelIdx);
        CopyInByOffset(gmOffset, realLen, computeLen);
        Compute(computeLen);
        CopyOutByOffset(gmOffset, realLen);
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ProcessChannelSplitL()
{
    uint32_t alignElements = static_cast<uint32_t>(32U / sizeof(T));
    for (int64_t rowProgress = 0; rowProgress < blockRowNum; ++rowProgress) {
        int64_t rowIdx = rowOffset + rowProgress;
        int64_t channelIdx = rowIdx % channelSize;
        LoadChannelWeight(channelIdx);

        for (int64_t tileOffset = 0; tileOffset < innerSize; tileOffset += ubLength) {
            int64_t remainLen = innerSize - tileOffset;
            uint32_t realLen = static_cast<uint32_t>(remainLen > ubLength ? ubLength : remainLen);
            uint32_t computeLen = AlignUp(realLen, alignElements);
            int64_t gmOffset = rowIdx * innerSize + tileOffset;

            CopyInByOffset(gmOffset, realLen, computeLen);
            Compute(computeLen);
            CopyOutByOffset(gmOffset, realLen);
        }
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ProcessChannelSplitLParallel()
{
    uint32_t alignElements = static_cast<uint32_t>(32U / sizeof(T));
    int64_t lastChannelIdx = -1;
    for (int64_t taskProgress = 0; taskProgress < taskNum; ++taskProgress) {
        int64_t taskIdx = taskOffset + taskProgress;
        int64_t rowIdx = taskIdx / tilesPerRow;
        int64_t tileIdx = taskIdx % tilesPerRow;
        int64_t tileOffset = tileIdx * ubLength;
        int64_t remainLen = innerSize - tileOffset;
        uint32_t realLen = static_cast<uint32_t>(remainLen > ubLength ? ubLength : remainLen);
        uint32_t computeLen = AlignUp(realLen, alignElements);
        int64_t channelIdx = rowIdx % channelSize;
        int64_t gmOffset = rowIdx * innerSize + tileOffset;

        if (channelIdx != lastChannelIdx) {
            LoadChannelWeight(channelIdx);
            lastChannelIdx = channelIdx;
        }
        CopyInByOffset(gmOffset, realLen, computeLen);
        Compute(computeLen);
        CopyOutByOffset(gmOffset, realLen);
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ProcessChannelNcWeightReuse()
{
    for (int64_t rowProgress = 0; rowProgress < blockRowNum; rowProgress += rowsPerTile) {
        int64_t tileRows = blockRowNum - rowProgress;
        tileRows = tileRows > rowsPerTile ? rowsPerTile : tileRows;
        uint32_t computeLen = static_cast<uint32_t>(tileRows * alignedChannelSize);
        int64_t nOffset = rowOffset + rowProgress;

        CopyInNcByRows(nOffset, tileRows);
        BuildNcWeightVec(tileRows);
        ComputeNc(computeLen);
        CopyOutNcByRows(nOffset, tileRows);
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ProcessChannelNcSplitCWeightReuse()
{
    uint32_t alignElements = static_cast<uint32_t>(32U / sizeof(T));
    for (int64_t taskProgress = 0; taskProgress < taskNum; ++taskProgress) {
        int64_t taskIdx = taskOffset + taskProgress;
        int64_t nIdx = taskIdx / tilesPerRow;
        int64_t cTileIdx = taskIdx % tilesPerRow;
        int64_t cTileChannels = innerSize == 1 ? alignedChannelSize : cTileLength;
        int64_t cOffset = cTileIdx * cTileChannels;
        int64_t remainC = channelSize - cOffset;
        uint32_t realC = static_cast<uint32_t>(remainC > cTileChannels ? cTileChannels : remainC);
        uint32_t realLen = static_cast<uint32_t>(realC * innerSize);
        uint32_t computeLen = innerSize == 1 ? static_cast<uint32_t>(alignedChannelSize) :
            AlignUp(realLen, alignElements);
        uint32_t weightLen = innerSize == 1 ? computeLen : AlignUp(realC, alignElements);
        int64_t gmOffset = nIdx * channelSize * innerSize + cOffset * innerSize;

        CopyWeightTile(cOffset, realC, weightLen);
        CopyInByOffset(gmOffset, realLen, computeLen);
        BuildNcWeightVec(1);
        ComputeNc(computeLen);
        CopyOutByOffset(gmOffset, realLen);
    }
}

template <typename T>
__aicore__ inline void Prelu<T>::ProcessChannelSmallLMultiRow()
{
    int64_t batchSize = (channelSize == 0 || innerSize == 0) ? 0 : totalLength / (channelSize * innerSize);
    int64_t lastCGroupIdx = -1;
    for (int64_t groupProgress = 0; groupProgress < groupCount; ++groupProgress) {
        int64_t groupIdx = groupOffset + groupProgress;
        int64_t cGroupIdx = batchSize == 0 ? 0 : groupIdx / batchSize;
        int64_t nIdx = batchSize == 0 ? 0 : groupIdx % batchSize;
        int64_t cOffset = cGroupIdx * groupRows;
        int64_t remainChannels = channelSize - cOffset;
        int64_t currentRows = remainChannels > groupRows ? groupRows : remainChannels;
        int64_t startRow = nIdx * channelSize + cOffset;
        if (currentRows <= 0) {
            continue;
        }
        uint32_t computeLen = static_cast<uint32_t>(currentRows * innerSizeAligned);

        CopyInSmallLRows(startRow, currentRows);
        if (cGroupIdx != lastCGroupIdx) {
            CopySmallLWeights(startRow, currentRows);
            BuildSmallLWeightVec(currentRows);
            lastCGroupIdx = cGroupIdx;
        }
        ComputeSmallLMultiRow(computeLen, currentRows);
        CopyOutSmallLRows(startRow, currentRows);
    }
}

} // namespace NsPrelu
#endif // PRELU_H
