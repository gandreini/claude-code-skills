---
name: compound-engineering
description: Extract learnings from the conversation to improve CLAUDE.md files, commands, and skills
allowed-tools: Read, Edit, Write, Glob, Grep
---

# Compound Engineering - Learning from Experience

## Purpose

Review the current conversation to extract valuable learnings that can improve future work. This is about **compounding knowledge** - turning one-time problem solving into permanent improvements.

## What to Analyze

Look through the entire conversation for:

### 1. Problems & Solutions
- What bugs or errors were encountered?
- What was the root cause?
- How was it diagnosed?
- What was the fix?

### 2. Patterns Discovered
- Code patterns specific to this project
- Common mistakes to avoid
- Useful debugging techniques
- File locations that weren't obvious

### 3. Project-Specific Knowledge
- How components interact
- Naming conventions used
- Configuration quirks
- Dependencies between files

### 4. Workflow Improvements
- Commands that could be automated
- Checks that should be done routinely
- Information that should be documented

## Files to Potentially Update

### Project CLAUDE.md
Location: Look for `CLAUDE.md` in the current project root

Add learnings about:
- Project-specific gotchas and quirks
- Important file relationships discovered
- Debugging tips for this codebase
- Common issues and their solutions

### Global CLAUDE.md
Location: `~/.claude/CLAUDE.md`

Add learnings about:
- General debugging strategies that worked
- Cross-project patterns
- Workflow improvements
- Tool usage tips

### Custom Commands
Location: `~/.claude/commands/` (or symlinked location)

Consider:
- New commands that would have helped
- Improvements to existing commands
- Missing functionality

### Skills
Location: `~/.claude/skills/`

Consider:
- New skills that would be useful
- Improvements to existing skills

## How to Report

### Step 1: Summarize Learnings
List each learning with:
- **What happened**: Brief description
- **The insight**: What we learned
- **Where to add it**: Which file should be updated

### Step 2: Propose Changes
For each file to update, show:
- The file path
- The specific addition or change
- Why it helps

### Step 3: Ask for Approval
Present all proposed changes and ask:
"Would you like me to apply these improvements? (all/select/none)"

## Important Rules

- **Be selective**: Only add truly useful learnings, not obvious things
- **Be concise**: Keep additions short and actionable
- **Don't duplicate**: Check if the learning already exists before adding
- **Focus on patterns**: One-off issues rarely need documentation
- **Explain the "why"**: Each addition should explain why it matters

## Example Learnings

Good learning to add:
```
- When deleting a file, check `functions.php` for require statements that reference it
```

Too obvious (don't add):
```
- PHP files need proper syntax
```

Too specific (probably don't add):
```
- On Jan 14 2026, the ai.rest-api.php file was deleted
```
