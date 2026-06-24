#!/usr/bin/env python3
"""#286 prioritize: set p1-p4 on the OPEN issues by UC-1 (churn) dependency order.

Use-case-driven: UC-1 (Motive churn) is the first use case; what it needs first ranks highest.
Tiers:
  p1 — the churn MVP core: ingest→architect→correctness→trained model (FEAT-1/2/3/6) + UC-1
  p2 — deliver + govern churn: deploy, run/monitor, governed self-serve (FEAT-4/5/9)
  p3 — substrate + GUI not blocking first churn: tiered storage, compute-near-data, GUI surface (FEAT-7/8/10)
  p4 — everything open that isn't on the churn path (other use cases, unlinked work)
Dependents (stories, tests, screens, controls, APIs, envs, runbooks, risks, releases) inherit the
best (lowest) tier among the features they touch. Run AFTER prune. Usage: python3 prioritize_issues.py [--dry]
"""
import json, subprocess, time, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
REPO = "oramasearch/zetta"
DRY = "--dry" in sys.argv
arts = json.load(open(f"{BASE}/artifacts.json"))
rels = json.load(open(f"{BASE}/relations.json"))
issue_map = json.load(open(f"{BASE}/issue-map.json"))

FEAT_TIER = {"FEAT-1": 1, "FEAT-2": 1, "FEAT-3": 1, "FEAT-6": 1,
             "FEAT-4": 2, "FEAT-5": 2, "FEAT-9": 2,
             "FEAT-7": 3, "FEAT-8": 3, "FEAT-10": 3}
KEEP = {"FEAT", "US", "UC", "API", "SCR", "CMP", "CTL", "ENV", "RUN", "TR", "TC", "TP", "RSK", "REL", "DEF"}

def prefix(k): return k.split("-")[0]

# artifact -> set of features it touches (either direction of the relation)
feat_of = {}
for r in rels:
    f, t = r["from"], r["to"]
    if prefix(t) == "FEAT":
        feat_of.setdefault(f, set()).add(t)
    if prefix(f) == "FEAT":
        feat_of.setdefault(t, set()).add(f)

def tier_of(k):
    if k == "UC-1":
        return 1
    if prefix(k) == "UC":
        return 4  # other use cases are not the first use case
    if k in FEAT_TIER:
        return FEAT_TIER[k]
    tiers = [FEAT_TIER[f] for f in feat_of.get(k, set()) if f in FEAT_TIER]
    return min(tiers) if tiers else 4

def gh(args): return subprocess.run(["gh"] + args, capture_output=True, text=True)

p = gh(["issue", "list", "--repo", REPO, "--state", "open", "--limit", "2000", "--json", "number,labels"])
open_labels = {it["number"]: {l["name"] for l in it["labels"]} for it in json.loads(p.stdout or "[]")}

changed = skipped = errors = 0
dist = {1: 0, 2: 0, 3: 0, 4: 0}
for a in arts:
    k = a["key"]
    if prefix(k) not in KEEP:
        continue
    n = issue_map.get(k)
    if not n or n not in open_labels:
        continue
    t = tier_of(k)
    dist[t] += 1
    want = f"p{t}"
    cur = open_labels[n]
    if want in cur:
        skipped += 1
        continue
    rm = [x for x in ("p1", "p2", "p3", "p4") if x in cur and x != want]
    if DRY:
        changed += 1
        print(f"[DRY] {k} #{n} {sorted(x for x in cur if x.startswith('p'))} -> {want}", flush=True)
        continue
    args = ["issue", "edit", str(n), "--repo", REPO, "--add-label", want]
    for x in rm:
        args += ["--remove-label", x]
    r = gh(args)
    if r.returncode == 0:
        changed += 1
        print(f"{k} #{n} -> {want}", flush=True)
    else:
        errors += 1
        print(f"ERROR {k} #{n}: {r.stderr[:150]}", flush=True)
    time.sleep(1.5)
print(f"\nDONE changed={changed} skipped={skipped} errors={errors}")
print(f"distribution among open keep-issues: p1={dist[1]} p2={dist[2]} p3={dist[3]} p4={dist[4]} (dry={DRY})")
