---
name: ship
description: "Use when the user invokes /ship or hands over a brief to build, implement, or ship a CODE feature or project end-to-end — a sentence, a voice note, or a link to a Linear issue / Notion doc. Triggers on '/ship', 'let's ship X', 'build this feature', 'start a new project'. Not for n8n workflows, content, or vault-only notes — those keep their own skills."
---

# ship — the brief-to-shipped pipeline

`ship` is a **thin orchestrator**: it sequences existing Compound Engineering (CE) and superpowers skills into one standardized loop and adds only the glue. It does NOT re-implement brainstorming, planning, review, or testing. Full rationale + the detailed reuse map live in the Obsidian vault at `Personal/projects/ship/design.md`.

## Two non-negotiables
1. **Obsidian-first.** All project docs live in the vault under `/<track>/projects/<name>/`. The code repo is only *linked*. CE skills default to writing into the repo's `docs/` — `ship`'s core custom job is to **bridge** every output into the vault project folder (`references/bridging.md`). Code → repo; docs → Obsidian.
2. **Two human gates.** Gate 1 after the plan; Gate 2 after all build phases. Autonomous in between.

## Pipeline
```
ENTRY  Intake ........ parse brief, ask for missing info, set up project
A 1.   Discovery ..... discovery.md   (4 streams)
  2.   Brainstorm .... brainstorm.md  (critical loop)
  3.   PRD ........... prd.md         (critical loop; EARS + metrics+targets)
  4.   Plan .......... plan.md        (phases; tests-first; +tracking +metrics-check)
  ★ GATE 1 — user approves PRD + plan
B (per phase → build/phase-N.md)
  5.   Implement (TDD)   6. Unit tests   7. Adversarial review
  8.   Design-system    9. E2E/browser  10. Demo   11. Compound (incremental)
  ★ GATE 2 — user reviews everything (all demos + full diff)
C 12.  Ship + CI autofix       13. Compound consolidation
```
Create a TodoWrite item per step of the current stage; tick as gates pass.

## Entry — Intake
1. **Read the brief** (fetch the link if it's one). Extract what's asked and for which product/track.
2. **Resume check.** If the project folder + anchor already exist, read the anchor's Status and **resume from the last incomplete step**.
3. **Resolve `resources.md`** (`references/resources-template.md`): project-level overrides track-level, lists merge. If neither exists, ask and create it.
4. **Ask only for missing essentials** (track, repo, name, design system, data sources) — one concise batch, then proceed.
5. **Scaffold** the folder + anchor (`references/anchor-template.md`). Write the problem statement into the anchor and **confirm it** before Discovery (problem-first).

## Stage A — Definition
1. **Discovery → `discovery.md`** — full discovery across **4 streams**: market, competitor benchmarking, user research (Reddit etc.), existing data (the project's own sources in `resources.md`). Use `deep-research`, web search, the `ce-web-researcher` / `ce-best-practices-researcher` / `ce-issue-intelligence-analyst` agents, and the declared MCPs. **Flag useful MCPs that aren't installed.** See `references/discovery-checklist.md`.
2. **Brainstorm → `brainstorm.md`** — `ce-brainstorm` (optionally `ce-ideate`), fed `discovery.md`. A **loop**: draft → self-critique → revise, repeated.
3. **PRD → `prd.md`** — draft with `ce-brainstorm`, then iterate with `ce-doc-review` until clean. Structure per `references/prd-template.md`: non-goals, **EARS** acceptance criteria, ✅/⚠️/🚫 boundaries, and metrics as **what + how + target** (`references/metrics.md`).
4. **Plan → `plan.md`** — `ce-plan`: stable-ID, checkable, **tests-first**, anti-scope-creep, split into **phases**. Must add a **metrics-tracking step** and a **metrics-check step**.

**★ GATE 1** — present `prd.md` + `plan.md`, wait for explicit approval, revise if asked.

## Stage B — Build (loop once per phase)
For each phase, create `build/phase-N-<slug>.md` (`references/phase-doc-template.md`) and run the loop; each gate must pass before the next:

| Step | Skill / agent | Gate |
|---|---|---|
| 5. Implement (TDD) | `ce-work` + `test-driven-development` | code written test-first |
| 6. Unit tests | `ce-work` / `tests-run` | green |
| 7. Adversarial review (+ reuse/consistency) | `ce-code-review` | no open P1s |
| 8. Design-system check (UI only) | `ce-design-implementation-reviewer` / `ce-figma-design-sync` | matches design system |
| 9. E2E / browser | `ce-test-browser` | green; add tests if missing |
| 10. Demo capture | `ce-demo-reel` | one recording per phase, linked in phase doc |
| 11. Compound (incremental) | capture into phase doc | learnings written while context is fresh |

Record gate outcomes, demo link, and learnings in the phase doc; update the anchor Status after each phase.

**★ GATE 2** — after ALL phases, surface every demo + the full diff, wait for review.

## Stage C — Ship
12. **Ship** — `ce-commit-push-pr`, then CI-watch + autofix (the `lfg` pattern): fix real issues, ≤3 iterations, record unresolved findings.
13. **Compound consolidation** — merge per-phase learnings into the anchor; **promote recurring fixes into rules/skills** (CLAUDE.md, new skills). Then register the **metrics follow-up** (anchor item; offer to schedule via the `schedule` skill).

We do NOT invoke `lfg` directly — it starts at `ce-plan`, with no discovery/brainstorm/PRD and no human gates. We take its build→ship pattern and wrap it.

## References
`bridging.md` (CE output → Obsidian) · `resources-template.md` · `discovery-checklist.md` · `prd-template.md` · `metrics.md` · `phase-doc-template.md` · `anchor-template.md`
