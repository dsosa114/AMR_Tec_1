# `amr_navigation`

Owns Nav2 configuration for collision-free Ackermann navigation between campus waypoints. It consumes the localization TF chain and perception-derived obstacle data; it does not own sensor drivers or localization filters.

| Directory | Add |
| --- | --- |
| `config/` | Nav2 planner, controller, costmap, recovery, velocity-smoothing, and waypoint parameters |
| `launch/` | Nav2 and waypoint-execution launch compositions |
| `behavior_trees/` | Project-specific Nav2 behavior trees |
| `maps/` | Navigation map assets and map-server metadata |

Configure a non-holonomic controller appropriate for Ackermann motion, realistic footprint/collision geometry, obstacle sources, speed limits, and stopping behavior. Keep the global frame `map` and robot base frame consistent with `amr_description` and `amr_localization`.
