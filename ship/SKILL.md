---
name: ship
description: "Use when the user invokes /ship or hands over a brief to build a CODE feature or project end-to-end. Runs the standardized pipeline brief → discovery → brainstorm → PRD → plan → per-phase build → ship → measure, orchestrating existing Compound Engineering and superpowers skills, with ALL documentation living in the Obsidian vault (not the code repo). Triggers on '/ship', 'let's ship X', 'new feature/project' for a code project, or sharing a brief / Linear issue / Notion doc to implement. Not for n8n workflows or vault-only notes — those keep their own skills."
---

# ship — the brief-to-shipped pipeline

`ship` is a **thin orchestrator**. It does NOT re-implement brainstorming, planning, review, or testing. It **sequences existing skills** — the Compound Engineering (CE) plugin and superpowers — into one standardized loop, and adds only the glue they don't provide. ~90% reuse; this skill owns the spine.

The full design rationale lives in the Obsidian vault at `Personal/projects/ship/design.md`. This file is the executable contract.

## Two non-negotiable principles

1. **Obsidian-first.** ALL documentation for a project lives in the Obsidian vault under `/<track>/projects/<project-name>/`. The code repo is only *linked*, never the home of docs. CE skills default to writing into the repo's `docs/` — `ship`'s main custom job is to **bridge** every output into the Obsidian project folder (see `references/bridging.md`).
2. **Two human gates, autonomous in between.** Gate 1 after the plan; Gate 2 after all build phases. Everything else runs without stopping.

## The pipeline at a glance

```
ENTRY  Intake ......... parse brief, ask for missing info, set up project
─────── Stage A — Definition (linear) ───────────────────────────
  1.   Discovery ...... discovery.md   (4 streams)
  2.   Brainstorm ..... brainstorm.md  (critical loop)
  3.   PRD ............ prd.md         (critical loop; EARS + metrics+targets)
  4.   Plan ........... plan.md        (phases; tests-first; +tracking +metrics-check)
  ★ GATE 1 — user approves PRD + plan
─────── Stage B — Build (loop ONCE PER PHASE) ───────────────────
  5.   Implement (TDD)        build/phase-N.md
  6.   Unit tests
  7.   Adversarial review (+ reuse/consistency)
  8.   Design-system check    (UI phases only)
  9.   E2E / browser
 10.   Demo capture           (one recording per phase)
 11.   Compound (incremental)
  ★ GATE 2 — user reviews everything (all demos + full diff)
─────── Stage C — Ship ──────────────────────────────────────────
 12.   Ship + CI autofix
 13.   Compound consolidation
```

Checklist discipline: when running `ship`, create a TodoWrite item per step of the current stage and tick them off as gates pass.

---

## ENTRY — Intake

The user triggers `/ship` with a **brief** — a sentence, a voice transcript, a pasted block, or a link (Linear issue, Notion doc, etc.). Then:

1. **Read the brief.** If it's a link, fetch it. Extract: what is being asked, for which product/track.
2. **Resume check.** If `/<track>/projects/<name>/` already exists with an anchor, read the anchor's **Status** section and **resume from the last incomplete step** instead of starting over.
3. **Resolve `resources.md`** (see `references/resources-template.md`): read the project-level file if present, then the track-level file, **merge with project winning**. If neither exists, ask the user and create it in the right place (track if recurring like Mondo, project if isolated).
4. **Ask for missing essentials only.** Track, code repo path, project name, design system, data sources — ask for whatever isn't already known from the brief or `resources.md`. Ask concisely (AskUserQuestion), one batch, then proceed.
5. **Scaffold.** Create `/<track>/projects/<project-name>/` and the anchor `<project-name>.md` from `references/anchor-template.md`. Write the problem statement into the anchor and **confirm it with the user** before discovery (problem-first).

Intake is the trigger, not a numbered step. Do not start Discovery until the problem is confirmed and `resources.md` resolved.

---

## Stage A — Definition

### 1. Discovery → `discovery.md`
A full-fledged discovery across **4 streams** — see `references/discovery-checklist.md`:
1. **Market** — market research relevant to the brief.
2. **Competitor benchmarking** — go online: who solves a similar problem, and how.
3. **User research** — understand the users (e.g. Reddit and other sources relevant to the brief).
4. **Existing data** — snapshot the current state via the project's own data sources (Mondo: Google Alerts, GSC, GA, Mixpanel).

Use **all** available tools: `deep-research` skill, web search/fetch, research agents (`ce-web-researcher`, `ce-best-practices-researcher`, `ce-issue-intelligence-analyst`), and the MCPs declared in `resources.md`. **Also flag MCPs/tools that are NOT installed but available** and worth adding to go deeper — list them in a "Tooling gaps" section of `discovery.md`.

### 2. Brainstorm (critical loop) → `brainstorm.md`
Invoke `ce-brainstorm` (optionally `ce-ideate` first). Feed `discovery.md` in as context. This is a **loop, not one-shot**: draft → self-critique (challenge assumptions, hunt gaps — CE's Product Pressure Test) → revise, repeated until it stops improving. Bridge the output into `brainstorm.md`.

### 3. PRD (critical loop) → `prd.md`
Draft the PRD with `ce-brainstorm`, then **iterate critically** with `ce-doc-review` (adversarial / product-lens / design-lens / security-lens personas): draft → review → criticize → improve, repeated until clean. Structure per `references/prd-template.md`: problem, goals, **non-goals**, user stories, functional/non-functional requirements, design & technical considerations, **acceptance criteria in EARS**, **boundary block (✅/⚠️/🚫)**, open questions. Every metric carries **what + how + numeric target** (see `references/metrics.md`).

### 4. Plan → split into phases → `plan.md`
Invoke `ce-plan`: stable-ID, checkable steps, **tests-first ordering**, anti-scope-creep. Output is N **phases**. Custom additions every plan must include: a **metrics-tracking implementation step**, and a **metrics check** step (verifies tracking *works*, not that targets are met).

### ★ GATE 1 — user approves PRD + plan
Stop. Present `prd.md` + `plan.md`. Wait for explicit approval. Apply changes and re-present if requested.

---

## Stage B — Build (loop once per phase)

For each phase in `plan.md`, create `build/phase-N-<slug>.md` from `references/phase-doc-template.md` and run the loop. Each step has a gate that must pass before the next:

| Step | Skill / agent | Gate |
|---|---|---|
| 5. Implement (TDD) | `ce-work` + superpowers `test-driven-development` | code written test-first |
| 6. Unit tests | `ce-work` / `tests-run` | green |
| 7. Adversarial review (+ reuse/consistency) | `ce-code-review` (adversarial, maintainability, pattern-recognition) | no open P1s |
| 8. Design-system check | `ce-design-implementation-reviewer` / `ce-figma-design-sync` | matches design system (UI phases only) |
| 9. E2E / browser | `ce-test-browser` | green; add tests if missing |
| 10. Demo capture | `ce-demo-reel` | one recording per phase, linked in phase doc |
| 11. Compound (incremental) | capture learnings into phase doc | learnings written while context is fresh |

Record gate outcomes, the demo link, and incremental learnings in the phase doc. Update the anchor Status after each phase.

### ★ GATE 2 — user reviews everything
After ALL phases complete, stop. Surface all per-phase demos + the full diff. Wait for the user's review before shipping.

---

## Stage C — Ship

### 12. Ship + CI autofix
Invoke `ce-commit-push-pr`. Then run the CI-watch + autofix loop (the `lfg` pattern): repair real issues, cap iterations (≤3), and **record unresolved findings** in the PR body / anchor rather than hiding them.

### 13. Compound consolidation
Merge the per-phase learnings into the anchor's Learnings section. Then **promote recurring fixes into rules/skills**: update `CLAUDE.md`, or create/extend a skill, so the next project is cheaper. Ask: *"would the system catch this automatically next time?"* — if not, that's the promotion to make.

Finally, register the **metrics follow-up** (see `references/metrics.md`): a dated checklist item in the anchor (e.g. +4 weeks / +3 months) comparing real vs target. Offer to schedule it as a cloud routine.

---

## Reuse map (what `ship` calls)

| Phase | Reuses | Custom glue |
|---|---|---|
| Intake | — | parse brief, ask missing info, resolve `resources.md`, scaffold |
| 1. Discovery | `ce-web-researcher`, `ce-best-practices-researcher`, `ce-issue-intelligence-analyst`, `deep-research`, MCPs | 4 streams, user research, existing-data read, uninstalled-MCP scan |
| 2. Brainstorm | `ce-brainstorm` (+ `ce-ideate`) | feed discovery; force loop; bridge to Obsidian |
| 3. PRD | `ce-brainstorm` + `ce-doc-review` | PRD structure (EARS, non-goals, boundaries, metrics+targets) |
| 4. Plan | `ce-plan` | tracking-impl step + metrics-check step |
| 5–6. Implement + unit | `ce-work` + `test-driven-development` + `tests-run` | — |
| 7. Adversarial review | `ce-code-review` | reuse/consistency emphasis |
| 8. Design-system | `ce-design-implementation-reviewer` / `ce-figma-design-sync` | point at project DS |
| 9. E2E | `ce-test-browser` | — |
| 10. Demo | `ce-demo-reel` | one per phase |
| 11 + 13. Compound | `ce-compound` idea | redirected to Obsidian; per-phase + consolidated |
| 12. Ship | `ce-commit-push-pr` + `lfg` CI loop | — |

We do **not** invoke `lfg` directly — it starts at `ce-plan` with no discovery/brainstorm/PRD and no human gates. We take its build→ship pattern and wrap it.

## References
- `references/bridging.md` — how to redirect each CE skill's output into Obsidian
- `references/resources-template.md` — `resources.md` schema + track/project resolution
- `references/discovery-checklist.md` — the 4 discovery streams + tooling-gap scan
- `references/prd-template.md` — PRD structure + EARS acceptance criteria
- `references/metrics.md` — metric = what + how + target; tracking gate; follow-up
- `references/phase-doc-template.md` — `build/phase-N.md` template
- `references/anchor-template.md` — project anchor `<project>.md` template
