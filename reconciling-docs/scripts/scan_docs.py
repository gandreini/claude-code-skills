#!/usr/bin/env python3
"""Recency-aware static scan for the reconciling-docs skill.

Gathers the deterministic evidence a reconciliation needs, so the model can
focus on the judgment: which conflicting doc is the current source of truth.
Standard library only -- no pip install required.

Per document it collects recency signals:
  - in-document dates (frontmatter date/updated/modified, and dates in the body)
  - git last-commit date (if the folder is a git repo)
  - filesystem mtime
  - version-like filename flags (v2, final, draft, updated, copy, dates, "(2)")

And across the set it surfaces:
  - likely version stacks (same-folder filenames that normalise to one base)
  - repeated filenames across folders (per-project files, NOT version stacks)
  - paragraphs duplicated across two or more docs
  - broken Obsidian [[wikilinks]] and relative markdown links

Usage:
  python3 scan_docs.py <folder> [--min-dupe-words 12] [--ignore DIR ...] [--json]
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ALWAYS_IGNORE = {".git", ".obsidian", ".trash"}
MIN_DT = datetime.min.replace(tzinfo=timezone.utc)

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FM_DATE_RE = re.compile(
    r"^(?:date|updated|modified|last[-_]updated|last[-_]modified):\s*([^\s#]+)",
    re.IGNORECASE | re.MULTILINE,
)
ISO_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
SUPERSEDE_RE = re.compile(r"\b(supersedes?|superseded|deprecat\w+|replaces?|obsolete)\b", re.IGNORECASE)
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
MDLINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
WORD_RE = re.compile(r"\w+", re.UNICODE)
CODEFENCE_RE = re.compile(r"```.*?```", re.DOTALL)

# Tokens that mark a filename as a version of some base doc.
VERSION_TOKEN_RE = re.compile(
    r"\b(v?\d+(\.\d+)*|final|finalv?\d*|draft|old|new|copy|updated|revised|"
    r"latest|backup|wip|\d{4}-\d{2}-\d{2}|\d{8})\b",
    re.IGNORECASE,
)
PAREN_NUM_RE = re.compile(r"\((\d+)\)\s*$")
TRAIL_NUM_RE = re.compile(r"[ _-]\d+$")


# Document roles in the funnel: exploration -> specification -> plan -> tasks ->
# status. Same-role docs for one goal are the primary reconciliation target;
# cross-role differences are the funnel working, not contradictions.
ROLE_FILENAME = [
    ("exploration",   re.compile(r"\b(brainstorm|ideas?|exploration|scratch)\b", re.I)),
    ("specification", re.compile(r"\b(requirements?|prd|spec|specification)\b", re.I)),
    ("plan",          re.compile(r"\b(plan|roadmap)\b", re.I)),
    ("tasks",         re.compile(r"\b(todo|tasks?|checklist|next[-_ ]?steps?)\b", re.I)),
    ("changelog",     re.compile(r"change[-_ ]?log\b", re.I)),  # matches changelog.md and CLAUDE_CHANGELOG.md
    ("status",        re.compile(r"\b(status|handoff|deploy(?:ment)?|"
                                 r"one[-_ ]?week[-_ ]?check|retro|report|done)\b", re.I)),
    ("index",         re.compile(r"\b(readme|index|overview)\b", re.I)),
]
ROLE_FOLDER = {"brainstorms": "exploration", "brainstorm": "exploration",
               "plans": "plan", "plan": "plan", "specs": "specification",
               "requirements": "specification", "tasks": "tasks"}
ROLE_FM_TYPE = {"feat": "plan", "fix": "plan"}
# Roles where 2+ docs for one goal is debt worth flagging. Multiple brainstorms or
# reference docs are fine; multiple READMEs are handled by repeated-filenames.
COMMITTAL_ROLES = {"specification", "plan", "tasks", "status"}
# Path parts that organise a project's docs but don't define a separate project.
DOC_SUBDIRS = {"docs", "doc", "plans", "plan", "brainstorms", "notes", "specs"}


def infer_role(stem: str, parent_name: str, fm_type) -> str:
    """Best-guess role from filename, then parent folder, then frontmatter type."""
    for role, rx in ROLE_FILENAME:
        if rx.search(stem):
            return role
    if parent_name.lower() in ROLE_FOLDER:
        return ROLE_FOLDER[parent_name.lower()]
    if fm_type and fm_type.lower() in ROLE_FM_TYPE:
        return ROLE_FM_TYPE[fm_type.lower()]
    return "other"


def project_key(rel: str) -> str:
    """Group docs by project, ignoring doc-organising subfolders (docs/, plans/),
    so a plan in plans/ and a todo in the project root count as one project."""
    parts = [p for p in Path(rel).parent.parts if p.lower() not in DOC_SUBDIRS]
    return "/".join(parts) if parts else "."


FM_TYPE_RE = re.compile(r"^type:\s*([^\s#]+)", re.IGNORECASE | re.MULTILINE)


def find_docs(root: Path, ignore: set) -> list:
    skip = ALWAYS_IGNORE | ignore
    return [
        p for p in root.rglob("*.md")
        if not any(part in skip for part in p.relative_to(root).parts)
    ]


def resolution_root(scan_root: Path, git_toplevel):
    """Where wikilinks resolve FROM — the whole vault/repo, not just the scanned
    subfolder. Obsidian resolves [[links]] vault-wide, so a link pointing outside
    the scanned subfolder is not broken; checking it against only the subfolder's
    files produces false positives. Prefer the enclosing Obsidian vault (the dir
    holding `.obsidian`), else the git toplevel, else the scan root itself."""
    for d in [scan_root, *scan_root.parents]:
        if (d / ".obsidian").is_dir():
            return d
    return git_toplevel or scan_root


def split_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    return (m.group(1), text[m.end():]) if m else (None, text)


def parse_date(s: str):
    m = ISO_DATE_RE.search(s)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def doc_dates(frontmatter, body):
    """Return (max_date_or_None, has_supersede_language)."""
    dates = []
    if frontmatter:
        for v in FM_DATE_RE.findall(frontmatter):
            d = parse_date(v)
            if d:
                dates.append(d)
    for v in ISO_DATE_RE.findall(body):
        d = parse_date(v)
        if d:
            dates.append(d)
    return (max(dates).isoformat() if dates else None,
            bool(SUPERSEDE_RE.search(body)))


def git_last_commit_dates(root: Path):
    """Map repo-relative path -> ISO last-commit date. {} if not a git repo."""
    try:
        top = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=10,
        )
        if top.returncode != 0:
            return None, {}
        toplevel = Path(top.stdout.strip())
        log = subprocess.run(
            ["git", "-C", str(root), "log", "--format=__C__%cI", "--name-only"],
            capture_output=True, text=True, timeout=60, errors="replace",
        )
        if log.returncode != 0:
            return toplevel, {}
        dates = {}
        current = None
        for line in log.stdout.splitlines():
            if line.startswith("__C__"):
                current = line[5:].strip()
            elif line.strip() and current and line not in dates:
                dates[line.strip()] = current  # log is newest-first; keep first seen
        return toplevel, dates
    except (subprocess.SubprocessError, OSError, ValueError):
        return None, {}


def filename_flags(stem: str):
    return sorted({m.group(0).lower() for m in VERSION_TOKEN_RE.finditer(stem)})


def cluster_base(stem: str) -> str:
    """Normalise a filename stem by stripping version tokens, for grouping."""
    s = stem.lower()
    s = PAREN_NUM_RE.sub("", s).strip()
    s = VERSION_TOKEN_RE.sub("", s)
    s = re.sub(r"[ _-]+", " ", s).strip(" -_")
    s = TRAIL_NUM_RE.sub("", s).strip()
    return s


def link_target(raw: str) -> str:
    t = raw.split("|", 1)[0].split("#", 1)[0].strip()
    if not t:
        return ""
    if t.lower().endswith(".md"):
        t = t[:-3]
    return Path(t).name.lower()


def normalize_block(block: str) -> str:
    block = re.sub(r"^[#>\-\*\d\.\s]+", "", block.strip())
    return re.sub(r"\s+", " ", block).lower()


def to_dt(iso):
    if not iso:
        return None
    try:
        if len(iso) == 10:
            return datetime.strptime(iso, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return datetime.fromisoformat(iso)
    except ValueError:
        return None


def scan(root: Path, min_dupe_words: int, ignore: set) -> dict:
    docs = find_docs(root, ignore)
    toplevel, git_dates = git_last_commit_dates(root)

    # Resolve wikilinks against the whole vault/repo, not just the scanned
    # subfolder, so links leaving the scope aren't false-flagged as broken.
    res_root = resolution_root(root, toplevel)
    link_basenames = (
        {p.stem.lower() for p in find_docs(res_root, ignore)}
        if res_root != root else {p.stem.lower() for p in docs}
    )
    link_scope = str(res_root) if res_root != root else None

    inventory = []
    clusters = defaultdict(list)
    broken = defaultdict(list)
    block_index = defaultdict(list)

    for p in docs:
        rel = str(p.relative_to(root))
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        fm, body = split_frontmatter(text)
        ddate, supersede = doc_dates(fm, body)

        git_iso = None
        if git_dates and toplevel:
            try:
                git_iso = git_dates.get(str(p.resolve().relative_to(toplevel)))
            except ValueError:
                git_iso = None
        mtime_iso = datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).isoformat(timespec="seconds")

        # Prefer reliable signals (in-doc date, git) over mtime, which a
        # checkout or sync resets to "now" and would otherwise mask everything.
        doc_dt, git_dt, mtime_dt = to_dt(ddate), to_dt(git_iso), to_dt(mtime_iso)
        reliable = [s for s in (doc_dt, git_dt) if s]
        if reliable:
            best = max(reliable)
            source = "doc" if (doc_dt and best == doc_dt) else "git"
        elif mtime_dt:
            best, source = mtime_dt, "mtime"
        else:
            best, source = None, None
        latest = best.isoformat(timespec="seconds") if best else None

        flags = filename_flags(p.stem)
        fm_type_m = FM_TYPE_RE.search(fm) if fm else None
        fm_type = fm_type_m.group(1) if fm_type_m else None
        role = infer_role(p.stem, p.parent.name, fm_type)
        inventory.append({
            "path": rel,
            "role": role,
            "project": project_key(rel),
            "doc_date": ddate,
            "git_date": git_iso,
            "mtime": mtime_iso,
            "latest": latest,
            "date_source": source,
            "supersede_language": supersede,
            "filename_flags": flags,
        })

        # Cluster version stacks per-folder: a README/TODO/plan in each project
        # subfolder is normal, not a version of the others. Grouping by (folder,
        # base) keeps stacks scoped to a single directory and avoids that false
        # positive when reconciling a parent of many project subfolders.
        base = cluster_base(p.stem)
        if base:
            clusters[(str(Path(rel).parent), base)].append(rel)

        for raw in WIKILINK_RE.findall(text):
            tgt = link_target(raw)
            if tgt and tgt not in link_basenames:
                broken[rel].append(f"[[{raw}]]")
        for raw in MDLINK_RE.findall(text):
            link = raw.split("#", 1)[0].split(" ", 1)[0].strip()
            if link and "://" not in link and not link.startswith(("#", "mailto:")) and link.lower().endswith(".md"):
                if not (p.parent / link).resolve().exists():
                    broken[rel].append(f"]({raw})")

        for block in re.split(r"\n\s*\n", body):
            norm = normalize_block(block)
            if len(WORD_RE.findall(norm)) >= min_dupe_words:
                block_index[norm].append((rel, re.sub(r"\s+", " ", block.strip())[:120]))

    # Version stacks: same normalised base in the SAME folder, 2+ distinct files.
    version_stacks = []
    for (folder, base), members in clusters.items():
        members = sorted(set(members))
        if len(members) >= 2:
            rows = [next(d for d in inventory if d["path"] == m) for m in members]
            rows.sort(key=lambda d: to_dt(d["latest"]) or MIN_DT, reverse=True)
            version_stacks.append({
                "base": base,
                "folder": folder,
                "members": [{"path": r["path"], "latest": r["latest"],
                             "flags": r["filename_flags"]} for r in rows],
            })
    version_stacks.sort(key=lambda s: -len(s["members"]))

    # Same base name in different folders: almost always one-per-project files
    # (README, TODO, changelog), NOT a version stack. Surfaced separately so the
    # model treats each as its own scope rather than a contradiction.
    by_base = defaultdict(set)
    for (folder, base), members in clusters.items():
        for m in set(members):
            by_base[base].add(m)
    repeated_filenames = sorted(
        ({"base": base, "locations": sorted(paths)}
         for base, paths in by_base.items()
         if len({str(Path(p).parent) for p in paths}) >= 2),
        key=lambda r: (-len(r["locations"]), r["base"]),
    )

    duplicates = []
    for norm, occ in block_index.items():
        distinct = sorted({o[0] for o in occ})
        if len(distinct) >= 2:
            duplicates.append({"snippet": occ[0][1], "locations": distinct, "count": len(occ)})
    duplicates.sort(key=lambda d: (-len(d["locations"]), -d["count"]))

    # Same-role pile-ups: 2+ docs of the same committal role in one project — the
    # primary reconciliation target (two plans, two task lists). Cross-role
    # differences (brainstorm vs plan) are the funnel working and are NOT flagged.
    role_groups = defaultdict(list)
    for d in inventory:
        if d["role"] in COMMITTAL_ROLES:
            role_groups[(d["project"], d["role"])].append(d)
    same_role_clusters = []
    for (proj, role), members in role_groups.items():
        if len(members) >= 2:
            members = sorted(members, key=lambda d: to_dt(d["latest"]) or MIN_DT, reverse=True)
            same_role_clusters.append({
                "project": proj, "role": role,
                "members": [{"path": m["path"], "latest": m["latest"]} for m in members],
            })
    same_role_clusters.sort(key=lambda c: (-len(c["members"]), c["project"], c["role"]))

    return {
        "root": str(root),
        "link_scope": link_scope,
        "is_git_repo": bool(git_dates),
        "total_docs": len(inventory),
        "documents": sorted(inventory, key=lambda d: to_dt(d["latest"]) or MIN_DT, reverse=True),
        "version_stacks": version_stacks,
        "repeated_filenames": repeated_filenames,
        "same_role_clusters": same_role_clusters,
        "duplicate_paragraphs": duplicates,
        "broken_links": {k: v for k, v in sorted(broken.items())},
    }


def render_text(r: dict) -> str:
    out = [f"# Reconciliation scan — {r['root']}", ""]
    out.append(f"Docs: {r['total_docs']}  |  git repo: {'yes' if r['is_git_repo'] else 'no'}  "
               f"|  same-role pile-ups: {len(r.get('same_role_clusters', []))}  "
               f"|  version stacks: {len(r['version_stacks'])}  "
               f"|  duplicate paragraphs: {len(r['duplicate_paragraphs'])}")
    if not r["is_git_repo"]:
        out.append("(no git history — recency rests on in-doc dates, filenames, and mtime, which is weaker)")
    out.append("")

    src = r.get("same_role_clusters", [])
    out.append("## Same-role pile-ups (PRIMARY target — 2+ docs of one role per project)")
    if src:
        for c in src[:30]:
            out.append(f"  {c['role']} ×{len(c['members'])} in {c['project']}/:")
            for m in c["members"]:
                out.append(f"      {m['path']}  (latest: {m['latest'] or 'unknown'})")
        if len(src) > 30:
            out.append(f"  ...and {len(src) - 30} more")
        out.append("  (two docs of the SAME role for one goal — candidates to collapse to one. "
                   "Cross-role differences like brainstorm-vs-plan are NOT here: that's the funnel.)")
    else:
        out.append("  none — at most one doc per committal role per project (well-organised)")
    out.append("")

    out.append("## Likely version stacks (same folder — compare these for supersession)")
    if r["version_stacks"]:
        for s in r["version_stacks"][:30]:
            loc = s.get("folder") or "."
            out.append(f"  base \"{s['base']}\" in {loc}/:")
            for m in s["members"]:
                flags = f" [{', '.join(m['flags'])}]" if m["flags"] else ""
                out.append(f"      {m['path']}  (latest: {m['latest'] or 'unknown'}){flags}")
        if len(r["version_stacks"]) > 30:
            out.append(f"  ...and {len(r['version_stacks']) - 30} more")
    else:
        out.append("  none")
    out.append("")

    rep = r.get("repeated_filenames", [])
    if rep:
        out.append("## Repeated filenames across folders (likely per-project, NOT versions)")
        for s in rep[:30]:
            out.append(f"  \"{s['base']}\": {', '.join(s['locations'])}")
        if len(rep) > 30:
            out.append(f"  ...and {len(rep) - 30} more")
        out.append("  (treat each as its own scope unless content shows they're truly the same doc)")
        out.append("")

    dup = r["duplicate_paragraphs"]
    out.append(f"## Duplicate paragraphs — {len(dup)} (same text in 2+ docs)")
    if dup:
        for d in dup[:30]:
            out.append(f"  - \"{d['snippet']}...\"")
            out.append(f"      in: {', '.join(d['locations'])}")
        if len(dup) > 30:
            out.append(f"  ...and {len(dup) - 30} more")
    else:
        out.append("  none")
    out.append("")

    out.append("## Recency table (newest first; 'via' = signal used; role = funnel stage)")
    docs = r["documents"]
    for d in docs[:50]:
        sup = " SUPERSEDE-LANG" if d["supersede_language"] else ""
        flags = f" [{', '.join(d['filename_flags'])}]" if d["filename_flags"] else ""
        src = d["date_source"]
        via = f" (via {src}{'—weak' if src == 'mtime' else ''})" if src else " (no date)"
        out.append(f"  {d['latest'] or 'unknown'}{via}  [{d.get('role', 'other')}]  {d['path']}{flags}{sup}")
        out.append(f"      doc-date: {d['doc_date'] or '-'}   git: {d['git_date'] or '-'}   mtime: {d['mtime']}")
    if len(docs) > 50:
        out.append(f"  ...and {len(docs) - 50} more (use --json for all)")
    out.append("")

    bl = r["broken_links"]
    total = sum(len(v) for v in bl.values())
    out.append(f"## Broken links — {total} across {len(bl)} docs")
    if r.get("link_scope"):
        out.append(f"  (wikilinks resolved vault-wide against {r['link_scope']})")
    if bl:
        for src, links in list(bl.items())[:25]:
            out.append(f"  - {src}: {', '.join(links[:10])}")
        if len(bl) > 25:
            out.append(f"  ...and {len(bl) - 25} more docs")
    else:
        out.append("  none")
    out.append("")
    out.append("Mechanical evidence only. Which conflicting doc is authoritative is a "
               "judgment call — read the clustered docs and apply the checklist.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Recency-aware docs reconciliation scan.")
    ap.add_argument("root", help="Folder to reconcile")
    ap.add_argument("--min-dupe-words", type=int, default=12)
    ap.add_argument("--ignore", action="append", default=[])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        sys.exit(f"Not a directory: {root}")

    result = scan(root, args.min_dupe_words, set(args.ignore))
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else render_text(result))


if __name__ == "__main__":
    main()
