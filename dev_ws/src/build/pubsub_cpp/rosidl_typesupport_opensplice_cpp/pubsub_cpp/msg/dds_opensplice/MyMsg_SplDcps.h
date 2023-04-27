#ifndef MYMSG_SPLTYPES_H
#define MYMSG_SPLTYPES_H

#include <c_base.h>
#include <c_misc.h>
#include <c_sync.h>
#include <c_collection.h>
#include <c_field.h>
#include <v_copyIn.h>

#include "ccpp_MyMsg_.h"
#include "pubsub_cpp/msg/rosidl_typesupport_opensplice_cpp__visibility_control.h"

extern c_metaObject __MyMsg__pubsub_cpp__load (c_base base);

extern c_metaObject __MyMsg__pubsub_cpp_msg__load (c_base base);

extern c_metaObject __MyMsg__pubsub_cpp_msg_dds___load (c_base base);

extern const char *pubsub_cpp_msg_dds__MyMsg__metaDescriptor[];
extern const int pubsub_cpp_msg_dds__MyMsg__metaDescriptorArrLength;
extern const int pubsub_cpp_msg_dds__MyMsg__metaDescriptorLength;
extern c_metaObject __pubsub_cpp_msg_dds__MyMsg___load (c_base base);
struct _pubsub_cpp_msg_dds__MyMsg_ ;
extern ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp v_copyin_result __pubsub_cpp_msg_dds__MyMsg___copyIn(c_base base, const struct pubsub_cpp::msg::dds_::MyMsg_ *from, struct _pubsub_cpp_msg_dds__MyMsg_ *to);
extern ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_pubsub_cpp void __pubsub_cpp_msg_dds__MyMsg___copyOut(const void *_from, void *_to);
struct _pubsub_cpp_msg_dds__MyMsg_ {
    c_long num_;
};

#undef OS_API
#endif
