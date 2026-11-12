# `amr_localization`

Owns state estimation and global localization configuration. It fuses wheel odometry, IMU, GNSS, and SLAM/localization outputs into a documented TF chain suitable for navigation.

| Directory | Add |
| --- | --- |
| `config/` | EKF/UKF, GNSS, map-localization, and sensor-fusion parameters |
| `launch/` | Localization and state-estimation launch files |
| `maps/` | Curated static map assets and metadata used by localization |

Document the authority for each transform. The expected navigation chain is `map -> odom -> base_link`; only one component may publish each transform. Keep covariance, timestamp, and sensor-frame configuration explicit in YAML.
