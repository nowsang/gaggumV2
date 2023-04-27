// generated from rosidl_typesupport_connext_cpp/resource/idl__rosidl_typesupport_connext_cpp.hpp.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice


#ifndef PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_CONNEXT_CPP_HPP_
#define PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_CONNEXT_CPP_HPP_

#include "rosidl_generator_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "pubsub_cpp/msg/rosidl_typesupport_connext_cpp__visibility_control.h"
#include "pubsub_cpp/msg/my_msg__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif

#include "pubsub_cpp/msg/dds_connext/MyMsg_Support.h"
#include "pubsub_cpp/msg/dds_connext/MyMsg_Plugin.h"
#include "ndds/ndds_cpp.h"

#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// forward declaration of internal CDR Stream
struct ConnextStaticCDRStream;

// forward declaration of DDS types
class DDSDomainParticipant;
class DDSDataWriter;
class DDSDataReader;


namespace pubsub_cpp
{

namespace msg
{
namespace typesupport_connext_cpp
{

DDS_TypeCode *
get_type_code__MyMsg();

bool
ROSIDL_TYPESUPPORT_CONNEXT_CPP_PUBLIC_pubsub_cpp
convert_ros_message_to_dds(
  const pubsub_cpp::msg::MyMsg & ros_message,
  pubsub_cpp::msg::dds_::MyMsg_ & dds_message);

bool
ROSIDL_TYPESUPPORT_CONNEXT_CPP_PUBLIC_pubsub_cpp
convert_dds_message_to_ros(
  const pubsub_cpp::msg::dds_::MyMsg_ & dds_message,
  pubsub_cpp::msg::MyMsg & ros_message);

bool
to_cdr_stream__MyMsg(
  const void * untyped_ros_message,
  ConnextStaticCDRStream * cdr_stream);

bool
to_message__MyMsg(
  const ConnextStaticCDRStream * cdr_stream,
  void * untyped_ros_message);

}  // namespace typesupport_connext_cpp

}  // namespace msg

}  // namespace pubsub_cpp


#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CONNEXT_CPP_PUBLIC_pubsub_cpp
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_connext_cpp,
  pubsub_cpp, msg,
  MyMsg)();

#ifdef __cplusplus
}
#endif


#endif  // PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_CONNEXT_CPP_HPP_
