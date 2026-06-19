# PRD template

The PRD is the source of truth for *what* and *why* — agent-executable. Iterate it critically (draft → `ce-doc-review` → improve, repeated). Keep *how* in `plan.md`, not here.

```markdown
---
date: YYYY-MM-DD
tags: [<track>, project, prd]
status: active
type: project
---

# <Project> — PRD

## 1. Problem statement
The user pain / business need. Why now. (Pulled from the confirmed problem + discovery.)

## 2. Goals & success metrics
Each metric has THREE parts — see references/metrics.md:
| Metric | How we measure it | Target |
|--------|-------------------|--------|
| e.g. organic sessions to the page | GA4 | +20% in 3 months |
| e.g. signup conversion | Mixpanel funnel | 2% → 3.5% |

## 3. Non-goals / out of scope
Explicit. Bounds what the agent may touch. (Critical — agents over-reach without this.)

## 4. User stories
- As a <user>, I want <action> so that <benefit>.

## 5. Functional requirements
What the system must do.

## 6. Non-functional requirements
Performance, security, accessibility, compliance.

## 7. Design considerations
UI/UX, and **design-system alignment** (which components/tokens; see resources.md).

## 8. Technical considerations
APIs, integrations, constraints, the linked repo(s).

## 9. Acceptance criteria (EARS)
Use EARS — fixed clause order — so criteria are testable:
- Ubiquitous:   The <system> shall <response>.
- State-driven: While <precondition>, the <system> shall <response>.
- Event-driven: When <trigger>, the <system> shall <response>.
- Unwanted:     If <unwanted condition>, then the <system> shall <response>.
Write the error/edge paths as "If…then…" — that's how you force the agent to handle them.

## 10. Boundary block
- ✅ Always do: <safe actions, no approval needed>
- ⚠️ Ask first: <high-impact actions>
- 🚫 Never do: <hard stops — e.g. never commit secrets, never touch prod data>

## 11. Open questions & risks
```

## EARS quick reference
EARS = Easy Approach to Requirements Syntax (Alistair Mavin). The five patterns above keep acceptance criteria unambiguous and machine-checkable. Always include at least one "If…then…" for the main failure mode.
