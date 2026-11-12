# Quick reference

## Preferred visual tools

| Task | Tool |
| --- | --- |
| Create, publish, and switch branches | GitHub Desktop |
| Review changed files and create commits | VS Code Source Control |
| Create pull requests and respond to reviews | VS Code GitHub Pull Requests or github.com |
| Run first-time workspace setup | VS Code task: **AMR: Set up workspace** |

## Copy-and-paste commands

Use these only when the visual tool is unavailable.

```bash
# See what changed
git status

# Create a feature branch from the current main branch
git switch main
git pull --ff-only
git switch -c feature/short-description

# Save a change on the feature branch
git add <file>
git commit -m "Describe the change"
git push -u origin feature/short-description

# Build and test from the workspace root (the parent of this repository)
colcon build --symlink-install
colcon test
colcon test-result --verbose
```

Do not use `git push --force`, `git rebase`, or `git reset --hard` during the sprint. If GitHub says a pull request is behind `main`, use **Update branch** on the pull-request page.

## If something goes wrong

| Situation | Safe action |
| --- | --- |
| The local push is blocked | Check that you are on a feature branch, then publish/open a pull request |
| A pull request is behind `main` | Use **Update branch** on GitHub |
| CI fails | Open the failed `ROS 2 Humble CI` job, fix the reported file, commit, and push the feature branch |
| You are unsure whether a command is safe | Stop and ask the project mentor before running it |
