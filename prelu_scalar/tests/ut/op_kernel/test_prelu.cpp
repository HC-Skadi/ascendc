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
    constexpr size_t weightByteSize = sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost = {-3.0f, -1.0f, 0.0f, 1.0f, 2.0f, -4.0f, 5.0f};
    std::vector<float> weightHost = {0.25f};
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
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = size;
    tilingData->tailNum = 1;
    tilingData->tailLength = size;
    tilingData->tileLength = size;
    
    ICPU_SET_TILING_KEY(0);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);
    
    ICPU_RUN_KF((prelu<0>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    std::vector<float> expected = {-0.75f, -0.25f, 0.0f, 1.0f, 2.0f, -1.0f, 5.0f};
    for (size_t i = 0; i < size; ++i) {
        EXPECT_NEAR(yHost[i], expected[i], 1e-6f);
    }
    
    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}
