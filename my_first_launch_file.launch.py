
# REMEMBER THAT IF THE PACKAGE OR EXECUTABLE DOES NOT MATCH YOUR DIRECTORY, IT WILL NOT WORK.
# Please alter the file name correctly: 'package', 'executable', and 'name' ('name' is optional but recommended to change).

import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_package',
            executable='simple_publisher',
            name='publisher_node'
        ),
        Node(
            package='my_first_package',
            executable='simple_subscriber',
            name='subscriber_node'
        )
    ])
