# Bridging CE/superpowers output into Obsidian

The defining constraint: **all docs live in the Obsidian vault**, but the CE skills default to writing artifacts into the *code repo* (`docs/brainstorms/`, `docs/plans/`, `docs/solutions/`). `ship` is the bridge. The canonical copy is ALWAYS the Obsidian one.

## Two bridging tactics (pick per skill)
1. **Redirect (preferred where supported).** When a skill lets you specify the output path or you can instruct it in-prompt, point it directly at the Obsidian project folder. Tell the skill: "write the output to `<vault>/<track>/projects/<name>/<doc>.md`."
2. **Relocate (fallback).** When a skill insists on writing to the repo `docs/`, let it write, then **move the file** into the Obsidian project folder under the canonical name, and leave a one-line pointer in the repo (`docs/…: moved to Obsidian vault — see project anchor`).

Either way: normalize the filename to ship's convention, update the anchor's Status + Documents, and never duplicate code into Obsidian (link the repo path instead).

## Per-skill mapping
| Skill | Default output | Bridge to | Tactic |
|-------|----------------|-----------|--------|
| `ce-brainstorm` | `docs/brainstorms/…` | `brainstorm.md` (and seed `prd.md`) | redirect, else relocate |
| `ce-doc-review` | inline / review notes | fold critique into `prd.md` revisions | redirect (in-prompt) |
| `ce-plan` | `docs/plans/…` | `plan.md` | redirect, else relocate |
| `ce-work` | code in repo + scratch | code stays in repo; status → `build/phase-N.md` | n/a for code; bridge notes |
| `ce-code-review` | review output | findings/verdict → `build/phase-N.md` | capture in-prompt |
| `ce-test-browser` | test run output | result → `build/phase-N.md` | capture |
| `ce-demo-reel` | GIF/video file + PR snippet | store/link recording in `build/phase-N.md` | capture link |
| `ce-compound` | `docs/solutions/…` | per-phase → `build/phase-N.md`; consolidated → anchor Learnings | relocate + summarize |
| `ce-commit-push-pr` | git commit + PR | PR link → anchor Status | capture link |

## Invariants
- **Code → repo. Docs → Obsidian.** No exceptions.
- The **anchor** is the index; keep its Status + Documents current after every step.
- Every bridged doc carries the standard vault frontmatter (`date / tags / status / type`).
- Repo path is recorded once in `resources.md`; docs *link* to it, never copy code.
