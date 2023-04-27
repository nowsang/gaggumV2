# Generated by CMake

if("${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}" LESS 2.5)
   message(FATAL_ERROR "CMake >= 2.6.0 required")
endif()
cmake_policy(PUSH)
cmake_policy(VERSION 2.6...3.18)
#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Protect against multiple inclusion, which would fail when already imported targets are added once more.
set(_targetsDefined)
set(_targetsNotDefined)
set(_expectedTargets)
foreach(_expectedTarget sioclient::sioclient sioclient::sioclient_tls)
  list(APPEND _expectedTargets ${_expectedTarget})
  if(NOT TARGET ${_expectedTarget})
    list(APPEND _targetsNotDefined ${_expectedTarget})
  endif()
  if(TARGET ${_expectedTarget})
    list(APPEND _targetsDefined ${_expectedTarget})
  endif()
endforeach()
if("${_targetsDefined}" STREQUAL "${_expectedTargets}")
  unset(_targetsDefined)
  unset(_targetsNotDefined)
  unset(_expectedTargets)
  set(CMAKE_IMPORT_FILE_VERSION)
  cmake_policy(POP)
  return()
endif()
if(NOT "${_targetsDefined}" STREQUAL "")
  message(FATAL_ERROR "Some (but not all) targets in this export set were already defined.\nTargets Defined: ${_targetsDefined}\nTargets not yet defined: ${_targetsNotDefined}\n")
endif()
unset(_targetsDefined)
unset(_targetsNotDefined)
unset(_expectedTargets)


# Create imported target sioclient::sioclient
add_library(sioclient::sioclient STATIC IMPORTED)

set_target_properties(sioclient::sioclient PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "C:/Users/SSAFY/Desktop/dev_ws/src/socket.io-client-cpp"
)

# Create imported target sioclient::sioclient_tls
add_library(sioclient::sioclient_tls STATIC IMPORTED)

set_target_properties(sioclient::sioclient_tls PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "C:/Users/SSAFY/Desktop/dev_ws/src/socket.io-client-cpp"
  INTERFACE_LINK_LIBRARIES "\$<LINK_ONLY:OpenSSL::SSL>;\$<LINK_ONLY:OpenSSL::Crypto>"
)

# Import target "sioclient::sioclient" for configuration "Debug"
set_property(TARGET sioclient::sioclient APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(sioclient::sioclient PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/Debug/sioclient.lib"
  )

# Import target "sioclient::sioclient_tls" for configuration "Debug"
set_property(TARGET sioclient::sioclient_tls APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(sioclient::sioclient_tls PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/Debug/sioclient_tls.lib"
  )

# Import target "sioclient::sioclient" for configuration "Release"
set_property(TARGET sioclient::sioclient APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(sioclient::sioclient PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/Release/sioclient.lib"
  )

# Import target "sioclient::sioclient_tls" for configuration "Release"
set_property(TARGET sioclient::sioclient_tls APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(sioclient::sioclient_tls PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/Release/sioclient_tls.lib"
  )

# Import target "sioclient::sioclient" for configuration "MinSizeRel"
set_property(TARGET sioclient::sioclient APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(sioclient::sioclient PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_MINSIZEREL "CXX"
  IMPORTED_LOCATION_MINSIZEREL "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/MinSizeRel/sioclient.lib"
  )

# Import target "sioclient::sioclient_tls" for configuration "MinSizeRel"
set_property(TARGET sioclient::sioclient_tls APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(sioclient::sioclient_tls PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_MINSIZEREL "CXX"
  IMPORTED_LOCATION_MINSIZEREL "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/MinSizeRel/sioclient_tls.lib"
  )

# Import target "sioclient::sioclient" for configuration "RelWithDebInfo"
set_property(TARGET sioclient::sioclient APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(sioclient::sioclient PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LOCATION_RELWITHDEBINFO "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/RelWithDebInfo/sioclient.lib"
  )

# Import target "sioclient::sioclient_tls" for configuration "RelWithDebInfo"
set_property(TARGET sioclient::sioclient_tls APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(sioclient::sioclient_tls PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELWITHDEBINFO "CXX"
  IMPORTED_LOCATION_RELWITHDEBINFO "C:/Users/SSAFY/Desktop/dev_ws/src/build/sioclient/RelWithDebInfo/sioclient_tls.lib"
  )

# This file does not depend on other imported targets which have
# been exported from the same project but in a separate export set.

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
cmake_policy(POP)
