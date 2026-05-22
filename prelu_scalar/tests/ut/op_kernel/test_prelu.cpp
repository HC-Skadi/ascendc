/*!
 * \file test_prelu.cpp
 * \brief Prelu 算子 kernel UT 测试
 * 
 * 独立运行，直接构造 tilingData，不依赖 op_host UT
 */

#include "prelu_tiling.h"
#include "../../../op_kernel/prelu.cpp"

#include <array>
#include <vector>
#include <iostream>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include "gtest/gtest.h"
#include "tikicpulib.h"

using namespace std;

class PreluKernelTest : public testing::Test {
protected:
    static void SetUpTestCase()
    {
        cout << "PreluKernelTest SetUp" << endl;
    }
    static void TearDownTestCase()
    {
        cout << "PreluKernelTest TearDown" << endl;
    }
};

TEST_F(PreluKernelTest, test_kernel_run)
{
    constexpr size_t size = 7;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 1;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = size * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size, 1);
    std::vector<float> weightHost(size, 1);
    std::vector<float> yHost(size, 0.0f);
    
    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    
    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);
    
    // 直接构造 tilingData（固定值，生成时确定）
    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalNum = size;
    tilingData->blockFactor = size;
    tilingData->ubFactor = size;
    
    ICPU_SET_TILING_KEY(0);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);
    
    ICPU_RUN_KF((prelu<0>), numBlocks, x, weight, y, workspace, tiling);
    
    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}
