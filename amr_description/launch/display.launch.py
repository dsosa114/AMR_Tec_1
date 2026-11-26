from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
import os
from ament_index_python.packages import get_package_share_path


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')
    use_jsp_gui = LaunchConfiguration('use_jsp_gui')
    use_ros_control = LaunchConfiguration('use_ros_control')
    use_mock_system = LaunchConfiguration('use_mock_system')

    urdf_path = os.path.join(get_package_share_path('amr_description'),
                             'urdf', 'amr.urdf')

    rviz_config_path = os.path.join(get_package_share_path('amr_description'),
                                    'rviz', 'display_config.rviz')

    robot_description = ParameterValue(Command(['xacro ', urdf_path,
                                                ' ',
                                                'use_ros_control:=',
                                                use_ros_control,
                                                ' ',
                                                'use_mock_system:=',
                                                use_mock_system,
                                                ]), value_type=str)

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description, 'use_sim_time': use_sim_time}]
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        condition=IfCondition(
            PythonExpression(
                ["'", use_jsp_gui, "' == 'true' and '", use_ros_control, "' == 'false'"])
        ),
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),
        DeclareLaunchArgument(
            'use_jsp_gui',
            default_value='true',
            description='Activate joint_state_publisher_gui if true'
        ),
        DeclareLaunchArgument(
            'use_ros_control',
            default_value='false',
            description='Activate ros_control if true'
        ),
        DeclareLaunchArgument(
            'use_mock_system',
            default_value='true',
            description='Activate mock system if true'
        ),
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])
