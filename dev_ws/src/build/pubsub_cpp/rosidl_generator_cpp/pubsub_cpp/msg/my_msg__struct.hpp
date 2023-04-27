// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pubsub_cpp:msg\MyMsg.idl
// generated code does not contain a copyright notice

#ifndef PUBSUB_CPP__MSG__MY_MSG__STRUCT_HPP_
#define PUBSUB_CPP__MSG__MY_MSG__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__pubsub_cpp__msg__MyMsg __attribute__((deprecated))
#else
# define DEPRECATED__pubsub_cpp__msg__MyMsg __declspec(deprecated)
#endif

namespace pubsub_cpp
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MyMsg_
{
  using Type = MyMsg_<ContainerAllocator>;

  explicit MyMsg_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->num = 0l;
    }
  }

  explicit MyMsg_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->num = 0l;
    }
  }

  // field types and members
  using _num_type =
    int32_t;
  _num_type num;

  // setters for named parameter idiom
  Type & set__num(
    const int32_t & _arg)
  {
    this->num = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pubsub_cpp::msg::MyMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const pubsub_cpp::msg::MyMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pubsub_cpp::msg::MyMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pubsub_cpp::msg::MyMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pubsub_cpp__msg__MyMsg
    std::shared_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pubsub_cpp__msg__MyMsg
    std::shared_ptr<pubsub_cpp::msg::MyMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MyMsg_ & other) const
  {
    if (this->num != other.num) {
      return false;
    }
    return true;
  }
  bool operator!=(const MyMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MyMsg_

// alias to use template instance with default allocator
using MyMsg =
  pubsub_cpp::msg::MyMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace pubsub_cpp

#endif  // PUBSUB_CPP__MSG__MY_MSG__STRUCT_HPP_
