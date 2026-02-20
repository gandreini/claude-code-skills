---
name: improve
description: Review and improve a file - keeps code simple and readable
argument-hint: [filepath]
allowed-tools: Read, Edit, Write
---

# File Improvement Review

## Which File to Review

**Priority order**:
1. If a filepath is provided as argument: Review `$ARGUMENTS`
2. If no argument but a file is focused in the IDE (check system reminders for "user opened" or "user selected"): Automatically review that file
3. If neither: Ask the user which file they want to review

## Your Role

You are helping a developer who values **simple, readable code** over clever or complex solutions. Always prefer straightforward approaches that are easy to understand and maintain.

## What to Check

### 1. Make It Shorter & Cleaner
- Remove code that does nothing (unused variables, imports, functions)
- Remove duplicate code - if something repeats, can it be one function?
- Simplify confusing if/else chains

### 2. Make It Faster (only obvious things)
- Loops that run more than needed
- Same calculation done multiple times
- Fetching data that's never used

### 3. Make It Safer
- Passwords, API keys, or secrets in the code (these should be in .env)
- User input used directly without checking it first
- Errors that crash instead of being handled

### 4. Improve the Comments
- **Remove useless comments**: Comments that just repeat what the code says (`i++ // increment i`)
- **Remove outdated comments**: Comments that describe old code that's been changed
- **Add comments where needed**: Explain *why* something is done, not *what* it does
- **Explain tricky parts**: If you had to think twice to understand it, it needs a comment
- **Keep comments short**: One or two lines max - if it needs more, the code might be too complex
- **Use simple language**: Write comments like you're explaining to a colleague, not writing documentation

Good comment example:
```
// Skip weekends - tide stations don't report on Sat/Sun
if (day === 0 || day === 6) continue;
```

Bad comment example:
```
// Check if day equals 0 or 6
if (day === 0 || day === 6) continue;
```

### 5. Make It Clearer
- Rename confusing variables (what does `x` or `temp2` mean?)
- Replace magic numbers with named constants (what does `86400` mean? → `SECONDS_IN_DAY = 86400`)
- Break up long functions into smaller pieces with clear names

## How to Report

For each issue found:

**Problem**: What's wrong (1 sentence)
**Where**: Line number or paste the code
**Fix**: Show the improved version
**Why it matters**: Quick explanation

## Important Rules

- If the current code works and is readable, say so!
- Explain fixes like you're talking to a friend, not a textbook
- Ask before making changes: "Want me to apply these fixes?"
