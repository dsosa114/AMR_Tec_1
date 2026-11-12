# `amr_description`

Defines the canonical physical and kinematic model of the AMR. The model must represent the mechanically coupled Ackermann drivetrain through the equivalent bicycle model: one steering joint and one traction joint.

| Directory | Add |
| --- | --- |
| `urdf/` | URDF/Xacro robot definition, links, joints, transmissions, and inertial properties |
| `meshes/` | Version-controlled visual and collision geometry referenced by the robot model |
| `config/` | Robot-description parameters and joint/frame configuration |
| `rviz/` | RViz displays for model and TF inspection |

Keep frame names, joint names, wheelbase, steering limits, and collision geometry consistent with `amr_control`, `amr_hardware`, and `amr_simulation`. Use `base_link` as the robot body frame and add sensor frames through fixed transforms in the model.
