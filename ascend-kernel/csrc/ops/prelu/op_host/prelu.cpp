// Licensed under the BSD 3-Clause License  (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "torch_kernel_helper.h"
#include "tiling/platform/platform_ascendc.h"
#include "aclrtlaunch_prelu.h"

namespace ascend_kernel {
namespace {
constexpr int64_t CACHE_LINE_BYTE_LENGTH = 512;
constexpr int64_t UB_ALIGN_BYTES = 32;

int64_t CeilDiv(int64_t x, int64_t y)
{
    return (x + y - 1) / y;
}

int64_t AlignUp(int64_t x, int64_t align)
{
    return CeilDiv(x, align) * align;
}
}  // namespace

at::Tensor prelu(const at::Tensor &self, const at::Tensor &weight)
{
    TORCH_CHECK(self.device().type() == DEVICE_TYPE, "prelu: self must be an NPU tensor");
    TORCH_CHECK(weight.device().type() == DEVICE_TYPE, "prelu: weight must be an NPU tensor");
    TORCH_CHECK(self.scalar_type() == weight.scalar_type(),
                "prelu: self and weight must have the same dtype, got ", self.scalar_type(),
                " and ", weight.scalar_type());
    TORCH_CHECK(self.scalar_type() == at::kHalf || self.scalar_type() == at::kFloat ||
                    self.scalar_type() == at::kBFloat16,
                "prelu: only float16, bfloat16 and float32 are supported, got ",
                self.scalar_type());
    TORCH_CHECK(weight.dim() <= 1, "prelu: weight must be a scalar or 1-D tensor");
    TORCH_CHECK(weight.numel() == 1 || (self.dim() >= 2 && weight.numel() == self.size(1)),
                "prelu: weight.numel() must be 1 or match self.size(1) for inputs with dim >= 2");

    at::Tensor selfContiguous = self.contiguous();
    at::Tensor weightContiguous = weight.contiguous();
    at::Tensor output = at::empty_like(selfContiguous);

    int64_t totalLength = selfContiguous.numel();
    if (totalLength == 0) {
        return output.reshape(self.sizes());
    }

    int64_t dtypeSize = selfContiguous.element_size();
    int64_t dtypeCode = 0;  // 0=half, 1=float, 2=bfloat16
    if (selfContiguous.scalar_type() == at::kFloat) {
        dtypeCode = 1;
    } else if (selfContiguous.scalar_type() == at::kBFloat16) {
        dtypeCode = 2;
    }

    int64_t weightMode = weightContiguous.numel() == 1 ? 0 : 1;
    int64_t channelSize = selfContiguous.dim() >= 2 ? selfContiguous.size(1) : 1;
    int64_t innerSize = 1;
    if (selfContiguous.dim() >= 2) {
        for (int64_t i = 2; i < selfContiguous.dim(); ++i) {
            innerSize *= selfContiguous.size(i);
        }
    } else {
        innerSize = totalLength;
    }

    auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();
    int64_t coreNum = static_cast<int64_t>(ascendcPlatform->GetCoreNumAiv());
    uint64_t ubSize = 0;
    ascendcPlatform->GetCoreMemSize(platform_ascendc::CoreMemType::UB, ubSize);
    int64_t ubSizeLimit = static_cast<int64_t>(ubSize);

    int64_t cacheLineElements = CACHE_LINE_BYTE_LENGTH / dtypeSize;
    int64_t totalLengthCore = CeilDiv(totalLength, coreNum);
    int64_t totalLengthCoreAlign = AlignUp(totalLengthCore, cacheLineElements);
    int64_t usedCoreNum = CeilDiv(totalLength, totalLengthCoreAlign);
    int64_t formerNum = usedCoreNum - 1;
    int64_t formerLength = totalLengthCoreAlign;
    int64_t tailLength = totalLength - formerNum * formerLength;

    int64_t bufferCoefficient = dtypeSize == 2 ? 24 : 28;
    int64_t maxTileElements = ubSizeLimit / bufferCoefficient;
    int64_t alignElements = UB_ALIGN_BYTES / dtypeSize;
    int64_t tileLength = (maxTileElements / alignElements) * alignElements;
    TORCH_CHECK(tileLength > 0, "prelu: calculated tileLength must be positive");

    uint32_t blockDim = static_cast<uint32_t>(usedCoreNum);
    EXEC_KERNEL_CMD(prelu, blockDim,
                    selfContiguous, weightContiguous, output,
                    formerNum, formerLength, tailLength, tileLength,
                    dtypeCode, weightMode, channelSize, innerSize);

    return output.reshape(self.sizes());
}

}  // namespace ascend_kernel
