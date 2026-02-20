# Color System

## THE RULES

1. **NEVER use pure gray** (0% saturation) - Always tint your grays
2. **NEVER use pure black** (#000) for text - Use soft darks
3. **NEVER use solid gray borders** - Use alpha transparency
4. **ALWAYS decide your tint direction** before coding (warm vs cool)

## Tinted Grays (REQUIRED)

Pick ONE tint direction and apply consistently:

### Blue-Tinted (Tech/SaaS)
```css
:root {
  --gray-50:  hsl(210, 17%, 98%);
  --gray-100: hsl(210, 14%, 95%);
  --gray-200: hsl(210, 12%, 90%);
  --gray-300: hsl(210, 10%, 80%);
  --gray-400: hsl(210, 10%, 65%);
  --gray-500: hsl(210, 10%, 50%);
  --gray-600: hsl(210, 12%, 40%);
  --gray-700: hsl(210, 14%, 30%);
  --gray-800: hsl(210, 16%, 20%);
  --gray-900: hsl(210, 18%, 12%);
}
```

### Warm-Tinted (Friendly/Approachable)
```css
:root {
  --gray-50:  hsl(40, 15%, 98%);
  --gray-100: hsl(40, 12%, 95%);
  --gray-500: hsl(40, 8%, 50%);
  --gray-900: hsl(40, 15%, 12%);
}
```

**Key**: Darker grays need MORE saturation to maintain perceived temperature.

## Text Colors (NEVER #000)

```css
:root {
  --text-primary: #111827;    /* NOT #000 */
  --text-secondary: #374151;
  --text-tertiary: #6b7280;
  --text-muted: #9ca3af;
}
```

Or use alpha for automatic blending:
```css
:root {
  --text-primary: rgba(0, 0, 0, 0.87);
  --text-secondary: rgba(0, 0, 0, 0.6);
}
```

## Border Colors (ALPHA REQUIRED)

NEVER use solid grays for borders. Use alpha transparency:

```css
:root {
  --border-subtle: rgba(0, 0, 0, 0.08);
  --border-default: rgba(0, 0, 0, 0.12);
  --border-strong: rgba(0, 0, 0, 0.16);
}
```

This lets borders blend with any background.

## Dark Mode

NEVER use pure black (#000). Use deep tinted grays:

```css
:root.dark {
  --bg-base: #0F1115;      /* NOT #000 */
  --bg-card: #161A20;
  --bg-elevated: #1C2127;
  
  --border-subtle: rgba(255, 255, 255, 0.06);
  --border-default: rgba(255, 255, 255, 0.10);
}
```

Dark mode colors need LOWER saturation to avoid vibration.

## Semantic Colors

```css
:root {
  /* Success */
  --success-bg: hsl(142, 70%, 95%);
  --success-border: hsl(142, 60%, 40%);
  --success-text: hsl(142, 70%, 25%);

  /* Error */
  --error-bg: hsl(0, 70%, 95%);
  --error-border: hsl(0, 60%, 50%);
  --error-text: hsl(0, 70%, 30%);

  /* Warning */
  --warning-bg: hsl(45, 90%, 95%);
  --warning-border: hsl(45, 80%, 45%);
  --warning-text: hsl(45, 80%, 25%);
}
```

## Contrast Requirements

- Body text: Minimum 4.5:1 (target 7:1)
- Large text (18px+): Minimum 3:1
- UI components: Minimum 3:1

## INVALID PATTERNS

```css
/* Pure black text - WRONG */
color: #000000;
color: #000;

/* Pure gray - WRONG */
background: #808080;
background: hsl(0, 0%, 50%);

/* Solid gray border - WRONG */
border: 1px solid #ccc;
border: 1px solid #e5e5e5;

/* Pure black dark mode - WRONG */
background: #000;
```
