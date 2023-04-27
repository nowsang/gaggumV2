#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "sioclient::sioclient" for configuration "Debug"
set_property(TARGET sioclient::sioclient APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(sioclient::sioclient PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/sioclient.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS sioclient::sioclient )
list(APPEND _IMPORT_CHECK_FILES_FOR_sioclient::sioclient "${_IMPORT_PREFIX}/lib/sioclient.lib" )

# Import target "sioclient::sioclient_tls" for configuration "Debug"
set_property(TARGET sioclient::sioclient_tls APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(sioclient::sioclient_tls PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/sioclient_tls.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS sioclient::sioclient_tls )
list(APPEND _IMPORT_CHECK_FILES_FOR_sioclient::sioclient_tls "${_IMPORT_PREFIX}/lib/sioclient_tls.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
