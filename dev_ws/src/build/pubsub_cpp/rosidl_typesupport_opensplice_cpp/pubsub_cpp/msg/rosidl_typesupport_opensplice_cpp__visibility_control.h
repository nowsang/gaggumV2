// generated from rosidl_typesupport_opensplice_cpp/resource/visibility_control.h.in
// generated code does not contain a copyright notice

#ifndef PUBSUB_CPP__MSG__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP__VISIBILITY_CONTROL_H_
#define PUBSUB_CPP__MSG__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP__VISIBILITY_CONTROL_H_

#ifdef __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_pubsub_cpp __attribute__ ((dllexport))
    #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_IMPORT_pubsub_cpp __attribute__ ((dllimport))
  #else
    #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_pubsub_cpp __declspec(dllexport)
    #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_IMPORT_pubsub_cpp __declspec(dllimport)
  #endif
  #ifdef ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_BUILDING_DLL_pubsub_cpp
    #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_pubsub_cpp
  #else
    #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_IMPORT_pubsub_cpp
  #endif
#else
  #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_EXPORT_pubsub_cpp
  #define ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp
#endif

#ifdef __cplusplus
}
#endif

#endif  // PUBSUB_CPP__MSG__ROSIDL_TYPESUPPORT_OPENSPLICE_CPP__VISIBILITY_CONTROL_H_
