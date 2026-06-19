# `resources.md` — schema & resolution

The reusable resource config for a project or a whole track. Holds everything `ship` needs to *operate* (not the work output): the linked code repo, design system, test commands, and the data sources / MCPs used in discovery.

## Two levels, with inheritance

- **Track level** — `/<track>/resources.md` (e.g. `/Mondo/resources.md`). Defaults shared by every project in the track. Use this when the track has stable, recurring resources (the Mondo case).
- **Project level** — `/<track>/projects/<name>/resources.md`. For an isolated one-off project with its own resources, or to **override/extend** the track defaults.

**Resolution rule (run at Intake):** read project-level first, then track-level, **merge with project winning**. Scalar fields: project overrides track. List fields (data sources, MCPs): **project entries are added to** track entries. If neither file exists, ask the user and create one in the right place (track if recurring, project if isolated; ask if unsure).

## Schema

```markdown
---
date: YYYY-MM-DD
tags: [<track>, resources]
status: active
type: reference
---

# <Track or Project> — resources

## Code repos
| Name | Path | Stack | Notes |
|------|------|-------|-------|
| Web App | /Users/.../mondosurf-web | Next.js | public site |
<!-- For Mondo, this can simply say: see the `mondo` skill. -->

## Design system
- Source: <path / Figma file / token source>
- Reviewer target: <what ce-design-implementation-reviewer should compare against>

## Commands
- unit:  <command>
- e2e:   <command>
- lint:  <command>
- build: <command>

## Data sources (for Discovery stream 4 — existing data)
| Source | Tool / MCP | What it tells us |
|--------|-----------|------------------|
| Search Console | gscServer | queries, rankings, indexing |
| Analytics | analytics-mcp (GA4) | traffic, behaviour |
| Product analytics | Mixpanel | funnels, events |
| Google Alerts | (manual / feed) | brand & topic mentions |

## Discovery MCPs (streams 1–3 — looking outward)
- google-trends — demand/interest
- web-search / web-fetch — market + competitors
- deep-research — deep multi-source synthesis
<!-- Note any MCP NOT installed but worth adding for this project. -->

## Tracker (optional)
- Issues: <Linear / GitHub / Notion>
```

## Mondo note
Mondo's repos are already enumerated in the `mondo` skill — `/Mondo/resources.md` can reference it (`Code repos: see the mondo skill`) instead of duplicating paths, and focus on data sources, design system, and commands.
