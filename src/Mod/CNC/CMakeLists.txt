add_subdirectory(libs/libarea/)

SET(CNCMain_SRCS
    InitGui.py
    CNCGui.py
)
SOURCE_GROUP("" FILES ${CNCMain_SRCS})

SET(CNCIcons_SRCS
    Icons/end_mill.png
    Icons/end_mill.xpm
)
SOURCE_GROUP("cncicons" FILES ${CNCIcons_SRCS})

SET(machining_ops_SRCS
    machining_ops/__init__.py
)
SOURCE_GROUP("machining_ops" FILES ${machining_ops_SRCS})

SET(utils_SRCS
    utils/__init__.py
    utils/Math.py
    utils/Paths.py
    utils/Translator.py
)
SOURCE_GROUP("utils" FILES ${utils_SRCS})

SET(libs_SO
    libs/libarea/area.so
)


SET(all_files ${CNCMain_SRCS} ${CNCIcons_SRCS} ${utils_SRCS} ${machining_ops_SRCS}  )

ADD_CUSTOM_TARGET(CNC ALL
    SOURCES ${all_files}
)

fc_copy_sources("Mod/CNC" "CNC" ${all_files})

INSTALL(
    FILES
        ${utils_SRCS}
    DESTINATION
        Mod/CNC/utils
)

INSTALL(
    FILES
        ${CNCIcons_SRCS}
    DESTINATION
        Mod/CNC/Icons
)

INSTALL(
    FILES
        ${machining_ops_SRCS}
    DESTINATION
        Mod/CNC/machining_ops
)

INSTALL(
    FILES
        ${CNCMain_SRCS}
    DESTINATION
        Mod/CNC
)

