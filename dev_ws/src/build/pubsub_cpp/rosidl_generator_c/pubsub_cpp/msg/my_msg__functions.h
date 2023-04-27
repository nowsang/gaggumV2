// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice

#ifndef PUBSUB_CPP__MSG__MY_MSG__FUNCTIONS_H_
#define PUBSUB_CPP__MSG__MY_MSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_generator_c/visibility_control.h"
#include "pubsub_cpp/msg/rosidl_generator_c__visibility_control.h"

#include "pubsub_cpp/msg/my_msg__struct.h"

/// Initialize msg/MyMsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * pubsub_cpp__msg__MyMsg
 * )) before or use
 * pubsub_cpp__msg__MyMsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
bool
pubsub_cpp__msg__MyMsg__init(pubsub_cpp__msg__MyMsg * msg);

/// Finalize msg/MyMsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
void
pubsub_cpp__msg__MyMsg__fini(pubsub_cpp__msg__MyMsg * msg);

/// Create msg/MyMsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * pubsub_cpp__msg__MyMsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
pubsub_cpp__msg__MyMsg *
pubsub_cpp__msg__MyMsg__create();

/// Destroy msg/MyMsg message.
/**
 * It calls
 * pubsub_cpp__msg__MyMsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
void
pubsub_cpp__msg__MyMsg__destroy(pubsub_cpp__msg__MyMsg * msg);


/// Initialize array of msg/MyMsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * pubsub_cpp__msg__MyMsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
bool
pubsub_cpp__msg__MyMsg__Sequence__init(pubsub_cpp__msg__MyMsg__Sequence * array, size_t size);

/// Finalize array of msg/MyMsg messages.
/**
 * It calls
 * pubsub_cpp__msg__MyMsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
void
pubsub_cpp__msg__MyMsg__Sequence__fini(pubsub_cpp__msg__MyMsg__Sequence * array);

/// Create array of msg/MyMsg messages.
/**
 * It allocates the memory for the array and calls
 * pubsub_cpp__msg__MyMsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
pubsub_cpp__msg__MyMsg__Sequence *
pubsub_cpp__msg__MyMsg__Sequence__create(size_t size);

/// Destroy array of msg/MyMsg messages.
/**
 * It calls
 * pubsub_cpp__msg__MyMsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pubsub_cpp
void
pubsub_cpp__msg__MyMsg__Sequence__destroy(pubsub_cpp__msg__MyMsg__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // PUBSUB_CPP__MSG__MY_MSG__FUNCTIONS_H_
