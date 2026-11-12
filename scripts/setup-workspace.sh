#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/setup-workspace.sh [--with-zed] [--skip-build]

Run this script from any location. By default it configures the Git guardrails,
installs ROS package dependencies with rosdep, and builds the workspace.

  --with-zed    Import the pinned ZED wrapper after the ZED SDK is installed.
  --skip-build  Configure the workspace without running colcon build.
EOF
}

with_zed=false
skip_build=false

while (($#)); do
  case "$1" in
    --with-zed)
      with_zed=true
      ;;
    --skip-build)
      skip_build=true
      ;;
    --help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown option: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd -- "$script_dir/.." && pwd)"
workspace_root="$(cd -- "$repository_root/.." && pwd)"

if [[ -z "${ROS_DISTRO:-}" ]]; then
  for candidate in jazzy humble; do
    if [[ -f "/opt/ros/$candidate/setup.bash" ]]; then
      ROS_DISTRO="$candidate"
      break
    fi
  done
fi

if [[ "${ROS_DISTRO:-}" != "humble" && "${ROS_DISTRO:-}" != "jazzy" ]]; then
  cat >&2 <<'EOF'
ROS 2 Humble or Jazzy is required. Install one distribution, then source its
/opt/ros/<distribution>/setup.bash file before running this script.
EOF
  exit 1
fi

source "/opt/ros/$ROS_DISTRO/setup.bash"

for command in colcon git rosdep; do
  if ! command -v "$command" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$command" >&2
    printf 'Install the setup tools described in docs/quick-reference.md, then run this script again.\n' >&2
    exit 1
  fi
done

git -C "$repository_root" config core.hooksPath "$repository_root/.githooks"
git -C "$repository_root" config pull.ff only
git -C "$repository_root" config push.default simple
git -C "$repository_root" config fetch.prune true

if "$with_zed"; then
  if ! command -v vcs >/dev/null 2>&1; then
    printf 'Missing required command for --with-zed: vcs\n' >&2
    printf 'Install python3-vcstool, then run this script again.\n' >&2
    exit 1
  fi

  third_party_root="$repository_root/third_party"
  if [[ ! -d "$third_party_root/zed-ros2-wrapper/.git" ]]; then
    mkdir -p "$third_party_root"
    vcs import "$third_party_root" < "$repository_root/dependencies.repos"
  fi
fi

rosdep update
rosdep install \
  --from-paths "$workspace_root/src" \
  --ignore-src \
  --rosdistro "$ROS_DISTRO" \
  -r \
  -y

if ! "$skip_build"; then
  (
    cd "$workspace_root"
    colcon build --symlink-install
  )
fi

printf 'Workspace setup complete for ROS 2 %s.\n' "$ROS_DISTRO"
