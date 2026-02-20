---
name: changelog
description: Update CLAUDE_CHANGELOG.md with recent modifications
allowed-tools: Bash(git diff:*), Bash(git status:*), Bash(cat:*), Bash(test:*), Bash(date:*)
---

# Context
- Today's date: !`date +%Y-%m-%d`
- Changelog exists: !`test -f CLAUDE_CHANGELOG.md && echo "yes" || echo "no"`
- Current changelog content: !`test -f CLAUDE_CHANGELOG.md && head -100 CLAUDE_CHANGELOG.md || echo "n/a"`
- Uncommitted changes: !`git diff`
- Staged changes: !`git diff --cached`
- Current status: !`git status --short`

# Task
Update (or create) CLAUDE_CHANGELOG.md with the recent modifications.

## If the file doesn't exist, create it with this header:
```markdown
# Claude Session Changelog

Log of modifications made during Claude Code sessions. This file helps track what was changed, when, and why — providing context for both the developer and Claude across sessions.

---
```

## Then add an entry for today's date using this format:
```markdown
## YYYY-MM-DD

### Added
- (new files, features)

### Changed
- (modifications to existing code)

### Fixed
- (bug fixes)

### Removed
- (deleted code, files)

### Refactored
- (code restructuring without behavior change)

### Files affected
- (list all modified files)
```

## Rules:
1. If today's date section already exists, append to it (don't duplicate the date header)
2. Only include sections that apply (skip empty sections like "Removed" if nothing was removed)
3. Be specific about what changed and why
4. Group related changes together
5. List all affected files at the end of the date section
6. Keep descriptions concise but informative

Update the file now based on the uncommitted changes shown above.
