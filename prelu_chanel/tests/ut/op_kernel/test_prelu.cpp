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
    memset(tiling, 0, tilingDataSize);
    
    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);
    
    // 直接构造 tilingData（固定值，生成时确定）
    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = size;
    tilingData->tailLength = size;
    tilingData->tileLength = size;
    tilingData->channelSize = 1;
    tilingData->innerSize = 1;
    tilingData->innerSizeAligned = 1;
    tilingData->baseRows = 0;
    tilingData->extraRows = 0;
    
    ICPU_SET_TILING_KEY(PRELU_TPL_SCALAR_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);
    
    ICPU_RUN_KF((prelu<PRELU_TPL_SCALAR_MODE>), numBlocks, x, weight, y, workspace, tiling);

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

TEST_F(PreluKernelTest, test_channel_weight_run)
{
    constexpr size_t n = 2;
    constexpr size_t c = 3;
    constexpr size_t l = 5;
    constexpr size_t size = n * c * l;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 1;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = c * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size);
    for (size_t i = 0; i < size; ++i) {
        xHost[i] = static_cast<float>(static_cast<int>(i % 7) - 3);
    }
    std::vector<float> weightHost = {0.1f, 0.2f, 0.3f};
    std::vector<float> yHost(size, 0.0f);

    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    memset(tiling, 0, tilingDataSize);

    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);

    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = 0;
    tilingData->tailLength = 0;
    tilingData->tileLength = 8;
    tilingData->channelSize = c;
    tilingData->innerSize = l;
    tilingData->innerSizeAligned = 8;
    tilingData->baseRows = n * c;
    tilingData->extraRows = 0;

    ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_FULL_L_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);

    ICPU_RUN_KF((prelu<PRELU_TPL_CHANNEL_FULL_L_MODE>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    for (size_t row = 0; row < n * c; ++row) {
        float weightValue = weightHost[row % c];
        for (size_t i = 0; i < l; ++i) {
            size_t offset = row * l + i;
            float expected = xHost[offset] > 0.0f ? xHost[offset] : xHost[offset] * weightValue;
            EXPECT_NEAR(yHost[offset], expected, 1e-6f);
        }
    }

    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}

TEST_F(PreluKernelTest, test_channel_nc_weight_reuse_run)
{
    constexpr size_t n = 4;
    constexpr size_t c = 3;
    constexpr size_t size = n * c;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 2;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = c * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size);
    for (size_t i = 0; i < size; ++i) {
        xHost[i] = static_cast<float>(static_cast<int>(i % 9) - 4);
    }
    std::vector<float> weightHost = {0.1f, 0.2f, 0.3f};
    std::vector<float> yHost(size, 0.0f);

    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    memset(tiling, 0, tilingDataSize);

    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);

    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = 0;
    tilingData->tailLength = 0;
    tilingData->tileLength = 16;
    tilingData->channelSize = c;
    tilingData->innerSize = 1;
    tilingData->innerSizeAligned = 8;
    tilingData->baseRows = 2;
    tilingData->extraRows = 0;

    ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);

    ICPU_RUN_KF((prelu<PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    for (size_t row = 0; row < n; ++row) {
        for (size_t col = 0; col < c; ++col) {
            size_t offset = row * c + col;
            float weightValue = weightHost[col];
            float expected = xHost[offset] > 0.0f ? xHost[offset] : xHost[offset] * weightValue;
            EXPECT_NEAR(yHost[offset], expected, 1e-6f);
        }
    }

    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}

TEST_F(PreluKernelTest, test_channel_nc_weight_reuse_c33_run)
{
    constexpr size_t n = 2;
    constexpr size_t c = 33;
    constexpr size_t alignedC = 40;
    constexpr size_t size = n * c;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 2;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = c * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size);
    for (size_t i = 0; i < size; ++i) {
        xHost[i] = static_cast<float>(static_cast<int>(i % 17) - 8);
    }
    std::vector<float> weightHost(c);
    for (size_t i = 0; i < c; ++i) {
        weightHost[i] = 0.03f * static_cast<float>(i + 1);
    }
    std::vector<float> yHost(size, 0.0f);

    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    memset(tiling, 0, tilingDataSize);

    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);

    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = 0;
    tilingData->tailLength = 0;
    tilingData->tileLength = alignedC;
    tilingData->channelSize = c;
    tilingData->innerSize = 1;
    tilingData->innerSizeAligned = alignedC;
    tilingData->baseRows = 1;
    tilingData->extraRows = 0;

    ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);

    ICPU_RUN_KF((prelu<PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    for (size_t row = 0; row < n; ++row) {
        for (size_t col = 0; col < c; ++col) {
            size_t offset = row * c + col;
            float expected = xHost[offset] > 0.0f ? xHost[offset] : xHost[offset] * weightHost[col];
            EXPECT_NEAR(yHost[offset], expected, 1e-6f);
        }
    }

    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}

TEST_F(PreluKernelTest, test_channel_small_l_weight_reuse_run)
{
    constexpr size_t n = 3;
    constexpr size_t c = 4;
    constexpr size_t l = 3;
    constexpr size_t rowAlignedSize = 16;
    constexpr size_t size = n * c * l;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 1;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = c * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size);
    for (size_t i = 0; i < size; ++i) {
        xHost[i] = static_cast<float>(static_cast<int>(i % 11) - 5);
    }
    std::vector<float> weightHost = {0.1f, 0.2f, 0.3f, 0.4f};
    std::vector<float> yHost(size, 0.0f);

    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    memset(tiling, 0, tilingDataSize);

    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);

    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = 0;
    tilingData->tailLength = 0;
    tilingData->tileLength = rowAlignedSize * n;
    tilingData->channelSize = c;
    tilingData->innerSize = l;
    tilingData->innerSizeAligned = rowAlignedSize;
    tilingData->baseRows = n;
    tilingData->extraRows = 0;

    ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);

    ICPU_RUN_KF((prelu<PRELU_TPL_CHANNEL_NC_WEIGHT_REUSE_MODE>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    for (size_t row = 0; row < n; ++row) {
        for (size_t col = 0; col < c; ++col) {
            float weightValue = weightHost[col];
            for (size_t inner = 0; inner < l; ++inner) {
                size_t offset = row * c * l + col * l + inner;
                float expected = xHost[offset] > 0.0f ? xHost[offset] : xHost[offset] * weightValue;
                EXPECT_NEAR(yHost[offset], expected, 1e-6f);
            }
        }
    }

    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}

TEST_F(PreluKernelTest, test_channel_weight_split_l_run)
{
    constexpr size_t n = 1;
    constexpr size_t c = 2;
    constexpr size_t l = 20;
    constexpr size_t size = n * c * l;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 1;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = c * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size);
    for (size_t i = 0; i < size; ++i) {
        xHost[i] = static_cast<float>(static_cast<int>(i % 9) - 4);
    }
    std::vector<float> weightHost = {0.1f, 0.4f};
    std::vector<float> yHost(size, 0.0f);

    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    memset(tiling, 0, tilingDataSize);

    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);

    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = 0;
    tilingData->tailLength = 0;
    tilingData->tileLength = 8;
    tilingData->channelSize = c;
    tilingData->innerSize = l;
    tilingData->innerSizeAligned = 24;
    tilingData->baseRows = n * c;
    tilingData->extraRows = 0;

    ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_SPLIT_L_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);

    ICPU_RUN_KF((prelu<PRELU_TPL_CHANNEL_SPLIT_L_MODE>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    for (size_t row = 0; row < n * c; ++row) {
        float weightValue = weightHost[row % c];
        for (size_t i = 0; i < l; ++i) {
            size_t offset = row * l + i;
            float expected = xHost[offset] > 0.0f ? xHost[offset] : xHost[offset] * weightValue;
            EXPECT_NEAR(yHost[offset], expected, 1e-6f);
        }
    }

    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}

TEST_F(PreluKernelTest, test_channel_weight_split_l_parallel_run)
{
    constexpr size_t n = 1;
    constexpr size_t c = 2;
    constexpr size_t l = 20;
    constexpr size_t size = n * c * l;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 4;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = c * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size);
    for (size_t i = 0; i < size; ++i) {
        xHost[i] = static_cast<float>(static_cast<int>(i % 11) - 5);
    }
    std::vector<float> weightHost = {0.25f, 0.5f};
    std::vector<float> yHost(size, 0.0f);

    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    memset(tiling, 0, tilingDataSize);

    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);

    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = 0;
    tilingData->tailLength = 0;
    tilingData->tileLength = 8;
    tilingData->channelSize = c;
    tilingData->innerSize = l;
    tilingData->innerSizeAligned = 24;
    tilingData->tilesPerRow = 3;
    tilingData->baseTasks = 1;
    tilingData->extraTasks = 2;

    ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);

    ICPU_RUN_KF((prelu<PRELU_TPL_CHANNEL_SPLIT_L_PARALLEL_MODE>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    for (size_t row = 0; row < n * c; ++row) {
        float weightValue = weightHost[row % c];
        for (size_t i = 0; i < l; ++i) {
            size_t offset = row * l + i;
            float expected = xHost[offset] > 0.0f ? xHost[offset] : xHost[offset] * weightValue;
            EXPECT_NEAR(yHost[offset], expected, 1e-6f);
        }
    }

    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}

TEST_F(PreluKernelTest, test_channel_nc_split_c_weight_reuse_run)
{
    constexpr size_t n = 2;
    constexpr size_t c = 20;
    constexpr size_t size = n * c;
    constexpr size_t tilingDataSize = sizeof(PreluTilingData);
    constexpr uint32_t numBlocks = 5;

    constexpr size_t xByteSize = size * sizeof(float);
    constexpr size_t weightByteSize = c * sizeof(float);
    constexpr size_t yByteSize = size * sizeof(float);
    std::vector<float> xHost(size);
    for (size_t i = 0; i < size; ++i) {
        xHost[i] = static_cast<float>(static_cast<int>(i % 13) - 6);
    }
    std::vector<float> weightHost(c);
    for (size_t i = 0; i < c; ++i) {
        weightHost[i] = 0.05f * static_cast<float>(i + 1);
    }
    std::vector<float> yHost(size, 0.0f);

    uint8_t* x = (uint8_t*)AscendC::GmAlloc(xByteSize);
    uint8_t* weight = (uint8_t*)AscendC::GmAlloc(weightByteSize);
    uint8_t* y = (uint8_t*)AscendC::GmAlloc(yByteSize);
    uint8_t* workspace = (uint8_t*)AscendC::GmAlloc(32);
    uint8_t* tiling = (uint8_t*)AscendC::GmAlloc(tilingDataSize);
    memset(tiling, 0, tilingDataSize);

    memcpy(x, xHost.data(), xByteSize);
    memcpy(weight, weightHost.data(), weightByteSize);

    PreluTilingData* tilingData = reinterpret_cast<PreluTilingData*>(tiling);
    tilingData->totalLength = size;
    tilingData->usedCoreNum = numBlocks;
    tilingData->formerNum = 0;
    tilingData->formerLength = 0;
    tilingData->tailLength = 0;
    tilingData->tileLength = 8;
    tilingData->channelSize = c;
    tilingData->innerSize = 1;
    tilingData->innerSizeAligned = 8;
    tilingData->tilesPerRow = 3;
    tilingData->baseTasks = 1;
    tilingData->extraTasks = 1;

    ICPU_SET_TILING_KEY(PRELU_TPL_CHANNEL_NC_SPLIT_C_WEIGHT_REUSE_MODE);
    AscendC::SetKernelMode(KernelMode::AIV_MODE);

    ICPU_RUN_KF((prelu<PRELU_TPL_CHANNEL_NC_SPLIT_C_WEIGHT_REUSE_MODE>), numBlocks, x, weight, y, workspace, tiling);

    memcpy(yHost.data(), y, yByteSize);
    for (size_t row = 0; row < n; ++row) {
        for (size_t col = 0; col < c; ++col) {
            size_t offset = row * c + col;
            float expected = xHost[offset] > 0.0f ? xHost[offset] : xHost[offset] * weightHost[col];
            EXPECT_NEAR(yHost[offset], expected, 1e-6f);
        }
    }

    AscendC::GmFree(x);
    AscendC::GmFree(weight);
    AscendC::GmFree(y);
    AscendC::GmFree(workspace);
    AscendC::GmFree(tiling);
}
