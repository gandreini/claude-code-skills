# Shadow System

## THE RULE

**NEVER use single-layer shadows.** Single shadows look flat and cheap because CSS box-shadow can't simulate real light behavior. Multi-layer shadows simulate contact shadows, key light, and ambient light.

## Multi-Layer Pattern (REQUIRED)

Use the **doubling pattern**—each layer doubles offset and blur:

```css
/* Standard card shadow - USE THIS */
box-shadow: 
  0 1px 2px rgba(0,0,0,0.06),
  0 2px 4px rgba(0,0,0,0.06),
  0 4px 8px rgba(0,0,0,0.06);

/* Elevated element (dropdown, modal) */
box-shadow: 
  0 1px 2px rgba(0,0,0,0.05),
  0 4px 8px rgba(0,0,0,0.05),
  0 8px 16px rgba(0,0,0,0.05),
  0 16px 32px rgba(0,0,0,0.05);
```

**Rule**: More layers = lower opacity per layer.

## Tinted Shadows (REQUIRED)

NEVER use pure black `rgba(0,0,0,x)`. Tint to match your color scheme:

```css
:root {
  /* Blue-tinted for tech/SaaS */
  --shadow-color: 220deg 10% 20%;
  
  --shadow-sm: 
    0 1px 2px hsl(var(--shadow-color) / 0.1),
    0 2px 4px hsl(var(--shadow-color) / 0.1);
  
  --shadow-md:
    0 1px 2px hsl(var(--shadow-color) / 0.08),
    0 4px 8px hsl(var(--shadow-color) / 0.08),
    0 8px 16px hsl(var(--shadow-color) / 0.08);
  
  --shadow-lg:
    0 2px 4px hsl(var(--shadow-color) / 0.06),
    0 4px 8px hsl(var(--shadow-color) / 0.06),
    0 8px 16px hsl(var(--shadow-color) / 0.06),
    0 16px 32px hsl(var(--shadow-color) / 0.06);
}
```

## Elevation Mapping

| Component | Shadow | Notes |
|-----------|--------|-------|
| Cards (default) | `shadow-sm` | Subtle lift |
| Cards (hover) | `shadow-md` | Increase on interaction |
| Dropdowns | `shadow-lg` | Always elevated |
| Modals | `shadow-lg` | Always elevated |
| Tooltips | `shadow-md` | Medium elevation |

## Dark Mode

Shadows disappear on dark backgrounds. Use **inner highlight borders** instead:

```css
.card-dark {
  background: #161A20;
  box-shadow: 
    0 0 0 1px rgba(255,255,255,0.08) inset,  /* Edge highlight */
    0 4px 12px rgba(0,0,0,0.4);  /* Subtle shadow */
}
```

## INVALID PATTERNS

These are WRONG—never use:

```css
/* Single layer - WRONG */
box-shadow: 0 4px 6px rgba(0,0,0,0.1);

/* Pure black - WRONG */
box-shadow: 0 2px 4px #000;

/* Too heavy - WRONG */
box-shadow: 0 10px 30px rgba(0,0,0,0.3);
```
