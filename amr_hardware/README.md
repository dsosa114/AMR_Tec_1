# `amr_hardware`

Owns hardware-facing ROS 2 nodes and `ros2_control` hardware interfaces for the vehicle, LiDAR, cameras, IMU, GNSS, and safety I/O. It converts device protocols into ROS interfaces without embedding navigation policy.

| Directory | Add |
| --- | --- |
| `include/amr_hardware/` | Public C++ headers for drivers and hardware plugins |
| `src/` | Driver implementations and `ros2_control` hardware plugin sources |
| `config/` | Device ports, calibration paths, safety limits, and hardware parameters |

Export plugin metadata and install it through CMake when adding a `ros2_control` hardware plugin. The actuator interface must expose the single traction and steering command paths used by `amr_control`; enforce hardware limits here as the last safety boundary.
