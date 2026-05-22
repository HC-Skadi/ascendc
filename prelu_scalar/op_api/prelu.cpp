/**
 * @file prelu.cpp
 * @brief ACLNN L0 API 实现
 */

#include "prelu.h"
#include "opdev/op_log.h"
#include "opdev/op_dfx.h"
#include "opdev/shape_utils.h"
#include "opdev/make_op_executor.h"

using namespace op;

namespace l0op {

OP_TYPE_REGISTER(Prelu);

static const std::initializer_list<op::DataType> AICORE_DTYPE_SUPPORT_LIST = {
    DataType::DT_FLOAT, DataType::DT_INT32
};

// TODO: 实现形状推导和 kernel 调度
const aclTensor* Prelu(const aclTensor* x, const aclTensor* weight, const aclTensor* y, aclOpExecutor* executor)
{
    // TODO: 实现 L0 API 逻辑
    return nullptr;
}

} // namespace l0op
