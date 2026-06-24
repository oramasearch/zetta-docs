# Data & Storage

The control-plane store, its tables, and retention rules.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Data Stores

### DS-1 — Control-plane store (ZettaDB CRDT)  {: #ds-1 }

`draft`  ·  `data_store`  ·  issue [#79](https://github.com/oramasearch/zetta/issues/79)

ZettaDB's CRDT-replicated store holding all platform control-plane state.

Projects, execution graphs + versions, validation reports, runs + outputs, node registry, capability grants, audit events, source-connection refs, deployment targets. No separate Postgres. See ADR-1/DR-1.

**Realizes / depends on / relates to:** contains → [`TBL-1`](data.md#tbl-1) · contains → [`TBL-10`](data.md#tbl-10) · contains → [`TBL-11`](data.md#tbl-11) · contains → [`TBL-12`](data.md#tbl-12) · contains → [`TBL-2`](data.md#tbl-2) · contains → [`TBL-3`](data.md#tbl-3) · contains → [`TBL-4`](data.md#tbl-4) · contains → [`TBL-5`](data.md#tbl-5) · contains → [`TBL-6`](data.md#tbl-6) · contains → [`TBL-7`](data.md#tbl-7) · contains → [`TBL-8`](data.md#tbl-8) · contains → [`TBL-9`](data.md#tbl-9) · relates to → [`ADR-1`](architecture.md#adr-1)

### DS-2 — Large-object store  {: #ds-2 }

`draft`  ·  `data_store`  ·  issue [#80](https://github.com/oramasearch/zetta/issues/80)

ZettaDB large objects for models, indexes, tabular-IR files, and uploaded artifacts.

Holds trained models, built indexes, Parquet/CSV/Automerge graph files, and imported artifacts (n8n JSON). Peer-to-peer transfer with SHA-256 verification.

### DS-3 — Tiered data store (hot/cold)  {: #ds-3 }

`draft`  ·  `data_store`  ·  issue [#81](https://github.com/oramasearch/zetta/issues/81)

In-memory indexes (hot) aging to cold storage, re-warmed on request.

Materialized views + source snapshots placed across tiers. The cost+locality layer. See ADR-5/FEAT-7.

**Realizes / depends on / relates to:** relates to → [`ADR-5`](architecture.md#adr-5)
**Referenced by:** [`RET-4`](data.md#ret-4) relates to

## Data Tables

### TBL-1 — project  {: #tbl-1 }

`draft`  ·  `data_table`  ·  issue [#236](https://github.com/oramasearch/zetta/issues/236)

Project records (intent + provenance + ownership).

Control-plane store. Maps to ENT-1.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-2 — execution_graph  {: #tbl-2 }

`draft`  ·  `data_table`  ·  issue [#237](https://github.com/oramasearch/zetta/issues/237)

Execution-graph headers + current version pointer.

Control-plane store. Maps to ENT-3.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-3 — graph_version  {: #tbl-3 }

`draft`  ·  `data_table`  ·  issue [#238](https://github.com/oramasearch/zetta/issues/238)

Immutable versioned graph snapshots (code-form ref + tabular-form ref).

Control-plane store. Maps to ENT-4; bodies in the large-object store.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-4 — validation_report  {: #tbl-4 }

`draft`  ·  `data_table`  ·  issue [#239](https://github.com/oramasearch/zetta/issues/239)

Correctness-gate results per graph version.

Control-plane store. Maps to ENT-5.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-5 — run  {: #tbl-5 }

`draft`  ·  `data_table`  ·  issue [#240](https://github.com/oramasearch/zetta/issues/240)

Run records: status, timing, target, graph version.

Control-plane store. Maps to ENT-12.

**Referenced by:** [`DS-1`](data.md#ds-1) contains · [`RET-2`](data.md#ret-2) relates to

### TBL-6 — run_output  {: #tbl-6 }

`draft`  ·  `data_table`  ·  issue [#241](https://github.com/oramasearch/zetta/issues/241)

Outputs produced by a run, with lineage + provenance.

Control-plane store (pointers) + large-object store (bodies). Maps to ENT-16.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-7 — node_registry  {: #tbl-7 }

`draft`  ·  `data_table`  ·  issue [#242](https://github.com/oramasearch/zetta/issues/242)

Cluster nodes: identity, role, placement, status.

Control-plane store. Backs orchestration + mTLS. Maps to ENT-25.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-8 — audit_event  {: #tbl-8 }

`draft`  ·  `data_table`  ·  issue [#243](https://github.com/oramasearch/zetta/issues/243)

Append-only audit of graph changes, deploys, data access, capability use.

Control-plane store. Maps to ENT-23; see CTL-5.

**Referenced by:** [`DS-1`](data.md#ds-1) contains · [`RET-1`](data.md#ret-1) relates to

### TBL-9 — capability_grant  {: #tbl-9 }

`draft`  ·  `data_table`  ·  issue [#244](https://github.com/oramasearch/zetta/issues/244)

Capability grants: principal/key → scope, TTL.

Control-plane store. Maps to ENT-22; see ADR-12.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-10 — source_connection  {: #tbl-10 }

`draft`  ·  `data_table`  ·  issue [#245](https://github.com/oramasearch/zetta/issues/245)

Source connections with secret-references (never inline secrets).

Control-plane store. Maps to ENT-17; see CTL-3.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-11 — materialized_view  {: #tbl-11 }

`draft`  ·  `data_table`  ·  issue [#246](https://github.com/oramasearch/zetta/issues/246)

Materialized-view definitions + freshness/lag + tier placement.

Control-plane store (metadata); data in tiered store. Maps to ENT-18.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

### TBL-12 — deployment_target  {: #tbl-12 }

`draft`  ·  `data_table`  ·  issue [#247](https://github.com/oramasearch/zetta/issues/247)

Deployment targets: Cloud Interface binding + creds-ref + placement.

Control-plane store. Maps to ENT-6.

**Referenced by:** [`DS-1`](data.md#ds-1) contains

## Retention Rules

### RET-1 — Audit retention (long-lived, immutable)  {: #ret-1 }

`draft`  ·  `data_retention_rule`  ·  issue [#194](https://github.com/oramasearch/zetta/issues/194)

Audit events retained long-term, append-only, tamper-evident.

Governance requirement; supports compliance + no-egress verification. Covers audit_event.

**Realizes / depends on / relates to:** relates to → [`TBL-8`](data.md#tbl-8)

### RET-2 — Run-history retention  {: #ret-2 }

`draft`  ·  `data_retention_rule`  ·  issue [#195](https://github.com/oramasearch/zetta/issues/195)

Run + output metadata retained per policy; large outputs subject to tiering.

Configurable; feeds the experience loop + lineage.

**Realizes / depends on / relates to:** relates to → [`TBL-5`](data.md#tbl-5)

### RET-3 — Ephemeral node-identity TTL  {: #ret-3 }

`draft`  ·  `data_retention_rule`  ·  issue [#196](https://github.com/oramasearch/zetta/issues/196)

Burst-node identities + capability grants are short-lived and revoked on teardown.

Prevents identity sprawl from burst provisioning. See RSK-9/ADR-20.

**Realizes / depends on / relates to:** relates to → [`ENT-8`](domain-model.md#ent-8)

### RET-4 — Cold-storage retention + eviction  {: #ret-4 }

`draft`  ·  `data_retention_rule`  ·  issue [#197](https://github.com/oramasearch/zetta/issues/197)

Tiered data ages to cold and is evicted/re-warmed per policy.

Cost control for the tiered store. See ADR-5.

**Realizes / depends on / relates to:** relates to → [`DS-3`](data.md#ds-3)
