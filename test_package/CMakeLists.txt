project(LibTest)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_DEFINITIONS(-std=c++11) # Or -std=c++0x
add_executable(libtest test.cpp)
target_link_libraries(libtest ${CONAN_LIBS})
