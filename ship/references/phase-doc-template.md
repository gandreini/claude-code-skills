# Phase doc template — `build/phase-N-<slug>.md`

One file per build phase. It is the running record of the per-phase loop (steps 5–11): what the phase does, the gate outcomes, the demo, and the learnings captured while context is fresh.

```markdown
---
date: YYYY-MM-DD
tags: [<track>, project, build]
status: active   # active | done
type: project
---

# Phase N — <slug>

## Goal
What this phase delivers (1–3 sentences). Links to the plan.md unit(s) it implements.

## Scope
- In:  <what this phase touches>
- Out: <what it deliberately doesn't>

## Build loop
| Step | Status | Evidence / notes |
|------|--------|------------------|
| 5. Implement (TDD) | ☐/✅ | commit(s): … |
| 6. Unit tests | ☐/✅ | command + result |
| 7. Adversarial review | ☐/✅ | P1s: none / list; ce-code-review output |
| 8. Design-system check | ☐/✅/n/a | reviewer verdict (UI phases only) |
| 9. E2E / browser | ☐/✅ | command + result |
| 10. Demo capture | ☐/✅ | link to recording/GIF |
| 11. Compound (incremental) | ☐/✅ | see Learnings below |

## Demo
- <link to the GIF/video for this phase>

## Learnings (incremental compound)
- What worked, what didn't, any gotcha. Captured now, consolidated into the anchor at ship.
- Candidate rule/skill promotions: <anything worth making automatic>
```

Granularity rule: one phase doc per plan phase. If a phase has no UI, mark step 8 `n/a`. Keep evidence concrete (commands + results, not "passed").
