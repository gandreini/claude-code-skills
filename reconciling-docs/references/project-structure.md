# Project structure & naming convention

The target shape reconciliation normalizes a project toward. Read this when the
user wants docs *organized* (consistent layout/naming), not only de-conflicted.
Apply it the same way as every other resolution: report first, then apply only on
request, archiving (never deleting) and committing first.

## The canonical project layout

One folder per project. Flat — no `docs/`, `plans/`, `brainstorms/` subfolders.

```
<project>/
  <project>.md      ← anchor: the human digest        (type: overview)
  requirements.md   ← the PRD / spec                  (type: requirements)
  plan.md           ← the implementation plan         (type: plan)
  tasks.md          ← todo / next-steps               (type: tasks)
  status.md         ← current state / handoff         (type: status)
  changelog.md      ← log, if any                     (type: changelog)
  brainstorm.md     ← exploration, optional           (type: exploration)
  <topic>.md        ← topical record / learning       (type: note)
  _archived/        ← superseded docs kept for history
```

Two rules make this serve both the human and the agent:

1. **The anchor is the only prefixed file** (`<project>.md`) — the one globally
   unique, linkable name. Every other doc is a **bare role name** (`plan.md`,
   `status.md`). The folder supplies the project context, so the prefix would be
   redundant noise. (Bare names collide across projects in Obsidian's basename
   resolution — link to inner docs with the path form `[[<project>/plan|plan]]`.)
2. **Every doc carries frontmatter `type:` and `status:`.** Role lives in the
   frontmatter, not just the filename — that is what the scan and the agent key
   off, independent of naming. `date:` (and `updated:`) go in frontmatter, not
   filenames.

## The anchor is a human digest, not another doc

`<project>.md` is the **human-readable rollup**: a short what/why, then a *summary*
of requirements, plan, status, and the top open tasks — each linking to its full
detail doc. You read one doc to be caught up; the detail docs (verbose,
agent-facing) carry the depth.

The anchor **summarizes, it never owns new facts.** Every line must be traceable to
a detail doc — **never introduce a fact, framing, status, or `[[link]]` that isn't in
the docs you're summarizing.** This explicitly includes project relationships: don't
call a project a "lever of X", a sub-project of Y, or link it to a sibling unless a
detail doc says so. When unsure whether something is supported, **omit it.** (Real
failure caught in testing: a digest invented a "lever of [[a-sibling-project]]"
relationship by pattern-matching another project — pure fabrication.) This is why the anchor is a
`⚠`-flagged action in apply mode: generated prose must be eyeballed.

The no-invention rule sets the direction of truth for one new finding type:

- **Summary drift** — an anchor section no longer reflects its source doc. The
  detail doc **always wins**; refresh the anchor's summary from it (never edit the
  detail to match the anchor). Also: a detail doc with no summary in the anchor →
  add one; an anchor summary whose source was archived → remove it.

Summary drift is the *easy* reconciliation — there is no winner to judge, so the
apply mode can refresh the digest as a high-confidence, reversible action.

## Role vocabulary

`overview` (anchor) · `requirements` · `plan` · `tasks` · `status` · `changelog`
· `exploration` (brainstorm/ideation) · `note` (topical record / learning) ·
`reference`. A role only takes a **qualifier** when it genuinely repeats:
`status-2026-06-18.md` (an intrinsic dated snapshot — the one allowed date-in-name)
or `tasks-external.md` (a second, distinct list). A repeated committal role is
usually a same-role pile-up to collapse, not to keep.

**Keep the bare-role convention consistent across tools.** When a tool's own
convention names a role-doc differently (e.g. CLAUDE.md historically wrote
`CLAUDE_CHANGELOG.md`), prefer to **align the tool to the bare-role name** —
`changelog.md` — and update that tool's instructions, rather than carry a one-off
exception. (The global CLAUDE.md was updated to `changelog.md` for exactly this.)
The scan still recognizes a legacy `CLAUDE_CHANGELOG.md` as the `changelog` role so
older repos reconcile cleanly.

## Not project docs — leave these alone

- **Root meta interface:** `AGENTS.md`, `CLAUDE.md`, `CONCEPTS.md`, `STRATEGY.md`,
  `README.md`. Shared contracts (CE and other tools read them). Never rename,
  rerole, or fold them into a project doc.
- **Config:** `.compound-engineering/`, `.claude/` — never moved into the vault.
- **Non-docs:** PDFs, images, `data/`, `scripts/`. Per the vault's own rule
  ("code stays in the repo"), these don't belong in a vault project — flag to move
  back to the repo; don't rename them.

## Mapping Compound-Engineering output → vault convention

CE writes in-repo, history-preserving, with everything in shared `docs/*` folders
whose filenames carry date+sequence+type to disambiguate. The vault uses
per-project folders, so the disambiguation moves to the folder and filenames go
bare. Both are internally consistent; reconciliation is the bridge at the
repo→vault boundary.

| CE (in-repo)                                   | Vault (flat, per project)                       |
|------------------------------------------------|-------------------------------------------------|
| `docs/brainstorms/<slug>-requirements.md`      | `requirements.md` (type: requirements)          |
| `docs/brainstorms/` other exploration          | `brainstorm.md` / `brainstorm-<topic>.md` (exploration) |
| `docs/ideation/…`                              | `brainstorm-<topic>.md` (exploration)           |
| `docs/plans/YYYY-MM-DD-NNN-<type>-<name>-plan.md` (latest) | `plan.md` (type: plan)               |
| `docs/plans/…` older dated plans               | `_archived/` (history kept, not deleted)        |
| `docs/solutions/…` learnings                   | `notes.md` / topical `<topic>.md` (note), or leave in repo |
| ce-work handoff / status notes                 | `status.md` (type: status)                      |
| `pulse-reports/`, `dogfood-reports/`, `residual-review-findings/` | ephemeral — leave in repo, don't ingest |
| `AGENTS.md` / `CONCEPTS.md` / `STRATEGY.md` / `CLAUDE.md` | unchanged at project root              |
| — (no CE equivalent)                           | `<project>.md` ← the human digest anchor (skill creates it) |

**Collapse CE's plan history.** CE accumulates dated plans by design; the vault
keeps one living `plan.md` (latest wins) and archives the older dated ones to
`_archived/`. That is the same-role-pile-up resolution applied to a version stack.

Archive with **`_archived/`** (matches CE's `solutions/_archived`), never delete.
