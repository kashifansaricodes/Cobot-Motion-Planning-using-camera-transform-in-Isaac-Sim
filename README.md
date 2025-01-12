# Cobot Simulation and Motion Planning using camera transform in Isaac Sim  

## Overview  
This project demonstrates the development and testing of a collaborative robot (Cobot) simulation environment using Isaac Sim and ROS 2. The work includes setting up a realistic simulation, integrating MoveIt for motion planning, and testing advanced robotic motion scenarios.  

---
![image](https://github.com/user-attachments/assets/716a5dfa-55d3-46b1-b43a-0954e05bcb8f)

![image](https://github.com/user-attachments/assets/f5073d00-8a4f-4fe7-8f37-7a6aafa9d9e8)

![image](https://github.com/user-attachments/assets/f650168a-e2ec-411a-80c4-836cfdc8d82a)
---


## Key Achievements  
1. **Simulation Environment Setup**  
   - Imported assets such as a manipulator, table, and objects (e.g., fruits) into Isaac Sim.  
   - Defined rigidity and colloidal presets to simulate realistic interactions and collisions.  

2. **MoveIt Integration**  
   - Installed and tested MoveIt with the Franka Emika Panda and UR3 robots in RViz and Isaac Sim.  
   - Configured kinematic models, motion planning parameters, and planner algorithms for UR3.  

3. **Action Graphs for ROS 2 Integration**  
   - Developed action graphs to enable cross-communication between ROS 2 (MoveIt) and Isaac Sim.  
   - Ensured real-time data exchange for motion planning and robot state updates.  

4. **Differential Drive Robot Control**  
   - Built and optimized action graphs for visual scripting and control of a differential drive mobile robot.  
   - Enhanced capabilities for motion execution, sensor data processing, and decision-making.  

5. **Cross-Platform Testing**  
   - Enabled seamless cross-communication between RViz and Isaac Sim using custom ROS nodes.  
   - Validated motion planning and execution across platforms with real-time updates.  

## Planned Strategies  
- Use an RGB depth camera to capture 360° video and extract frames for CNN training.  
- Train the network to identify and locate apples within the simulation environment.  
- Leverage depth sensing to calculate the distance and orient the robot end effector toward the target.  

## Challenges and Learnings  
- Overcame ROS debugging complexities and limited online resources for Isaac Sim.  
- Gained insights into integrating emerging simulation tools with traditional robotic frameworks.  

## Skills Demonstrated  
- Isaac Sim, ROS 2, MoveIt, RViz, Motion Planning, Visual Scripting, CNN Training, Depth Sensing.  

For more details and visuals, visit the [Google Drive folder](https://drive.google.com/drive/folders/1hRI_1AgbNIawvDGQ_VaMHWF7d1ilYS5R?usp=sharing).  
