#ifndef NUM_SPLTYPES_H
#define NUM_SPLTYPES_H

#include <c_base.h>
#include <c_misc.h>
#include <c_sync.h>
#include <c_collection.h>
#include <c_field.h>
#include <v_copyIn.h>

#include "ccpp_Num_.h"
#include "tutorial_interfaces/msg/rosidl_typesupport_opensplice_cpp__visibility_control.h"

extern c_metaObject __Num__tutorial_interfaces__load (c_base base);

extern c_metaObject __Num__tutorial_interfaces_msg__load (c_base base);

extern c_metaObject __Num__tutorial_interfaces_msg_dds___load (c_base base);

extern const char *tutorial_interfaces_msg_dds__Num__metaDescriptor[];
extern const int tutorial_interfaces_msg_dds__Num__metaDescriptorArrLength;
extern const int tutorial_interfaces_msg_dds__Num__metaDescriptorLength;
extern c_metaObject __tutorial_interfaces_msg_dds__Num___load (c_base base);
struct _tutorial_interfaces_msg_dds__Num_ ;
extern ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces v_copyin_result __tutorial_interfaces_msg_dds__Num___copyIn(c_base base, const struct tutorial_interfaces::msg::dds_::Num_ *from, struct _tutorial_interfaces_msg_dds__Num_ *to);
extern ROSIDL_TYPESUPPORT_OPENSPLICE_CPP_PUBLIC_tutorial_interfaces void __tutorial_interfaces_msg_dds__Num___copyOut(const void *_from, void *_to);
struct _tutorial_interfaces_msg_dds__Num_ {
    c_longlong num_;
};

#undef OS_API
#endif
