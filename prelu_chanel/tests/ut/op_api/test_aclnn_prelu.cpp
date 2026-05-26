#include <iostream>
#include <gtest/gtest.h>
#include "opdev/platform.h"
#include "aclnn_prelu.h"
#include "test_utils.h"

using namespace std;
using namespace op;
using namespace op_api_test;

class AclnnPreluTest : public testing::Test {
protected:
    void SetUp() override {
        cout << "AclnnPreluTest SetUp" << endl;
    }
    
    void TearDown() override {
        cout << "AclnnPreluTest TearDown" << endl;
    }
};

TEST_F(AclnnPreluTest, FloatDtypeSuccess) {
    auto x = TestTensorFactory::CreateTensor({7}, DataType::DT_FLOAT);
    ASSERT_NE(x, nullptr);
    auto weight = TestTensorFactory::CreateTensor({1}, DataType::DT_FLOAT);
    ASSERT_NE(weight, nullptr);
    auto y = TestTensorFactory::CreateTensor({7}, DataType::DT_FLOAT);
    ASSERT_NE(y, nullptr);

    uint64_t workspaceSize = 0;
    aclOpExecutor* executor = nullptr;
    
    auto ret = aclnnPreluGetWorkspaceSize(x, weight, y, &workspaceSize, &executor);
    EXPECT_EQ(ret, ACLNN_SUCCESS);
    
    TestTensorFactory::DestroyTensor(x);
    TestTensorFactory::DestroyTensor(weight);
    TestTensorFactory::DestroyTensor(y);
}
