---
name: extract-subprojects
description: Analyze codebase to find reusable components worth extracting as open-source projects
allowed-tools: Glob, Grep, Read, WebSearch, Write, Bash
---

# Subproject Extraction Analyzer

## Purpose

Analyze the current project to identify code that could be extracted into standalone open-source projects. This supports a "build in public" strategy by finding reusable components worth sharing, writing about, and building reputation around.

## Analysis Process

### Step 1: Discover and Read ALL Code Files

**CRITICAL**: Do not make assumptions based on file names or descriptions. You must read the actual implementation.

1. **List all code files**:
   ```bash
   # Find all source files
   find . -type f -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.tsx"
   # Or use Glob for specific patterns
   ```

2. **Read ALL files over 200 lines**:
   - Don't skip files based on "boring" names (e.g., `comparison.py`, `utils.py`)
   - Don't assume you know what a file does from its name
   - Files with generic names often contain sophisticated logic
   - **You cannot evaluate code you haven't read**

3. **Create an inventory**:
   - List each significant file (>200 lines)
   - Note its purpose (after reading it, not guessing)
   - Identify external API calls, algorithms, frameworks used
   - Flag files with reusable patterns

**Common Mistakes to Avoid**:
- ❌ "This file is called 'comparison.py' so it's probably just HTML generation"
- ❌ "I'll focus on the 'core' files and skip support modules"
- ❌ "The README says this is simple, so I don't need to read it"
- ✅ "I'll read every significant file to understand what it actually does"

### Step 2: Categorize Code by Patterns

After reading all files, categorize what you found:

1. **Utility Functions & Helpers**
   - Parsers, formatters, validators
   - Algorithmic code that solves specific problems
   - Math/scientific calculations

2. **Components & UI Elements**
   - React/Vue/Svelte components with generic use cases
   - Design system elements
   - Reusable hooks or composables

3. **API Wrappers & Integrations**
   - Third-party API clients
   - Multi-provider comparison tools
   - SDK-like code
   - Authentication/authorization helpers

4. **Data Processing & Algorithms**
   - Transform functions
   - Complex calculations
   - Data structure implementations
   - Optimization algorithms

5. **Build Tools & Developer Tools**
   - Custom webpack/vite plugins
   - CLI tools
   - Code generators or scaffolding tools
   - Testing utilities

6. **Comparison & Validation Tools**
   - Multi-provider comparison logic
   - Validation frameworks
   - Benchmarking utilities

For each potential extraction candidate, assess:

#### Reusability Score (1-10)
- How generic is it? (framework-agnostic = higher score)
- Does it solve a common problem?
- Is it well-isolated or tightly coupled?
- How much refactoring would be needed?

#### Uniqueness Assessment
- Use **WebSearch** to check:
  - GitHub repos with similar functionality
  - npm/PyPI packages that do the same thing
  - Stack Overflow questions about this problem
- Compare features: Does this code have unique advantages?
- Check quality of alternatives: Are they maintained? Well-documented?

#### Extraction Complexity
- **Dependencies**: List what it depends on
  - External packages
  - Internal modules
  - Circular dependencies?
- **Licensing issues**: Check if dependencies have compatible licenses
- **Effort estimate**:
  - Low (< 1 day): Drop-in extraction, minimal changes
  - Medium (1-3 days): Some refactoring, documentation needed
  - High (> 1 week): Significant work, architectural changes

#### Market Potential
- Is this interesting enough to write about?
- Does it solve a painful problem?
- Would developers search for this?
- LinkedIn/Twitter shareability factor

### Step 4: Web Research Strategy

For each candidate, search:

1. **GitHub**: `"<functionality>" language:<lang> stars:>100`
   - Example: `"react debounce hook" language:typescript stars:>100`
2. **Package Registries**:
   - npm: Search for related keywords
   - PyPI: Check for Python alternatives
   - packagist (PHP), crates.io (Rust), etc.
3. **Quality Assessment**:
   - Last commit date (abandoned if > 2 years?)
   - Number of issues vs. stars
   - Documentation quality
   - Bundle size (for JS packages)

**Flag candidates where**:
- Nothing similar exists
- Existing solutions are unmaintained (> 1 year no updates)
- Existing solutions have poor quality (many open issues, no docs)
- This code has clear advantages (faster, simpler API, better DX)

### Step 5: Generate Markdown Report

Create a comprehensive report at `./EXTRACTION_CANDIDATES.md` with this structure:

```markdown
# Subproject Extraction Analysis

**Project analyzed**: [project name]
**Analysis date**: [date]
**Technology stack**: [React, TypeScript, etc.]

---

## 🏆 Top Candidates

### 1. [Suggested Package Name]

**Location**: `src/path/to/code`
**Type**: [Utility / Component / API Wrapper / Tool]
**Reusability Score**: [X/10]

#### What it does
[Brief description in 2-3 sentences]

#### Why extract it?
- [Reason 1: Solves common problem]
- [Reason 2: No good alternatives exist]
- [Reason 3: Market potential]

#### Market research
- **Existing alternatives**:
  - [package-name](link) - [brief assessment: unmaintained / limited features / etc.]
  - OR "No close alternatives found"
- **Search volume**: [High/Medium/Low based on GitHub/npm searches]
- **Unique advantages**: [What makes this better]

#### Extraction details
- **Effort estimate**: [Low/Medium/High] - [time estimate]
- **Dependencies to include**:
  ```
  - dependency-1 (MIT)
  - dependency-2 (Apache 2.0)
  ```
- **Licensing**: ✅ No issues / ⚠️ [specific concern]
- **Suggested package name**: `package-name-here`
- **Target registry**: npm / PyPI / etc.

#### Build-in-public potential
- **Article ideas**:
  - [Suggested blog post title]
  - [Another angle to write about]
- **Demo potential**: [Can you create a compelling demo?]
- **Target audience**: [Who would use this?]

---

[Repeat for each top candidate]

## 🔍 Other Candidates

[Shorter entries for less compelling but still viable candidates]

## ❌ Not Recommended

[Brief list of code that seemed interesting but isn't worth extracting, with reasons]

---

## Prioritization Recommendation

Based on market potential, extraction effort, and uniqueness:

1. **Extract first**: [Name] - [one sentence why]
2. **Extract second**: [Name] - [one sentence why]
3. **Consider later**: [Name] - [one sentence why]

## Next Steps

For the top candidate, consider:
1. Create new GitHub repo: `username/package-name`
2. Set up package scaffolding (package.json, README, etc.)
3. Extract and refactor code
4. Write comprehensive documentation
5. Create demo/examples
6. Publish to npm/PyPI
7. Write announcement article
8. Share on LinkedIn/Twitter
```

## Pre-Analysis Checklist

Before writing your report, verify you have:

- [ ] Listed ALL Python/JS/TS files in the project
- [ ] Read EVERY file over 200 lines (no exceptions)
- [ ] Read files based on actual content, not assumptions about names
- [ ] Identified external API integrations by reading code, not guessing
- [ ] Found algorithmic/calculation code by reading implementations
- [ ] Discovered comparison/validation frameworks (often in "boring" named files)
- [ ] Cataloged all dependencies and their licenses

**If you skipped any files**: Go back and read them. You cannot evaluate code you haven't seen.

## Important Rules

1. **Be selective**: Only flag truly valuable code worth the extraction effort
2. **Real market research**: Don't guess about alternatives - actually search
3. **Honest assessment**: If extraction is too complex, say so
4. **Consider maintenance**: Can the user maintain this long-term?
5. **Build-in-public angle**: Prioritize code that's interesting to write/talk about
6. **No false positives**: Better to find 2 great candidates than 10 mediocre ones

## Technology-Specific Notes

- **JavaScript/TypeScript**: Check npm, consider bundle size, tree-shaking
- **Python**: Check PyPI, consider Python version compatibility
- **React**: Consider React version compatibility, peer dependencies
- **PHP**: Check Packagist, consider PHP version support
- **Go**: Check if it's suitable for go.dev modules

## Questions to Ask User (if needed)

- What type of projects are you most interested in extracting? (utilities, components, tools)
- Any specific technologies you want to focus on?
- Target audience: Developers in general, or specific community (React devs, Python devs, etc.)?
- Preferred license for extracted projects? (MIT, Apache 2.0, etc.)

## Output

Present the complete analysis as a markdown report and offer to:
1. Save it as `EXTRACTION_CANDIDATES.md` in the project root
2. Discuss specific candidates in detail
3. Help prioritize which to extract first
4. Assist with extraction of the chosen candidate

---

**Remember**: The goal is finding code worth building a reputation around - focus on quality over quantity.
