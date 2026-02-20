# Spacing System

## THE RULE

**ONLY use 8px grid values.** Any spacing not on this grid is INVALID.

## Valid Values (ONLY THESE)

```
4, 8, 12, 16, 24, 32, 48, 64, 96
```

4px is ONLY for micro-spacing (icon-to-text gaps).

## INVALID Values (NEVER USE)

```
10, 14, 18, 20, 22, 30, 36, 40, 50, 60, 70, 80
```

If you catch yourself writing `padding: 10px` or `gap: 14px`, STOP and fix it.

## Spacing Scale

```css
:root {
  --space-1: 4px;    /* Micro only */
  --space-2: 8px;    /* Tight */
  --space-3: 12px;   /* Compact */
  --space-4: 16px;   /* Default */
  --space-6: 24px;   /* Comfortable */
  --space-8: 32px;   /* Generous */
  --space-12: 48px;  /* Large sections */
  --space-16: 64px;  /* Hero sections */
  --space-24: 96px;  /* Dramatic spacing */
}
```

## Gestalt Rule (MANDATORY)

**Inner padding MUST be less than outer margin.**

Elements close together appear grouped. Space inside < space between.

```css
/* CORRECT */
.card { padding: 16px; }
.card-grid { gap: 24px; }  /* Outer > inner */

/* WRONG */
.card { padding: 24px; }
.card-grid { gap: 16px; }  /* Inner > outer breaks grouping */
```

## Button Padding (1:2 Ratio)

Vertical : Horizontal = 1 : 2

```css
.btn-sm { padding: 6px 12px; height: 32px; }
.btn-md { padding: 8px 16px; height: 40px; }
.btn-lg { padding: 12px 24px; height: 48px; }
.btn-icon { padding: 8px; width: 40px; height: 40px; }
```

## Component Reference

| Component | Padding | Gap Between |
|-----------|---------|-------------|
| Buttons | 8-12px / 16-24px | 8px |
| Cards | 16-24px | 24px |
| Inputs | 8-12px / 12-16px | — |
| Form fields | — | 16-24px |
| Modals | 24-32px | — |
| Sections | 48-64px | — |

## Premium Whitespace

**Start with MORE space than feels necessary.**

Premium designs use 1.5-2× typical spacing. When in doubt, add space.

```css
/* Generic */
.section { padding: 32px 0; }

/* Premium */
.section { padding: 64px 0; }
```

## INVALID PATTERNS

```css
/* Off-grid values - WRONG */
padding: 10px;
margin: 15px;
gap: 18px;

/* Inner > outer - WRONG */
.card { padding: 32px; }
.grid { gap: 16px; }

/* Arbitrary values - WRONG */
margin-top: 13px;
padding-bottom: 22px;
```
