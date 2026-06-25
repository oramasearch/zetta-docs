# Glossary

Load-bearing terms.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Glossary Terms

### GLO-1 — Intelligence Velocity  {: #glo-1 }

`draft`  ·  `glossary_term`  ·  issue [#149](https://github.com/oramasearch/zetta/issues/149)

Time from intent → deployed, running, correct intelligence.

The product's headline metric and tagline ('Intelligence Velocity for Big Thinkers'). Target: hours, not quarters.

**Realizes / depends on / relates to:** relates to → [`VIS-1`](strategy.md#vis-1)

### GLO-2 — Execution graph  {: #glo-2 }

`draft`  ·  `glossary_term`  ·  issue [#150](https://github.com/oramasearch/zetta/issues/150)

The compiled IR of a data/AI system (connect→clean→model→index→serve→act).

The inspectable, versioned intermediate representation Orama Zetta compiles intent/artifacts into, validates, deploys, and runs.

**Realizes / depends on / relates to:** relates to → [`FEAT-2`](backlog.md#feat-2)

### GLO-3 — Compute-near-data  {: #glo-3 }

`draft`  ·  `glossary_term`  ·  issue [#151](https://github.com/oramasearch/zetta/issues/151)

Running code on the node where the data lives.

Embedded Lua / DataFrame execution on the Orama Zetta node holding the data — no warehouse round-trip, no exfiltration.

**Realizes / depends on / relates to:** relates to → [`FEAT-8`](backlog.md#feat-8)

### GLO-4 — Tiered storage  {: #glo-4 }

`draft`  ·  `glossary_term`  ·  issue [#152](https://github.com/oramasearch/zetta/issues/152)

Source → in-memory index → cold storage → re-warm on request.

Orama Zetta's storage tiering that materializes expensive source data into cheap fast indexes and ages it out, re-warming on demand.

**Realizes / depends on / relates to:** relates to → [`FEAT-7`](backlog.md#feat-7)

### GLO-5 — Correctness gate  {: #glo-5 }

`draft`  ·  `glossary_term`  ·  issue [#153](https://github.com/oramasearch/zetta/issues/153)

The validation a generated graph must pass before it can deploy.

Schema/type checks, data-leakage + point-in-time checks for ML steps, and a correctness eval (compile AND run AND produce the right answer).

**Realizes / depends on / relates to:** relates to → [`FEAT-3`](backlog.md#feat-3)

### GLO-6 — Orly  {: #glo-6 }

`draft`  ·  `glossary_term`  ·  issue [#154](https://github.com/oramasearch/zetta/issues/154)

Orama's first-party DSL — a Lua alternative for the code-form IR and extensions.

A higher-level, inspectable plan language tailored to Orama Zetta orchestration; a concrete Runner alongside Lua. See ADR-13.

**Realizes / depends on / relates to:** relates to → [`ADR-13`](architecture.md#adr-13)

### GLO-7 — Runner  {: #glo-7 }

`draft`  ·  `glossary_term`  ·  issue [#155](https://github.com/oramasearch/zetta/issues/155)

Common interface that executes a code-form IR/extension step in the sandbox.

Concrete runners: Lua, Orly (R1), Python (later). See ADR-11.

**Realizes / depends on / relates to:** relates to → [`ADR-11`](architecture.md#adr-11)

### GLO-8 — Extension  {: #glo-8 }

`draft`  ·  `glossary_term`  ·  issue [#156](https://github.com/oramasearch/zetta/issues/156)

A unit of customer/enterprise extensibility = code (Lua/Orly) and/or data (Parquet/CSV/Automerge).

How enterprises inject their own logic and rules (e.g. infra-creation rules) into the platform. Capability-sandboxed. See ADR-11/ADR-12.

**Realizes / depends on / relates to:** relates to → [`ADR-11`](architecture.md#adr-11)

### GLO-9 — Cloud Interface  {: #glo-9 }

`draft`  ·  `glossary_term`  ·  issue [#157](https://github.com/oramasearch/zetta/issues/157)

Abstraction over infrastructure orchestration; impls = local CLI (aws/az/gcloud/kubectl) or direct HTTP.

How the orchestrator node provisions infra and deploys headless Zetta nodes into a target. See ADR-15.

**Realizes / depends on / relates to:** relates to → [`ADR-15`](architecture.md#adr-15)

### GLO-10 — Capability token  {: #glo-10 }

`draft`  ·  `glossary_term`  ·  issue [#158](https://github.com/oramasearch/zetta/issues/158)

A deny-by-default grant scoping an extension's access to the invoking user's key/access.

The unit of authority in the extension sandbox; no ambient access, every use audited. See ADR-12.

**Realizes / depends on / relates to:** relates to → [`ADR-12`](architecture.md#adr-12)

### GLO-11 — DDF (distributed dataframe)  {: #glo-11 }

`draft`  ·  `glossary_term`  ·  issue [#159](https://github.com/oramasearch/zetta/issues/159)

Orama Zetta's rich, cluster-parallel dataframe API — native C++ operations over data spread across nodes.

The dataframe abstraction the runners and graph steps operate on; operations are re-implemented natively and parallelized across the cluster. The 'data engineering' substrate. See ADR-17.

**Realizes / depends on / relates to:** relates to → [`ARC-6`](architecture.md#arc-6)
**Referenced by:** [`API-2`](apis.md#api-2) relates to

### GLO-12 — Cluster-parallel execution  {: #glo-12 }

`draft`  ·  `glossary_term`  ·  issue [#160](https://github.com/oramasearch/zetta/issues/160)

Running any operation parallel/concurrent across cluster nodes, enabled by controlling the infrastructure.

Because Orama Zetta orchestrates and owns the infra, training/inference/DDF/data-eng/serving can be scaled across nodes for cost/performance rather than bound to a single machine or a vendor's warehouse. See ADR-17.

**Realizes / depends on / relates to:** relates to → [`ADR-17`](architecture.md#adr-17)

### GLO-13 — Ephemeral burst compute  {: #glo-13 }

`draft`  ·  `glossary_term`  ·  issue [#161](https://github.com/oramasearch/zetta/issues/161)

Provision-many → run-parallel → tear-down for temporary workloads (training, big DDF jobs).

A provisioning mode distinct from persistent cluster nodes: spin up N ephemeral nodes at once (often on Spot/low-priority capacity for cost), run a cluster-parallel job, then release them. See ADR-20.

**Realizes / depends on / relates to:** relates to → [`ADR-20`](architecture.md#adr-20)

### GLO-14 — AI project  {: #glo-14 }

`draft`  ·  `glossary_term`

The central artifact: a data/AI project instantiated from a use-case type on a team's data, composed of optional components, managed to success.

The **central item** of Orama Zetta. A user creates an **AI/data project** from a **use-case type** (e.g. churn) and points it at their own data; it owns its execution graph, **optional components** (steps the user toggles), runs, and provenance, and is **managed through its lifecycle to success**. See ENT-1 `Project` and the data-project-management ADR.

**Realizes / depends on / relates to:** relates to → [`ENT-1`](domain-model.md#ent-1)
