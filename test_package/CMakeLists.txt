cmake_minimum_required(VERSION 3.12)
project(test_package)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
find_package(MAVSDK MODULE REQUIRED)

add_executable(test test_package.cpp)
target_link_libraries(test PRIVATE MAVSDK::MAVSDK)

