---
name: docs-update
description: Update CLAUDE.md, README.md, and CLAUDE_CHANGELOG.md with recent changes
allowed-tools: Bash(git diff:*), Bash(git status:*), Bash(cat:*), Bash(test:*), Bash(date:*), Bash(ls:*)
---

# Context
- Today's date: !`date +%Y-%m-%d`
- Uncommitted changes: !`git diff --name-only`
- Staged changes: !`git diff --cached --name-only`
- Full diff: !`git diff`
- CLAUDE.md exists: !`test -f CLAUDE.md && echo "yes" || echo "no"`
- CLAUDE.md content: !`test -f CLAUDE.md && cat CLAUDE.md || echo "n/a"`
- README.md exists: !`test -f README.md && echo "yes" || echo "no"`
- README.md content: !`test -f README.md && cat README.md || echo "n/a"`
- CLAUDE_CHANGELOG.md exists: !`test -f CLAUDE_CHANGELOG.md && echo "yes" || echo "no"`
- CLAUDE_CHANGELOG.md recent: !`test -f CLAUDE_CHANGELOG.md && head -80 CLAUDE_CHANGELOG.md || echo "n/a"`

# Task
Review the recent changes and update the documentation files accordingly.

## 1. CLAUDE.md
Update with any changes relevant to Claude's understanding of the project:
- New or modified API endpoints
- Changed file structure or architecture
- New dependencies or tools
- Updated coding conventions or patterns
- New environment variables or configuration

Keep the existing structure and style. Only add/modify sections that are affected by the changes.

## 2. README.md
Update with any user-facing changes:
- New features or capabilities
- Changed installation or setup steps
- Updated usage examples
- New requirements or dependencies
- API changes (if public)

Keep the existing structure and style. Only add/modify sections that are affected by the changes.

## 3. CLAUDE_CHANGELOG.md
Add an entry for today's changes following the existing format:
- Create the file if it doesn't exist
- If today's date exists, append to it
- Use sections: Added, Changed, Fixed, Removed, Refactored
- List affected files

## Rules:
1. Don't make changes if there's nothing relevant to update
2. Preserve existing formatting and style
3. Be concise but informative
4. Don't remove existing content unless it's outdated
5. Report what was updated in each file

Update the files now based on the changes shown above.
