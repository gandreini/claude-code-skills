# `success.md` — the definition-of-success doc

The durable "did this work?" reference for a project. Drafted from the PRD's success definition, finalized at ship, and **revisited after release** to check whether the key results were hit. This is the primary future reference — when someone reopens the project months later, `success.md` answers "was it worth it?".

It is its own document (`/<track>/projects/<name>/success.md`), not a table buried in the anchor. The anchor links to it.

## What it holds
- **Definition of success** — 1–2 sentences: what "this worked" actually means.
- **Key results** — the metrics framed as targets to hit, with baseline, target, and the event(s)/telemetry that measure them.
- **Telemetry & events** — the specific events to instrument and the tool they land in (Mixpanel, GA4, Search Console, …).
- **Verification schedule** — the time(s) after release to check. **Defined here** (e.g. +4 weeks, +3 months).
- **Verification log** — filled in post-release: actual vs target, verdict, action.

## Lifecycle
1. **PRD (Stage A)** — define metrics, events, telemetry, and the success definition. These flow into `success.md`.
2. **Build (Stage B)** — implement the tracking; the metrics-check gate verifies **each event/metric here is actually live in the tool** (fire a real event, see it land), not just that "some" tracking exists.
3. **Ship (Stage C)** — finalize `success.md` with concrete verify-by dates; register the verification (anchor item; offer to schedule via the `schedule` skill).
4. **After release** — at each verify-by date, pull the actual numbers from the tool, fill the log, and record hit / miss / partial per key result.

## Template
```markdown
---
date: YYYY-MM-DD
tags: [<track>, project, success]
status: active   # active | verified
type: project
---

# <Project> — Success

## Definition of success
What "this worked" means, in plain words.

## Key results
| KR | Metric | Telemetry / tool | Event(s) | Baseline | Target | Verify by |
|----|--------|------------------|----------|----------|--------|-----------|
| KR1 | e.g. signup conversion | Mixpanel funnel | signup_started → signup_completed | 2% | 3.5% | 2026-08-01 (+4w) |
| KR2 | e.g. organic sessions | GA4 | page_view (guide pages) | 12k/mo | +20% | 2026-10-01 (+3m) |

## Telemetry & events to instrument
- <event name> — fired when … — lands in <tool> — properties: …

## Verification schedule
- +4 weeks (YYYY-MM-DD): early signal
- +3 months (YYYY-MM-DD): real read

## Verification log (filled post-release)
| Date | KR | Target | Actual | Verdict | Action |
|------|----|--------|--------|---------|--------|
```

Rule: a project is not "done" without a `success.md` carrying at least one key result with a target and a verify-by date. If success can't be defined, that's a signal the brief is too vague — surface it.
