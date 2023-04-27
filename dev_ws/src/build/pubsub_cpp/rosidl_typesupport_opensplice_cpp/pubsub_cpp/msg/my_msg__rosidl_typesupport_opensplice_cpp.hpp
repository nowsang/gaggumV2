// generated from rosidl_typesupport_opensplice_cpp/resource/idl__rosidl_typesupport_cpp.hpp.em
// generated code does not contain a copyright notice
#ifndef PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_HPP_
#define PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_HPP_
// generated from
// rosidl_typesupport_opensplice_cpp/resource/msg__rosidl_typesupport_opensplice_cpp.hpp.em
// generated code does not contain a copyright notice

#include "pubsub_cpp/msg/my_msg__struct.hpp"
#include "pubsub_cpp/msg/dds_opensplice/ccpp_MyMsg_.h"
#include "rosidl_generator_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "pubsub_cpp/msg/rosidl_typesupport_opensplice_cpp__visibility_control.h"

namespace DDS
{
class DomainParticipant;
class DataReader;
class DataWriter;
}  // namespace DDS

namespace pubsub_cpp
{
namespace msg
{
namespace typesupport_opensplice_cpp
{

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp
extern void register_type__MyMsg(
  DDS::DomainParticipant * participant,
  const char * type_name);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp
extern void convert_ros_message_to_dds(
  const pubsub_cpp::msg::MyMsg & ros_message,
  pubsub_cpp::msg::dds_::MyMsg_ & dds_message);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp
extern void publish__MyMsg(
  DDS::DataWriter * topic_writer,
  const void * untyped_ros_message);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp
extern void convert_dds_message_to_ros(
  const pubsub_cpp::msg::dds_::MyMsg_ & dds_message,
  pubsub_cpp::msg::MyMsg & ros_message);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp
extern bool take__MyMsg(
  DDS::DataReader * topic_reader,
  bool ignore_local_publications,
  void * untyped_ros_message,
  bool * taken);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_pubsub_cpp
const char *
serialize__MyMsg(
  const void * untyped_ros_message,
  void * serialized_data);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_pubsub_cpp
const char *
deserialize__MyMsg(
  const uint8_t * buffer,
  unsigned length,
  void * untyped_ros_message);

}  // namespace typesupport_opensplice_cpp

}  // namespace msg
}  // namespace pubsub_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_opensplice_cpp,
  pubsub_cpp, msg,
  MyMsg)();

#ifdef __cplusplus
}
#endif
#endif  // PUBSUB_CPP__MSG__MY_MSG__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_HPP_
