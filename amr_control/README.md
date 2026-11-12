# `amr_control`

Owns the control-layer configuration that turns motion commands into the AMR's equivalent bicycle-model steering and traction commands. Use this package for `ros2_control` controller setup and control-specific launch composition.

| Directory | Add |
| --- | --- |
| `config/` | Controller manager, Ackermann/bicycle-model parameters, joint limits, and controller YAML |
| `launch/` | Controller startup and spawner launch files |

Use the steering and traction joint names defined by `amr_description`; do not duplicate kinematic constants with conflicting values. Integrate with `ackermann_steering_controller` or an equivalent controller only after declaring its dependencies in this package.
