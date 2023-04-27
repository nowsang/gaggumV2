// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice
#include "pubsub_cpp/msg/my_msg__rosidl_typesupport_fastrtps_cpp.hpp"
#include "pubsub_cpp/msg/my_msg__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

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
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: num
  cdr << ros_message.num;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  pubsub_cpp::msg::MyMsg & ros_message)
{
  // Member: num
  cdr >> ros_message.num;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
get_serialized_size(
  const pubsub_cpp::msg::MyMsg & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: num
  {
    size_t item_size = sizeof(ros_message.num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pubsub_cpp
max_serialized_size_MyMsg(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: num
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _MyMsg__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const pubsub_cpp::msg::MyMsg *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _MyMsg__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<pubsub_cpp::msg::MyMsg *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _MyMsg__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const pubsub_cpp::msg::MyMsg *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _MyMsg__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_MyMsg(full_bounded, 0);
}

static message_type_support_callbacks_t _MyMsg__callbacks = {
  "pubsub_cpp::msg",
  "MyMsg",
  _MyMsg__cdr_serialize,
  _MyMsg__cdr_deserialize,
  _MyMsg__get_serialized_size,
  _MyMsg__max_serialized_size
};

static rosidl_message_type_support_t _MyMsg__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_MyMsg__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace pubsub_cpp

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_pubsub_cpp
const rosidl_message_type_support_t *
get_message_type_support_handle<pubsub_cpp::msg::MyMsg>()
{
  return &pubsub_cpp::msg::typesupport_fastrtps_cpp::_MyMsg__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pubsub_cpp, msg, MyMsg)() {
  return &pubsub_cpp::msg::typesupport_fastrtps_cpp::_MyMsg__handle;
}

#ifdef __cplusplus
}
#endif
