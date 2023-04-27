#include "Num_SplDcps.h"
#include "ccpp_Num_.h"

#include <v_copyIn.h>
#include <v_topic.h>
#include <os_stdlib.h>
#include <string.h>
#include <os_report.h>

v_copyin_result
__tutorial_interfaces_msg_dds__Num___copyIn(
    c_base base,
    const struct ::tutorial_interfaces::msg::dds_::Num_ *from,
    struct _tutorial_interfaces_msg_dds__Num_ *to)
{
    v_copyin_result result = V_COPYIN_RESULT_OK;
    (void) base;

    to->num_ = (c_longlong)from->num_;
    return result;
}

void
__tutorial_interfaces_msg_dds__Num___copyOut(
    const void *_from,
    void *_to)
{
    const struct _tutorial_interfaces_msg_dds__Num_ *from = (const struct _tutorial_interfaces_msg_dds__Num_ *)_from;
    struct ::tutorial_interfaces::msg::dds_::Num_ *to = (struct ::tutorial_interfaces::msg::dds_::Num_ *)_to;
    to->num_ = (::DDS::LongLong)from->num_;
}

