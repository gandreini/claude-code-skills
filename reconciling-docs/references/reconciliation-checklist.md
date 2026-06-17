# Reconciliation checklist

The judgment rubric for Step 3. The scan finds version stacks, duplicates, and recency signals; this file defines the calls a script can't make. Read it, then read the actual docs — most findings only surface when you read two docs together.

## First, classify each doc's role

Reconciliation works *within a role*, not across stages. Tag every doc with its place in the funnel:

> exploration (brainstorm, notes, ideas) → specification (requirements, PRD, spec) → plan → tasks (todo, checklist, next-steps) → status (status, handoff, changelog, deployment, README/index)

Signals: the `type:` frontmatter, the filename (`*-plan`, `*-requirements`, `todo`, `next-steps`), and the parent folder (`brainstorms/`, `plans/`). Each stage narrows the one before it — so two docs only *contradict* if they sit at the **same role for the same goal** and disagree.

## Is it a contradiction, or the funnel working?

Not every difference is a conflict. Before flagging, ask two things: *can both be true at once?* and *do these docs share a role and goal?*

**Real contradictions (flag these):**
- **Same-role pile-up — the primary target.** Two+ docs of the *same role* for the *same goal* that disagree: two plans, two task/todo lists, two PRDs, two status docs. Collapse to one; archive or merge the rest.
- Two same-role docs state the same fact with different values — a number, date, name, path, decision.
- Two same-role docs give opposite instructions for the same situation ("deploy from main" / "deploy from a release tag").
- A doc that claims **current state** (status/index/README/handoff) asserts something false about the built system.

**The funnel working — do NOT flag, do NOT "fix":**
- An exploratory doc explored options a later plan didn't choose. The unchosen ideas are the *record of why the choice was made* — never edit a brainstorm to match the plan.
- Different roles at different commitment levels on one topic — a brainstorm weighing A/B/C vs a plan committing to B. Expected, not a contradiction.
- An older plan/brainstorm being *behind* what shipped. At most a light "superseded by [[current]]" pointer on a plan; nothing on a pure brainstorm. Reality docs (status/deployment) carry the truth — the earlier intent docs don't need rewriting to agree.
- Different scopes that only look similar; a summary of another doc; same meaning, different wording.

When unsure, flag it as a question for the user rather than asserting a conflict that may not exist.

**Contradictions can live inside one doc, not just between two.** A doc revised in place often updates one section and leaves another stale — a decision changed in the "Decisions" list but not in an earlier "Summary", a number corrected in one table but not its restatement below. The cross-doc framing ("read two docs side by side") will miss these, so read each doc as a whole and check it against *itself*. The scan's `SUPERSEDE-LANG` flag and any in-doc `updated:` date are cues that a doc was edited after creation — exactly the docs most likely to carry a stale leftover. When a doc contradicts itself, the later/more-specific section (a dated "Decision", a detailed requirement) usually wins over an early summary; fix the summary to match.

## Supersession patterns

These are the shapes the "newer silently replaced older" problem takes. Watch for them:

- **Version stack** — `plan.md`, `plan-v2.md`, `plan-final.md`. Usually one is current and the rest are history nobody archived. Identify the current one; propose archiving the rest.
- **Decision drift** — an early "we'll use X" doc, then a later doc casually assuming Y, with no doc recording the switch. The later one usually reflects reality; confirm and make the older one point to it.
- **Duplicated-then-edited** — a doc was copied and one copy edited. They now disagree in the edited spots. The edited copy is usually newer; verify with dates.
- **Orphaned scratch docs** — `notes.md`, `tmp.md`, `summary 2.md` that captured a moment and were never reconciled into the main docs. Often safe to archive once their unique content is folded in.
- **Reality outran the plan** — an intent doc (plan/spec) records what was *intended*, then a later status/handoff/deployment doc describes what was *actually built*, and they diverge. The reality doc **outranks** the intent doc on any fact about what exists. **But the action depends on the lagging doc's role** (don't over-correct): if the wrong doc is itself a *state-claiming* doc — a README, project index, or status doc asserting a falsehood about the current system — **fix it**, that's a real bug. If it's a *plan/spec* that simply describes superseded intent, a light "superseded by [[current]]" pointer is enough — do **not** rewrite the plan to match reality. If it's an *exploration/brainstorm*, leave it entirely; being overtaken by reality is its natural end state. The thing to hunt is the *index/status doc lying about the current system*, not every plan that history moved past.

- **Summary drift (anchor digest vs detail).** When a project uses the digest-anchor convention (`<project>.md` summarizing `requirements`/`plan`/`status`/`tasks`), the anchor *summarizes* and never owns new facts. If a summary section disagrees with its detail doc, the **detail wins** — refresh the summary, never edit the detail to match the anchor. There's no winner to judge here, so it's a high-confidence, reversible fix. See `references/project-structure.md`.

**Not a supersession pattern — repeated filenames across folders.** When reconciling a parent of several project subfolders, the same filename recurs once per project (`README.md`, `TODO.md`, `CLAUDE_CHANGELOG.md`, `next-steps.md`). The scan lists these under "Repeated filenames across folders" precisely *because they are not a version stack*. Each belongs to its own project scope. Only treat two same-named docs as a real conflict if their content shows they're meant to be the same document (e.g. one was copied out of the other), not merely that they share a name.

## Weighing the recency signals

The script reports, per doc: in-document dates, git last-commit date, mtime, and version-like filename flags. Combine them:

- **Signals agree** → high confidence. State the winner plainly.
- **Signals disagree** (e.g. mtime is recent but git date and in-doc date are old — a re-save or sync touched the file) → trust the *content and git* signals over mtime, and say why.
- **No dated signals at all** (untracked, undated docs) → fall back to filename hints and content, and flag the recommendation as low-confidence.
- **The newer doc looks exploratory** (a draft, a "thinking out loud" note) while the older is a clean settled record → newer-wins may be wrong. Surface both and ask.

Recency tells you which is *latest*. Whether latest means *authoritative* is the user's call — make the recommendation, show the evidence, let them confirm.

## Repetition

Substantial content living in two places will drift into the contradictions above. Consolidate: keep one canonical doc, replace the copies with a link or fold them in. A short repeated reminder is fine; a duplicated process or spec is debt.

## Clarity and conciseness

Once docs agree, make them readable:
- **Buried point** — the conclusion arrives late. Lead with it.
- **Bloat** — long passages that restate themselves; trim.
- **Undefined terms / ambiguous references** — "the new approach" with no anchor.

These matter, but they rank below correctness — reconcile the conflicts first.

## Severity tiers

- **Critical** — contradictions a reader could act on and get wrong.
- **High** — likely-superseded docs and substantial duplication: correct-ish today, rotting, and the source of tomorrow's contradictions.
- **Medium** — clarity problems.
- **Low** — minor conciseness and style.

## How to write a finding

Specific enough to act on without re-investigating:

- **What's in dispute** — the claim, with the conflicting text quoted briefly.
- **The docs and their evidence** — each doc by name, with its recency signals.
- **Recommended source of truth** — one doc, with the reason (cite the strongest signal).
- **Action for the loser** — archive / mark superseded / merge. One concrete option, not a menu.

**Example finding:**
> **Critical — auth flow conflict.** [[onboarding]] (git: 2024-02, no in-doc date) says new users verify by SMS. [[auth-spec-v2]] (git: 2024-09, frontmatter `updated: 2024-09-12`, filename flagged `v2`) says email magic-link. Both signals point to `auth-spec-v2` as current. **Source of truth: [[auth-spec-v2]].** Action for [[onboarding]]: update the verification line to match and add `superseded` note on the old method, or link to the spec. Confirm SMS wasn't intentionally kept as a fallback before changing.
