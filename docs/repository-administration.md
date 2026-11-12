# Repository administration

Configure these rules for the `main` branch through **Settings** > **Rules** > **Rulesets** (or branch protection rules if rulesets are unavailable). Apply the rules to administrators as well as contributors.

## Required branch rules

| Rule | Setting |
| --- | --- |
| Deletion | Restrict deletions |
| Pull requests | Require a pull request before merging |
| Approval | Require 1 approval |
| Approval freshness | Dismiss stale approvals when new commits are pushed |
| Review discussion | Require conversation resolution before merging |
| Status checks | Require status checks to pass and require branches to be up to date |
| Required check | Select `ROS 2 Humble CI / build-and-test` after its first successful run |
| Pushes | Block force pushes |
| History | Require linear history |

Under **Settings** > **General** > **Pull Requests**, enable **Allow squash merging** and disable merge-commit merging. Squash merges keep `main` linear and avoid requiring students to rebase feature branches.

## Deploy key

Keep the onboard computer deploy key **read-only**. It should fetch approved commits from `main` only; no robot or shared device needs write access to this repository.

## Administrator checks

1. Merge this workflow configuration through a pull request.
2. Confirm that the `ROS 2 Humble CI / build-and-test` check completes on the pull request.
3. Select that check in the branch rule only after GitHub has observed it.
4. Try a direct push to `main` from a non-administrator account to confirm it is rejected.
5. Confirm that a contributor can complete the GitHub Desktop flow in [the contributor guide](git-workflow.md).

The local `.githooks/pre-push` hook is a convenience guardrail, not a substitute for the GitHub rules: contributors can bypass local hooks, but protected branches cannot be bypassed by normal pushes.
