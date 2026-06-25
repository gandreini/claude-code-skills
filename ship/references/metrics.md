# Metrics & success lifecycle

Impact is only visible after the feature has lived for weeks/months — so success spans four moments. Don't conflate "tracking works" with "target reached." The durable artifact is **`success.md`** (`references/success-template.md`).

## In the PRD — define what success means
The PRD must define, not just a vague goal:
- **Definition of success** — what "this worked" means in plain words.
- **Metrics** — what + how + target: the metric, the measurement tool (GA4, Mixpanel, Search Console…), and the number to hit (e.g. "2% → 3.5%"). A metric without a target is not done — pin the number.
- **Events & telemetry** — the specific events to instrument and the tool they land in. Targets need events behind them; name them now.
- **Key results** — the targets framed as KRs (hit / miss), each with a verify-by horizon.

These flow straight into `success.md`.

## In the plan & build — implement tracking, gate on "it works"
- `plan.md` must include a **metrics-tracking implementation step** (instrument the events / wire up GA4 / Mixpanel / etc.).
- The build gate: **every event/metric in `success.md` is actually live in the tool** — fire a real event, see it land. Not "some tracking exists" — each defined one, verified.
- We do NOT gate ship on "target reached" — that's unknowable at ship time.

## At ship — finalize `success.md`
Write concrete verify-by dates (default **+4 weeks** early signal, **+3 months** real read). Register the verification: a dated anchor item, and **offer to schedule** it as a cloud routine (the `schedule` skill) so it isn't forgotten.

## After release — verify key results
At each verify-by date, pull the actual numbers via the declared tool, fill the **verification log** in `success.md`, and record hit / miss / partial per key result + any action. This is the moment the project earns (or doesn't) its "done."
