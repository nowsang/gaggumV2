// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice
#include "pubsub_cpp/msg/my_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
pubsub_cpp__msg__MyMsg__init(pubsub_cpp__msg__MyMsg * msg)
{
  if (!msg) {
    return false;
  }
  // num
  return true;
}

void
pubsub_cpp__msg__MyMsg__fini(pubsub_cpp__msg__MyMsg * msg)
{
  if (!msg) {
    return;
  }
  // num
}

pubsub_cpp__msg__MyMsg *
pubsub_cpp__msg__MyMsg__create()
{
  pubsub_cpp__msg__MyMsg * msg = (pubsub_cpp__msg__MyMsg *)malloc(sizeof(pubsub_cpp__msg__MyMsg));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pubsub_cpp__msg__MyMsg));
  bool success = pubsub_cpp__msg__MyMsg__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
pubsub_cpp__msg__MyMsg__destroy(pubsub_cpp__msg__MyMsg * msg)
{
  if (msg) {
    pubsub_cpp__msg__MyMsg__fini(msg);
  }
  free(msg);
}


bool
pubsub_cpp__msg__MyMsg__Sequence__init(pubsub_cpp__msg__MyMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  pubsub_cpp__msg__MyMsg * data = NULL;
  if (size) {
    data = (pubsub_cpp__msg__MyMsg *)calloc(size, sizeof(pubsub_cpp__msg__MyMsg));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pubsub_cpp__msg__MyMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pubsub_cpp__msg__MyMsg__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
pubsub_cpp__msg__MyMsg__Sequence__fini(pubsub_cpp__msg__MyMsg__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      pubsub_cpp__msg__MyMsg__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

pubsub_cpp__msg__MyMsg__Sequence *
pubsub_cpp__msg__MyMsg__Sequence__create(size_t size)
{
  pubsub_cpp__msg__MyMsg__Sequence * array = (pubsub_cpp__msg__MyMsg__Sequence *)malloc(sizeof(pubsub_cpp__msg__MyMsg__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = pubsub_cpp__msg__MyMsg__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
pubsub_cpp__msg__MyMsg__Sequence__destroy(pubsub_cpp__msg__MyMsg__Sequence * array)
{
  if (array) {
    pubsub_cpp__msg__MyMsg__Sequence__fini(array);
  }
  free(array);
}
