#!/usr/bin/env python3
"""zetta-sync Phase A+B: one keyed, agent-ready GitHub issue per wtm artifact.

Goal: every issue is a SELF-CONTAINED brief a worktree agent can act on with no
extra context — provenance, content, a derived Definition of Done, traceability
cross-linked to sibling issues BY ISSUE NUMBER, a References block (engine repo +
build, blueprint docs page, product context, wtm source-of-truth), and a
"picking this up" footer.

Phase A: create missing issues (idempotent — keyed by `[KEY]` title prefix).
Phase B: reconcile EVERY body against the now-complete key->issue# map so
         traceability + DoD cross-link by #number (GitHub autolinks). Edits
         only when the rendered body differs from what's live, so re-runs are cheap.

Reads artifacts.json + relations.json (dumped from wtm; READ-ONLY on wtm — never
calls a wtm write tool). Saves issue-map.json incrementally (resumable).
Throttled + retries on GitHub secondary rate limits.

Usage:  python3 create_issues.py [--dry]
"""
import json, subprocess, time, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = "oramasearch/zetta"
DOCS_REPO = "oramasearch/zetta-docs"
DRY = "--dry" in sys.argv

arts = json.load(open(f"{BASE}/artifacts.json"))
rels = json.load(open(f"{BASE}/relations.json"))
MAP = f"{BASE}/issue-map.json"
issue_map = json.load(open(MAP)) if os.path.exists(MAP) else {}

by_key = {a["key"]: a for a in arts}

out_rel, in_rel = {}, {}
for r in rels:
    rt = r.get("relation") or r.get("type")
    out_rel.setdefault(r["from"], []).append((rt, r["to"]))
    in_rel.setdefault(r["to"], []).append((rt, r["from"]))

# wtm domain -> MkDocs page that will render the artifact (anchor = key-lower)
DOMAIN_PAGE = {
    "strategy": "strategy", "stakeholder": "personas", "requirements": "requirements",
    "architecture": "architecture", "domain": "domain-model", "data": "data",
    "api": "apis", "security": "security", "ux": "ux", "delivery": "delivery",
    "backlog": "backlog", "testing": "testing", "risk": "risks", "governance": "governance",
}
def page_for(a):
    if a["type"] == "glossary_term":
        return "glossary"
    return DOMAIN_PAGE.get(a["domain"], a["domain"])

def docs_url(a):
    return f"https://github.com/{DOCS_REPO}/blob/main/docs/{page_for(a)}.md#{a['key'].lower()}"

def label_for(a):
    if a["type"] == "glossary_term":
        return "glossary"
    return {"requirements": "requirement"}.get(a["domain"], a["domain"])

def issue_url(k):
    n = issue_map.get(k)
    return f"https://github.com/{REPO}/issues/{n}" if n else None

def ref(k):
    """Reference to another artifact: '#42 (FEAT-3 — title)' once minted, else '`FEAT-3` (title)'."""
    title = by_key.get(k, {}).get("title", "")
    suffix = f" — {title}" if title else ""
    if k in issue_map:
        return f"#{issue_map[k]} (`{k}`{suffix})"
    return f"`{k}`{(' — ' + title) if title else ''}"

def gh(args, stdin=None):
    return subprocess.run(["gh"] + args, input=stdin, capture_output=True, text=True)

# Relations that express "this is done when ..."
OUT_DOD = {"realizes", "implements", "satisfies", "refines", "decomposes", "mitigates"}
IN_PROVE = {"verifies", "satisfies", "mitigates"}

def render_body(a):
    k = a["key"]
    pr = a.get("priority") or "p3"
    L = [
        f'> **wtm:** ORAMA-ZETTA / `{k}`  ·  **type:** `{a["type"]}`  ·  **domain:** `{a["domain"]}`  ·  **status:** {a.get("status","draft")}  ·  **priority:** {pr}',
        "",
        a.get("summary") or "",
        "",
    ]
    body = (a.get("body") or "").strip()
    if body:
        L += [body, ""]

    # ── Definition of done (derived from the traceability graph) ────────────
    dod = []
    for t, o in out_rel.get(k, []):
        if t in OUT_DOD:
            dod.append(f"- [ ] {t.replace('_',' ').capitalize()} {ref(o)}")
    provers = [f for t, f in in_rel.get(k, []) if t in IN_PROVE]
    if provers:
        dod.append("- [ ] Satisfies its checks: " + ", ".join(ref(f) for f in sorted(set(provers))))
    dod.append("- [ ] Behaviour matches the summary/body above.")
    dod.append(f"- [ ] If scope shifts, update wtm artifact `{k}` (source of truth) and re-run `zetta-sync` — do not hand-edit this issue.")
    L += ["## Definition of done", *dod, ""]

    # ── Traceability (cross-linked to sibling issues by number) ─────────────
    out = [f"- this **{t.replace('_',' ')}** → {ref(o)}" for t, o in out_rel.get(k, [])]
    inc = [f"- {ref(f)} **{t.replace('_',' ')}** → this" for t, f in in_rel.get(k, [])]
    if out or inc:
        L += ["## Traceability"]
        if out:
            L += ["**Depends on / realizes / relates to:**", *out, ""]
        if inc:
            L += ["**Referenced by:**", *inc, ""]

    # ── References (equip the agent) ────────────────────────────────────────
    L += [
        "## References",
        "- **Engine code:** https://github.com/oramasearch/zetta — read the root `CLAUDE.md` (C++26, CMake build; SDL3/ImGui desktop = cluster node). This issue lives in that repo; PRs land there.",
        f"- **Blueprint page:** {docs_url(a)} — the rendered MkDocs section for this artifact (live Railway URL backfilled once deployed).",
        "- **Product context:** https://github.com/oramasearch/amaro-docs/tree/main/docs/modules/orama-zetta  ·  https://github.com/oramasearch/amaro-bridge/tree/main/docs/projects/orama-platform-2",
        f"- **Source of truth:** wtm project `ORAMA-ZETTA`, artifact `{k}`. Edit the artifact, not this issue.",
        "",
    ]

    # ── Worktree-agent orientation ──────────────────────────────────────────
    self_ref = f"`#{issue_map[k]}`" if k in issue_map else "this issue"
    L += [
        "## Picking this up (worktree agent)",
        "1. `gh repo clone oramasearch/zetta && cd zetta` — read `CLAUDE.md` for build, layout, and conventions.",
        "2. Read the **Blueprint page** above and walk this issue's **Traceability** neighbours (follow the `#`-links — they are the dependencies and the things that verify you).",
        f"3. Implement against the **Definition of done**. Open a PR that references {self_ref} with `Related to` (no `fixes #` / no auto-close; full URLs).",
        f"4. Keep the wtm blueprint authoritative — if scope changes, update artifact `{k}` and re-sync.",
        "",
        "_Generated from the wtm ORAMA-ZETTA blueprint by `zetta-sync`. Do not hand-edit; edit the artifact and re-sync._",
    ]
    return "\n".join(L)

def save_map():
    if not DRY:
        json.dump(issue_map, open(MAP, "w"), indent=0)

def keysort(a):
    pre, _, n = a["key"].partition("-")
    return (pre, int(n) if n.isdigit() else 0)

# ── Pre-load existing issues (one read): number, title, AND body ────────────
body_now = {}   # key -> body currently live on GitHub
p = gh(["issue", "list", "--repo", REPO, "--state", "all", "--limit", "1000",
        "--json", "number,title,body"])
for it in json.loads(p.stdout or "[]"):
    t = it["title"]
    if t.startswith("[") and "]" in t:
        key = t[1:t.index("]")]
        issue_map.setdefault(key, it["number"])
        body_now[key] = it.get("body") or ""
save_map()

ordered = sorted(arts, key=keysort)

# ── Phase A — create missing issues ─────────────────────────────────────────
created = skipped = errors = 0
for a in ordered:
    k = a["key"]
    if k in issue_map:
        skipped += 1
        continue
    title = f'[{k}] {a["title"]}'
    labels = []
    for l in ["zetta-blueprint", label_for(a), a.get("priority") or "p3"]:
        labels += ["--label", l]
    body = render_body(a)
    if DRY:
        created += 1
        print(f"[DRY create] {k}  ({title})", flush=True)
        continue
    ok = False
    for attempt in range(6):
        r = gh(["issue", "create", "--repo", REPO, "--title", title] + labels + ["--body-file", "-"],
               stdin=body)
        if r.returncode == 0:
            num = int(r.stdout.strip().splitlines()[-1].rstrip("/").split("/")[-1])
            issue_map[k] = num
            body_now[k] = body
            save_map()
            created += 1
            ok = True
            print(f"[{created+skipped:3}/{len(arts)}] create {k} -> #{num}", flush=True)
            break
        e = (r.stderr or "").lower()
        if any(s in e for s in ("rate limit", "secondary", "abuse", "try again")):
            time.sleep(45 * (attempt + 1))
        else:
            errors += 1
            print(f"ERROR create {k}: {r.stderr[:200]}", flush=True)
            break
    if ok:
        time.sleep(2.5)

print(f"\nPhase A done: created={created} skipped={skipped} errors={errors} mapped={len(issue_map)}/{len(arts)}")

# ── Phase B — reconcile every body against the COMPLETE map (#number links) ──
edited = unchanged = berr = 0
for a in ordered:
    k = a["key"]
    if k not in issue_map:
        continue  # never created (error in A) — skip
    want = render_body(a)
    if want.strip() == (body_now.get(k, "") or "").strip():
        unchanged += 1
        continue
    if DRY:
        edited += 1
        print(f"[DRY edit] {k} -> #{issue_map[k]}", flush=True)
        continue
    ok = False
    for attempt in range(6):
        r = gh(["issue", "edit", str(issue_map[k]), "--repo", REPO, "--body-file", "-"], stdin=want)
        if r.returncode == 0:
            body_now[k] = want
            edited += 1
            ok = True
            print(f"edit {k} -> #{issue_map[k]}", flush=True)
            break
        e = (r.stderr or "").lower()
        if any(s in e for s in ("rate limit", "secondary", "abuse", "try again")):
            time.sleep(45 * (attempt + 1))
        else:
            berr += 1
            print(f"ERROR edit {k}: {r.stderr[:200]}", flush=True)
            break
    if ok:
        time.sleep(2.5)

print(f"\nPhase B done: edited={edited} unchanged={unchanged} errors={berr}")
print(f"DONE mapped={len(issue_map)}/{len(arts)}  (dry={DRY})")
