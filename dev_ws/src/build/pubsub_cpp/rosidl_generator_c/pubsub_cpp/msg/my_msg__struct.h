// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice

#ifndef PUBSUB_CPP__MSG__MY_MSG__STRUCT_H_
#define PUBSUB_CPP__MSG__MY_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/MyMsg in the package pubsub_cpp.
typedef struct pubsub_cpp__msg__MyMsg
{
  int32_t num;
} pubsub_cpp__msg__MyMsg;

// Struct for a sequence of pubsub_cpp__msg__MyMsg.
typedef struct pubsub_cpp__msg__MyMsg__Sequence
{
  pubsub_cpp__msg__MyMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pubsub_cpp__msg__MyMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PUBSUB_CPP__MSG__MY_MSG__STRUCT_H_
