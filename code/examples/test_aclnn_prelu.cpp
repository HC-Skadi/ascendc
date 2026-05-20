#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdint>
#include <vector>
#include "acl/acl.h"
#include "aclnn_prelu.h"

#define CHECK_RET(cond, return_expr) \
    do {                             \
        if (!(cond)) {               \
            return_expr;             \
        }                            \
    } while (0)

#define LOG_PRINT(message, ...)         \
    do {                                \
        printf(message, ##__VA_ARGS__); \
    } while (0)

int64_t GetShapeSize(const std::vector<int64_t>& shape)
{
    int64_t shapeSize = 1;
    for (auto i : shape) {
        shapeSize *= i;
    }
    return shapeSize;
}

void DestroyTensor(aclTensor*& tensor, void*& deviceAddr)
{
    if (tensor != nullptr) {
        aclDestroyTensor(tensor);
        tensor = nullptr;
    }
    if (deviceAddr != nullptr) {
        aclrtFree(deviceAddr);
        deviceAddr = nullptr;
    }
}

int Init(int32_t deviceId, aclrtStream* stream)
{
    auto ret = aclInit(nullptr);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclInit failed. ERROR: %d\n", ret); return ret);
    ret = aclrtSetDevice(deviceId);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtSetDevice failed. ERROR: %d\n", ret); return ret);
    ret = aclrtCreateStream(stream);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtCreateStream failed. ERROR: %d\n", ret); return ret);
    return 0;
}

template <typename T>
int CreateAclTensor(
    const std::vector<T>& hostData, const std::vector<int64_t>& shape, void** deviceAddr, aclDataType dataType,
    aclTensor** tensor)
{
    auto size = GetShapeSize(shape) * sizeof(T);
    auto ret = aclrtMalloc(deviceAddr, size, ACL_MEM_MALLOC_HUGE_FIRST);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtMalloc failed. ERROR: %d\n", ret); return ret);
    ret = aclrtMemcpy(*deviceAddr, size, hostData.data(), size, ACL_MEMCPY_HOST_TO_DEVICE);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtMemcpy failed. ERROR: %d\n", ret); aclrtFree(*deviceAddr);
              *deviceAddr = nullptr; return ret);

    std::vector<int64_t> strides(shape.size(), 1);
    for (int64_t i = static_cast<int64_t>(shape.size()) - 2; i >= 0; i--) {
        strides[i] = shape[i + 1] * strides[i + 1];
    }

    *tensor = aclCreateTensor(
        shape.data(), shape.size(), dataType, strides.data(), 0, aclFormat::ACL_FORMAT_ND, shape.data(), shape.size(),
        *deviceAddr);
    CHECK_RET(*tensor != nullptr, LOG_PRINT("aclCreateTensor failed.\n"); aclrtFree(*deviceAddr);
              *deviceAddr = nullptr; return 1);
    return 0;
}

int main()
{
    int32_t deviceId = 0;
    aclrtStream stream = nullptr;
    void* workspaceAddr = nullptr;
    uint64_t workspaceSize = 0;
    auto ret = Init(deviceId, &stream);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("Init acl failed. ERROR: %d\n", ret); return ret);

    // 构造输入 tensor
    aclTensor* x = nullptr;
    void* xDeviceAddr = nullptr;
    aclTensor* weight = nullptr;
    void* weightDeviceAddr = nullptr;
    aclTensor* y = nullptr;
    void* yDeviceAddr = nullptr;
    auto Cleanup = [&](int result) {
        DestroyTensor(x, xDeviceAddr);
        DestroyTensor(weight, weightDeviceAddr);
        DestroyTensor(y, yDeviceAddr);
        if (workspaceAddr != nullptr) {
            aclrtFree(workspaceAddr);
            workspaceAddr = nullptr;
        }
        if (stream != nullptr) {
            aclrtDestroyStream(stream);
            stream = nullptr;
        }
        aclrtResetDevice(deviceId);
        aclFinalize();
        return result;
    };

    std::vector<int64_t> xShape = {7};
    std::vector<float> xHostData = {-3.0f, -1.0f, 0.0f, 1.0f, 2.0f, -4.0f, 5.0f};
    ret = CreateAclTensor(xHostData, xShape, &xDeviceAddr, aclDataType::ACL_FLOAT, &x);
    CHECK_RET(ret == ACL_SUCCESS, return Cleanup(ret));
    std::vector<int64_t> weightShape = {1};
    std::vector<float> weightHostData = {0.25f};
    ret = CreateAclTensor(weightHostData, weightShape, &weightDeviceAddr, aclDataType::ACL_FLOAT, &weight);
    CHECK_RET(ret == ACL_SUCCESS, return Cleanup(ret));

    // 构造输出 tensor
    std::vector<int64_t> yShape = {7};
    std::vector<float> yHostData(7, 0);
    ret = CreateAclTensor(yHostData, yShape, &yDeviceAddr, aclDataType::ACL_FLOAT, &y);
    CHECK_RET(ret == ACL_SUCCESS, return Cleanup(ret));

    // 调用 aclnnPrelu 第一段接口
    aclOpExecutor* executor = nullptr;
    ret = aclnnPreluGetWorkspaceSize(x, weight, y, &workspaceSize, &executor);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclnnPreluGetWorkspaceSize failed. ERROR: %d\n", ret);
              return Cleanup(ret));
    CHECK_RET(executor != nullptr, LOG_PRINT("aclnnPreluGetWorkspaceSize returned null executor.\n");
              ret = 1; return Cleanup(ret));
    LOG_PRINT("workspaceSize: %llu\n", static_cast<unsigned long long>(workspaceSize));

    // 申请 workspace
    if (workspaceSize > 0) {
        ret = aclrtMalloc(&workspaceAddr, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
        CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("allocate workspace failed. ERROR: %d\n", ret); return Cleanup(ret));
    }

    // 调用 aclnnPrelu 第二段接口
    ret = aclnnPrelu(workspaceAddr, workspaceSize, executor, stream);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclnnPrelu failed. ERROR: %d\n", ret); return Cleanup(ret));

    // 同步等待
    ret = aclrtSynchronizeStream(stream);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtSynchronizeStream failed. ERROR: %d\n", ret); return Cleanup(ret));

    std::vector<float> yResult(7, 0.0f);
    ret = aclrtMemcpy(yResult.data(), yResult.size() * sizeof(float), yDeviceAddr, yResult.size() * sizeof(float),
                      ACL_MEMCPY_DEVICE_TO_HOST);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("copy output failed. ERROR: %d\n", ret); return Cleanup(ret));
    LOG_PRINT("prelu output:");
    for (auto value : yResult) {
        LOG_PRINT(" %.6f", value);
    }
    LOG_PRINT("\n");

    {
        std::vector<float> expected = {-0.75f, -0.25f, 0.0f, 1.0f, 2.0f, -1.0f, 5.0f};
        bool pass = true;
        for (size_t i = 0; i < expected.size(); ++i) {
            if (std::fabs(yResult[i] - expected[i]) > 1e-5f) {
                LOG_PRINT("mismatch at %zu: actual=%.6f expected=%.6f\n", i, yResult[i], expected[i]);
                pass = false;
            }
        }
        CHECK_RET(pass, ret = 1; return Cleanup(ret));
        LOG_PRINT("prelu check passed.\n");
    }

    return Cleanup(ret);
}
