// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice

#ifndef PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_generator_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "pubsub_cpp/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "pubsub_cpp/msg/my_msg__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace pubsub_cpp
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
cdr_serialize(
  const pubsub_cpp::msg::MyMsg & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  pubsub_cpp::msg::MyMsg & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
get_serialized_size(
  const pubsub_cpp::msg::MyMsg & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
max_serialized_size_MyMsg(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace pubsub_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pubsub_cpp, msg, MyMsg)();

#ifdef __cplusplus
}
#endif

#endif  // PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
