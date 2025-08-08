cmake_minimum_required(VERSION 3.24)
project(cuda_versions LANGUAGES CXX CUDA)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CUDA_STANDARD 17)

if (MSVC)
  set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded")  # static /MT runtime
endif()

find_package(CUDAToolkit REQUIRED)

add_executable(cuda_versions main.cu)
target_link_libraries(cuda_versions PRIVATE CUDA::cudart)

# Compile for fewer architectures to speed up build (focus on common ones)
set_target_properties(cuda_versions PROPERTIES CUDA_ARCHITECTURES "75;86")