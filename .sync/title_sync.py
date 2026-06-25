#!/usr/bin/env python3
"""Sync GitHub issue TITLES to the blueprint ([KEY] <current title>).

create_issues.py reconciles bodies but sets the title only at creation — so renamed
artifacts (ZettaDB→Orama Zetta, UC-1 retitle) left stale issue titles. This fixes them.
Idempotent + throttled. Usage: python3 title_sync.py [--dry]
"""
import json, subprocess, time, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
REPO = "oramasearch/zetta"
DRY = "--dry" in sys.argv
arts = json.load(open(f"{BASE}/artifacts.json"))
issue_map = json.load(open(f"{BASE}/issue-map.json"))

p = subprocess.run(["gh", "issue", "list", "--repo", REPO, "--state", "all",
                    "--limit", "2000", "--json", "number,title"], capture_output=True, text=True)
cur = {it["number"]: it["title"] for it in json.loads(p.stdout or "[]")}

changed = same = errors = 0
for a in arts:
    k = a["key"]
    n = issue_map.get(k)
    if not n:
        continue
    want = f"[{k}] {a['title']}"
    if cur.get(n) == want:
        same += 1
        continue
    if DRY:
        changed += 1
        print(f"[DRY] #{n}: {cur.get(n)!r} -> {want!r}", flush=True)
        continue
    r = subprocess.run(["gh", "issue", "edit", str(n), "--repo", REPO, "--title", want],
                       capture_output=True, text=True)
    if r.returncode == 0:
        changed += 1
        print(f"#{n} {k} -> {want}", flush=True)
    else:
        errors += 1
        print(f"ERROR #{n} {k}: {r.stderr[:120]}", flush=True)
    time.sleep(1.2)
print(f"\nDONE titles changed={changed} same={same} errors={errors} (dry={DRY})")
