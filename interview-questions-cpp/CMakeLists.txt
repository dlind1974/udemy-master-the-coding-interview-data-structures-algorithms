cmake_minimum_required(VERSION 3.14)  # Ensure minimum version for GoogleTest

# Set the project name and specify the C++ standard
project(InterviewQuestionsCpp VERSION 1.0 DESCRIPTION "Interview Test Suite" LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable testing functionalities in CMake
enable_testing()

# Include the FetchContent module which can download dependencies
include(FetchContent)

# Declare GoogleTest as a fetchable content
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG release-1.12.1  # You can adjust the version as needed
)

# Make GoogleTest available for use
FetchContent_MakeAvailable(googletest)

# Collect all .cpp files in the interview questions directories
file(GLOB TEST_SOURCES 
     "top-interview-questions/*.cpp"
     "google-interview-questions/*.cpp"
     "amazon-interview-questions/*.cpp")

# Define the test executable using the collected source files
add_executable(interview_test ${TEST_SOURCES})

# Link GoogleTest libraries to the test executable
target_link_libraries(interview_test gtest_main)

# Include GoogleTest's functionalities
include(GoogleTest)

# Automatically discover tests that are defined in GoogleTest test cases
gtest_discover_tests(interview_test)
