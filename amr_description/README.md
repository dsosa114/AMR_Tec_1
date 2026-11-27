# `amr_description`

Defines the canonical physical and kinematic model of the AMR Tec 1. The model represents the four-wheeled Ackermann-steered platform with integrated inertia, collision geometry, and mounted sensors.

## Directory Structure

| Directory | Purpose |
| --- | --- |
| `urdf/` | URDF/Xacro robot model with links, joints, inertial properties, and sensor mounts |
| `meshes/` | Visual and collision geometry (STL) for chassis, wheels, and sensors |
| `config/` | Robot-description parameters and frame configuration (reserved for expansion) |
| `rviz/` | RViz configurations for model visualization and frame inspection |
| `launch/` | Launch files for model display and testing |

## Model Components

### Chassis and Drivetrain
- **Base Frame:** `base_link` (robot body) over `base_footprint` (ground reference)
- **Wheels:** Four continuous wheels with rolling dynamics
  - Front right/left: `front_right_wheel_link`, `front_left_wheel_link`
  - Rear right/left: `rear_right_wheel_link`, `rear_left_wheel_link`
- **Inertia:** Computed from CAD geometry with center-of-mass offsets

### Integrated Sensors
- **Velodyne VLP-16:** `Lidar-link` (3D point cloud)
- **Stereolabs ZED 2i:** `ZED_link` (stereo depth and RGB)
- **Bosch BNO055 IMU:** `Imu_link` (9-DOF IMU)
- **u-blox ZED-F9P (optional):** `RTK_link` (RTK GNSS)

## Usage

Visualize the model in RViz:

```bash
ros2 launch amr_description display.launch.py
```

## Coordination

Maintain consistency in frame names, joint names, wheelbase, steering/traction configuration, and collision geometry across:
- `amr_control` (controller configuration)
- `amr_hardware` (hardware drivers and actuators)
- `amr_simulation` (simulator models and physics)
