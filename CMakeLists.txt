cmake_minimum_required(VERSION 3.14.0 FATAL_ERROR)
project(Cmake_in_ml VERSION 0.1.0 LANGUAGES NONE)

SET(IRIS_URL "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" CACHE STRING "URL to the IRIS data")
set(IRIS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/data/raw)
set(IRIS_FILE ${IRIS_DIR}/iris.csv)
ADD_CUSTOM_COMMAND(OUTPUT ${IRIS_FILE}
    COMMAND ${CMAKE_COMMAND} -E echo "Downloading IRIS."
    COMMAND python src/data/download.py ${IRIS_URL} ${IRIS_FILE}
    COMMAND ${CMAKE_COMMAND} -E echo "Done. Checkout ${IRIS_FILE}."
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    )
ADD_CUSTOM_TARGET(rawdata ALL DEPENDS ${IRIS_FILE})

###############################################
# Alternative way of cleaning processed.xlsx
###############################################
# SET(PROCESSED_FILE ${CMAKE_CURRENT_SOURCE_DIR}/data/processed/processed.pickle)
# ADD_CUSTOM_COMMAND(OUTPUT ${PROCESSED_FILE}
#     COMMAND python src/data/preprocess.py ${IRIS_FILE} ${PROCESSED_FILE} --excel data/processed/processed.xlsx
#     WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#     DEPENDS rawdata
#     )
# ADD_CUSTOM_TARGET(preprocess DEPENDS rawdata)
# # Additional files to clean 
# set_property(DIRECTORY PROPERTY ADDITIONAL_MAKE_CLEAN_FILES
#     ${CMAKE_CURRENT_SOURCE_DIR}/data/processed/processed.xlsx
#     )
###############################################

LIST(APPEND PROCESSED_FILE "${CMAKE_CURRENT_SOURCE_DIR}/data/processed/processed.pickle"
    "${CMAKE_CURRENT_SOURCE_DIR}/data/processed/processed.xlsx"
    )
ADD_CUSTOM_COMMAND(OUTPUT ${PROCESSED_FILE}
    COMMAND python src/data/preprocess.py ${IRIS_FILE} data/processed/processed.pickle --excel data/processed/processed.xlsx
    COMMAND ${CMAKE_COMMAND} -E echo "Done. Checkout ${PROCESSED_FILE}."
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS rawdata ${IRIS_FILE}
    )
ADD_CUSTOM_TARGET(preprocess DEPENDS ${PROCESSED_FILE})

SET(EXPLORATORY_IMG ${CMAKE_CURRENT_SOURCE_DIR}/reports/figures/exploratory.png)
ADD_CUSTOM_COMMAND(OUTPUT ${EXPLORATORY_IMG}
    COMMAND python src/visualization/exploratory.py ${PROCESSED_FILE} ${EXPLORATORY_IMG}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS ${PROCESSED_FILE}
    )
ADD_CUSTOM_TARGET(exploratory DEPENDS ${EXPLORATORY_IMG})
