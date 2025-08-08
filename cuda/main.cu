#include <iostream>
#include <string>
#include <cuda_runtime.h>
#include <cuda.h>

// Simple integer to string conversion that works with CUDA
std::string intToString(int value) {
    if (value == 0) return "0";
    
    std::string result;
    bool negative = value < 0;
    if (negative) value = -value;
    
    while (value > 0) {
        result = char('0' + value % 10) + result;
        value /= 10;
    }
    
    if (negative) result = "-" + result;
    return result;
}

static std::string decodeCudaVersion(int v) {
    int major = v / 1000;
    int minor = (v % 1000) / 10;
    return intToString(major) + "." + intToString(minor);
}

int main() {
    int driverVersion = 0, runtimeVersion = 0;
    cudaError_t rc1 = cudaDriverGetVersion(&driverVersion);
    cudaError_t rc2 = cudaRuntimeGetVersion(&runtimeVersion);

    std::cout << "CUDA driver rc=" << (int)rc1
              << " version=" << driverVersion
              << " (" << decodeCudaVersion(driverVersion) << ")\n";

    std::cout << "CUDA runtime rc=" << (int)rc2
              << " version=" << runtimeVersion
              << " (" << decodeCudaVersion(runtimeVersion) << ")\n";

    return 0;
}