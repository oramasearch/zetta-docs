# APIs

The native cluster API, DDF, Runner, Cloud Interface, MCP, and CLI surfaces.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Interfaces

### API-1 — ZettaDB native cluster API (C++)  {: #api-1 }

`draft`  ·  `interface`  ·  issue [#21](https://github.com/oramasearch/zetta/issues/21)

The high-performance in-node C++ API that runners and compute jobs call where the data lives.

Compute-near-data surface; capability-mediated. Basis for DDF, training/inference, indexing. See ADR-4/ADR-17.

**Realizes / depends on / relates to:** relates to → [`ADR-4`](architecture.md#adr-4)

### API-2 — DDF API (distributed dataframe)  {: #api-2 }

`draft`  ·  `interface`  ·  issue [#22](https://github.com/oramasearch/zetta/issues/22)

Cluster-parallel dataframe operations over data spread across nodes.

Native C++; the data-engineering substrate. See GLO-11/ADR-17.

**Realizes / depends on / relates to:** relates to → [`GLO-11`](glossary.md#glo-11)

### API-3 — Runner interface  {: #api-3 }

`draft`  ·  `interface`  ·  issue [#23](https://github.com/oramasearch/zetta/issues/23)

Common interface a runner implements to execute code-form IR/extension steps in the sandbox.

Concrete: Lua, Orly (R1), Python (later). See ADR-11.

**Realizes / depends on / relates to:** relates to → [`ADR-11`](architecture.md#adr-11)

### API-4 — Cloud Interface  {: #api-4 }

`draft`  ·  `interface`  ·  issue [#24](https://github.com/oramasearch/zetta/issues/24)

Common interface for infra orchestration; impls = local CLI or direct HTTP.

createCluster/addNode/burstProvision/teardown. See ADR-15/ADR-19/ADR-20.

**Realizes / depends on / relates to:** relates to → [`ADR-15`](architecture.md#adr-15)

### API-5 — Extension & Capability API  {: #api-5 }

`draft`  ·  `interface`  ·  issue [#25](https://github.com/oramasearch/zetta/issues/25)

The sandbox host API extensions call — mediated by capability tokens, audited.

Deny-by-default; no fs/network egress. See ADR-12/CTL-1.

**Realizes / depends on / relates to:** relates to → [`ADR-12`](architecture.md#adr-12)

### API-6 — MCP endpoint  {: #api-6 }

`draft`  ·  `interface`  ·  issue [#26](https://github.com/oramasearch/zetta/issues/26)

Agent-facing Model Context Protocol surface over the platform.

Lets an agent (P4) author graphs / drive runs within governance. Consumable by Claude/others.

**Realizes / depends on / relates to:** relates to → [`PER-4`](personas.md#per-4)

### API-7 — CLI  {: #api-7 }

`draft`  ·  `interface`  ·  issue [#27](https://github.com/oramasearch/zetta/issues/27)

Headless command-line surface for orchestration + automation.

Any authenticated node can orchestrate via the CLI (headless). Mirrors GUI actions.

**Realizes / depends on / relates to:** relates to → [`FEAT-4`](backlog.md#feat-4)

### API-8 — Desktop control API (local IPC/HTTP)  {: #api-8 }

`draft`  ·  `interface`  ·  issue [#28](https://github.com/oramasearch/zetta/issues/28)

The local surface the SDL3/ImGui desktop uses to drive the node.

In-process/native (desktop is a node). Backs FEAT-10 / ADR-14.

**Realizes / depends on / relates to:** relates to → [`FEAT-10`](backlog.md#feat-10)
