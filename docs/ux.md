# UX

Screens, journeys, and UI components.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Screens

### SCR-1 — Dashboard  {: #scr-1 }

`draft`  ·  `screen`  ·  issue [#222](https://github.com/oramasearch/zetta/issues/222)

Entry point showing projects, recent runs, and Intelligence Velocity KPIs; quick actions to create/import and resume work.

Entry point showing projects, recent runs, and Intelligence Velocity KPIs; quick actions to create/import and resume work.

**Realizes / depends on / relates to:** relates to → [`BR-1`](requirements.md#br-1)
**Referenced by:** [`BR-1`](requirements.md#br-1) relates to

### SCR-2 — New Project (Intent + Import)  {: #scr-2 }

`draft`  ·  `screen`  ·  issue [#223](https://github.com/oramasearch/zetta/issues/223)

Capture natural-language intent, upload/import artifacts (R1: n8n JSON), and create a project with provenance.

Capture natural-language intent, upload/import artifacts (R1: n8n JSON), and create a project with provenance.

**Realizes / depends on / relates to:** realizes → [`FEAT-1`](backlog.md#feat-1)
**Referenced by:** [`FR-1`](requirements.md#fr-1) realizes · [`FR-2`](requirements.md#fr-2) realizes

### SCR-3 — Graph Workspace  {: #scr-3 }

`draft`  ·  `screen`  ·  issue [#224](https://github.com/oramasearch/zetta/issues/224)

View compiled execution-graph IR, edit nodes/edges/config, manage versions, and prepare for validation.

View compiled execution-graph IR, edit nodes/edges/config, manage versions, and prepare for validation.

**Realizes / depends on / relates to:** realizes → [`FEAT-2`](backlog.md#feat-2)
**Referenced by:** [`CMP-1`](ux.md#cmp-1) realizes · [`FR-3`](requirements.md#fr-3) realizes

### SCR-4 — Correctness Gate  {: #scr-4 }

`draft`  ·  `screen`  ·  issue [#225](https://github.com/oramasearch/zetta/issues/225)

Run and review validation checks (compile/type/smoke test; planned checks indicated) and block/allow deployment.

Run and review validation checks (compile/type/smoke test; planned checks indicated) and block/allow deployment.

**Realizes / depends on / relates to:** realizes → [`FEAT-3`](backlog.md#feat-3)
**Referenced by:** [`CMP-2`](ux.md#cmp-2) realizes · [`FR-4`](requirements.md#fr-4) realizes

### SCR-5 — Deploy  {: #scr-5 }

`draft`  ·  `screen`  ·  issue [#226](https://github.com/oramasearch/zetta/issues/226)

Select placement target (R1 local; planned k8s/cloud gated), configure prerequisites, and perform one-button deploy with status.

Select placement target (R1 local; planned k8s/cloud gated), configure prerequisites, and perform one-button deploy with status.

**Realizes / depends on / relates to:** realizes → [`FEAT-4`](backlog.md#feat-4)
**Referenced by:** [`CMP-3`](ux.md#cmp-3) realizes · [`FR-5`](requirements.md#fr-5) realizes

### SCR-6 — Runs, Outputs & Lineage  {: #scr-6 }

`draft`  ·  `screen`  ·  issue [#227](https://github.com/oramasearch/zetta/issues/227)

Start runs, monitor execution, inspect logs, retrieve outputs, and view lineage and audit-relevant events per run.

Start runs, monitor execution, inspect logs, retrieve outputs, and view lineage and audit-relevant events per run.

**Realizes / depends on / relates to:** realizes → [`FEAT-5`](backlog.md#feat-5)
**Referenced by:** [`CMP-4`](ux.md#cmp-4) realizes · [`FR-6`](requirements.md#fr-6) realizes

### SCR-7 — Admin & Settings  {: #scr-7 }

`draft`  ·  `screen`  ·  issue [#228](https://github.com/oramasearch/zetta/issues/228)

Manage identity/key scope (V1), secret references, node registry, provider integrations (local shipped; others planned), and view audit logs/approval queues.

Manage identity/key scope (V1), secret references, node registry, provider integrations (local shipped; others planned), and view audit logs/approval queues.

**Realizes / depends on / relates to:** realizes → [`FEAT-9`](backlog.md#feat-9)
**Referenced by:** [`CMP-5`](ux.md#cmp-5) realizes · [`DR-1`](requirements.md#dr-1) relates to · [`FR-7`](requirements.md#fr-7) realizes

## Journeys

### JRN-1 — Ingest → architect → deploy → run  {: #jrn-1 }

`draft`  ·  `journey`  ·  issue [#167](https://github.com/oramasearch/zetta/issues/167)

The core journey: describe/import → see the validated graph → one-button deploy → watch it run with lineage.

Spans SCR-2→SCR-3→SCR-4→SCR-5→SCR-6. The product's spine. Realizes the four-step flow.

**Realizes / depends on / relates to:** relates to → [`FEAT-10`](backlog.md#feat-10)

### JRN-2 — Burst-train a model  {: #jrn-2 }

`draft`  ·  `journey`  ·  issue [#168](https://github.com/oramasearch/zetta/issues/168)

Define a training job → burst N ephemeral nodes → cluster-parallel train → tear down → model served.

Temporary-workload journey; spot capacity + cost cap; eviction-tolerant. See ADR-20/FEAT-6.

**Realizes / depends on / relates to:** relates to → [`ADR-20`](architecture.md#adr-20)

### JRN-3 — Self-serve ask (governed)  {: #jrn-3 }

`draft`  ·  `journey`  ·  issue [#169](https://github.com/oramasearch/zetta/issues/169)

A business user asks in plain language and gets a grounded, access-scoped answer — no ticket.

Sam (P3). Scoped to identity; trust surfaced (sources/freshness/confidence). See FEAT-9.

**Realizes / depends on / relates to:** relates to → [`FEAT-9`](backlog.md#feat-9)

### JRN-4 — Migrate from Amaro desktop  {: #jrn-4 }

`draft`  ·  `journey`  ·  issue [#170](https://github.com/oramasearch/zetta/issues/170)

Point at the existing Amaro Tauri SQLite DB → import projects/state into ZettaDB.

One-time migration journey. See TR-1/ADR-14.

**Realizes / depends on / relates to:** relates to → [`TR-1`](requirements.md#tr-1)

## UI Components

### CMP-1 — Graph canvas (ImGui)  {: #cmp-1 }

`draft`  ·  `ui_component`  ·  issue [#67](https://github.com/oramasearch/zetta/issues/67)

Visualize + edit the execution graph (nodes/edges/config, both IR forms).

SDL3/ImGui. Shows code-form + tabular-form; edits re-validate. Backs SCR-3.

**Realizes / depends on / relates to:** realizes → [`SCR-3`](ux.md#scr-3)

### CMP-2 — Correctness panel (ImGui)  {: #cmp-2 }

`draft`  ·  `ui_component`  ·  issue [#68](https://github.com/oramasearch/zetta/issues/68)

Shows validation checks + pass/fail with reasons; gates deploy.

Backs SCR-4. Surfaces schema/leakage/point-in-time + eval results.

**Realizes / depends on / relates to:** realizes → [`SCR-4`](ux.md#scr-4)

### CMP-3 — Placement / deploy picker (ImGui)  {: #cmp-3 }

`draft`  ·  `ui_component`  ·  issue [#69](https://github.com/oramasearch/zetta/issues/69)

Choose target (local/k8s/VPC/cloud), configure prerequisites, one-button deploy.

Backs SCR-5. Drives the Cloud Interface.

**Realizes / depends on / relates to:** realizes → [`SCR-5`](ux.md#scr-5)

### CMP-4 — Run monitor (ImGui)  {: #cmp-4 }

`draft`  ·  `ui_component`  ·  issue [#70](https://github.com/oramasearch/zetta/issues/70)

Live run status, logs, outputs, lineage, cost/latency.

Backs SCR-6. Streams results + lineage.

**Realizes / depends on / relates to:** realizes → [`SCR-6`](ux.md#scr-6)

### CMP-5 — Admin panel (ImGui)  {: #cmp-5 }

`draft`  ·  `ui_component`  ·  issue [#71](https://github.com/oramasearch/zetta/issues/71)

Node registry, capabilities/keys, audit log, approval queue, source connections.

Backs SCR-7. Governance surface.

**Realizes / depends on / relates to:** realizes → [`SCR-7`](ux.md#scr-7)
