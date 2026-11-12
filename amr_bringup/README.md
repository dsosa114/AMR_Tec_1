# `amr_bringup`

Owns the launch compositions used for simulation, development, and real robot deployment. Keep dependency-specific launch files here rather than making users start individual subsystem nodes manually.

| Directory | Add |
| --- | --- |
| `launch/` | Top-level launch files that compose description, hardware/control, perception, localization, and navigation |
| `config/` | Deployment parameters, remappings, and robot-specific overrides |
| `rviz/` | RViz configurations used by launch files |

Launch files should expose `use_sim_time`, namespace, frame, and parameter-file arguments where applicable. Hardware-only settings belong in `amr_hardware`; Nav2, localization, and perception settings stay in their respective packages.
