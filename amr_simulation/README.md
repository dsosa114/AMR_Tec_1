# `amr_simulation`

Owns reproducible simulation scenarios for the AMR before field deployment. Simulation must exercise the same steering, traction, TF, sensor topics, and navigation interfaces used on the robot.

| Directory | Add |
| --- | --- |
| `launch/` | Simulator startup, robot spawn, and full-stack simulation launch files |
| `config/` | Simulator bridge, sensor-noise, and simulation-specific parameters |
| `models/` | Simulator-specific robot and environmental models |
| `worlds/` | Campus-representative simulation worlds |

Use `use_sim_time` throughout launch composition. Keep the simulated drivetrain constrained to the same one-steering-joint/one-traction-joint bicycle model as the physical description, and make frame/topic mappings match hardware deployment.
