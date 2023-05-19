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
find_package(std_msgs REQUIRED)
find_package(gaggum_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sioclient REQUIRED)
find_package(Boost REQUIRED COMPONENTS system)


include_directories(${sioclient_INCLUDE_DIRS})

# 실행 파일 추가 및 이름 지정
add_executable(time_13 nodes/time_13.cpp)
ament_target_dependencies(time_13 rclcpp sioclient)
target_link_libraries(time_13 sioclient Boost::system)

add_executable(time_15 nodes/time_15.cpp)
ament_target_dependencies(time_15 rclcpp sioclient)
target_link_libraries(time_15 sioclient Boost::system)

add_executable(gaggum_socket nodes/gaggum_socket.cpp)
ament_target_dependencies(gaggum_socket rclcpp sioclient gaggum_msgs std_msgs)
target_link_libraries(gaggum_socket sioclient Boost::system)


# 실행 파일을 찾을 수 있도록 섹션 추가
install(TARGETS
  time_13
  time_15
  gaggum_socket  
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
