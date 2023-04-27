#include "MyMsg_SplDcps.h"
#include "ccpp_MyMsg_.h"

#include <v_copyIn.h>
#include <v_topic.h>
#include <os_stdlib.h>
#include <string.h>
#include <os_report.h>

v_copyin_result
__pubsub_cpp_msg_dds__MyMsg___copyIn(
    c_base base,
    const struct ::pubsub_cpp::msg::dds_::MyMsg_ *from,
    struct _pubsub_cpp_msg_dds__MyMsg_ *to)
{
    v_copyin_result result = V_COPYIN_RESULT_OK;
    (void) base;

    to->num_ = (c_long)from->num_;
    return result;
}

void
__pubsub_cpp_msg_dds__MyMsg___copyOut(
    const void *_from,
    void *_to)
{
    const struct _pubsub_cpp_msg_dds__MyMsg_ *from = (const struct _pubsub_cpp_msg_dds__MyMsg_ *)_from;
    struct ::pubsub_cpp::msg::dds_::MyMsg_ *to = (struct ::pubsub_cpp::msg::dds_::MyMsg_ *)_to;
    to->num_ = (::DDS::Long)from->num_;
}

