INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_BURSTREAM burstream)

FIND_PATH(
    BURSTREAM_INCLUDE_DIRS
    NAMES burstream/api.h
    HINTS $ENV{BURSTREAM_DIR}/include
        ${PC_BURSTREAM_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    BURSTREAM_LIBRARIES
    NAMES gnuradio-burstream
    HINTS $ENV{BURSTREAM_DIR}/lib
        ${PC_BURSTREAM_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/burstreamTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(BURSTREAM DEFAULT_MSG BURSTREAM_LIBRARIES BURSTREAM_INCLUDE_DIRS)
MARK_AS_ADVANCED(BURSTREAM_LIBRARIES BURSTREAM_INCLUDE_DIRS)
