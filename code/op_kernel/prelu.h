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

namespace NsPrelu {

using namespace AscendC;

constexpr int32_t BUFFER_NUM = 2;

template <typename T>
class Prelu {
public:
    __aicore__ inline Prelu(){};

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData);
    __aicore__ inline void Process();

private:
    __aicore__ inline void CopyIn(int64_t progress, int64_t currentNum);
    __aicore__ inline void CopyOut(int64_t progress, int64_t currentNum);
    __aicore__ inline void Compute(int64_t progress, int64_t currentNum);
    __aicore__ inline float GetAlpha(int64_t globalOffset);
    __aicore__ inline void ComputeSegment(AscendC::LocalTensor<float> yFp32,
                                          AscendC::LocalTensor<float> xFp32,
                                          int64_t localOffset, int64_t currentNum, float alpha);

private:
    TPipe pipe;
    TQue<QuePosition::VECIN, BUFFER_NUM> inputQueueX;
    TQue<QuePosition::VECIN, 1> inputQueueWeight;
    TQue<QuePosition::VECOUT, BUFFER_NUM> outputQueueY;
    TBuf<TPosition::VECCALC> xFp32Buf;
    TBuf<TPosition::VECCALC> posBuf;
    TBuf<TPosition::VECCALC> negBuf;

    GlobalTensor<T> inputGMX;
    GlobalTensor<T> weightGM;
    GlobalTensor<T> outputGMY;

    int64_t blockOffset_ = 0;
    int64_t blockLength_ = 0;
    int64_t ubLength_ = 0;
    int64_t weightMode_ = 0;
    int64_t channelSize_ = 1;
    int64_t innerSize_ = 1;
};

template <typename T>
__aicore__ inline void Prelu<T>::Init(GM_ADDR x, GM_ADDR weight, GM_ADDR y, const PreluTilingData* tilingData)
{
    int64_t blockIdx = AscendC::GetBlockIdx();
    int64_t remainLength = tilingData->totalNum - tilingData->blockFactor * blockIdx;
    blockLength_ = remainLength > tilingData->blockFactor ? tilingData->blockFactor : remainLength;
    blockLength_ = blockLength_ > 0 ? blockLength_ : 0;
    blockOffset_ = tilingData->blockFactor * blockIdx;
    ubLength_ = tilingData->ubFactor;
    weightMode_ = tilingData->weightMode;
    channelSize_ = tilingData->channelSize;
    innerSize_ = tilingData->innerSize;

    inputGMX.SetGlobalBuffer((__gm__ T*)x + blockOffset_, blockLength_);
    weightGM.SetGlobalBuffer((__gm__ T*)weight);
    outputGMY.SetGlobalBuffer((__gm__ T*)y + blockOffset_, blockLength_);

    pipe.InitBuffer(inputQueueX, BUFFER_NUM, ubLength_ * sizeof(T));
    pipe.InitBuffer(inputQueueWeight, 1, 32);
    pipe.InitBuffer(outputQueueY, BUFFER_NUM, ubLength_ * sizeof(T));
    pipe.InitBuffer(xFp32Buf, ubLength_ * sizeof(float));
    pipe.InitBuffer(posBuf, ubLength_ * sizeof(float));
    pipe.InitBuffer(negBuf, ubLength_ * sizeof(float));
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyIn(int64_t progress, int64_t currentNum)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.template AllocTensor<T>();
    AscendC::DataCopyParams copyParams;
    copyParams.blockCount = 1;
    copyParams.blockLen = currentNum * sizeof(T);
    copyParams.srcStride = 0;
    copyParams.dstStride = 0;
    AscendC::DataCopyPad(xLocal, inputGMX[progress * ubLength_], copyParams, {false, 0, 0, 0});
    inputQueueX.EnQue(xLocal);
}

template <typename T>
__aicore__ inline float Prelu<T>::GetAlpha(int64_t globalOffset)
{
    int64_t weightOffset = 0;
    if (weightMode_ == 1) {
        weightOffset = (globalOffset / innerSize_) % channelSize_;
    }

    AscendC::LocalTensor<T> weightLocal = inputQueueWeight.template AllocTensor<T>();
    AscendC::DataCopyParams copyParams;
    copyParams.blockCount = 1;
    copyParams.blockLen = sizeof(T);
    copyParams.srcStride = 0;
    copyParams.dstStride = 0;
    AscendC::DataCopyPad(weightLocal, weightGM[weightOffset], copyParams, {false, 0, 0, 0});
    inputQueueWeight.EnQue(weightLocal);
    weightLocal = inputQueueWeight.template DeQue<T>();
    float alpha = static_cast<float>(weightLocal.GetValue(0));
    inputQueueWeight.FreeTensor(weightLocal);
    return alpha;
}

template <typename T>
__aicore__ inline void Prelu<T>::ComputeSegment(AscendC::LocalTensor<float> yFp32,
                                                AscendC::LocalTensor<float> xFp32,
                                                int64_t localOffset, int64_t currentNum, float alpha)
{
    AscendC::LocalTensor<float> posLocal = posBuf.Get<float>();
    AscendC::LocalTensor<float> negLocal = negBuf.Get<float>();
    AscendC::Maxs(posLocal[localOffset], xFp32[localOffset], 0.0f, currentNum);
    AscendC::Mins(negLocal[localOffset], xFp32[localOffset], 0.0f, currentNum);
    AscendC::Muls(negLocal[localOffset], negLocal[localOffset], alpha, currentNum);
    AscendC::Add(yFp32[localOffset], posLocal[localOffset], negLocal[localOffset], currentNum);
}

template <typename T>
__aicore__ inline void Prelu<T>::Compute(int64_t progress, int64_t currentNum)
{
    AscendC::LocalTensor<T> xLocal = inputQueueX.template DeQue<T>();
    AscendC::LocalTensor<T> yLocal = outputQueueY.template AllocTensor<T>();

    if constexpr (sizeof(T) == sizeof(float)) {
        AscendC::LocalTensor<float> xFp32 = xLocal.template ReinterpretCast<float>();
        AscendC::LocalTensor<float> yFp32 = yLocal.template ReinterpretCast<float>();
        int64_t localOffset = 0;
        while (localOffset < currentNum) {
            int64_t globalOffset = blockOffset_ + progress * ubLength_ + localOffset;
            int64_t segmentLength = currentNum - localOffset;
            if (weightMode_ == 1) {
                int64_t offsetInChannel = globalOffset % innerSize_;
                int64_t channelRemain = innerSize_ - offsetInChannel;
                segmentLength = segmentLength < channelRemain ? segmentLength : channelRemain;
            }
            float alpha = GetAlpha(globalOffset);
            ComputeSegment(yFp32, xFp32, localOffset, segmentLength, alpha);
            localOffset += segmentLength;
        }
    } else {
        AscendC::LocalTensor<float> xFp32 = xFp32Buf.Get<float>();
        AscendC::Cast(xFp32, xLocal, AscendC::RoundMode::CAST_NONE, currentNum);
        int64_t localOffset = 0;
        while (localOffset < currentNum) {
            int64_t globalOffset = blockOffset_ + progress * ubLength_ + localOffset;
            int64_t segmentLength = currentNum - localOffset;
            if (weightMode_ == 1) {
                int64_t offsetInChannel = globalOffset % innerSize_;
                int64_t channelRemain = innerSize_ - offsetInChannel;
                segmentLength = segmentLength < channelRemain ? segmentLength : channelRemain;
            }
            float alpha = GetAlpha(globalOffset);
            ComputeSegment(xFp32, xFp32, localOffset, segmentLength, alpha);
            localOffset += segmentLength;
        }
        AscendC::Cast(yLocal, xFp32, AscendC::RoundMode::CAST_ROUND, currentNum);
    }

    outputQueueY.template EnQue<T>(yLocal);
    inputQueueX.FreeTensor(xLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::CopyOut(int64_t progress, int64_t currentNum)
{
    AscendC::LocalTensor<T> yLocal = outputQueueY.template DeQue<T>();
    AscendC::DataCopyParams copyParams;
    copyParams.blockCount = 1;
    copyParams.blockLen = currentNum * sizeof(T);
    copyParams.srcStride = 0;
    copyParams.dstStride = 0;
    AscendC::DataCopyPad(outputGMY[progress * ubLength_], yLocal, copyParams);
    outputQueueY.FreeTensor(yLocal);
}

template <typename T>
__aicore__ inline void Prelu<T>::Process()
{
    int64_t loopCount = (blockLength_ + ubLength_ - 1) / ubLength_;
    for (int64_t i = 0; i < loopCount; ++i) {
        int64_t currentNum = (i == loopCount - 1) ? (blockLength_ - ubLength_ * i) : ubLength_;
        CopyIn(i, currentNum);
        Compute(i, currentNum);
        CopyOut(i, currentNum);
    }
}

} // namespace NsPrelu
#endif // PRELU_H
