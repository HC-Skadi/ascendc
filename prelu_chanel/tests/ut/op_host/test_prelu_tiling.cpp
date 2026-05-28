#include <iostream>
#include <gtest/gtest.h>
#include "tiling_context_faker.h"
#include "tiling_case_executor.h"
#include "prelu_tiling_data.h"

namespace PreluUT {
using namespace std;
using namespace ge;
using namespace gert;
static const std::string OP_NAME = "Prelu";

struct PreluTestParam {
    std::string caseName;
    std::initializer_list<int64_t> xShape;
    ge::DataType xDtype;
    ge::Format xFormat;
    std::initializer_list<int64_t> weightShape;
    ge::DataType weightDtype;
    ge::Format weightFormat;
    std::initializer_list<int64_t> yShape;
    ge::DataType yDtype;
    ge::Format yFormat;
    std::string socVersion;
    ge::graphStatus status;
    uint64_t expectTilingKey;
    std::string expectTilingData;
    std::vector<size_t> expectWorkspaces;
    uint64_t maxAIVNum;
    uint64_t ubSize;
    uint64_t tilingDataMaxSize;
};

static PreluTestParam testCases[] = {
    {"prelu_0", {7}, ge::DT_FLOAT, ge::FORMAT_ND, {1}, ge::DT_FLOAT, ge::FORMAT_ND, {7}, ge::DT_FLOAT,
        ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 0UL,
        "7 1 0 128 7 10880 1 1 1 0 0 0 0 0 0 0 0 0 0 ",
        {0}, 64, 262144, 4096},
    {"prelu_nc_one_as_scalar", {1, 1, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, {1}, ge::DT_FLOAT, ge::FORMAT_ND,
        {1, 1, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 0UL,
        "20000 40 39 512 32 10880 1 1 1 0 0 0 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel", {2, 3, 5}, ge::DT_FLOAT, ge::FORMAT_ND, {3}, ge::DT_FLOAT, ge::FORMAT_ND, {2, 3, 5},
        ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 1UL,
        "30 6 0 0 0 10880 3 5 8 1 0 0 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_nc_weight_reuse", {64, 3}, ge::DT_FLOAT, ge::FORMAT_ND, {3}, ge::DT_FLOAT, ge::FORMAT_ND,
        {64, 3}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 4UL,
        "192 40 0 0 0 9320 3 1 8 1 24 0 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_nc_weight_reuse_small_n", {1, 3}, ge::DT_FLOAT, ge::FORMAT_ND, {3}, ge::DT_FLOAT,
        ge::FORMAT_ND, {1, 3}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 4UL,
        "3 1 0 0 0 9320 3 1 8 1 0 0 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_nc_weight_reuse_c33", {2, 33}, ge::DT_FLOAT, ge::FORMAT_ND, {33}, ge::DT_FLOAT,
        ge::FORMAT_ND, {2, 33}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 4UL,
        "66 2 0 0 0 9320 33 1 40 1 0 0 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_nc_weight_reuse_nchw_ones", {1, 1024, 1, 1}, ge::DT_FLOAT, ge::FORMAT_ND, {1024},
        ge::DT_FLOAT, ge::FORMAT_ND, {1, 1024, 1, 1}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B",
        ge::GRAPH_SUCCESS, 4UL, "1024 1 0 0 0 8192 1024 1 1024 1 0 0 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_small_l_weight_reuse", {8, 128, 4}, ge::DT_FLOAT, ge::FORMAT_ND, {128},
        ge::DT_FLOAT, ge::FORMAT_ND, {8, 128, 4}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B",
        ge::GRAPH_SUCCESS, 4UL, "4096 8 0 0 0 9216 128 4 512 1 0 0 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_nc_weight_reuse_n13_c47_l19", {13, 47, 19}, ge::DT_FLOAT, ge::FORMAT_ND, {47},
        ge::DT_FLOAT, ge::FORMAT_ND, {13, 47, 19}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B",
        ge::GRAPH_SUCCESS, 4UL, "11609 13 0 0 0 8960 47 19 896 1 0 0 0 0 0 0 0 0 0 ",
        {0}, 64, 262144, 4096},
    {"prelu_channel_small_l_multi_row_n100_c197_l31", {100, 197, 31}, ge::DT_FLOAT, ge::FORMAT_ND, {197},
        ge::DT_FLOAT, ge::FORMAT_ND, {100, 197, 31}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B",
        ge::GRAPH_SUCCESS, 6UL, "610700 40 0 0 0 512 197 31 32 0 0 0 0 0 16 1300 32 20 13 ",
        {0}, 64, 262144, 4096},
    {"prelu_channel_small_l_split_c_benefit_low", {1, 2048, 7}, ge::DT_FLOAT, ge::FORMAT_ND, {2048},
        ge::DT_FLOAT, ge::FORMAT_ND, {1, 2048, 7}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B",
        ge::GRAPH_SUCCESS, 6UL, "14336 40 0 0 0 128 2048 7 8 0 0 0 0 0 16 128 3 8 128 ", {0}, 64, 262144, 4096},
    {"prelu_channel_medium_l_split_c_weight_reuse", {1, 2048, 7, 7}, ge::DT_FLOAT, ge::FORMAT_ND, {2048},
        ge::DT_FLOAT, ge::FORMAT_ND, {1, 2048, 7, 7}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B",
        ge::GRAPH_SUCCESS, 6UL, "100352 40 0 0 0 896 2048 49 56 0 0 0 0 0 16 128 3 8 128 ", {0}, 64, 262144, 4096},
    {"prelu_channel_nc_split_c_weight_reuse", {1, 70000}, ge::DT_FLOAT, ge::FORMAT_ND, {70000},
        ge::DT_FLOAT, ge::FORMAT_ND, {1, 70000}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B",
        ge::GRAPH_SUCCESS, 5UL, "70000 9 0 0 0 8160 70000 1 8160 0 0 9 1 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_split", {64, 2, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, {2}, ge::DT_FLOAT, ge::FORMAT_ND,
        {64, 2, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 2UL,
        "2560000 40 0 0 0 10880 2 20000 20000 3 8 2 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_split_benefit_low", {16, 2, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, {2}, ge::DT_FLOAT,
        ge::FORMAT_ND, {16, 2, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 2UL,
        "640000 32 0 0 0 10880 2 20000 20000 1 0 2 0 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
    {"prelu_channel_split_parallel", {1, 2, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, {2}, ge::DT_FLOAT,
        ge::FORMAT_ND, {1, 2, 20000}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 3UL,
        "40000 40 0 0 0 1024 2 20000 20000 0 0 20 1 0 0 0 0 0 0 ", {0}, 64, 262144, 4096},
};

class PreluTilingTest : public testing::TestWithParam<PreluTestParam> {
protected:
    static void SetUpTestCase() {
        std::cout << "PreluTilingTest SetUp." << std::endl;
    }
    static void TearDownTestCase() {
        std::cout << "PreluTilingTest TearDown." << std::endl;
    }
};

struct PreluCompileInfo {} compileInfo;

static void TestOneParamCase(const PreluTestParam &param)
{
    gert::StorageShape xShape = {param.xShape, param.xShape};
    gert::StorageShape weightShape = {param.weightShape, param.weightShape};
    gert::StorageShape yShape = {param.yShape, param.yShape};
    std::vector<gert::TilingContextPara::TensorDescription> inputTensorDesc_(
        {{xShape, param.xDtype, param.xFormat},
        {weightShape, param.weightDtype, param.weightFormat}});
    std::vector<gert::TilingContextPara::TensorDescription> outputTensorDesc_(
        {{yShape, param.yDtype, param.yFormat}});
    std::vector<gert::TilingContextPara::OpAttr> attrs_;

    gert::TilingContextPara tilingContextPara(
        OP_NAME,
        inputTensorDesc_,
        outputTensorDesc_,
        attrs_,
        &compileInfo,
        param.maxAIVNum,
        param.ubSize,
        param.tilingDataMaxSize);
    ExecuteTestCase(tilingContextPara, param.status, param.expectTilingKey,
                    param.expectTilingData, param.expectWorkspaces);
}

TEST_P(PreluTilingTest, tiling_test)
{
    const PreluTestParam &param = GetParam();
    TestOneParamCase(param);
}

INSTANTIATE_TEST_SUITE_P(
    PreluTilingTests,
    PreluTilingTest,
    testing::ValuesIn(testCases));

}
