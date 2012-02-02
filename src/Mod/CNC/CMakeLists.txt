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

SET(Machining_SRCS
    Machining/__init__.py
)
SOURCE_GROUP("Machining" FILES ${Machining_SRCS})

SET(utils_SRCS
    utils/__init__.py
    utils/Math.py
    utils/Paths.py
    utils/Translator.py
)
SOURCE_GROUP("utils" FILES ${utils_SRCS})

SET(all_files ${CNCMain_SRCS} ${CNCIcons_SRCS} ${utils_SRCS} ${Machining_SRCS})

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
        ${Machining_SRCS}
    DESTINATION
        Mod/CNC/Machining
)

INSTALL(
    FILES
        ${CNCMain_SRCS}
    DESTINATION
        Mod/CNC
)

