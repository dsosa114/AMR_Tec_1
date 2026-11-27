import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

PKG = 'amr_localization'


def generate_launch_description():
    ekf_yaml = os.path.join(get_package_share_directory(PKG), 'config', 'ekf.yaml')

    return LaunchDescription([
        DeclareLaunchArgument('serial_port', default_value='/dev/ttyACM0'),
        DeclareLaunchArgument('baud', default_value='115200'),

        Node(package=PKG, executable='sensor_node.py', name='sensor_node',
             parameters=[{'port': LaunchConfiguration('serial_port'),
                          'baud': LaunchConfiguration('baud')}]),

        # IMU mounting (x y z yaw pitch roll parent child) - adjust to your mounting
        Node(package='tf2_ros', executable='static_transform_publisher',
             arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'imu_link']),

        Node(package='robot_localization', executable='ekf_node',
             name='ekf_filter_node', output='screen',
             parameters=[ekf_yaml],
             remappings=[('odometry/filtered', '/odometry/filtered')]),
    ])
