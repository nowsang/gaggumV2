#----------------------------------------------------------------
# Generated CMake target import file for configuration "MinSizeRel".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "sioclient::sioclient" for configuration "MinSizeRel"
set_property(TARGET sioclient::sioclient APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(sioclient::sioclient PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_MINSIZEREL "CXX"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/lib/sioclient.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS sioclient::sioclient )
list(APPEND _IMPORT_CHECK_FILES_FOR_sioclient::sioclient "${_IMPORT_PREFIX}/lib/sioclient.lib" )

# Import target "sioclient::sioclient_tls" for configuration "MinSizeRel"
set_property(TARGET sioclient::sioclient_tls APPEND PROPERTY IMPORTED_CONFIGURATIONS MINSIZEREL)
set_target_properties(sioclient::sioclient_tls PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_MINSIZEREL "CXX"
  IMPORTED_LOCATION_MINSIZEREL "${_IMPORT_PREFIX}/lib/sioclient_tls.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS sioclient::sioclient_tls )
list(APPEND _IMPORT_CHECK_FILES_FOR_sioclient::sioclient_tls "${_IMPORT_PREFIX}/lib/sioclient_tls.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
