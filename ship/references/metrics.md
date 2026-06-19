# Metrics lifecycle

Impact is only visible after the feature has lived for weeks/months — so metrics span three moments. Don't conflate "tracking works" with "target reached."

## In the PRD — metric = what + how + target
Every success metric carries three parts:
- **What** — the metric (e.g. organic sessions, signup conversion, retention).
- **How** — the measurement method/tool (e.g. GA4, Mixpanel funnel, Search Console).
- **Target** — the number to hit and by when (e.g. "+20% in 3 months", "2% → 3.5%").

A metric without a target is not done. Pin the number.

## In the plan & build — implement tracking, gate on "it works"
- `plan.md` must include a **metrics-tracking implementation step** (instrument the events / wire up GA4/Mixpanel/etc.).
- The build gate is: **the tracking works** — events fire, data lands in the right tool, the metric is actually trackable. Verify with a real event, not an assertion.
- We do NOT gate ship on "target reached" — that's unknowable at ship time.

## After ship — follow-up: real vs target
Register a dated follow-up in the anchor's "Metrics follow-up" section:
- Default cadence: **+4 weeks** (early signal) and **+3 months** (real read).
- Each follow-up: pull the actual number via the declared tool, compare to target, note the verdict + any action.
- **Offer to schedule** it as a cloud routine (the `schedule` skill) so it isn't forgotten; if the user declines, the dated anchor item is the reminder.
