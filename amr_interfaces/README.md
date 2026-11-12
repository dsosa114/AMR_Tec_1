# `amr_interfaces`

Contains project-specific ROS contracts shared across packages. Prefer standard ROS messages when they express the required data; add an interface here only when the project needs a stable custom contract.

| Directory | Add |
| --- | --- |
| `msg/` | Custom data messages |
| `srv/` | Request/response operations |
| `action/` | Long-running, cancelable operations |

When adding an interface, declare `rosidl_default_generators` and all referenced interface packages in `package.xml`, generate it in `CMakeLists.txt`, and add `rosidl_default_runtime` as an execution dependency. Keep interfaces transport-oriented and avoid package-specific implementation details.
