# Development environments

## Platform contract

The NVIDIA Jetson Orin Nano is the production reference platform. It runs Ubuntu 22.04 with ROS 2 Humble, which is the deployment API and ABI target. The optional second Orin Nano must use the same Humble environment when it hosts distributed workloads such as RTAB-Map.

Development hosts may use Ubuntu 24.04 with ROS 2 Jazzy for editing, simulation, and rapid iteration. A Jazzy build is not sufficient release validation: every change that will run on the Jetson must also build and test in Humble before deployment.

Do not source Humble and Jazzy in the same shell or share `build/`, `install/`, or `log/` directories between them. Use separate workspaces, worktrees, or containers for each distribution.

## Dependency strategy

`dependencies.repos` is the single pinned source manifest shared by Humble and Jazzy. It contains only the ZED wrapper because it depends on the vendor ZED SDK and is not managed as a standard ROS release dependency. The selected `humble-v5.1.0` release supports both Humble and Jazzy.

Import it into a dedicated external-source directory from the workspace root:

```bash
mkdir -p src/third_party
vcs import src/third_party < src/dependencies.repos
```

Install the ZED SDK version required by the manifest and the platform CUDA/JetPack packages before building the wrapper. On Jetson JetPack 6 installations, the wrapper additionally requires the `nvidia-jetpack` and `nvidia-jetpack-dev` packages.

Install released ROS dependencies through `rosdep` after packages that use them declare their dependencies:

```bash
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro "$ROS_DISTRO" -r -y
```

For the Humble Jetson image, use released packages for the sensor and localization stack instead of cloning duplicate source copies:

```bash
sudo apt install \
  ros-humble-velodyne \
  ros-humble-rtabmap-ros \
  ros-humble-robot-localization \
  ros-humble-nav2-bringup \
  ros-humble-rplidar-ros \
  ros-humble-ublox \
  ros-humble-nmea-navsat-driver \
  ros-humble-zed-msgs
```

The RPLidar and u-blox packages are optional because their sensors are optional. The BNO055 requires an AMR-owned ROS 2 driver in `amr_hardware`; do not add an Arduino library to this workspace as a substitute for that driver.

## Build matrix

| Environment | Purpose | Required validation |
| --- | --- | --- |
| Jetson Orin Nano / Humble | Robot deployment, hardware drivers, ZED, and field operation | Build and test all AMR packages; verify sensor and actuator integration on hardware |
| Secondary Orin Nano / Humble | Optional distributed RTAB-Map or perception workload | Build the matching Humble source revision; verify networked topic and TF behavior |
| Developer host / Jazzy | Editing, simulation, and non-hardware development | Build and test the workspace; do not treat it as Jetson deployment validation |

Use the same AMR source revision in both distributions. When an upstream source dependency no longer supports both distributions, add separate, explicitly pinned `dependencies.humble.repos` and `dependencies.jazzy.repos` files; do not change the production Humble pin to satisfy a Jazzy-only dependency.

## Package ownership

- `amr_hardware` owns Velodyne, ZED, BNO055, optional RPLidar, and optional u-blox device configuration and driver launch integration.
- `amr_perception` owns ZED/LiDAR calibration, synchronized processing, and SLAM-facing point-cloud/image products.
- `amr_localization` owns the BNO055, wheel odometry, and optional RTK GNSS fusion configuration, plus the `map -> odom -> base_link` TF contract.
- `amr_simulation` provides equivalent sensor topics and the same frame and command interfaces without vendor hardware dependencies.

Add a package dependency to both `package.xml` and `CMakeLists.txt` only when that package actually launches, links, or imports the corresponding ROS component.
