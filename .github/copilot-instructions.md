# AMR Tec 1 Copilot Instructions

## Workspace commands

This repository is the `src/` directory of a ROS 2 workspace. Run `colcon` commands from its parent directory:

```bash
cd ..
colcon build
colcon test
colcon test-result --verbose
```

Build or test one package with:

```bash
colcon build --packages-select amr_bringup
colcon test --packages-select amr_bringup
```

To run one CTest test after building, use its CTest name or a regex:

```bash
colcon test --packages-select amr_bringup --ctest-args -R '<test-name-or-regex>'
```

The packages currently declare only `ament_lint_auto` test dependencies, so package testing runs the auto-discovered ament linters; no named application tests or standalone formatter command exist yet.

## Architecture

The workspace is organized as ROS 2 `ament_cmake` packages with clear subsystem boundaries:

- `amr_bringup` composes deployment launch files, parameters, and RViz profiles.
- `amr_control` owns Ackermann/bicycle-model controller configuration.
- `amr_description` owns URDF/Xacro, meshes, frames, and model visualization.
- `amr_hardware` owns hardware drivers and `ros2_control` hardware interfaces.
- `amr_interfaces` owns project-specific messages, services, and actions.
- `amr_localization` owns state estimation, localization configuration, and maps.
- `amr_navigation` owns Nav2 configuration, behavior trees, and waypoint navigation assets.
- `amr_perception` owns LiDAR/camera processing, calibration, and SLAM-facing assets.
- `amr_simulation` owns simulator configuration, models, worlds, and launch files.

The packages install their shareable asset directories but remain implementation scaffolds: there are no package-to-package dependencies, nodes, plugins, generated interfaces, or launch definitions yet. Add dependencies consistently to both the relevant `package.xml` and `CMakeLists.txt` as packages become connected.

## Package conventions

- Update the root `README.md` as the workspace gains implemented packages, dependencies, build steps, or operational workflows so it reflects the repository's current state.
- Keep each package as `ament_cmake` (package format 3) and preserve its package name in both `project(...)` and `<name>`.
- Use `.gitkeep` files to retain intentionally empty asset directories; do not use `COLCON_IGNORE` inside a package, because it prevents colcon from discovering that directory.
- The CMake templates apply `-Wall -Wextra -Wpedantic` for GCC and Clang; new C++ code must build cleanly with these flags.
- Tests are activated through `BUILD_TESTING` and discovered with `ament_lint_auto_find_test_dependencies()`. Add test/lint dependencies to the package's `package.xml`, rather than manually duplicating dependency lists in CMake.
- Copyright and `cpplint` checks are explicitly marked as found in every package's test block. Keep those settings aligned across packages unless intentionally enabling those checks repository-wide.
