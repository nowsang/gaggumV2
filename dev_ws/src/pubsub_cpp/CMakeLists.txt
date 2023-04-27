  cmake_minimum_required(VERSION 3.5)
  project(pubsub_cpp)

  # Default to C++14
  if(NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 14)
  endif()

  if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
  endif()

  set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient")
  # set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "C:/path/to/sioclient/build/install")
  # set(CMAKE_PREFIX_PATH "${CMAKE_PREFIX_PATH};C:/Users/SSAFY/Desktop/dev_ws/src")

  # find dependencies
  find_package(ament_cmake REQUIRED)
  find_package(rclcpp REQUIRED)
  find_package(std_msgs REQUIRED)
  find_package(tutorial_interfaces REQUIRED)
  # find_package(socket.io-client-cpp REQUIRED)
  find_package(sioclient REQUIRED)
  
  # Build
  add_executable(pub src/pub.cpp)
  ament_target_dependencies(pub rclcpp std_msgs tutorial_interfaces)

  add_executable(sub src/sub.cpp)
  ament_target_dependencies(sub rclcpp std_msgs tutorial_interfaces)

  add_executable(socket src/socket.cpp)
  # target_link_libraries(socket sioclient)
  ament_target_dependencies(socket rclcpp std_msgs tutorial_interfaces sioclient)


  

  # Install
  install(TARGETS
    pub
    sub    
    socket
    DESTINATION lib/${PROJECT_NAME})


  if(BUILD_TESTING)
    find_package(ament_lint_auto REQUIRED)
    # the following line skips the linter which checks for copyrights
    # uncomment the line when a copyright and license is not present in all source files
    #set(ament_cmake_copyright_FOUND TRUE)
    # the following line skips cpplint (only works in a git repo)
    # uncomment the line when this package is not in a git repo
    #set(ament_cmake_cpplint_FOUND TRUE)
    ament_lint_auto_find_test_dependencies()
  endif()

  ament_package()
