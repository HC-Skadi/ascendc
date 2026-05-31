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
constexpr int64_t SMALL_CHANNEL_SCALAR_INNER = 16;
constexpr int64_t SMALL_CHANNEL_SCALAR_CHANNEL = 16;
constexpr uint32_t SMALL_CHANNEL_SCALAR_NUM = 4096;

template <typename T>
__aicore__ inline void CopyGmToLocalPad(LocalTensor<T>& dst, const GlobalTensor<T>& src, uint32_t dataNum)
{
    DataCopyExtParams copyParams{1, static_cast<uint32_t>(dataNum * sizeof(T)), 0, 0, 0};
    DataCopyPadExtParams<T> padParams{false, 0, 0, 0};
    DataCopyPad(dst, src, copyParams, padParams);
}

template <typename T>
__aicore__ inline void CopyLocalToGmPad(const GlobalTensor<T>& dst, const LocalTensor<T>& src, uint32_t dataNum)
{
    DataCopyExtParams copyParams{1, static_cast<uint32_t>(dataNum * sizeof(T)), 0, 0, 0};
    DataCopyPad(dst, src, copyParams);
}

template <typename T, uint32_t schMode>
class Prelu {
public:
    __aicore__ inline Prelu() {}

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe);
    __aicore__ inline void Process();

private:
    __aicore__ inline void CopyIn(int64_t progress, uint32_t currentNum);
    __aicore__ inline void CopyOut(int64_t progress, uint32_t currentNum);
    __aicore__ inline void Compute(int64_t progress, uint32_t currentNum);
    __aicore__ inline void ComputeScalar(uint32_t currentNum, LocalTensor<T>& xLocal, LocalTensor<T>& yLocal);
    __aicore__ inline void ComputeChannel(int64_t progress, uint32_t currentNum, LocalTensor<T>& xLocal, LocalTensor<T>& yLocal);
    __aicore__ inline void ComputeChannelScalar(
        int64_t progress, uint32_t currentNum, LocalTensor<T>& xLocal, LocalTensor<T>& yLocal);
    __aicore__ inline void FillChannelWeight(LocalTensor<T>& dst, int64_t progress, uint32_t currentNum);
    __aicore__ inline void FillChannelWeightFp32(LocalTensor<float>& dst, int64_t progress, uint32_t currentNum);
    __aicore__ inline T LoadWeight(int64_t weightOffset);
    __aicore__ inline float LoadWeightFp32(int64_t weightOffset);

private:
    TPipe* pipe_ = nullptr;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueY;
    TBuf<TPosition::VECCALC> tmpXFp32;
    TBuf<TPosition::VECCALC> tmpBufWeight;
    TBuf<TPosition::VECCALC> tmpBufProd;
    TBuf<TPosition::VECCALC> tmpBufMask;

    GlobalTensor<T> inputGMX;
    GlobalTensor<T> inputGMWeight;
    GlobalTensor<T> outputGMY;

    T weightVal;
    float weightValFp32 = 0.0f;
    int64_t blockOffset = 0;
    int64_t blockLength = 0;
    int64_t ubLength = 0;
    int64_t channelSize = 1;
    int64_t innerSize = 1;
};

__aicore__ inline float ToFloat(const bfloat16_t& bVal)
{
    uint16_t weightBits = *reinterpret_cast<const uint16_t*>(&bVal);
    uint32_t floatBits = static_cast<uint32_t>(weightBits) << 16;
    return *reinterpret_cast<float*>(&floatBits);
}

__aicore__ inline bfloat16_t ToBfloat16(float value)
{
    uint32_t floatBits = *reinterpret_cast<uint32_t*>(&value);
    uint32_t roundBias = 0x7FFFU + ((floatBits >> 16U) & 1U);
    uint16_t bf16Bits = static_cast<uint16_t>((floatBits + roundBias) >> 16U);
    return *reinterpret_cast<bfloat16_t*>(&bf16Bits);
}

template <typename ComputeT>
__aicore__ inline uint32_t AlignCompareLength(uint32_t currentNum)
{
    constexpr uint32_t compareAlignBytes = 256U;
    constexpr uint32_t alignElements = compareAlignBytes / sizeof(ComputeT);
    return ((currentNum + alignElements - 1U) / alignElements) * alignElements;
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::Init(
    GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData, TPipe* pipe)
{
    pipe_ = pipe;
    int64_t blockIdx = GetBlockIdx();
    blockOffset = blockIdx * tilingData->formerLength;
    if (blockIdx < tilingData->formerNum) {
        blockLength = tilingData->formerLength;
    } else if (blockIdx < tilingData->usedCoreNum) {
        blockLength = tilingData->tailLength;
    } else {
        blockLength = 0;
    }
    ubLength = tilingData->tileLength;
    channelSize = tilingData->channelSize > 0 ? tilingData->channelSize : 1;
    innerSize = tilingData->innerSize > 0 ? tilingData->innerSize : 1;

    inputGMX.SetGlobalBuffer((__gm__ T*)x + blockOffset, blockLength);
    inputGMWeight.SetGlobalBuffer((__gm__ T*)weight, tilingData->weightSize);
    outputGMY.SetGlobalBuffer((__gm__ T*)y + blockOffset, blockLength);

    if constexpr (std::is_same_v<T, bfloat16_t>) {
        T scalarWeight = *((__gm__ T*)weight);
        weightValFp32 = ToFloat(scalarWeight);
    } else {
        T scalarWeight = *((__gm__ T*)weight);
        weightVal = scalarWeight;
    }

    pipe_->InitBuffer(inputQueueX, BUFFER_NUM, ubLength * sizeof(T));
    pipe_->InitBuffer(outputQueueY, BUFFER_NUM, ubLength * sizeof(T));
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        pipe_->InitBuffer(tmpXFp32, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufWeight, ubLength * sizeof(float));
        pipe_->InitBuffer(tmpBufProd, ubLength * sizeof(float));
    } else {
        pipe_->InitBuffer(tmpBufWeight, ubLength * sizeof(T));
        pipe_->InitBuffer(tmpBufProd, ubLength * sizeof(T));
    }
    pipe_->InitBuffer(tmpBufMask, ubLength * sizeof(uint8_t));
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::CopyIn(int64_t progress, uint32_t currentNum)
{
    LocalTensor<T> xLocal = inputQueueX.AllocTensor<T>();
    CopyGmToLocalPad(xLocal, inputGMX[progress * ubLength], currentNum);
    inputQueueX.EnQue(xLocal);
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::CopyOut(int64_t progress, uint32_t currentNum)
{
    LocalTensor<T> yLocal = outputQueueY.DeQue<T>();
    CopyLocalToGmPad(outputGMY[progress * ubLength], yLocal, currentNum);
    outputQueueY.FreeTensor(yLocal);
}

template <typename T, uint32_t schMode>
__aicore__ inline T Prelu<T, schMode>::LoadWeight(int64_t weightOffset)
{
    return inputGMWeight.GetValue(weightOffset);
}

template <typename T, uint32_t schMode>
__aicore__ inline float Prelu<T, schMode>::LoadWeightFp32(int64_t weightOffset)
{
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        return ToFloat(inputGMWeight.GetValue(weightOffset));
    } else {
        return static_cast<float>(inputGMWeight.GetValue(weightOffset));
    }
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::FillChannelWeight(
    LocalTensor<T>& dst, int64_t progress, uint32_t currentNum)
{
    uint32_t localOffset = 0;
    while (localOffset < currentNum) {
        int64_t globalOffset = blockOffset + progress * ubLength + localOffset;
        int64_t offsetInChannel = globalOffset % innerSize;
        int64_t remainInChannel = innerSize - offsetInChannel;
        int64_t remainInTile = static_cast<int64_t>(currentNum) - static_cast<int64_t>(localOffset);
        uint32_t segmentLength = static_cast<uint32_t>(
            remainInChannel < remainInTile ? remainInChannel : remainInTile);
        int64_t weightOffset = (globalOffset / innerSize) % channelSize;
        T weight = LoadWeight(weightOffset);
        for (uint32_t i = 0; i < segmentLength; ++i) {
            dst.SetValue(localOffset + i, weight);
        }
        localOffset += segmentLength;
    }
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::FillChannelWeightFp32(
    LocalTensor<float>& dst, int64_t progress, uint32_t currentNum)
{
    uint32_t localOffset = 0;
    while (localOffset < currentNum) {
        int64_t globalOffset = blockOffset + progress * ubLength + localOffset;
        int64_t offsetInChannel = globalOffset % innerSize;
        int64_t remainInChannel = innerSize - offsetInChannel;
        int64_t remainInTile = static_cast<int64_t>(currentNum) - static_cast<int64_t>(localOffset);
        uint32_t segmentLength = static_cast<uint32_t>(
            remainInChannel < remainInTile ? remainInChannel : remainInTile);
        int64_t weightOffset = (globalOffset / innerSize) % channelSize;
        float weight = LoadWeightFp32(weightOffset);
        for (uint32_t i = 0; i < segmentLength; ++i) {
            dst.SetValue(localOffset + i, weight);
        }
        localOffset += segmentLength;
    }
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::ComputeScalar(uint32_t currentNum, LocalTensor<T>& xLocal, LocalTensor<T>& yLocal)
{
    if constexpr (std::is_same_v<T, bfloat16_t>) {
        uint32_t compareLength = AlignCompareLength<float>(currentNum);
        LocalTensor<float> xFp32 = tmpXFp32.Get<float>();
        LocalTensor<float> prod = tmpBufProd.Get<float>();
        LocalTensor<uint8_t> mask = tmpBufMask.Get<uint8_t>();
        Cast(xFp32, xLocal, RoundMode::CAST_NONE, currentNum);
        Muls(prod, xFp32, weightValFp32, compareLength);
        CompareScalar(mask, xFp32, 0.0f, CMPMODE::GT, compareLength);
        Select(xFp32, mask, xFp32, prod, SELMODE::VSEL_TENSOR_TENSOR_MODE, compareLength);
        Cast(yLocal, xFp32, RoundMode::CAST_RINT, currentNum);
    } else {
        uint32_t compareLength = AlignCompareLength<T>(currentNum);
        LocalTensor<T> prod = tmpBufProd.Get<T>();
        LocalTensor<uint8_t> mask = tmpBufMask.Get<uint8_t>();
        Muls(prod, xLocal, weightVal, compareLength);
        CompareScalar(mask, xLocal, static_cast<T>(0), CMPMODE::GT, compareLength);
        Select(yLocal, mask, xLocal, prod, SELMODE::VSEL_TENSOR_TENSOR_MODE, compareLength);
    }
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::ComputeChannelScalar(
    int64_t progress, uint32_t currentNum, LocalTensor<T>& xLocal, LocalTensor<T>& yLocal)
{
    for (uint32_t i = 0; i < currentNum; ++i) {
        int64_t globalOffset = blockOffset + progress * ubLength + i;
        int64_t weightOffset = (globalOffset / innerSize) % channelSize;
        if constexpr (std::is_same_v<T, bfloat16_t>) {
            float xVal = ToFloat(xLocal.GetValue(i));
            float weight = LoadWeightFp32(weightOffset);
            float yVal = xVal > 0.0f ? xVal : xVal * weight;
            yLocal.SetValue(i, ToBfloat16(yVal));
        } else {
            float xVal = static_cast<float>(xLocal.GetValue(i));
            float weight = static_cast<float>(LoadWeight(weightOffset));
            float yVal = xVal > 0.0f ? xVal : xVal * weight;
            yLocal.SetValue(i, static_cast<T>(yVal));
        }
    }
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::ComputeChannel(
    int64_t progress, uint32_t currentNum, LocalTensor<T>& xLocal, LocalTensor<T>& yLocal)
{
    if (innerSize <= SMALL_CHANNEL_SCALAR_INNER && channelSize <= SMALL_CHANNEL_SCALAR_CHANNEL &&
        currentNum <= SMALL_CHANNEL_SCALAR_NUM) {
        ComputeChannelScalar(progress, currentNum, xLocal, yLocal);
        return;
    }

    if constexpr (std::is_same_v<T, bfloat16_t>) {
        LocalTensor<float> xFp32 = tmpXFp32.Get<float>();
        LocalTensor<float> weightFp32 = tmpBufWeight.Get<float>();
        LocalTensor<float> prod = tmpBufProd.Get<float>();
        LocalTensor<uint8_t> mask = tmpBufMask.Get<uint8_t>();
        if (innerSize == 1) {
            uint32_t compareLength = AlignCompareLength<float>(currentNum);
            Cast(xFp32, xLocal, RoundMode::CAST_NONE, currentNum);
            FillChannelWeightFp32(weightFp32, progress, currentNum);
            Mul(prod, xFp32, weightFp32, compareLength);
            CompareScalar(mask, xFp32, 0.0f, CMPMODE::GT, compareLength);
            Select(xFp32, mask, xFp32, prod, SELMODE::VSEL_TENSOR_TENSOR_MODE, compareLength);
            Cast(yLocal, xFp32, RoundMode::CAST_RINT, currentNum);
        } else {
            uint32_t localOffset = 0;
            while (localOffset < currentNum) {
                int64_t globalOffset = blockOffset + progress * ubLength + localOffset;
                int64_t offsetInChannel = globalOffset % innerSize;
                int64_t remainInChannel = innerSize - offsetInChannel;
                int64_t remainInTile = static_cast<int64_t>(currentNum) - static_cast<int64_t>(localOffset);
                uint32_t segmentLength = static_cast<uint32_t>(
                    remainInChannel < remainInTile ? remainInChannel : remainInTile);
                int64_t weightOffset = (globalOffset / innerSize) % channelSize;
                float weight = LoadWeightFp32(weightOffset);
                uint32_t compareLength = AlignCompareLength<float>(segmentLength);
                Cast(xFp32, xLocal[localOffset], RoundMode::CAST_NONE, segmentLength);
                Muls(prod, xFp32, weight, compareLength);
                CompareScalar(mask, xFp32, 0.0f, CMPMODE::GT, compareLength);
                Select(prod, mask, xFp32, prod, SELMODE::VSEL_TENSOR_TENSOR_MODE, compareLength);
                Cast(yLocal[localOffset], prod, RoundMode::CAST_RINT, segmentLength);
                localOffset += segmentLength;
            }
        }
    } else {
        LocalTensor<T> tmp = tmpBufWeight.Get<T>();
        LocalTensor<T> prod = tmpBufProd.Get<T>();
        LocalTensor<uint8_t> mask = tmpBufMask.Get<uint8_t>();
        if (innerSize == 1) {
            uint32_t compareLength = AlignCompareLength<T>(currentNum);
            FillChannelWeight(tmp, progress, currentNum);
            Mul(prod, xLocal, tmp, compareLength);
            CompareScalar(mask, xLocal, static_cast<T>(0), CMPMODE::GT, compareLength);
            Select(yLocal, mask, xLocal, prod, SELMODE::VSEL_TENSOR_TENSOR_MODE, compareLength);
        } else {
            uint32_t localOffset = 0;
            while (localOffset < currentNum) {
                int64_t globalOffset = blockOffset + progress * ubLength + localOffset;
                int64_t offsetInChannel = globalOffset % innerSize;
                int64_t remainInChannel = innerSize - offsetInChannel;
                int64_t remainInTile = static_cast<int64_t>(currentNum) - static_cast<int64_t>(localOffset);
                uint32_t segmentLength = static_cast<uint32_t>(
                    remainInChannel < remainInTile ? remainInChannel : remainInTile);
                int64_t weightOffset = (globalOffset / innerSize) % channelSize;
                T weight = LoadWeight(weightOffset);
                uint32_t compareLength = AlignCompareLength<T>(segmentLength);
                Adds(tmp, xLocal[localOffset], static_cast<T>(0), segmentLength);
                Muls(prod, tmp, weight, compareLength);
                CompareScalar(mask, tmp, static_cast<T>(0), CMPMODE::GT, compareLength);
                Select(prod, mask, tmp, prod, SELMODE::VSEL_TENSOR_TENSOR_MODE, compareLength);
                Adds(yLocal[localOffset], prod, static_cast<T>(0), segmentLength);
                localOffset += segmentLength;
            }
        }
    }
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::Compute(int64_t progress, uint32_t currentNum)
{
    LocalTensor<T> xLocal = inputQueueX.DeQue<T>();
    LocalTensor<T> yLocal = outputQueueY.AllocTensor<T>();

    if constexpr (schMode == PRELU_TPL_SCH_MODE_CHANNEL) {
        ComputeChannel(progress, currentNum, xLocal, yLocal);
    } else {
        ComputeScalar(currentNum, xLocal, yLocal);
    }

    outputQueueY.EnQue<T>(yLocal);
    inputQueueX.FreeTensor(xLocal);
}

template <typename T, uint32_t schMode>
__aicore__ inline void Prelu<T, schMode>::Process()
{
    int64_t tileNum = (blockLength + ubLength - 1) / ubLength;
    for (int64_t i = 0; i < tileNum; ++i) {
        uint32_t currentNum = static_cast<uint32_t>((i == tileNum - 1) ? (blockLength - i * ubLength) : ubLength);
        CopyIn(i, currentNum);
        Compute(i, currentNum);
        CopyOut(i, currentNum);
    }
}

} // namespace NsPrelu
#endif // PRELU_H
