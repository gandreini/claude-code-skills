---
name: reconciling-docs
description: "Use when the user wants to reconcile, consolidate, clean up, de-duplicate, tidy, or sort out a folder or Obsidian vault of accumulated Markdown docs, notes, plans, or specs — especially when documents a coding agent piled up over time have begun to contradict, duplicate, or silently supersede each other and the user needs to know which version is authoritative. Triggers even without the word 'reconcile' — also 'these docs disagree', 'which doc is current', 'too many overlapping notes', 'clean up this vault/project folder'. Works on a single folder or a parent folder of many project subfolders."
---

# Reconciling Docs

A coding agent working in a project folder tends to keep *adding* documents — plans, specs, notes, summaries. Over time they drift: two *plan* docs for one goal say different things, a second *task list* appears, nobody marked which is current. This skill makes the set **well-organized**: one authoritative doc per goal, no contradicting duplicates, current and clear.

**Reconciliation is not flattening — divergence across stages is the system working.** A brainstorm that explores five directions and a later plan that commits to one are *supposed* to differ. The brainstorm is not "wrong" and must **never** be edited to match the plan — the exploration is a valuable record of why the chosen path won. Do not back-propagate decisions into exploratory docs.

The real target is narrower: **redundant or contradictory docs that share the same role and goal** — two plans, two task lists, two PRDs for one objective, saying different things — plus genuine duplication and docs that misstate the current state. **Reconcile within a role, not across stages.** When two same-role docs conflict, the defining problem is **supersession**: usually the newer is the truth and the older is stale debt. Deciding which version wins, and collapsing to one, is the whole job.

## Scope discipline: only the in-scope docs are sources

**The single source of truth is the set of docs being reconciled — nothing else.** Do not import facts, statuses, or `[[links]]` from your own memory of other projects, other folders, or earlier in the session. When reconciling several projects in one run, treat each project's folder as a sealed scope: one project's framing must never bleed into another's. Every claim you write (especially in a generated digest) must be traceable to a doc *in that scope*; if it isn't there, leave it out. (Real failure mode: a digest invented a "lever of [[a-sibling-project]]" relationship by pattern-matching another project carried in context — pure cross-scope bleed.)

## Two modes: report (default) vs apply (opt-in)

The skill runs one of two ways, chosen from the user's request:

- **Report mode (default).** "reconcile / review / check / what's inconsistent in X" → run the workflow through the report and **stop. Read-only — change nothing.**
- **Apply mode (opt-in).** "reconcile and fix / clean up / consolidate / sort out / organize / reconcile straight away / just do it" → do everything report mode does, then **apply the resolutions** per "Apply mode" below.

When the verb is ambiguous, **default to report** and offer to apply — applying edits the user's real notes, so read-only is the safe default.

**Apply mode runs near-autonomously after one question.** Its single interactive touchpoint is confirming the **project stage** (see "The one question") — inferred and presented for a quick yes/correct. After that it does not pause on each judgment call — it acts on **everything reversible**, makes its best call on contested winners, and surfaces those calls in a terse summary afterward. This is safe only because of the safety net (git snapshot + archive-never-delete): a wrong call is one `git revert` away, not lost data. The human's role moves from approving each step to **reading the synthetic summary and reverting anything mis-judged.** The only hard stops left are genuinely irreversible actions (deletion) and the no-git-repo case — see "Apply mode".

## What to reconcile — and what to leave alone

Every doc has a **role** in a lifecycle that funnels from open to committed:

> exploration (brainstorm, notes, ideas) → specification (requirements, PRD, spec) → plan → tasks (todo, checklist, next-steps) → status (status, handoff, changelog, deployment, README/index)

Each stage *narrows* the one before it. Divergence **down** the funnel is correct and expected.

**Leave alone (not findings):**
- An exploratory doc that considered options the later plan didn't pick. The unchosen ideas are the record of the decision — do not "correct" or prune them to match what shipped.
- Different roles covering the same topic at different commitment levels (a brainstorm weighing A/B/C vs a plan choosing B). Not a contradiction.
- An old plan/brainstorm being *behind* what was later built — at most it earns a light "superseded by [[current]]" pointer, never a rewrite. Exploratory docs don't even need that.

**Reconcile (the real targets):**
- **Same-role pile-up (primary).** Two or more docs of the *same role* for the *same goal* that disagree — two plans, two task/todo lists, two PRDs, two status docs. Collapse to **one** authoritative doc per role+goal; archive or merge the rest.
- **State misstatements.** Any doc (especially status/index/README) that asserts something false about the current built system.
- **Genuine duplication.** The same content maintained in two places, which will drift.
- **Summary drift.** A project anchor's digest no longer matches its detail doc — the detail wins, refresh the digest. See `references/project-structure.md`.
- **Structure & naming (when asked).** Inconsistent layout/filenames across projects. Normalize toward the convention in `references/project-structure.md`. This is opt-in organization, separate from content conflicts.

The test for a contradiction is: *do these two docs occupy the same role and goal, and disagree?* If they're different stages of the funnel, it's not a contradiction — it's the funnel.

## The one question: project stage

Status reconciliation has a ground truth that isn't in the docs and is fragile to verify from code (often impossible — the real state is deployed, not in a local file). The human knows it instantly. So the skill asks **one** question — **"What stage is this project at?"** — and with that answer does the rest autonomously. In apply mode this is the *only* interactive touchpoint.

**Infer, then confirm** — don't ask cold. Read the likely stage from the docs and present it for the user to accept or correct (one pre-filled prompt; in a multi-project run, all projects at once, so it stays a single cheap interaction).

| Stage | Authoritative for state | What the skill then does |
|---|---|---|
| **Exploring** | nothing is "current truth" yet | leave brainstorms; don't force-resolve |
| **Planning** | requirements / plan (latest) | reconcile plan + spec; flag any doc claiming it's built |
| **Building** | plan + tasks/status (in-progress) | keep working docs active; status = in progress |
| **Shipped (live)** | status / handoff / reality docs | fix any "planned / pending / next: write the plan" line; plans → historical intent (funnel); set `status: shipped` |
| **Archived** | status = complete, nothing open | archive working docs (tasks, checklists) to `_archived/`; set `status: archived` |

The **declared stage is the top authority for state claims** — above reality-doc recency, above git. A doc that disagrees with it is stale by definition: fix or archive it. (This is why "is enforcement live?" or "next: implementation plan" on a shipped project resolve instantly once the stage is known.)

**Headless fallback (no human to ask):** in an autonomous/cron run, infer the stage from the docs — and, if the project frontmatter has a `repos:` pointer that resolves locally, corroborate from git, flagged `⚠ inferred, prod state unconfirmed`. The human question is always preferred; code-check is only the fallback.

## How to judge which doc is newer

For **state claims** (is it built? live? done?), the **declared project stage** (see "The one question") outranks everything below — a doc that contradicts the confirmed stage is stale, full stop. For everything else, never trust a single signal. The scan script collects four, in roughly descending order of reliability:

1. **Explicit in-document statements** — "supersedes X", "as of <date>", "deprecated", a frontmatter `date:`/`updated:`. The author's own claim about currency is the strongest evidence.
2. **Git last-commit date** — if the folder is a git repo, when the file was last changed in history. Reliable, since it survives file rewrites.
3. **File modification time (mtime)** — weakest. Agent rewrites, git checkouts, and cloud sync all reset it. A hint, not proof.
4. **Version-like filenames** — `plan-v2.md`, `spec-final.md`, `notes-updated.md`. Suggestive of a version stack, but `final` is famously unreliable. Treat as a flag to investigate, not a verdict.

**Recommend newer-wins, but verify.** A newer doc can be an abandoned draft or a tangent, while the older one holds the settled decision. When signals disagree or the newer doc looks exploratory, say so and ask rather than asserting.

## Workflow

### Step 1 — Locate the folder and confirm scope
Reconcile whatever folder the user points at, **and all Markdown beneath it** — the scan recurses automatically. Note whether it's a git repo (the script detects this) — git history is your best recency signal. Confirm before reconciling a very large folder.

**Single project vs multi-project parent.** A folder can be one project's docs, or a *parent of many project subfolders* (e.g. a `projects/` folder of per-project subfolders). When it's a parent, **reconcile within each project subfolder, not across them.** Two projects describing different things the same way is not a contradiction. Tell-tale sign in the scan: the "Repeated filenames across folders" section — a `README.md`/`TODO.md`/`changelog.md` in each project is one-per-project, *not* a version stack. Only compare docs that share a real scope: same subfolder, or cross-project only when one doc explicitly references another. Group your report by project so the user sees per-project findings.

### Step 2 — Run the scan (the deterministic half)
Run `scripts/scan_docs.py` against the folder. It produces: **same-role pile-ups** (2+ docs of one role per project — the primary target), a per-doc recency table tagged with each doc's inferred role, likely version stacks (same-folder filename clusters), repeated filenames across folders (per-project files to *not* mistake for versions), duplicated paragraphs, and broken links. See "Running the scan". Summarise what it surfaced before going deeper — the same-role pile-ups first.

### Step 3 — Establish the project stage, then reconcile
**First, settle the stage** (see "The one question"): infer it per project from the docs and confirm with the user — in apply mode this is the single human touchpoint; in a headless run, infer it. The confirmed stage is the top authority for every state claim below.

Then read `references/reconciliation-checklist.md` first — it defines what counts as a contradiction (vs a harmless difference), the supersession patterns, how to weigh the recency signals, and the severity tiers. Then read the docs the scan grouped together — version stacks, docs sharing duplicated content, and docs on the same topic. **A contradiction only appears when you read two docs side by side**, so compare within each cluster. For each conflict, use the recency evidence to decide which doc is current.

### Step 4 — Synthetic summary (both modes diverge here)
- **Report mode:** give the **scannable summary of what you'd change** — counts plus the handful of changes that matter, grouped by project (see "Highlights format") — as the decision surface, then continue to the full report (Step 5). This is a checkpoint; change nothing.
- **Apply mode (near-autonomous):** **do not pause for approval.** Skip straight to acting (Step 6); the synthetic summary is delivered *after* the changes (Apply mode Step D), with `⚠` flags + a revert handle.

### Step 5 — Write the full reconciliation report (report mode)
Report mode only. Use the template below. Lead with contradictions/pile-ups. For each, show the conflicting claims, the recency evidence per doc, the recommended source of truth with the reason, and the proposed action for the loser. Then stop. (Apply mode skips this — it offers `expand` for the same detail on demand.)

### Step 6 — Apply (apply mode only)
Follow "Apply mode" below: snapshot → act on everything reversible (best call + flag on the hard ones) → hard-stop only on deletion / no-snapshot → re-scan → super-synthetic feedback.

## Running the scan

```bash
python3 scripts/scan_docs.py <folder>
```

Useful flags:
- `--min-dupe-words 12` — shortest paragraph length considered a duplicate (default 12).
- `--ignore <dir>` — extra folder to skip (repeatable). `.git`, `.obsidian`, `.trash` are always skipped.
- `--json` — machine-readable output (use this if the recency table is long; it carries every doc's full signals).

Read the output as a map of *where to look*. "Version stack" and "duplicate paragraph" are facts; "these two contradict and this one wins" is your judgment in Step 3.

## Highlights format

A tight synthesis the user can act on in seconds. Counts, then the few changes that matter most — ranked by severity, grouped by project, each one line: what's wrong → what you'd do. Link the full report for detail; don't restate it.

```markdown
## Reconciliation highlights — <folder>
Reviewed N docs across P projects. Found: C contradictions · S superseded stacks · D duplicate clusters · B broken links.

**Would change (most important first):**
- 🔴 <project-a>: [[doc-x]] and [[doc-y]] disagree on <thing> → keep [[doc-y]] (newer: git 2026-06), mark [[doc-x]] superseded.
- 🟠 <project-b>: [[plan]], [[plan-v2]] are a version stack → archive [[plan]], keep [[plan-v2]].
- 🟡 <project-a>: [[notes]] duplicates a section of [[spec]] → replace with a link.

Nothing here is changed yet. Want the full report, or should I apply the 🔴/🟠 items?
```

Keep it to the items worth a decision. If there are 30 low-severity nits, say "+27 minor (clarity, broken links) — in the full report" rather than listing them.

## Report structure

Use this template. Keep findings specific; skip empty sections.

```markdown
# Reconciliation report — <folder> (<date>)

## Summary
- Docs reviewed: N (across P projects) | Contradictions: C | Likely-superseded stacks: S | Duplicate clusters: D

## Findings by project
Group the sections below per project subfolder when reconciling a multi-project parent. A single-project folder needs no grouping.

## Same-role pile-ups — resolve these first
The primary target: 2+ docs of one role (plan, tasks, spec, status) for one goal that diverge. For each: which is authoritative, and what to do with the rest (collapse to one — merge unique content into the winner, archive the losers).

## Contradictions
For each conflict between same-role docs (or a state doc that misstates reality):
**<the claim in dispute>**
- [[doc-a]] — <role, recency evidence> — says: <X>
- [[doc-b]] — <role, recency evidence> — says: <Y>
- **Source of truth: [[doc-b]]** — <why, citing the strongest signal>. Action for [[doc-a]]: archive / mark `superseded_by: [[doc-b]]` / merge into [[doc-b]].

(Do not list brainstorm-vs-plan or other cross-stage funnel differences here — those are not findings.)

## Likely superseded — version stacks
For each filename cluster (e.g. plan, plan-v2, plan-final): which is current, and what to do with the rest.

## Duplicated content
For each overlap: which doc is canonical, replace the copies with a link or merge.

## Clarity & conciseness
Notes that are unclear, bloated, or bury the point — with a suggested direction.

## Broken links
Broken [[wikilinks]] by source doc.
```

## Apply mode

Near-autonomous: act on everything reversible, make the best call on the hard ones, **flag those calls in the summary instead of pausing for each.** The git snapshot + archive-never-delete net is what makes this safe — without it, fall back to asking.

### Step A — Snapshot first (the net that licenses autonomy)
Before changing anything, create a clean restore point:
- Confirm the folder is in a **git repo**. If it is, commit current state: `git add -A && git commit -m "pre-reconcile snapshot"` (note any pre-existing uncommitted changes to the user first — don't bury their work in the snapshot without saying so). Capture the commit SHA for the summary.
- If it is **not** a git repo, there is no clean rollback — autonomy is unsafe, so fall back to **report-only** (or archive-only, ask-before-each) and say why.
- Archiving means moving to `_archived/`, **never deleting.**

### Step B — Act on everything reversible
Apply in batches, safest first. With the snapshot in place, this includes the former "ask" cases — make the best call and flag it:
1. **Refresh anchor digests** (summary drift) — detail wins, no judgment.
2. **Annotate / archive superseded docs** (`status: superseded`, `superseded_by: [[current]]`; move losers to `_archived/`).
3. **Fix state/index/README lines** that misstate current reality.
4. **Normalize structure & naming** to `references/project-structure.md` (flatten, bare role names, create the `<project>.md` anchor, move non-docs out).
5. **Collapse same-role pile-ups** — pick the current doc on the recency evidence, fold unique content from the losers into the winner, archive the losers. This is the former "ask" case; now act and **flag it** (see Step D).

When moving/renaming, **update inbound `[[wikilinks]]`**. Make the **smallest change** that resolves each issue — don't rewrite a doc to fix one line. Never back-propagate into exploratory docs (the funnel).

### Step C — The only hard stops
Pause and ask **only** when an action is genuinely irreversible or unrecoverable:
- **Deletion** (vs archive) — always requires explicit say-so.
- **No git snapshot** was possible (Step A fell back).
Everything else is acted on and reported, not blocked.

### Step D — Super-synthetic feedback (the safety surface)
Re-run `scan_docs.py` to confirm pile-ups cleared, then report in **≤ ~8 lines**: a one-line headline with counts + the snapshot SHA, one line per action grouped by type, and a **`⚠` on every low-confidence judgment call** (contested winner, weak/disagreeing recency signals, an exploratory-looking newer doc) so the user's eye lands exactly where a revert might be needed. End with the revert handle. Terse by default; offer "say `expand` for the full report." Shape:

```
Reconciled <folder> — <N> changes · snapshot <sha>
✅ <auto fixes, one line>
🔀 merged <a>+<b> → <c>   ⚠ low-confidence: <the call made>
🗄 archived <n> → _archived/
↩ revert: git revert <sha>   ·   expand for detail
```

## Reference files

- `references/reconciliation-checklist.md` — the judgment rubric: contradictions vs harmless differences, supersession patterns, weighing recency signals, severity tiers, and how to write a finding. Read before Step 3.
- `references/project-structure.md` — the target layout & naming convention (flat per-project, bare role files, `<project>.md` human-digest anchor), the role vocabulary + frontmatter `type:`, the `_archived/` rule, and the Compound-Engineering → vault mapping. Read when the user wants docs *organized*, not only de-conflicted.
