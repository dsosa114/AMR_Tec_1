# AMR Tec 1

AMR Tec 1 is a collaborative Mechatronics Engineering and research project targeting real-world autonomous Ackermann navigation with ROS 2 Humble. The robot will use a mechanically coupled steering/traction drivetrain modeled as a bicycle model, 3D visual/LiDAR SLAM, and collision-free outdoor navigation between campus waypoints.

## Workspace layout

| Package | Responsibility |
| --- | --- |
| `amr_bringup` | Deployment launch files, configuration, and RViz startup profiles |
| `amr_control` | Ackermann/bicycle-model control configuration and controller integration |
| `amr_description` | URDF/Xacro model, meshes, frame configuration, and RViz assets |
| `amr_hardware` | Hardware drivers, actuator/sensor integration, and hardware parameters |
| `amr_interfaces` | Project-specific ROS messages, services, and actions |
| `amr_localization` | State estimation, localization, and map-related configuration |
| `amr_navigation` | Nav2 configuration, behavior trees, and waypoint navigation assets |
| `amr_perception` | LiDAR/camera processing, calibration, and SLAM-facing perception assets |
| `amr_simulation` | Simulation launch files, robot/world models, and simulator configuration |

## Build and test

This repository is the `src/` directory of a ROS 2 workspace. From its parent directory:

```bash
colcon build
colcon test
colcon test-result --verbose
```

Build or test a single package with `colcon build --packages-select <package>` or `colcon test --packages-select <package>`.

The packages are currently structural scaffolds. Add a dependency to both a package's `package.xml` and `CMakeLists.txt` when implementing a node, plugin, interface, or launch integration.

## Platform compatibility

The Jetson deployment target uses ROS 2 Humble, while development hosts may use ROS 2 Jazzy. Follow the [development-environment guide](docs/development-environments.md) for the compatibility policy, pinned external source import, released sensor/localization dependencies, and validation matrix.