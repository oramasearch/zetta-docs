# Requirements

Business → stakeholder → functional → non-functional → integration → data → transition.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Business Requirements

### BR-1 — Intelligence Velocity outcome  {: #br-1 }

`draft`  ·  `business_requirement`  ·  issue [#50](https://github.com/oramasearch/zetta/issues/50)

Reduce time from user intent to a deployed, running, correct intelligence workflow on customer-controlled infrastructure; primary KPI is median intent→running time per project and secondary KPIs are correctness pass rate, deploy success rate, and time-to-first-result.

Reduce time from user intent to a deployed, running, correct intelligence workflow on customer-controlled infrastructure; primary KPI is median intent→running time per project and secondary KPIs are correctness pass rate, deploy success rate, and time-to-first-result.

**Realizes / depends on / relates to:** relates to → [`SCR-1`](ux.md#scr-1)
**Referenced by:** [`FEAT-6`](backlog.md#feat-6) relates to · [`SCR-1`](ux.md#scr-1) relates to · [`SR-1`](requirements.md#sr-1) derives from

## Stakeholder Requirements

### SR-1 — Primary personas supported  {: #sr-1 }

`draft`  ·  `stakeholder_requirement`  ·  issue [#229](https://github.com/oramasearch/zetta/issues/229)

Support Charles (platform/AI lead), Dana (data scientist), Sam (analyst/business user), and an Agent operator, each with tailored capabilities and visibility consistent with governed self-service and key-scoped access in V1.

Support Charles (platform/AI lead), Dana (data scientist), Sam (analyst/business user), and an Agent operator, each with tailored capabilities and visibility consistent with governed self-service and key-scoped access in V1.

**Realizes / depends on / relates to:** derives from → [`BR-1`](requirements.md#br-1) · satisfies → [`FR-7`](requirements.md#fr-7)
**Referenced by:** [`FR-1`](requirements.md#fr-1) satisfies · [`FR-2`](requirements.md#fr-2) satisfies · [`FR-3`](requirements.md#fr-3) satisfies · [`FR-4`](requirements.md#fr-4) satisfies · [`FR-5`](requirements.md#fr-5) satisfies · [`FR-6`](requirements.md#fr-6) satisfies · [`FR-7`](requirements.md#fr-7) satisfies · [`PER-1`](personas.md#per-1) relates to · [`PER-2`](personas.md#per-2) relates to · [`PER-3`](personas.md#per-3) relates to · [`PER-4`](personas.md#per-4) relates to

## Functional Requirements

### FR-1 — Intent + artifact ingestion to project  {: #fr-1 }

`draft`  ·  `functional_requirement`  ·  issue [#142](https://github.com/oramasearch/zetta/issues/142)

Allow users to create a project by describing a data/AI problem in natural language and/or importing artifacts, and store the raw inputs with provenance for later re-compilation.

Allow users to create a project by describing a data/AI problem in natural language and/or importing artifacts, and store the raw inputs with provenance for later re-compilation.

**Realizes / depends on / relates to:** realizes → [`SCR-2`](ux.md#scr-2) · satisfies → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`FEAT-1`](backlog.md#feat-1) realizes · [`NFR-2`](requirements.md#nfr-2) verifies

### FR-2 — Artifact import support (R1 + planned)  {: #fr-2 }

`draft`  ·  `functional_requirement`  ·  issue [#143](https://github.com/oramasearch/zetta/issues/143)

Parse supported artifacts into an internal representation; R1 must support n8n workflow JSON import, while SQL scripts, notebooks, and schema files are planned and may appear as disabled or beta-gated options.

Parse supported artifacts into an internal representation; R1 must support n8n workflow JSON import, while SQL scripts, notebooks, and schema files are planned and may appear as disabled or beta-gated options.

**Realizes / depends on / relates to:** realizes → [`SCR-2`](ux.md#scr-2) · satisfies → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`FEAT-1`](backlog.md#feat-1) realizes

### FR-3 — Compile to execution-graph IR and allow review/edit  {: #fr-3 }

`draft`  ·  `functional_requirement`  ·  issue [#144](https://github.com/oramasearch/zetta/issues/144)

Compile intent/artifacts into a professionally-architected execution graph IR (connect → clean → model → index → serve → act) and provide a GUI to inspect, edit parameters, and persist versions of the graph.

Compile intent/artifacts into a professionally-architected execution graph IR (connect → clean → model → index → serve → act) and provide a GUI to inspect, edit parameters, and persist versions of the graph.

**Realizes / depends on / relates to:** realizes → [`SCR-3`](ux.md#scr-3) · satisfies → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`FEAT-2`](backlog.md#feat-2) realizes

### FR-4 — Correctness gate before deploy  {: #fr-4 }

`draft`  ·  `functional_requirement`  ·  issue [#145](https://github.com/oramasearch/zetta/issues/145)

Before deployment, run a correctness gate that includes compilation checks and executable validation; R1 includes schema/type checks and a runnable smoke test, while data-leakage and point-in-time checks are planned and shown as not-yet-enforced where applicable.

Before deployment, run a correctness gate that includes compilation checks and executable validation; R1 includes schema/type checks and a runnable smoke test, while data-leakage and point-in-time checks are planned and shown as not-yet-enforced where applicable.

**Realizes / depends on / relates to:** realizes → [`SCR-4`](ux.md#scr-4) · satisfies → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`FEAT-3`](backlog.md#feat-3) realizes

### FR-5 — One-button deploy with placement dial (R1 local; planned k8s/cloud)  {: #fr-5 }

`draft`  ·  `functional_requirement`  ·  issue [#146](https://github.com/oramasearch/zetta/issues/146)

Deploy ZettaDB nodes and the validated execution graph onto customer-controlled targets; R1 must deploy to a local ZettaDB node/runtime, while Kubernetes and major clouds/on-prem provisioners are planned behind feature flags.

Deploy ZettaDB nodes and the validated execution graph onto customer-controlled targets; R1 must deploy to a local ZettaDB node/runtime, while Kubernetes and major clouds/on-prem provisioners are planned behind feature flags.

**Realizes / depends on / relates to:** realizes → [`SCR-5`](ux.md#scr-5) · satisfies → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`FEAT-4`](backlog.md#feat-4) realizes · [`IR-1`](requirements.md#ir-1) depends on · [`NFR-1`](requirements.md#nfr-1) satisfies · [`NFR-2`](requirements.md#nfr-2) verifies

### FR-6 — Run orchestration, monitoring, and outputs  {: #fr-6 }

`draft`  ·  `functional_requirement`  ·  issue [#147](https://github.com/oramasearch/zetta/issues/147)

Execute deployed graphs, show run status (queued/running/succeeded/failed), logs, artifacts produced (datasets/models/indexes), and lineage linking outputs back to graph versions and inputs.

Execute deployed graphs, show run status (queued/running/succeeded/failed), logs, artifacts produced (datasets/models/indexes), and lineage linking outputs back to graph versions and inputs.

**Realizes / depends on / relates to:** realizes → [`SCR-6`](ux.md#scr-6) · satisfies → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`FEAT-5`](backlog.md#feat-5) realizes · [`NFR-1`](requirements.md#nfr-1) satisfies · [`NFR-2`](requirements.md#nfr-2) verifies

### FR-7 — Governed self-service: identity, key-scoped access, approvals, audit  {: #fr-7 }

`draft`  ·  `functional_requirement`  ·  issue [#148](https://github.com/oramasearch/zetta/issues/148)

Enforce governed self-service within the customer environment: V1 uses key-scoped access inherited from the login key; capture an immutable audit trail of graph changes, deploy actions, and data access; provide approval gates for risky actions (configurable). OAuth/Okta and finer-grained RBAC are planned.

Enforce governed self-service within the customer environment: V1 uses key-scoped access inherited from the login key; capture an immutable audit trail of graph changes, deploy actions, and data access; provide approval gates for risky actions (configurable). OAuth/Okta and finer-grained RBAC are planned.

**Realizes / depends on / relates to:** realizes → [`SCR-7`](ux.md#scr-7) · satisfies → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`FEAT-9`](backlog.md#feat-9) realizes · [`SR-1`](requirements.md#sr-1) satisfies

## Non-Functional Requirements

### NFR-1 — No data egress by default and verifiable execution locality  {: #nfr-1 }

`draft`  ·  `nonfunctional_requirement`  ·  issue [#175](https://github.com/oramasearch/zetta/issues/175)

Ensure data does not leave the customer-controlled environment by default; any outbound network access must be explicitly configured and auditable; provide evidence of execution locality (which node accessed which data).

Ensure data does not leave the customer-controlled environment by default; any outbound network access must be explicitly configured and auditable; provide evidence of execution locality (which node accessed which data).

**Realizes / depends on / relates to:** satisfies → [`FR-5`](requirements.md#fr-5) · satisfies → [`FR-6`](requirements.md#fr-6)
**Referenced by:** [`ADR-12`](architecture.md#adr-12) relates to · [`CTL-4`](security.md#ctl-4) relates to · [`FEAT-7`](backlog.md#feat-7) relates to · [`FEAT-8`](backlog.md#feat-8) relates to · [`RULE-2`](backlog.md#rule-2) relates to · [`STK-2`](personas.md#stk-2) relates to · [`TB-1`](security.md#tb-1) relates to · [`TC-2`](testing.md#tc-2) verifies · [`TP-1`](testing.md#tp-1) verifies

### NFR-2 — Reliability and responsiveness quality scenarios  {: #nfr-2 }

`draft`  ·  `nonfunctional_requirement`  ·  issue [#176](https://github.com/oramasearch/zetta/issues/176)

Provide responsive desktop UX and reliable deploy/run behavior: compilation and validation should be interactive for typical graphs; deployments should be resumable and runs should be observable and diagnosable.

Provide responsive desktop UX and reliable deploy/run behavior: compilation and validation should be interactive for typical graphs; deployments should be resumable and runs should be observable and diagnosable.

**Realizes / depends on / relates to:** verifies → [`FR-1`](requirements.md#fr-1) · verifies → [`FR-5`](requirements.md#fr-5) · verifies → [`FR-6`](requirements.md#fr-6)

## Integration Requirements

### IR-1 — Infrastructure and runtime integration surface  {: #ir-1 }

`draft`  ·  `integration_requirement`  ·  issue [#166](https://github.com/oramasearch/zetta/issues/166)

Integrate with local runtime in R1 and define provider interfaces for Kubernetes and cloud provisioners as planned modules; support secret references without exposing secret material in project or run records.

Integrate with local runtime in R1 and define provider interfaces for Kubernetes and cloud provisioners as planned modules; support secret references without exposing secret material in project or run records.

**Realizes / depends on / relates to:** depends on → [`FR-5`](requirements.md#fr-5) · relates to → [`ADR-7`](architecture.md#adr-7)
**Referenced by:** [`ADR-15`](architecture.md#adr-15) relates to · [`CTL-3`](security.md#ctl-3) relates to

## Data Requirements

### DR-1 — ZettaDB as control-plane state store  {: #dr-1 }

`draft`  ·  `data_requirement`  ·  issue [#78](https://github.com/oramasearch/zetta/issues/78)

Store control-plane state (projects, graph IR versions, node registry, run history, secret references, audit trail) in ZettaDB’s CRDT-replicated JSON store; no separate Postgres control plane is required.

Store control-plane state (projects, graph IR versions, node registry, run history, secret references, audit trail) in ZettaDB’s CRDT-replicated JSON store; no separate Postgres control plane is required.

**Realizes / depends on / relates to:** relates to → [`ADR-1`](architecture.md#adr-1) · relates to → [`SCR-7`](ux.md#scr-7)

## Transition Requirements

### TR-1 — Migrate from Amaro Tauri desktop via SQLite import  {: #tr-1 }

`draft`  ·  `transition_requirement`  ·  issue [#263](https://github.com/oramasearch/zetta/issues/263)

Import the existing Amaro Tauri app's SQLite database into ZettaDB; that's the bulk of migration.

Existing users are on the Amaro Tauri desktop, which stores state in a local **SQLite** database. **Transition:** read/import that SQLite data into ZettaDB's store so users carry their projects/state forward. Because the new desktop is a native ZettaDB node, migration is primarily a one-time data import, not a re-setup. Relates to ADR-14.

**Referenced by:** [`ADR-14`](architecture.md#adr-14) relates to · [`JRN-4`](ux.md#jrn-4) relates to · [`TC-7`](testing.md#tc-7) verifies
