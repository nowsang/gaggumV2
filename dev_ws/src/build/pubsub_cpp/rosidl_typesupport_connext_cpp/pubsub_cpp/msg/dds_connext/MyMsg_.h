

/*
WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

This file was generated from MyMsg_.idl using "rtiddsgen".
The rtiddsgen tool is part of the RTI Connext distribution.
For more information, type 'rtiddsgen -help' at a command shell
or consult the RTI Connext manual.
*/

#ifndef MyMsg__1168833922_h
#define MyMsg__1168833922_h

#ifndef NDDS_STANDALONE_TYPE
#ifndef ndds_cpp_h
#include "ndds/ndds_cpp.h"
#endif
#else
#include "ndds_standalone_type.h"
#endif

namespace pubsub_cpp {
    namespace msg {
        namespace dds_ {

            extern const char *MyMsg_TYPENAME;

            struct MyMsg_Seq;
            #ifndef NDDS_STANDALONE_TYPE
            class MyMsg_TypeSupport;
            class MyMsg_DataWriter;
            class MyMsg_DataReader;
            #endif

            class MyMsg_ 
            {
              public:
                typedef struct MyMsg_Seq Seq;
                #ifndef NDDS_STANDALONE_TYPE
                typedef MyMsg_TypeSupport TypeSupport;
                typedef MyMsg_DataWriter DataWriter;
                typedef MyMsg_DataReader DataReader;
                #endif

                DDS_Long   num_ ;

            };
            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_pubsub_cpp)
            /* If the code is building on Windows, start exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport __declspec(dllexport)
            #endif

            NDDSUSERDllExport DDS_TypeCode* MyMsg__get_typecode(void); /* Type code */

            DDS_SEQUENCE(MyMsg_Seq, MyMsg_);

            NDDSUSERDllExport
            RTIBool MyMsg__initialize(
                MyMsg_* self);

            NDDSUSERDllExport
            RTIBool MyMsg__initialize_ex(
                MyMsg_* self,RTIBool allocatePointers,RTIBool allocateMemory);

            NDDSUSERDllExport
            RTIBool MyMsg__initialize_w_params(
                MyMsg_* self,
                const struct DDS_TypeAllocationParams_t * allocParams);  

            NDDSUSERDllExport
            void MyMsg__finalize(
                MyMsg_* self);

            NDDSUSERDllExport
            void MyMsg__finalize_ex(
                MyMsg_* self,RTIBool deletePointers);

            NDDSUSERDllExport
            void MyMsg__finalize_w_params(
                MyMsg_* self,
                const struct DDS_TypeDeallocationParams_t * deallocParams);

            NDDSUSERDllExport
            void MyMsg__finalize_optional_members(
                MyMsg_* self, RTIBool deletePointers);  

            NDDSUSERDllExport
            RTIBool MyMsg__copy(
                MyMsg_* dst,
                const MyMsg_* src);

            #if (defined(RTI_WIN32) || defined (RTI_WINCE)) && defined(NDDS_USER_DLL_EXPORT_pubsub_cpp)
            /* If the code is building on Windows, stop exporting symbols.
            */
            #undef NDDSUSERDllExport
            #define NDDSUSERDllExport
            #endif
        } /* namespace dds_  */
    } /* namespace msg  */
} /* namespace pubsub_cpp  */

#endif /* MyMsg_ */

