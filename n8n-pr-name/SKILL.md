---
name: n8n-pr-name
description: Generate n8n-compliant PR title following their conventions
allowed-tools: Bash(git diff:*), Bash(git status:*), Bash(git log:*), Bash(cat:*), Bash(ls:*), Bash(find:*)
---

# Context

-   Uncommitted changes: !`git diff --name-only`
-   Staged changes: !`git diff --cached --name-only`
-   Full diff: !`git diff`
-   Recent commits not pushed: !`git log @{u}..HEAD --oneline 2>/dev/null || git log -5 --oneline`

# n8n PR Title Convention

Format: `<type>(<scope>): <summary>`

## Types (required):

-   `feat` — New feature
-   `fix` — Bug fix
-   `refactor` — Code restructuring (no behavior change)
-   `perf` — Performance improvement
-   `test` — Adding/updating tests
-   `docs` — Documentation only
-   `build` — Build system or dependencies
-   `ci` — CI configuration (GitHub Actions, etc.)
-   `chore` — Maintenance tasks

## Scopes (required):

-   `core` — Core n8n functionality
-   `editor` — Frontend/UI changes
-   `cli` — CLI-related changes
-   `API` — API changes
-   `benchmark` — Benchmark related
-   `* Node` — Node-specific changes (e.g., `Slack Node`, `HTTP Request Node`)

**Node-specific scope:** If modified files are inside `packages/nodes-base/nodes/<NodeName>/`, use the node's display name as scope (e.g., `Slack Node`, `HTTP Request Node`, `Loop Over Items Node`). Check the node's `displayName` property in the `.node.ts` file if unsure.

## Summary rules:

-   Imperative present tense ("Add feature" not "Added feature")
-   Capitalized first letter
-   No period at the end
-   Keep it concise but descriptive

## Examples:

-   `feat(editor): Add dark mode toggle`
-   `fix(Slack Node): Handle rate limiting correctly`
-   `refactor(core): Simplify credential encryption logic`
-   `test(HTTP Request Node): Add tests for binary data handling`
-   `docs(API): Update webhook documentation`

# Task

Analyze the code changes above and generate a PR title that:

1. Uses the correct type based on what changed
2. Uses the correct scope based on which part of n8n was modified
3. Has a clear, imperative summary

Output ONLY the PR title, nothing else. Example output:
`feat(editor): Add workflow tags filtering`
