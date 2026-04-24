cmake_minimum_required(VERSION 3.21)

project(depfiles LANGUAGES C)

set(BUILD_CONFIG "default" CACHE STRING "Build defconfig")

set(PROJECT_ROOT ${CMAKE_SOURCE_DIR})
cmake_path(NORMAL_PATH PROJECT_ROOT OUTPUT_VARIABLE PROJECT_ROOT_NORMALIZED)
list(APPEND CMAKE_MODULE_PATH ${PROJECT_ROOT}/cmake)

set(AUTOCONF_H ${CMAKE_BINARY_DIR}/kconfig/include/generated/yak/config.h)

include(kconfig)

add_executable(
	program
	main.c
	unrelated.c
)

target_include_directories(program PRIVATE
	# Contains config.h
	${CMAKE_BINARY_DIR}/kconfig/include/generated
)

set_target_properties(program PROPERTIES C_COMPILER_LAUNCHER
    "python3;${CMAKE_SOURCE_DIR}/fixdep.py;${KCONFIG_SYNC_DIR}")
