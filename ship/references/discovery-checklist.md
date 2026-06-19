# Discovery — the 4 streams

Discovery is a **full-fledged** investigation, not a quick context grab. Output goes to `discovery.md`. Run the streams in parallel where possible (dispatch research agents concurrently). Ground every claim in a source — cite URLs and the tool used.

## Stream 1 — Market
Understand the market around the brief: size/demand, trends, seasonality, adjacent solutions, pricing norms.
- Tools: `google-trends` MCP (demand/interest, related queries), web search/fetch, `deep-research` skill, `ce-best-practices-researcher` agent.

## Stream 2 — Competitor benchmarking
Who already solves a similar problem, and how. Capture: who they are, their approach, what's good, what's missing, what to beat.
- Tools: web search/fetch, `ce-web-researcher` agent, `deep-research`.

## Stream 3 — User research
Understand the users relevant to the brief: their language, pains, jobs-to-be-done, objections.
- Tools: web search of communities (Reddit, forums, reviews), `ce-web-researcher` agent. Quote real user voices where found.

## Stream 4 — Existing data (current state)
Snapshot how things stand *today* using the project's OWN data sources (from `resources.md`). This grounds the brief in reality, not guesses.
- Mondo example sources: Google Alerts (mentions), Search Console (`gscServer` — queries/rankings/indexing), Google Analytics (`analytics-mcp` — traffic/behaviour), Mixpanel (funnels/events).
- Also read existing product issues if a tracker is configured (`ce-issue-intelligence-analyst`).

## Tooling-gap scan (required)
While gathering, note any **MCP/tool that is NOT installed but available** and would deepen discovery (e.g. a Reddit MCP, a Mixpanel MCP, a specific competitor-intel tool). List them in a "Tooling gaps" section of `discovery.md` with a one-line reason, so the user can decide whether to install before going deeper.

## `discovery.md` shape
```markdown
---
date: YYYY-MM-DD
tags: [<track>, project, discovery]
status: active
type: reference
---

# <Project> — Discovery

## Summary (what we now know going in)
- 3–6 bullets, the load-bearing findings.

## 1. Market
## 2. Competitors
## 3. Users
## 4. Existing data (current state)

## Tooling gaps (MCPs/tools worth installing)
| Tool | Why it would help | Installed? |

## Sources
- URLs + tool used for each claim.
```
