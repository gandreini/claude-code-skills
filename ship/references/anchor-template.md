# Anchor template — `<project-name>.md`

The project's home page in Obsidian: status, doc index, consolidated learnings, and the metrics follow-up. It is also the **resume pointer** — Intake reads the Status section to continue a half-finished project.

```markdown
---
date: YYYY-MM-DD
tags: [<track>, project]
status: active   # active | shipped | archived
type: project
---

# <Project name>

One-line description. Linked code repo: `<path>` (details in resources.md).

## Problem
The confirmed problem statement (written at Intake, before discovery).

## Status
Current step in the pipeline — this is what Intake reads to resume.
- [ ] 1. Discovery — [[discovery]]
- [ ] 2. Brainstorm — [[brainstorm]]
- [ ] 3. PRD — [[prd]]
- [ ] 4. Plan — [[plan]]
- [ ] ★ Gate 1 (PRD + plan approved)
- [ ] Build phases — see build/
- [ ] ★ Gate 2 (review)
- [ ] 12. Shipped (PR: <link>)
- [ ] 13. Compound consolidated

## Documents
- [[discovery]] · [[brainstorm]] · [[prd]] · [[plan]]
- Build: [[build/phase-1-...]] …

## Learnings (consolidated at ship)
- Promoted to rules/skills: <what became automatic>

## Metrics follow-up
| When | Metric | Target | Actual | Verdict |
|------|--------|--------|--------|---------|
| +4 weeks (YYYY-MM-DD) | … | … | | |
| +3 months (YYYY-MM-DD) | … | … | | |
```
