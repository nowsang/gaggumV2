cmake_minimum_required(VERSION 3.5)
project(gaggum)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(gaggum_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# 실행 파일 추가 및 이름 지정
add_executable(talker nodes/testpub.cpp)
ament_target_dependencies(talker rclcpp gaggum_msgs)
add_executable(listener nodes/testsub.cpp)
ament_target_dependencies(listener rclcpp gaggum_msgs)
add_executable(move_turtle nodes/move_turtle.cpp)
ament_target_dependencies(move_turtle rclcpp geometry_msgs)


# 실행 파일을 찾을 수 있도록 섹션 추가
install(TARGETS
  talker
  listener
  move_turtle
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
