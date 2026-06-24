#!/usr/bin/env python3
"""zetta-sync Phase C: render the MkDocs site from the wtm dumps.

Reads .sync/{artifacts,relations,issue-map}.json (READ-ONLY on wtm) and writes:
  - docs/<page>.md      one page per blueprint domain (anchored, cross-linked,
                        each artifact linked to its GitHub issue #)
  - docs/diagrams/*.dot + *.svg   architecture / traceability / domain-context
  - docs/diagrams.md    embeds the rendered SVGs

Idempotent: regenerates every page from the dumps. Run directly:
    python3 render.py
Requires the Graphviz `dot` binary on PATH.
"""
import json, os, subprocess, textwrap, html

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(f"{BASE}/../docs")
REPO = "oramasearch/zetta"

arts = json.load(open(f"{BASE}/artifacts.json"))
rels = json.load(open(f"{BASE}/relations.json"))
issue_map = json.load(open(f"{BASE}/issue-map.json"))
by_key = {a["key"]: a for a in arts}

out_rel, in_rel = {}, {}
for r in rels:
    rt = r.get("relation") or r.get("type")
    out_rel.setdefault(r["from"], []).append((rt, r["to"]))
    in_rel.setdefault(r["to"], []).append((rt, r["from"]))

# ── Page layout: (slug, title, blurb, [prefixes in render order]) ───────────
PAGES = [
    ("strategy", "Strategy", "Vision, goals, KPIs, assumptions, and scope.",
        ["VIS", "GOAL", "KPI", "ASM", "SCP"]),
    ("personas", "Personas & Stakeholders", "Who Orama Zetta is for, and who buys it.",
        ["PER", "STK"]),
    ("requirements", "Requirements", "Business → stakeholder → functional → non-functional → integration → data → transition.",
        ["BR", "SR", "FR", "NFR", "IR", "DR", "TR"]),
    ("architecture", "Architecture", "The decisions (ADRs), the architecture elements they shape, and the quality scenarios that test them.",
        ["ADR", "ARC", "QAS"]),
    ("domain-model", "Domain Model", "Six bounded contexts and the entities, commands, and events inside them.",
        ["BC", "ENT", "CMD", "EVT"]),
    ("data", "Data & Storage", "The control-plane store, its tables, and retention rules.",
        ["DS", "TBL", "RET"]),
    ("apis", "APIs", "The native cluster API, DDF, Runner, Cloud Interface, MCP, and CLI surfaces.",
        ["API"]),
    ("security", "Security", "Threat model, trust boundaries, threats, controls, and permission rules.",
        ["TM", "TB", "THR", "CTL", "PERM"]),
    ("ux", "UX", "Screens, journeys, and UI components.",
        ["SCR", "JRN", "CMP"]),
    ("delivery", "Delivery", "Releases R1→R8, environments, runbooks, and baselines.",
        ["REL", "ENV", "RUN", "BL"]),
    ("backlog", "Backlog", "Features, user stories, use cases, and business rules.",
        ["FEAT", "US", "UC", "RULE"]),
    ("testing", "Testing", "The test plan and its test cases.",
        ["TP", "TC"]),
    ("risks", "Risks", "Gating risks and the decisions/controls that mitigate them.",
        ["RSK"]),
    ("governance", "Governance", "Reviews and approval gates.",
        ["REV", "APR"]),
    ("glossary", "Glossary", "Load-bearing terms.",
        ["GLO"]),
]

SECTION = {
    "VIS": "Product Vision", "GOAL": "Goals", "KPI": "KPIs", "ASM": "Assumptions", "SCP": "Scope",
    "PER": "Personas", "STK": "Stakeholders",
    "BR": "Business Requirements", "SR": "Stakeholder Requirements", "FR": "Functional Requirements",
    "NFR": "Non-Functional Requirements", "IR": "Integration Requirements", "DR": "Data Requirements",
    "TR": "Transition Requirements",
    "ADR": "Architecture Decisions", "ARC": "Architecture Elements", "QAS": "Quality Scenarios",
    "BC": "Bounded Contexts", "ENT": "Domain Entities", "CMD": "Commands", "EVT": "Events",
    "DS": "Data Stores", "TBL": "Data Tables", "RET": "Retention Rules",
    "API": "Interfaces",
    "TM": "Threat Models", "TB": "Trust Boundaries", "THR": "Threats", "CTL": "Security Controls",
    "PERM": "Permission Rules",
    "SCR": "Screens", "JRN": "Journeys", "CMP": "UI Components",
    "REL": "Releases", "ENV": "Environments", "RUN": "Runbooks", "BL": "Baselines",
    "FEAT": "Features", "US": "User Stories", "UC": "Use Cases", "RULE": "Business Rules",
    "TP": "Test Plans", "TC": "Test Cases",
    "RSK": "Risks", "REV": "Reviews", "APR": "Approvals", "GLO": "Glossary Terms",
}

# prefix -> page slug (for cross-links)
prefix_page = {}
for slug, _t, _b, prefixes in PAGES:
    for p in prefixes:
        prefix_page[p] = slug

def prefix_of(k):
    return k.split("-")[0]

def num(k):
    p, _, n = k.partition("-")
    return int(n) if n.isdigit() else 0

def klink(k):
    """Cross-link to an artifact's anchor on its page."""
    pg = prefix_page.get(prefix_of(k))
    if pg:
        return f"[`{k}`]({pg}.md#{k.lower()})"
    return f"`{k}`"

def ilink(k):
    n = issue_map.get(k)
    return f"[#{n}](https://github.com/{REPO}/issues/{n})" if n else None

def trace_lines(k):
    out = [(t, o) for t, o in out_rel.get(k, [])]
    inc = [(t, f) for t, f in in_rel.get(k, [])]
    lines = []
    if out:
        lines.append("**Realizes / depends on / relates to:** " +
                     " · ".join(f"{t.replace('_',' ')} → {klink(o)}" for t, o in out))
    if inc:
        lines.append("**Referenced by:** " +
                     " · ".join(f"{klink(f)} {t.replace('_',' ')}" for t, f in inc))
    return lines

def render_artifact(a):
    k = a["key"]
    L = [f'### {k} — {a["title"]}  {{: #{k.lower()} }}', ""]
    meta = [f'`{a.get("status","draft")}`', f'`{a["type"]}`']
    il = ilink(k)
    if il:
        meta.append(f"issue {il}")
    L += ["  ·  ".join(meta), ""]
    if a.get("summary"):
        L += [a["summary"].strip(), ""]
    body = (a.get("body") or "").strip()
    if body:
        L += [body, ""]
    tl = trace_lines(k)
    if tl:
        L += tl + [""]
    return "\n".join(L)

def render_page(slug, title, blurb, prefixes):
    L = [f"# {title}", "", blurb, "",
         "!!! note \"Generated from the wtm blueprint\"",
         "    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on "
         f"[`{REPO}`](https://github.com/{REPO}/issues). Do not hand-edit — re-run `zetta-sync`.", ""]
    present = [a for a in arts if prefix_of(a["key"]) in prefixes]
    for pre in prefixes:
        items = sorted([a for a in present if prefix_of(a["key"]) == pre], key=lambda a: num(a["key"]))
        if not items:
            continue
        L += [f"## {SECTION.get(pre, pre)}", ""]
        for a in items:
            L.append(render_artifact(a))
    path = f"{DOCS}/{slug}.md"
    open(path, "w").write("\n".join(L).rstrip() + "\n")
    return len(present)

# ── Graphviz ────────────────────────────────────────────────────────────────
DOMAIN_COLOR = {
    "strategy": "#e8eaf6", "stakeholder": "#e0f2f1", "requirements": "#e3f2fd",
    "architecture": "#fff3e0", "domain": "#f3e5f5", "data": "#e0f7fa",
    "api": "#f1f8e9", "security": "#ffebee", "ux": "#fce4ec", "delivery": "#ede7f6",
    "backlog": "#e8f5e9", "testing": "#fffde7", "risk": "#fbe9e7", "governance": "#eceff1",
}
def color_of(k):
    a = by_key.get(k)
    return DOMAIN_COLOR.get(a["domain"], "#ffffff") if a else "#ffffff"

def esc(s):
    return s.replace('"', "'").replace("\n", " ")

def node_line(k):
    a = by_key.get(k)
    title = esc(a["title"]) if a else ""
    wrapped = "\\n".join(textwrap.wrap(title, 22)[:3])
    return f'  "{k}" [label="{k}\\n{wrapped}", fillcolor="{color_of(k)}"];'

def build_dot(name, prefixes, rel_types, *, clusters=None, rankdir="LR"):
    keys = [a["key"] for a in arts if prefix_of(a["key"]) in prefixes]
    keyset = set(keys)
    edges = []
    for r in rels:
        rt = r.get("relation") or r.get("type")
        if rt in rel_types and r["from"] in keyset and r["to"] in keyset:
            edges.append((r["from"], rt, r["to"]))
    used = set()
    for f, _t, t in edges:
        used.add(f); used.add(t)
    L = [f'digraph {name} {{', f'  rankdir={rankdir}; bgcolor="transparent";',
         '  node [shape=box style="rounded,filled" fontname="Helvetica" fontsize=10];',
         '  edge [fontname="Helvetica" fontsize=8 color="#777777"];']
    if clusters:
        for ci, (label, cps) in enumerate(clusters):
            L.append(f'  subgraph cluster_{ci} {{ label="{esc(label)}"; style="rounded,filled"; '
                     f'fillcolor="#fafafa"; fontname="Helvetica"; fontsize=11;')
            for k in keys:
                if prefix_of(k) in cps:
                    L.append("  " + node_line(k))
            L.append("  }")
    else:
        for k in sorted(used, key=lambda k: (prefix_of(k), num(k))):
            L.append(node_line(k))
    for f, t, tk in edges:
        L.append(f'  "{f}" -> "{tk}" [label="{t.replace("_"," ")}"];')
    L.append("}")
    dot = f"{DOCS}/diagrams/{name}.dot"
    open(dot, "w").write("\n".join(L) + "\n")
    svg = f"{DOCS}/diagrams/{name}.svg"
    subprocess.run(["dot", "-Tsvg", dot, "-o", svg], check=True)
    return len(used), len(edges)

def render_diagrams():
    stats = {}
    stats["architecture"] = build_dot(
        "architecture", {"ADR", "ARC", "QAS", "RSK"},
        {"refines", "relates_to", "mitigates"})
    stats["traceability"] = build_dot(
        "traceability",
        {"VIS", "GOAL", "KPI", "BR", "SR", "FR", "NFR", "FEAT", "US", "SCR", "RSK", "TP", "TC"},
        {"refines", "realizes", "satisfies", "derives_from", "verifies", "mitigates", "relates_to"})
    bcs = [(by_key[f"BC-{i}"]["title"], {"ENT"}) for i in range(1, 7)]
    # cluster ENTs under their BC via the contains relation
    ent_cluster = {}
    for r in rels:
        if (r.get("relation") == "contains") and prefix_of(r["from"]) == "BC" and prefix_of(r["to"]) == "ENT":
            ent_cluster.setdefault(r["from"], []).append(r["to"])
    clusters = []
    for i in range(1, 7):
        bk = f"BC-{i}"
        clusters.append((by_key[bk]["title"], set()))  # placeholder; fill via explicit keys below
    stats["domain-context"] = build_domain_context(ent_cluster)
    return stats

def build_domain_context(ent_cluster):
    L = ['digraph domain_context {', '  rankdir=LR; bgcolor="transparent";',
         '  node [shape=box style="rounded,filled" fontname="Helvetica" fontsize=10 fillcolor="#f3e5f5"];']
    n = 0
    for i in range(1, 7):
        bk = f"BC-{i}"
        ents = sorted(ent_cluster.get(bk, []), key=num)
        L.append(f'  subgraph cluster_{i} {{ label="{esc(by_key[bk]["title"])}"; '
                 f'style="rounded,filled"; fillcolor="#fafafa"; fontname="Helvetica"; fontsize=11;')
        for e in ents:
            L.append("  " + node_line(e)); n += 1
        L.append("  }")
    # entity → feature realizations as cross-edges (dashed)
    e = 0
    for r in rels:
        if r.get("relation") == "realizes" and prefix_of(r["from"]) == "ENT" and prefix_of(r["to"]) == "FEAT":
            pass  # FEAT not in this diagram; skip to keep it a pure domain map
    L.append("}")
    dot = f"{DOCS}/diagrams/domain-context.dot"
    open(dot, "w").write("\n".join(L) + "\n")
    subprocess.run(["dot", "-Tsvg", dot, "-o", f"{DOCS}/diagrams/domain-context.svg"], check=True)
    return (n, 0)

def render_diagrams_page(stats):
    L = ["# Diagrams", "",
         "Rendered from the blueprint with Graphviz. Sources (`.dot`) live beside the SVGs in "
         f"[`docs/diagrams/`](https://github.com/oramasearch/zetta-docs/tree/main/docs/diagrams).", "",
         "!!! note \"Generated\"",
         "    Re-run `zetta-sync` to regenerate. Do not hand-edit.", "",
         "## Architecture — decisions & elements", "",
         f"ADRs, architecture elements, quality scenarios, and the risks they mitigate "
         f"({stats['architecture'][0]} nodes, {stats['architecture'][1]} edges).", "",
         "![Architecture](diagrams/architecture.svg)",
         "[`architecture.dot`](diagrams/architecture.dot)", "",
         "## Traceability — vision to verification", "",
         f"The spine: vision → goals → KPIs, business → stakeholder → functional requirements → "
         f"features → screens/stories, plus the test cases and risks that touch them "
         f"({stats['traceability'][0]} nodes, {stats['traceability'][1]} edges).", "",
         "![Traceability](diagrams/traceability.svg)",
         "[`traceability.dot`](diagrams/traceability.dot)", "",
         "## Domain context — bounded contexts & entities", "",
         f"The six bounded contexts and the domain entities inside them "
         f"({stats['domain-context'][0]} entities).", "",
         "![Domain context](diagrams/domain-context.svg)",
         "[`domain-context.dot`](diagrams/domain-context.dot)", ""]
    open(f"{DOCS}/diagrams.md", "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    total = 0
    for slug, title, blurb, prefixes in PAGES:
        n = render_page(slug, title, blurb, prefixes)
        total += n
        print(f"page {slug:14} {n:3} artifacts")
    stats = render_diagrams()
    render_diagrams_page(stats)
    for name, (nodes, edges) in stats.items():
        print(f"diagram {name:16} {nodes} nodes  {edges} edges")
    print(f"\nrendered {total} artifacts across {len(PAGES)} pages + 3 diagrams")
