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
    {"prelu_0", {7}, ge::DT_FLOAT, ge::FORMAT_ND, {1}, ge::DT_FLOAT, ge::FORMAT_ND, {7}, ge::DT_FLOAT, ge::FORMAT_ND, "Ascend910B", ge::GRAPH_SUCCESS, 0UL, "7 1 0 128 1 7 10880 ", {0}, 64, 262144, 4096},
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
