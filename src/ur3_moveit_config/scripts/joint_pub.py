#!/usr/bin/env python3

import rclpy
from sensor_msgs.msg import JointState

joints_dict = {}


def joint_states_callback(message):
    global joints_dict

    joint_commands = JointState()

    joint_commands.header = message.header

    for i, name in enumerate(message.name):
        # Storing arm joint names and positions
        joints_dict[name] = message.position[i]

    joint_commands.name = list(joints_dict.keys())
    joint_commands.position = list(joints_dict.values())
    print(joint_commands)
    # Publishing combined message containing all arm and finger joints
    pub.publish(joint_commands)


def main():
    global pub

    rclpy.init()
    node = rclpy.create_node("fetch_combined_joints_publisher")
    pub = node.create_publisher(JointState, "/joint_command", 1)
    node.create_subscription(JointState, "/joint_states", joint_states_callback, 1)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

