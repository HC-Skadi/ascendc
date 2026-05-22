/**
 * @file aclnn_prelu.h
 * @brief ACLNN L2 API 接口声明
 */

#ifndef ACLNN_PRELU_H_
#define ACLNN_PRELU_H_

#include "aclnn/aclnn_base.h"

#ifndef ACLNN_API
#define ACLNN_API __attribute__((visibility("default")))
#endif

#ifdef __cplusplus
extern "C" {
#endif

ACLNN_API aclnnStatus aclnnPreluGetWorkspaceSize(
    const aclTensor *x,
    const aclTensor *weight,
    const aclTensor *y,
    uint64_t *workspaceSize,
    aclOpExecutor **executor);

ACLNN_API aclnnStatus aclnnPrelu(
    void *workspace,
    uint64_t workspaceSize,
    aclOpExecutor *executor,
    aclrtStream stream);

#ifdef __cplusplus
}
#endif

#endif // ACLNN_PRELU_H_
