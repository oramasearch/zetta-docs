# zetta-docs

The **Orama Zetta** documentation website — the design blueprint, references, and Graphviz diagrams — published as a static MkDocs Material site, hosted on Railway.

> *Intelligence Velocity for Big Thinkers.*

## What this is

A generated, browsable rendering of the Orama Zetta blueprint. The content is **synchronized from the worktree-manager (wtm) blueprint** (project `ORAMA-ZETTA`) by the `zetta-sync` skill — it is **not hand-maintained**. The skill keeps three surfaces in lockstep:

1. **wtm artifacts** (the source of truth — strategy, requirements, architecture/ADRs, domain model, security, delivery, backlog, testing, risks, glossary),
2. **this docs website** (`docs/*.md` + pre-rendered `docs/diagrams/*.svg`),
3. **GitHub issues** on `oramasearch/zetta` (one per actionable artifact, keyed to its wtm key).

Re-run the sync skill to refresh after the blueprint changes. Do not edit `docs/*.md` by hand — changes will be overwritten on the next sync.

## Run locally

```sh
pip install -r requirements.txt
mkdocs serve        # http://127.0.0.1:8000
```

## Deploy (Railway)

Railway builds the `Dockerfile` (`builder = "DOCKERFILE"` in `railway.toml`): it `pip install`s MkDocs Material, runs `mkdocs build`, and serves the static `site/` on `$PORT`. Diagrams are pre-rendered SVGs committed under `docs/diagrams/`, so no graphviz system dependency is needed in the container.

## Related

- Engine: [`oramasearch/zetta`](https://github.com/oramasearch/zetta) (the ZettaDB engine; issues live here).
- Blueprint source: wtm project `ORAMA-ZETTA`.
- Bridge planning: `docs/projects/orama-platform-2/` in `oramasearch/amaro-bridge`.
