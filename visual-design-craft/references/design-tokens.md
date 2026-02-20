# Complete Design Tokens

Copy this as a starting point. Customize the tint (210 = blue) and shadow color to match your design direction.

```css
:root {
  /* ========== TYPOGRAPHY ========== */
  
  /* CHANGE THIS - pick a distinctive font */
  --font-display: 'Your Display Font', sans-serif;
  --font-body: 'Your Body Font', sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
  
  /* Type scale */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  --text-6xl: 4rem;
  
  /* ========== SPACING (8px grid) ========== */
  
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;
  
  /* ========== COLORS (Blue-tinted) ========== */
  /* Change hue (210) to customize tint */
  
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
  
  /* Semantic text */
  --text-primary: var(--gray-900);
  --text-secondary: var(--gray-700);
  --text-tertiary: var(--gray-500);
  --text-muted: var(--gray-400);
  
  /* Backgrounds */
  --bg-page: var(--gray-50);
  --bg-card: #ffffff;
  --bg-elevated: #ffffff;
  
  /* Borders (alpha, not solid) */
  --border-subtle: rgba(0, 0, 0, 0.08);
  --border-default: rgba(0, 0, 0, 0.12);
  --border-strong: rgba(0, 0, 0, 0.16);
  
  /* ========== RADIUS ========== */
  
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-default: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;
  
  /* ========== SHADOWS (Multi-layer, tinted) ========== */
  
  --shadow-color: 220deg 10% 20%;
  
  --shadow-sm: 
    0 1px 2px hsl(var(--shadow-color) / 0.08),
    0 2px 4px hsl(var(--shadow-color) / 0.08);
  
  --shadow-md: 
    0 1px 2px hsl(var(--shadow-color) / 0.06),
    0 4px 8px hsl(var(--shadow-color) / 0.06),
    0 8px 16px hsl(var(--shadow-color) / 0.06);
  
  --shadow-lg: 
    0 2px 4px hsl(var(--shadow-color) / 0.05),
    0 4px 8px hsl(var(--shadow-color) / 0.05),
    0 8px 16px hsl(var(--shadow-color) / 0.05),
    0 16px 32px hsl(var(--shadow-color) / 0.05);
  
  /* ========== TRANSITIONS ========== */
  
  --duration-fast: 150ms;
  --duration-normal: 200ms;
  --duration-slow: 300ms;
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-spring: cubic-bezier(0.25, 1, 0.5, 1);
}

/* ========== DARK MODE ========== */

:root.dark, [data-theme="dark"] {
  --gray-50:  hsl(210, 20%, 8%);
  --gray-100: hsl(210, 18%, 12%);
  --gray-200: hsl(210, 16%, 18%);
  --gray-300: hsl(210, 14%, 25%);
  --gray-400: hsl(210, 12%, 35%);
  --gray-500: hsl(210, 10%, 45%);
  --gray-600: hsl(210, 10%, 55%);
  --gray-700: hsl(210, 10%, 70%);
  --gray-800: hsl(210, 12%, 82%);
  --gray-900: hsl(210, 14%, 93%);
  
  --bg-page: #0F1115;
  --bg-card: #161A20;
  --bg-elevated: #1C2127;
  
  --border-subtle: rgba(255, 255, 255, 0.06);
  --border-default: rgba(255, 255, 255, 0.10);
  --border-strong: rgba(255, 255, 255, 0.16);
}

/* ========== BASE STYLES ========== */

body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: 1.6;
  color: var(--text-primary);
  background: var(--bg-page);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1 { 
  font-family: var(--font-display);
  font-size: var(--text-5xl); 
  line-height: 1.1; 
  letter-spacing: -0.02em;
  font-weight: 700;
}

h2 { 
  font-family: var(--font-display);
  font-size: var(--text-4xl); 
  line-height: 1.2; 
  letter-spacing: -0.02em;
  font-weight: 600;
}

h3 { 
  font-size: var(--text-2xl); 
  line-height: 1.3; 
  letter-spacing: -0.01em;
  font-weight: 600;
}

p { 
  max-width: 65ch; 
}

.uppercase {
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Components */
.btn {
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-default);
  font-weight: 500;
  transition: all var(--duration-fast) var(--ease-out);
}

.btn:focus-visible {
  outline: 2px solid var(--text-primary);
  outline-offset: 2px;
}

.card {
  padding: var(--space-6);
  border-radius: var(--radius-lg);
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  box-shadow: var(--shadow-sm);
  transition: box-shadow var(--duration-normal) var(--ease-out);
}

.card:hover {
  box-shadow: var(--shadow-md);
}

.input {
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-default);
  border: 1px solid var(--border-default);
  transition: border-color var(--duration-fast), box-shadow var(--duration-fast);
}

.input:focus {
  border-color: var(--text-primary);
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.1);
  outline: none;
}
```
