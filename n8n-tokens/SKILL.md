---
name: n8n-tokens
description: n8n Design System Token Validator
argument-hint: [filepath]
---

# n8n Design System Token Validator

Analyze the CSS in the specified file and suggest design system tokens/primitives for any hardcoded values found.

## Philosophy

This tool is a **helpful assistant**, not a strict linter. It:
- Finds hardcoded values (colors, spacing, etc.)
- Suggests relevant tokens or primitives from the design system
- Lets the developer decide whether to use them

Component styles should be **co-located** with their components (in `.vue` files), not in global token files. Primitives can be used directly in component styles, especially with `light-dark()` for theming.

## Instructions

1. **Get the target file**: Use the file path provided as argument: $ARGUMENTS. If no argument is provided, check if there's a file currently open/focused in the IDE and use that.

2. **Read the design system files** from the n8n repository:
   - Primitives: `packages/frontend/@n8n/design-system/src/css/_primitives.scss`
   - Light tokens: `packages/frontend/@n8n/design-system/src/css/_tokens.new.scss`
   - Dark tokens: `packages/frontend/@n8n/design-system/src/css/_tokens.dark.new.scss`

3. **Read the target file** and analyze all CSS (including `<style>` blocks in Vue files).

4. **Check for issues** in the following categories:

### Category 1: Cross-Component Token Misuse (ERROR)
**This is the only strict rule.** Flag when a component uses tokens belonging to another component.

Detection:
- Extract component name from filename (e.g., `Toggle.vue` → "toggle")
- Scan for CSS variables with other component names (e.g., `--button--*`, `--modal--*`, `--card--*`)
- Flag as ERROR if component X uses tokens prefixed with component Y

Example violation:
```css
/* Toggle.vue */
.toggle {
  background-color: var(--button--background-color); /* ERROR: Using button token in toggle */
}
```

Why this matters: This creates hidden coupling between components. If button styles change, toggle breaks unexpectedly.

### Category 2: Hardcoded Color Values (SUGGESTION)
Look for hardcoded colors that could use tokens or primitives:
- Hex colors: `#fff`, `#000`, `#ff5722`, etc.
- RGB/RGBA: `rgb(...)`, `rgba(...)`
- HSL/HSLA: `hsl(...)`, `hsla(...)`
- Named colors: `white`, `black`, `red`, `blue`, etc. (except in CSS function names)

### Category 3: Hardcoded Spacing Values (SUGGESTION)
Look for hardcoded spacing that could use `--spacing-*` tokens:
- Pixel values in margin, padding, gap: `8px`, `16px`, `24px`, etc.
- Rem values that don't use variables

### Category 4: Hardcoded Border Radius (SUGGESTION)
Look for hardcoded border-radius that could use `--radius-*` tokens:
- `border-radius: 4px`, `border-radius: 8px`, etc.

### Category 5: Hardcoded Font Values (SUGGESTION)
Look for hardcoded typography that could use tokens:
- `font-size: 14px` instead of `--font-size-*`
- `font-weight: 600` instead of `--font-weight-*`
- `line-height: 1.5` instead of `--line-height-*`

5. **Output a report** with the following format:

```
## Token Validation Report for: [filename]

### Summary
- Errors: X (cross-component token misuse)
- Suggestions: Y (hardcoded values found)

### Errors (Must Fix)

#### Cross-Component Token Misuse
| Line | Code | Issue |
|------|------|-------|
| ... | ... | Using `--button--*` token in Toggle component |

### Suggestions (Consider Using Tokens)

#### Hardcoded Colors
| Line | Code | Consider Using |
|------|------|----------------|
| ... | `#ffffff` | `var(--color--white)` or `var(--background--surface)` |

#### Hardcoded Spacing
| Line | Code | Consider Using |
|------|------|----------------|
| ... | `padding: 16px` | `var(--spacing--sm)` |

#### Hardcoded Border Radius
| Line | Code | Consider Using |
|------|------|----------------|
| ... | `border-radius: 8px` | `var(--radius--xs)` |

#### Hardcoded Typography
| Line | Code | Consider Using |
|------|------|----------------|
| ... | `font-size: 14px` | `var(--font-size--sm)` |

### When Hardcoded Values May Be Acceptable
- Animation keyframes
- SVG-specific values
- Values with no semantic equivalent in the token system

Even in these cases, the suggestion is shown so the developer can evaluate if a token would be more consistent.
```

6. **Token Mapping Suggestions**: When suggesting tokens, use these semantic mappings:
   - For backgrounds: `--background--surface`, `--background--brand`, `--background--success`, etc.
   - For text colors: `--text-color`, `--text-color--subtle`, `--text-color--success`, etc.
   - For borders: `--border-color`, `--border-color--subtle`, `--border-color--strong`, etc.
   - For icons: `--icon-color`, `--icon-color--subtle`, `--icon-color--success`, etc.
   - For spacing: `--spacing--2xs` (8px), `--spacing--xs` (12px), `--spacing--sm` (16px), etc.
   - For radius: `--radius--3xs` (4px), `--radius--xs` (8px), `--radius--sm` (12px), etc.
   - Primitives can also be suggested: `--color--neutral-*`, `--color--blue-*`, etc.

7. **Exceptions to ignore**:
   - CSS custom property definitions (lines that define variables with `:`)
   - Comments
   - URLs and data URIs
   - `transparent`, `inherit`, `currentColor`, `initial`, `unset`
   - Values of `0` (zero doesn't need a unit)

## Component Co-location Best Practice

Styles should live in the component file, not in global token files:

```css
/* ✅ Good: Component-scoped theming in Button.vue */
.button {
  --button-bg: light-dark(var(--color--neutral-100), var(--color--neutral-900));
  background-color: var(--button-bg);
}

/* ❌ Bad: Component-specific tokens in global _tokens.scss */
/* This encourages other components to misuse --button--* tokens */
```

Global tokens are for truly shared concepts: text colors, icon colors, brand colors, spacing, radius, typography.
