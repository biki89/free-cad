add_subdirectory(libs/libarea/)

SET(posts_SRCS
    posts/nc.py
    posts/nc_read.py
    posts/iso.py
    posts/iso_read.py
    posts/iso_codes.py
    posts/iso_crc.py
    posts/iso_crc_read.py
    posts/iso_modal.py
    posts/iso_modal_read.py
    posts/centroid1.py
    posts/centroid1_read.py
    posts/emc2.py
    posts/emc2_read.py

)
SOURCE_GROUP("posts" FILES ${posts_SRCS})


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

SET(cnc_LIBS
    libs/libarea/area.so
)


SET(all_files ${CNCMain_SRCS} ${CNCIcons_SRCS} ${utils_SRCS} ${machining_ops_SRCS} ${posts_SRCS} )

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
        ${cnc_LIBS}
    DESTINATION
        Mod/CNC/
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
        ${posts_SRCS}
    DESTINATION
        Mod/CNC/posts
)



INSTALL(
    FILES
        ${CNCMain_SRCS}
    DESTINATION
        Mod/CNC
)

