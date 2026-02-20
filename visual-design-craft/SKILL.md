---
name: visual-design-craft
description: Enforce premium visual polish when creating any frontend UI—Linear/Vercel/Stripe-level craft. MUST use when building components, pages, dashboards, or any web interface. Applies strict technical rules for spacing, shadows, typography, and colors. Also use when improving, polishing, or auditing existing UI code for design quality.
---

This skill enforces technical craft rules that separate amateur UI from premium quality. These are MANDATORY constraints, not suggestions. Every UI output MUST comply.

## BEFORE WRITING ANY CODE

STOP. Make these decisions first and state them explicitly:

1. **Aesthetic direction**: Dark or light? Warm-tinted or cool-tinted grays? Sharp corners or rounded? Dense or spacious?

2. **Typography choice**: Pick a distinctive font. NEVER default to Inter, Roboto, Arial, or system-ui. Choose something with character that fits the context.

3. **Color temperature**: Your grays MUST be tinted. Pick: blue-tinted (tech/SaaS), warm-tinted (friendly/approachable), or another deliberate choice.

4. **One memorable detail**: What single element will make this unforgettable? A distinctive hover effect? Unusual spacing rhythm? Bold color accent?

**CRITICAL**: State these choices before writing code. Different prompts MUST produce different designs. NEVER converge on the same solution twice.

## MANDATORY CRAFT RULES

### Spacing: 8px Grid

**ONLY these values are valid**: 4, 8, 12, 16, 24, 32, 48, 64, 96

- 4px ONLY for micro-spacing (icon gaps)
- NEVER use 10px, 14px, 18px, 22px, 30px
- Inner padding < outer margins (always)

### Shadows: Multi-Layer REQUIRED

**NEVER single-layer shadows.** This is the #1 amateur mistake.

```css
/* WRONG */
box-shadow: 0 4px 6px rgba(0,0,0,0.1);

/* CORRECT - minimum 2 layers */
box-shadow: 
  0 1px 2px rgba(0,0,0,0.06),
  0 4px 8px rgba(0,0,0,0.06),
  0 12px 24px rgba(0,0,0,0.08);
```

See [references/shadows.md](references/shadows.md) for elevation system.

### Typography: Tracking Rules

```css
h1, h2 { letter-spacing: -0.02em; }  /* TIGHTEN large text */
.uppercase { letter-spacing: 0.05em; } /* LOOSEN all-caps */
p { max-width: 65ch; }  /* ALWAYS constrain line length */
```

See [references/typography.md](references/typography.md) for full scale.

### Colors: NEVER Pure Gray or Black

```css
/* WRONG */
color: #000000;
background: #808080;

/* CORRECT */
--text-primary: #111827;  /* Soft dark */
--gray-500: hsl(210, 10%, 50%);  /* Tinted */
--border: rgba(0, 0, 0, 0.12);  /* Alpha, not solid */
```

See [references/colors.md](references/colors.md) for full palette.

### Border Radius: Nested Calculation

`Inner radius = Outer radius - Padding`

Card 16px radius + 8px padding → inner elements get 8px radius.

### Transitions

ALL interactive elements MUST have:
- Transitions: 150-200ms with ease-out
- Hover states: subtle but visible
- Focus states: 2px offset ring

## SELF-CHECK BEFORE RESPONDING

Verify your output against this checklist:

- [ ] Stated aesthetic direction before coding
- [ ] Font is NOT Inter/Roboto/Arial/system-ui
- [ ] All spacing values on 8px grid
- [ ] All shadows are multi-layer (2+ layers)
- [ ] No pure black text (#000)
- [ ] All grays are tinted
- [ ] Headings have negative letter-spacing
- [ ] Body text has max-width
- [ ] All interactive elements have transitions
- [ ] Design feels distinctive, not generic

If any check fails, fix it before responding.

## REFERENCE FILES

For detailed specifications and complete token systems:

- **Shadows**: [references/shadows.md](references/shadows.md) - Multi-layer patterns, elevation tokens
- **Typography**: [references/typography.md](references/typography.md) - Scale, line-height, weight hierarchy  
- **Spacing**: [references/spacing.md](references/spacing.md) - Component padding, button ratios
- **Colors**: [references/colors.md](references/colors.md) - Tinted palettes, semantic colors, dark mode
- **Full tokens**: [references/design-tokens.md](references/design-tokens.md) - Production-ready CSS variables
