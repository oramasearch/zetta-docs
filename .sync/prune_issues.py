#!/usr/bin/env python3
"""#285 prune: close reference/design issues (kept + linked), keep buildable work + risks + releases.

An issue is a request to produce an artifact (software / docs / report). Reference/design
artifacts produce none → close with a reason comment, NEVER delete. Idempotent + throttled.
Run AFTER the re-sync so titles/bodies are current. Usage: python3 prune_issues.py [--dry]
"""
import json, subprocess, time, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
REPO = "oramasearch/zetta"
DRY = "--dry" in sys.argv
arts = json.load(open(f"{BASE}/artifacts.json"))
issue_map = json.load(open(f"{BASE}/issue-map.json"))

# Keep OPEN (buildable work + live trackers). Everything else = reference → close.
KEEP = {"FEAT", "US", "UC", "API", "SCR", "CMP", "CTL", "ENV", "RUN", "TR", "TC", "TP", "RSK", "REL", "DEF"}

def prefix(k): return k.split("-")[0]
def numpart(k):
    p = k.split("-"); return int(p[1]) if len(p) > 1 and p[1].isdigit() else 0
def gh(args): return subprocess.run(["gh"] + args, capture_output=True, text=True)

p = gh(["issue", "list", "--repo", REPO, "--state", "open", "--limit", "2000", "--json", "number"])
open_nums = {it["number"] for it in json.loads(p.stdout or "[]")}

closed = skipped = errors = 0
for a in sorted(arts, key=lambda a: (prefix(a["key"]), numpart(a["key"]))):
    k = a["key"]
    if prefix(k) in KEEP:
        continue
    n = issue_map.get(k)
    if not n or n not in open_nums:
        skipped += 1
        continue
    comment = (
        "Closing as a **reference / blueprint artifact** — no standalone deliverable "
        "(no code, docs, or report needed from this issue itself).\n\n"
        "It stays part of the blueprint and remains linked: it is realized / verified by the "
        "work issues in its **Traceability** section. Reopen if a concrete artifact emerges.\n\n"
        f"Source of truth: the wtm `ORAMA-ZETTA` artifact `{k}`. Edit the artifact, not this issue."
    )
    if DRY:
        closed += 1
        print(f"[DRY close] {k} -> #{n}", flush=True)
        continue
    ok = False
    for attempt in range(6):
        r = gh(["issue", "close", str(n), "--repo", REPO, "--reason", "not planned", "--comment", comment])
        if r.returncode == 0:
            closed += 1
            ok = True
            print(f"[{closed:3}] closed {k} -> #{n}", flush=True)
            break
        e = (r.stderr or "").lower()
        if any(s in e for s in ("rate limit", "secondary", "abuse", "try again")):
            time.sleep(45 * (attempt + 1))
        else:
            errors += 1
            print(f"ERROR {k} #{n}: {r.stderr[:150]}", flush=True)
            break
    if ok:
        time.sleep(2.0)
print(f"\nDONE closed={closed} skipped={skipped} errors={errors} (dry={DRY})")
