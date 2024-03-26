cmake_minimum_required(VERSION 3.22)
project(ur3_moveit_config)

find_package(ament_cmake REQUIRED)

ament_package()
#Install python scripts
install(PROGRAMS
  scripts/joint_pub.py
  DESTINATION lib/${PROJECT_NAME}
)
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION share/${PROJECT_NAME})
install(FILES .setup_assistant DESTINATION share/${PROJECT_NAME})
