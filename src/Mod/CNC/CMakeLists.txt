#CNC Workbench cmake lists

#build C++ libs for machining
#libarea for profiling and pocketing
add_subdirectory(libs/libarea)

#I want to use 'if(IS_DIRECTORY....' form to make
#it easier to populate directories, without having to list
#all the scripts by hand

#make directory for libs- if it isn't there already
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/libs/)
    message("CNC Workbench libs directory is already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/libs/)
    message("CNC Workbench libs directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/libs/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/libs/)

#check to see if the posts directory needs to be created
#and populated with post files
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/posts/)
    message("posts directory already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/posts/)
    message("CNC posts directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/posts/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/posts/)

file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/posts/*.py" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/posts/ ${p} COPYONLY)
endforeach()

#copy python files in parent directory
file( GLOB pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/*.py" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/ ${p} COPYONLY)
endforeach()

#check to see if the Icons directory needs to be created
#and populated 
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Icons/)
    message("CNC Workbench Icons directory is already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Icons/)
    message("CNC Workbench Icons directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Icons/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Icons/)

#copy icons
file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/Icons/*" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/Icons/ ${p} COPYONLY)
endforeach()


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
        ${machining_ops_SRCS}
    DESTINATION
        Mod/CNC/machining_ops
)




#I found that this needed to go towards the end of the script
#otherwise the *.so files weren't copied in
#recursively copy *.so libs into libs directory
file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/libs/*.so" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/libs/ ${p} COPYONLY)
endforeach()
