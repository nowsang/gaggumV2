// generated from rosidl_typesupport_opensplice_cpp/resource/idl__rosidl_typesupport_cpp.hpp.em
// generated code does not contain a copyright notice
#ifndef TUTORIAL_INTERFACES__MSG__NUM__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_HPP_
#define TUTORIAL_INTERFACES__MSG__NUM__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_HPP_
// generated from
// rosidl_typesupport_opensplice_cpp/resource/msg__rosidl_typesupport_opensplice_cpp.hpp.em
// generated code does not contain a copyright notice

#include "tutorial_interfaces/msg/num__struct.hpp"
#include "tutorial_interfaces/msg/dds_opensplice/ccpp_Num_.h"
#include "rosidl_generator_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "tutorial_interfaces/msg/rosidl_typesupport_opensplice_cpp__visibility_control.h"

namespace DDS
{
class DomainParticipant;
class DataReader;
class DataWriter;
}  // namespace DDS

namespace tutorial_interfaces
{
namespace msg
{
namespace typesupport_opensplice_cpp
{

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces
extern void register_type__Num(
  DDS::DomainParticipant * participant,
  const char * type_name);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces
extern void convert_ros_message_to_dds(
  const tutorial_interfaces::msg::Num & ros_message,
  tutorial_interfaces::msg::dds_::Num_ & dds_message);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces
extern void publish__Num(
  DDS::DataWriter * topic_writer,
  const void * untyped_ros_message);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces
extern void convert_dds_message_to_ros(
  const tutorial_interfaces::msg::dds_::Num_ & dds_message,
  tutorial_interfaces::msg::Num & ros_message);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces
extern bool take__Num(
  DDS::DataReader * topic_reader,
  bool ignore_local_publications,
  void * untyped_ros_message,
  bool * taken);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_tutorial_interfaces
const char *
serialize__Num(
  const void * untyped_ros_message,
  void * serialized_data);

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_tutorial_interfaces
const char *
deserialize__Num(
  const uint8_t * buffer,
  unsigned length,
  void * untyped_ros_message);

}  // namespace typesupport_opensplice_cpp

}  // namespace msg
}  // namespace tutorial_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
  rosidl_typesupport_opensplice_cpp,
  tutorial_interfaces, msg,
  Num)();

#ifdef __cplusplus
}
#endif
#endif  // TUTORIAL_INTERFACES__MSG__NUM__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_HPP_
