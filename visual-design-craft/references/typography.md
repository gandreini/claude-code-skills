# Typography System

## THE RULES

1. **NEVER use Inter, Roboto, Arial, or system-ui as primary font** - These are generic. Pick something distinctive.
2. **ALWAYS tighten letter-spacing on headings** - Large text looks loose at default tracking.
3. **ALWAYS loosen letter-spacing on uppercase** - All-caps needs room to breathe.
4. **ALWAYS constrain line length** - Body text max 65 characters.

## Type Scale (USE THESE VALUES)

```css
:root {
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px - minimum for body */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  --text-4xl: 2.25rem;   /* 36px */
  --text-5xl: 3rem;      /* 48px */
  --text-6xl: 4rem;      /* 64px */
}
```

## Letter-Spacing (MANDATORY)

```css
/* TIGHTEN large text */
h1, h2 { letter-spacing: -0.02em; }
h3, h4 { letter-spacing: -0.01em; }

/* NORMAL for body */
p, .body { letter-spacing: 0; }

/* LOOSEN all-caps */
.uppercase { letter-spacing: 0.05em; }

/* LOOSEN small text */
.caption, .label { letter-spacing: 0.01em; }
```

## Line-Height (Inverse Rule)

**Larger text = tighter line-height. Smaller text = looser.**

| Size | Line-Height | Use |
|------|-------------|-----|
| 48px+ | 1.0–1.1 | Display, hero |
| 32-48px | 1.1–1.2 | H1, H2 |
| 24-32px | 1.2–1.3 | H3, H4 |
| 16-20px | 1.5–1.6 | Body text |
| 12-14px | 1.4–1.5 | Captions |

```css
h1 { font-size: 3rem; line-height: 1.1; }
h2 { font-size: 2.25rem; line-height: 1.2; }
h3 { font-size: 1.5rem; line-height: 1.3; }
p { font-size: 1rem; line-height: 1.6; }
```

## Line Length (MANDATORY)

```css
/* ALWAYS constrain body text */
p, .prose { max-width: 65ch; }

/* Narrow for captions, sidebars */
.narrow { max-width: 45ch; }
```

## Font Weight Hierarchy

Use 2-3 weights maximum:

| Element | Weight |
|---------|--------|
| Body | 400 |
| Labels, buttons | 500 |
| Subheadings | 500-600 |
| Headings | 600-700 |

## Font Smoothing (Dark Backgrounds)

ALWAYS apply on dark mode:

```css
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

## INVALID PATTERNS

```css
/* No tracking on headings - WRONG */
h1 { letter-spacing: normal; }

/* Tight tracking on caps - WRONG */
.uppercase { letter-spacing: -0.02em; }

/* Unconstrained body text - WRONG */
p { /* no max-width */ }

/* Same line-height everywhere - WRONG */
h1, h2, h3, p { line-height: 1.5; }
```
