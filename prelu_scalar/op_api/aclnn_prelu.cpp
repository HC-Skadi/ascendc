/**
 * @file aclnn_prelu.cpp
 * @brief ACLNN L2 API 实现
 */

#include "aclnn_prelu.h"
#include "prelu.h"
#include "aclnn_kernels/contiguous.h"
#include "aclnn_kernels/common/op_error_check.h"
#include "opdev/op_log.h"
#include "opdev/op_dfx.h"
#include "opdev/common_types.h"
#include "opdev/data_type_utils.h"
#include "opdev/make_op_executor.h"
#include "opdev/platform.h"

using namespace op;

#define ACLNN_MAX_SHAPE_RANK 8

static const std::initializer_list<op::DataType> AICORE_DTYPE_SUPPORT_LIST = {
    DataType::DT_FLOAT, DataType::DT_INT32
};

// TODO: 实现参数检查和 L0 调用
extern "C" aclnnStatus aclnnPreluGetWorkspaceSize(
    const aclTensor* x,
    const aclTensor* weight,
    const aclTensor* y,
    uint64_t* workspaceSize,
    aclOpExecutor** executor)
{
    // TODO: 实现 GetWorkspaceSize 逻辑
    auto uniqueExecutor = CREATE_EXECUTOR();
    CHECK_RET(uniqueExecutor.get() != nullptr, ACLNN_ERR_INNER_CREATE_EXECUTOR);

    *workspaceSize = 0;
    uniqueExecutor.ReleaseTo(executor);
    return ACLNN_SUCCESS;
}

extern "C" aclnnStatus aclnnPrelu(
    void* workspace,
    uint64_t workspaceSize,
    aclOpExecutor* executor,
    aclrtStream stream)
{
    return CommonOpExecutorRun(workspace, workspaceSize, executor, stream);
}
