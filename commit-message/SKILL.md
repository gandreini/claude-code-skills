---
name: commit-message
description: Generate a commit message for all uncommitted changes
allowed-tools: Bash(git diff:*), Bash(git status:*)
---

# Context
- Uncommitted changes: !`git diff`
- Staged changes: !`git diff --cached`
- Current status: !`git status --short`

# Task
Write a concise, clear commit message for all the uncommitted changes above.

## Format
- **First line**: Emoji prefix + summary - keep under 72 characters
- **Blank line**
- **Bullet list**: Details of what was changed

## Emoji prefixes (required)
Use these emoji prefixes based on the PRIMARY change type:
- ✨ New feature
- 🐛 Bug fix
- 📝 Documentation
- ♻️ Refactor
- 🧪 Tests
- 🔧 Configuration/chore
- 🚀 Performance improvement
- 🗑️ Remove code/files

**Rules for mixed changes:**
- Use the emoji for the PRIMARY change
- The message text must reference ALL changes made
- If too many changes to list: end with "and more modifications"

## Title rules
The title MUST reference ALL changes in the bullet list, not just one item. Count the distinct topics in your bullet list before writing the title.

**Strategy based on number of distinct changes:**
1. **Single topic**: Name it directly → "✨ Add user authentication"
2. **2-3 related topics**: Find a unifying theme → "🐛 Fix API security and validation issues"
3. **2-3 unrelated topics**: List the main ones → "🐛 Fix login bug, update styles, and clean up tests"
4. **4+ topics**: Mention the biggest one + qualifier → "♻️ Refactor auth module and various improvements"

**Qualifiers to signal additional changes:**
- "and additional improvements"
- "with related fixes"
- "and various updates"
- "plus cleanup"
- "and more"

**Bad example** (title only mentions one of three things):
```
✨ Add login endpoint

- Create login and logout endpoints
- Add JWT token validation middleware
- Update user model with password hashing
```

**Good example** (unified theme covers all three):
```
✨ Add user authentication to the API

- Create login and logout endpoints
- Add JWT token validation middleware
- Update user model with password hashing
```

**Good example** (unrelated changes, lists main topics):
```
🐛 Fix date parsing, update navbar styles, and refactor tests

- Correct timezone handling in date parser
- Change navbar background color
- Split test file into smaller units
```

**Good example** (many changes, uses qualifier):
```
♻️ Refactor authentication module and various improvements

- Restructure auth service into smaller functions
- Fix session expiration bug
- Update error messages
- Remove deprecated helper functions
- Add missing TypeScript types
```

Output ONLY the commit message, nothing else.
