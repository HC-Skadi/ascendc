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

template <typename T>
__aicore__ inline void CopyGmToLocalPad(
    LocalTensor<T>& dst, const GlobalTensor<T>& src, uint32_t dataNum, uint32_t alignedDataNum)
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
    __aicore__ inline void ProcessScalar();
    __aicore__ inline void ProcessChannelFullL();
    __aicore__ inline void ProcessChannelSplitL();

private:
    __aicore__ inline void CopyIn(int64_t progress, uint32_t currentNum);
    __aicore__ inline void CopyInByOffset(int64_t gmOffset, uint32_t currentNum, uint32_t alignedNum);
    __aicore__ inline void CopyOut(int64_t progress, uint32_t currentNum);
    __aicore__ inline void CopyOutByOffset(int64_t gmOffset, uint32_t currentNum);
    __aicore__ inline void Compute(uint32_t currentNum);
    __aicore__ inline void LoadChannelWeight(int64_t channelIdx);
    __aicore__ inline void InitBuffers();

private:
    TPipe* pipe_ = nullptr;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueY;
    TBuf<TPosition::VECCALC> tmpXFp32;
    TBuf<TPosition::VECCALC> tmpBufPos;
    TBuf<TPosition::VECCALC> tmpBufNeg;

    GlobalTensor<T> inputGMX;
    GlobalTensor<T> outputGMY;

    GM_ADDR weightGM = nullptr;
    T weightVal;
    float weightValFp32 = 0.0f;
    int64_t blockLength = 0;
    int64_t ubLength = 0;
    int64_t channelSize = 1;
    int64_t innerSize = 1;
    int64_t innerSizeAligned = 1;
    int64_t rowOffset = 0;
    int64_t blockRowNum = 0;
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

} // namespace NsPrelu
#endif // PRELU_H
