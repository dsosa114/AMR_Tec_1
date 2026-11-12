# `amr_perception`

Owns LiDAR and camera processing that supports 3D visual/LiDAR SLAM, obstacle observation, and sensor calibration. Device acquisition remains in `amr_hardware`; this package transforms synchronized ROS data into perception products.

| Directory | Add |
| --- | --- |
| `config/` | Point-cloud, image, SLAM, synchronization, and obstacle-processing parameters |
| `launch/` | Perception and SLAM launch files |
| `calibration/` | Camera intrinsics and LiDAR-camera extrinsics |
| `models/` | Versioned inference or reconstruction models and their metadata |

Use the sensor frames from `amr_description`, preserve message timestamps through processing, and publish data with explicit frame IDs. Keep large learned-model artifacts out of Git unless the team explicitly adopts an artifact-management process.
