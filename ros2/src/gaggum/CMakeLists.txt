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
find_package(sensor_msgs REQUIRED)
find_package(sioclient REQUIRED)
find_package(Boost REQUIRED COMPONENTS system)
find_package(nav_msgs REQUIRED)

include_directories(${sioclient_INCLUDE_DIRS})

# 실행 파일 추가 및 이름 지정
add_executable(talker nodes/testpub.cpp)
ament_target_dependencies(talker rclcpp gaggum_msgs)

add_executable(listener nodes/testsub.cpp)
ament_target_dependencies(listener rclcpp gaggum_msgs)

add_executable(move_turtle nodes/move_turtle.cpp)
ament_target_dependencies(move_turtle rclcpp geometry_msgs)

add_executable(socket_pub nodes/socket_pub.cpp)
ament_target_dependencies(socket_pub rclcpp sioclient)
target_link_libraries(socket_pub sioclient Boost::system)

add_executable(socket_sub nodes/socket_sub.cpp)
ament_target_dependencies(socket_sub rclcpp sioclient)
target_link_libraries(socket_sub sioclient Boost::system)

add_executable(time_control nodes/time_control.cpp)
ament_target_dependencies(time_control rclcpp sioclient)
target_link_libraries(time_control sioclient Boost::system)

add_executable(auto_move nodes/auto_move.cpp)
ament_target_dependencies(auto_move rclcpp sioclient)
target_link_libraries(auto_move sioclient Boost::system)

add_executable(wall_tracking nodes/wall_tracking.cpp)
ament_target_dependencies(wall_tracking rclcpp sensor_msgs geometry_msgs)

add_executable(a_star nodes/a_star.cpp)
ament_target_dependencies(a_star rclcpp nav_msgs)


# 실행 파일을 찾을 수 있도록 섹션 추가
install(TARGETS
  talker
  listener
  move_turtle
  socket_pub
  socket_sub
  time_control
  auto_move
  wall_tracking
  a_star
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
