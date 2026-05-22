/**
 * @file prelu.h
 * @brief ACLNN L0 API 接口声明
 */

#ifndef OP_API_INC_LEVEL0_PRELU_H_
#define OP_API_INC_LEVEL0_PRELU_H_

#include "opdev/op_executor.h"

namespace l0op {

const aclTensor* Prelu(const aclTensor* x, const aclTensor* weight, const aclTensor* y, aclOpExecutor* executor);

} // namespace l0op

#endif // OP_API_INC_LEVEL0_PRELU_H_
