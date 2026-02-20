# Claude Code Skills

This directory contains custom skills for Claude Code. Skills extend Claude's capabilities with specialized prompts and workflows.

## What Are Skills?

Skills are reusable prompt templates that Claude can invoke using slash commands (e.g., `/commit-message`, `/improve`, `/tests-run`). They provide context-aware assistance for common development tasks.

As of January 2026, Anthropic merged the concept of **Custom Commands** and **Skills** into a unified system. Both formats work identically - skills are simply the modern, more powerful format.

## Directory Structure

```
skills/
├── README.md                    # This file
├── agentation/                  # Symlink to shared skill
├── find-skills/                 # Symlink to shared skill
├── frontend-design/             # Frontend UI creation
├── visual-design-craft/         # Premium UI polish enforcement
├── changelog/                   # Update CLAUDE_CHANGELOG.md
├── commit-message/              # Generate commit messages
├── compound-engineering/        # Extract learnings to improve docs
├── docs-update/                 # Update all documentation files
├── improve/                     # Code review and improvement
├── n8n-pr-description/          # Generate n8n PR descriptions
├── n8n-pr-name/                 # Generate n8n PR titles
├── n8n-tokens/                  # n8n design system validator
└── tests-run/                   # Detect and run tests
```

## Skill Format

Each skill is a folder containing a `SKILL.md` file with this structure:

```markdown
---
name: skill-name
description: Brief description of what this skill does
argument-hint: [optional-argument]
allowed-tools: Tool1, Tool2, Tool3
---

# Skill prompt content goes here

Use $ARGUMENTS to reference command-line arguments.
Use !`command` for dynamic shell execution.
```

### Frontmatter Fields

- **name** (required): The skill name, used as `/skill-name`
- **description** (required): Short description shown in skill listings
- **argument-hint** (optional): Hint text for expected arguments
- **allowed-tools** (optional): Restrict which tools Claude can use

### Dynamic Content

Skills can execute shell commands dynamically:
- `!`command`` - Execute and embed output
- `$ARGUMENTS` - Reference user-provided arguments

Example:
```markdown
- Current branch: !`git branch --show-current`
- Target file: $ARGUMENTS
```

## Available Skills

### Development Workflow

- **/commit-message** - Generate conventional commit messages with emoji prefixes
- **/changelog** - Update CLAUDE_CHANGELOG.md with recent changes
- **/docs-update** - Update CLAUDE.md, README.md, and CLAUDE_CHANGELOG.md
- **/tests-run** - Auto-detect and run available tests (npm, pytest, cargo, etc.)

### Code Quality

- **/improve** - Review and improve code for simplicity and readability
- **/compound-engineering** - Extract learnings to improve documentation and workflows

### n8n Specific

- **/n8n-pr-name** - Generate n8n-compliant PR titles
- **/n8n-pr-description** - Generate n8n-compliant PR descriptions
- **/n8n-tokens** - Validate design system token usage

### Frontend Development

- **/frontend-design** - Create distinctive, production-grade UI interfaces
- **/visual-design-craft** - Enforce premium visual polish (Linear/Vercel quality)

### Utilities

- **/find-skills** - Discover and install new skills
- **/agentation** - Add visual feedback toolbar to Next.js projects

## Using Skills

Invoke a skill with a slash command:

```bash
# Simple invocation
/commit-message

# With arguments
/improve src/components/Button.tsx

# Skills work anywhere in your message
Can you /tests-run and then /commit-message?
```

## Creating New Skills

1. **Create a folder**: `mkdir -p skills/my-skill`
2. **Create SKILL.md**: Add frontmatter and prompt content
3. **Test it**: Use `/my-skill` to invoke

Example minimal skill:

```markdown
---
name: my-skill
description: Does something useful
---

# Task

Do the thing based on this context:
- Current directory: !`pwd`
- Files here: !`ls -la`
```

## Migration from Commands

This folder was migrated from the legacy `claude-commands/` format. The old `.md` files in `claude-commands/` still work but are deprecated. All functionality has been moved to this modern skill format.

**Key differences:**
- Commands: Single `.md` files in `~/.claude/commands/`
- Skills: Folders with `SKILL.md` in `~/.claude/skills/`
- Skills support additional features like sub-agents and dynamic file loading

## Best Practices

1. **Keep skills focused** - One skill should do one thing well
2. **Use allowed-tools** - Restrict tools for safety and clarity
3. **Add argument hints** - Help users know what to provide
4. **Dynamic context** - Use `!`command`` to gather relevant context
5. **Clear output** - Structure output for easy consumption

## File Location

This directory is designed to be symlinked to:
- **Alias**: `~/.claude/skills/` (symlink to wherever you clone this repo)

## Resources

- [Official Skills Documentation](https://code.claude.com/docs/en/skills)
- [Skills Repository](https://github.com/anthropics/skills)
- [Claude Code Release Notes](https://releasebot.io/updates/anthropic/claude-code)

## Contributing

To share a skill with others:
1. Ensure the skill is well-documented
2. Test it thoroughly
3. Consider submitting to the [official skills repo](https://github.com/anthropics/skills)
