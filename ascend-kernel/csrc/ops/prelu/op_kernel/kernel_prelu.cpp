// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "kernel_operator.h"

constexpr int32_t BUFFER_NUM = 2;

template <typename T>
class KernelPrelu {
public:
    __aicore__ inline KernelPrelu() {}

    __aicore__ inline void Init(GM_ADDR x, GM_ADDR weight, GM_ADDR y,
                                int64_t formerNum, int64_t formerLength, int64_t tailLength,
                                int64_t tileLength, int64_t weightMode,
                                int64_t channelSize, int64_t innerSize)
    {
        int64_t blockIdx = AscendC::GetBlockIdx();
        if (blockIdx < formerNum) {
            blockLength = formerLength;
            blockOffset = formerLength * blockIdx;
        } else {
            blockLength = tailLength;
            blockOffset = formerLength * formerNum;
        }

        this->tileLength = tileLength;
        this->weightMode = weightMode;
        this->channelSize = channelSize;
        this->innerSize = innerSize;

        xGm.SetGlobalBuffer((__gm__ T *)x + blockOffset, blockLength);
        yGm.SetGlobalBuffer((__gm__ T *)y + blockOffset, blockLength);
        weightGm.SetGlobalBuffer((__gm__ T *)weight);

        pipe.InitBuffer(inQueueX, BUFFER_NUM, tileLength * sizeof(T));
        pipe.InitBuffer(outQueueY, BUFFER_NUM, tileLength * sizeof(T));
        pipe.InitBuffer(weightQueue, 1, 32);
        pipe.InitBuffer(xFp32Buf, tileLength * sizeof(float));
        pipe.InitBuffer(posBuf, tileLength * sizeof(float));
        pipe.InitBuffer(negBuf, tileLength * sizeof(float));
    }

    __aicore__ inline void Process()
    {
        int64_t tileNum = (blockLength + tileLength - 1) / tileLength;
        for (int64_t i = 0; i < tileNum; ++i) {
            int64_t curTileLength = tileLength;
            if (i == tileNum - 1) {
                curTileLength = blockLength - i * tileLength;
            }
            CopyIn(i, curTileLength);
            Compute(i, curTileLength);
            CopyOut(i, curTileLength);
        }
    }

private:
    __aicore__ inline void CopyIn(int64_t progress, int64_t curTileLength)
    {
        AscendC::LocalTensor<T> xLocal = inQueueX.AllocTensor<T>();
        AscendC::DataCopyExtParams copyParams{
            1, static_cast<uint32_t>(curTileLength * sizeof(T)), 0, 0, 0};
        AscendC::DataCopyPadExtParams<T> padParams{false, 0, 0, static_cast<T>(0)};
        AscendC::DataCopyPad(xLocal, xGm[progress * tileLength], copyParams, padParams);
        inQueueX.EnQue(xLocal);
    }

    __aicore__ inline float GetAlpha(int64_t globalOffset)
    {
        int64_t weightOffset = 0;
        if (weightMode == 1) {
            weightOffset = (globalOffset / innerSize) % channelSize;
        }
        AscendC::LocalTensor<T> weightLocal = weightQueue.AllocTensor<T>();
        AscendC::DataCopyExtParams copyParams{1, static_cast<uint32_t>(sizeof(T)), 0, 0, 0};
        AscendC::DataCopyPadExtParams<T> padParams{false, 0, 0, static_cast<T>(0)};
        AscendC::DataCopyPad(weightLocal, weightGm[weightOffset], copyParams, padParams);
        weightQueue.EnQue(weightLocal);
        weightLocal = weightQueue.DeQue<T>();
        float alpha = static_cast<float>(weightLocal.GetValue(0));
        weightQueue.FreeTensor(weightLocal);
        return alpha;
    }

    __aicore__ inline void ComputeSegmentFp32(AscendC::LocalTensor<float> yFp32,
                                              AscendC::LocalTensor<float> xFp32,
                                              int64_t localOffset, int64_t len,
                                              float alpha)
    {
        AscendC::LocalTensor<float> posLocal = posBuf.Get<float>();
        AscendC::LocalTensor<float> negLocal = negBuf.Get<float>();
        AscendC::Maxs(posLocal[localOffset], xFp32[localOffset], 0.0f, len);
        AscendC::Mins(negLocal[localOffset], xFp32[localOffset], 0.0f, len);
        AscendC::Muls(negLocal[localOffset], negLocal[localOffset], alpha, len);
        AscendC::Add(yFp32[localOffset], posLocal[localOffset], negLocal[localOffset], len);
    }

    __aicore__ inline void ComputeFp32Tile(AscendC::LocalTensor<float> yFp32,
                                           AscendC::LocalTensor<float> xFp32,
                                           int64_t progress, int64_t curTileLength)
    {
        int64_t localOffset = 0;
        while (localOffset < curTileLength) {
            int64_t globalOffset = blockOffset + progress * tileLength + localOffset;
            int64_t segmentLength = curTileLength - localOffset;
            if (weightMode == 1) {
                int64_t offsetInChannel = globalOffset % innerSize;
                int64_t channelRemain = innerSize - offsetInChannel;
                segmentLength = segmentLength < channelRemain ? segmentLength : channelRemain;
            }
            float alpha = GetAlpha(globalOffset);
            ComputeSegmentFp32(yFp32, xFp32, localOffset, segmentLength, alpha);
            localOffset += segmentLength;
        }
    }

    __aicore__ inline void Compute(int64_t progress, int64_t curTileLength)
    {
        AscendC::LocalTensor<T> xLocal = inQueueX.DeQue<T>();
        AscendC::LocalTensor<T> yLocal = outQueueY.AllocTensor<T>();

        if constexpr (sizeof(T) == sizeof(float)) {
            AscendC::LocalTensor<float> xFp32 = xLocal.template ReinterpretCast<float>();
            AscendC::LocalTensor<float> yFp32 = yLocal.template ReinterpretCast<float>();
            ComputeFp32Tile(yFp32, xFp32, progress, curTileLength);
        } else {
            AscendC::LocalTensor<float> xFp32 = xFp32Buf.Get<float>();
            AscendC::Cast(xFp32, xLocal, AscendC::RoundMode::CAST_NONE, curTileLength);
            ComputeFp32Tile(xFp32, xFp32, progress, curTileLength);
            AscendC::Cast(yLocal, xFp32, AscendC::RoundMode::CAST_ROUND, curTileLength);
        }

        outQueueY.EnQue<T>(yLocal);
        inQueueX.FreeTensor(xLocal);
    }

    __aicore__ inline void CopyOut(int64_t progress, int64_t curTileLength)
    {
        AscendC::LocalTensor<T> yLocal = outQueueY.DeQue<T>();
        AscendC::DataCopyExtParams copyParams{
            1, static_cast<uint32_t>(curTileLength * sizeof(T)), 0, 0, 0};
        AscendC::DataCopyPad(yGm[progress * tileLength], yLocal, copyParams);
        outQueueY.FreeTensor(yLocal);
    }

private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::TPosition::VECIN, BUFFER_NUM> inQueueX;
    AscendC::TQue<AscendC::TPosition::VECOUT, BUFFER_NUM> outQueueY;
    AscendC::TQue<AscendC::TPosition::VECIN, 1> weightQueue;
    AscendC::TBuf<AscendC::TPosition::VECCALC> xFp32Buf;
    AscendC::TBuf<AscendC::TPosition::VECCALC> posBuf;
    AscendC::TBuf<AscendC::TPosition::VECCALC> negBuf;
    AscendC::GlobalTensor<T> xGm;
    AscendC::GlobalTensor<T> yGm;
    AscendC::GlobalTensor<T> weightGm;
    int64_t blockLength = 0;
    int64_t blockOffset = 0;
    int64_t tileLength = 0;
    int64_t weightMode = 0;
    int64_t channelSize = 1;
    int64_t innerSize = 1;
};

extern "C" __global__ __aicore__ void prelu(GM_ADDR x, GM_ADDR weight, GM_ADDR y,
                                            int64_t formerNum, int64_t formerLength,
                                            int64_t tailLength, int64_t tileLength,
                                            int64_t dtypeCode, int64_t weightMode,
                                            int64_t channelSize, int64_t innerSize)
{
    if (dtypeCode == 1) {
        KernelPrelu<float> op;
        op.Init(x, weight, y, formerNum, formerLength, tailLength, tileLength,
                weightMode, channelSize, innerSize);
        op.Process();
    } else if (dtypeCode == 2) {
        KernelPrelu<bfloat16_t> op;
        op.Init(x, weight, y, formerNum, formerLength, tailLength, tileLength,
                weightMode, channelSize, innerSize);
        op.Process();
    } else {
        KernelPrelu<half> op;
        op.Init(x, weight, y, formerNum, formerLength, tailLength, tileLength,
                weightMode, channelSize, innerSize);
        op.Process();
    }
}
