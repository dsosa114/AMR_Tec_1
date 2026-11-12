# Git workflow for contributors

Use GitHub Desktop or the VS Code **Source Control** and **GitHub Pull Requests** views. You do not need to use `git rebase`, force-push, or `vcs` commands during normal project work.

## First-time setup

1. Clone the repository into the `src/` directory of a ROS 2 workspace with GitHub Desktop.
2. Open the repository folder in VS Code and install the recommended extensions when prompted.
3. In VS Code, run **Terminal: Run Task**, then select **AMR: Set up workspace**. This enables the local Git push guardrails, installs declared ROS dependencies, and builds the workspace.
4. On the Jetson, source ROS 2 Humble before running setup. On Ubuntu 24.04 development machines, source ROS 2 Jazzy. See [development environments](development-environments.md).

## Everyday contribution flow

1. In GitHub Desktop, select **Current Branch** > **New Branch**. Use names such as `feature/zed-launch`, `fix/imu-frame`, or `docs/git-guide`.
2. Make changes, then use the **Source Control** view to review, stage, and commit them with a short description.
3. Select **Publish Branch** in GitHub Desktop or VS Code.
4. Create a pull request using the GitHub Desktop prompt or the VS Code GitHub Pull Requests view. The template prompts for the build/test result.
5. Address review comments and wait for **ROS 2 Humble CI** to pass.
6. When GitHub reports that the branch is behind `main`, use the pull-request page's **Update branch** button. Do not force-push or run a rebase.
7. After one approval and all conversations are resolved, use **Squash and merge** in the GitHub pull-request page.

Never push directly to `main`. The local hook blocks it, and the repository rules must also reject it.

## Onboard computer workflow

The onboard computer uses a read-only deploy key. It may fetch and fast-forward to approved `main` changes, but it cannot push:

```bash
git switch main
git pull --ff-only
```

Run this only from a clean checkout. Hardware configuration that must remain local belongs outside the repository or in an ignored, machine-specific configuration file.
