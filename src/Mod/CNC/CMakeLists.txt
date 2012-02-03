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


#check to see if the machining_ops directory needs to be created
#and populated 
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/machining_ops/)
    message("CNC Workbench machining_ops directory is already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/machining_ops/)
    message("CNC Workbench machining_ops directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/machining_ops/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/machining_ops/)

#copy machining_ops
file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/machining_ops/*.py" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/machining_ops/ ${p} COPYONLY)
endforeach()


#check to see if the utils directory needs to be created
#and populated 
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/utils/)
    message("CNC Workbench utils directory is already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/utils/)
    message("CNC Workbench utils directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/utils/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/utils/)

#copy utils
file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/utils/*.py" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/utils/ ${p} COPYONLY)
endforeach()

#check to see if the Gui directory needs to be created
#and populated 
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Gui/)
    message("CNC Workbench Gui directory is already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Gui/)
    message("CNC Workbench Gui directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Gui/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/Gui/)

#copy Gui ui files
file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/Gui/*.ui" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/Gui/ ${p} COPYONLY)
endforeach()


#check to see if the backplot directory needs to be created
#and populated 
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/backplot/)
    message("CNC Workbench backplot directory is already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/backplot/)
    message("CNC Workbench backplot directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/backplot/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/backplot/)

#copy backplot files
file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/backplot/*.py" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/backplot/ ${p} COPYONLY)
endforeach()



#check to see if the tmp directory needs to be created
#and populated 
if(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/tmp/)
    message("CNC Workbench tmp directory is already there")
else(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/tmp/)
    message("CNC Workbench tmp directory does not exist")
    message("creating it now....")
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/tmp/)
endif(IS_DIRECTORY ${CMAKE_BINARY_DIR}/Mod/CNC/tmp/)

#I found that this needed to go towards the end of the script
#otherwise the *.so files weren't copied in
#recursively copy *.so libs into libs directory
file( GLOB_RECURSE pattern_files RELATIVE
  "${CMAKE_CURRENT_SOURCE_DIR}/" "${CMAKE_CURRENT_SOURCE_DIR}/libs/*.so" )
foreach(p IN LISTS pattern_files)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${p}
    ${CMAKE_BINARY_DIR}/Mod/CNC/libs/ ${p} COPYONLY)
endforeach()
