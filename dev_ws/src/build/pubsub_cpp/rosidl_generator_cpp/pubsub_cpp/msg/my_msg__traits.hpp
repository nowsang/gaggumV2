// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice

#ifndef PUBSUB_CPP__MSG__MY_MSG__TRAITS_HPP_
#define PUBSUB_CPP__MSG__MY_MSG__TRAITS_HPP_

#include "pubsub_cpp/msg/my_msg__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<pubsub_cpp::msg::MyMsg>()
{
  return "pubsub_cpp::msg::MyMsg";
}

template<>
struct has_fixed_size<pubsub_cpp::msg::MyMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<pubsub_cpp::msg::MyMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<pubsub_cpp::msg::MyMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PUBSUB_CPP__MSG__MY_MSG__TRAITS_HPP_
