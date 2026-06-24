# Testing

The test plan and its test cases.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Test Plans

### TP-1 — Orama Zetta verification plan  {: #tp-1 }

`draft`  ·  `test_plan`  ·  issue [#262](https://github.com/oramasearch/zetta/issues/262)

How the blueprint's features + NFRs are verified — correctness gate eval, no-egress, deploy reliability, velocity.

**Correctness:** an eval set of generated graphs measuring compile+run+correct-answer rate (floor before self-service GA); the entity-resolution division-correct case. **No data egress:** run a full ingest→deploy→run cycle under network capture; assert zero outbound. **Deploy reliability:** one-button deploy success + self-heal on node failure. **Intelligence Velocity:** instrument intent→deployed timing spans per stage. **Governance:** audit completeness for every graph change/deploy/data access; identity-scoped results.

**Realizes / depends on / relates to:** contains → [`TC-1`](testing.md#tc-1) · contains → [`TC-2`](testing.md#tc-2) · contains → [`TC-3`](testing.md#tc-3) · contains → [`TC-4`](testing.md#tc-4) · contains → [`TC-5`](testing.md#tc-5) · contains → [`TC-6`](testing.md#tc-6) · contains → [`TC-7`](testing.md#tc-7) · contains → [`TC-8`](testing.md#tc-8) · verifies → [`FEAT-3`](backlog.md#feat-3) · verifies → [`FEAT-4`](backlog.md#feat-4) · verifies → [`FEAT-6`](backlog.md#feat-6) · verifies → [`FEAT-9`](backlog.md#feat-9) · verifies → [`KPI-1`](strategy.md#kpi-1) · verifies → [`NFR-1`](requirements.md#nfr-1) · verifies → [`QAS-1`](architecture.md#qas-1) · verifies → [`QAS-2`](architecture.md#qas-2)

## Test Cases

### TC-1 — Correctness-gate eval rate  {: #tc-1 }

`draft`  ·  `test_case`  ·  issue [#248](https://github.com/oramasearch/zetta/issues/248)

Measure % of generated graphs that compile AND run AND produce correct results against an eval set.

Verifies the correctness gate; floor before self-service GA. See KPI-2/FEAT-3.

**Realizes / depends on / relates to:** verifies → [`FEAT-3`](backlog.md#feat-3)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains

### TC-2 — No egress under network capture  {: #tc-2 }

`draft`  ·  `test_case`  ·  issue [#249](https://github.com/oramasearch/zetta/issues/249)

Run a full ingest→deploy→run cycle under packet capture; assert zero unexpected outbound.

Verifies NFR-1/CTL-4.

**Realizes / depends on / relates to:** verifies → [`NFR-1`](requirements.md#nfr-1)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains

### TC-3 — Deploy + self-heal on node failure  {: #tc-3 }

`draft`  ·  `test_case`  ·  issue [#250](https://github.com/oramasearch/zetta/issues/250)

One-button deploy succeeds; killing a node triggers reconcile/repair.

Verifies FEAT-4/ADR-7.

**Realizes / depends on / relates to:** verifies → [`FEAT-4`](backlog.md#feat-4)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains

### TC-4 — Entity-resolution division-correct  {: #tc-4 }

`draft`  ·  `test_case`  ·  issue [#251](https://github.com/oramasearch/zetta/issues/251)

The churn query resolves to the right division, never an averaged aggregate.

The canonical correctness case. Verifies FEAT-3/FEAT-2.

**Realizes / depends on / relates to:** verifies → [`FEAT-2`](backlog.md#feat-2)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains · [`UC-1`](backlog.md#uc-1) relates to

### TC-5 — Sandbox escape / over-scope denied  {: #tc-5 }

`draft`  ·  `test_case`  ·  issue [#252](https://github.com/oramasearch/zetta/issues/252)

A malicious extension cannot egress or read beyond its capability scope; attempts are denied + audited.

Verifies CTL-1/QAS-1.

**Realizes / depends on / relates to:** verifies → [`CTL-1`](security.md#ctl-1)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains

### TC-6 — Bulk burst identity + teardown revocation  {: #tc-6 }

`draft`  ·  `test_case`  ·  issue [#253](https://github.com/oramasearch/zetta/issues/253)

Bursting N nodes mints N distinct identities; teardown revokes them with no orphans.

Verifies ADR-20/ADR-18/RSK-9.

**Realizes / depends on / relates to:** relates to → [`ADR-20`](architecture.md#adr-20)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains

### TC-7 — SQLite migration import fidelity  {: #tc-7 }

`draft`  ·  `test_case`  ·  issue [#254](https://github.com/oramasearch/zetta/issues/254)

Importing the Amaro Tauri SQLite DB reproduces projects/state in Orama Zetta without loss.

Verifies TR-1/ADR-14.

**Realizes / depends on / relates to:** verifies → [`TR-1`](requirements.md#tr-1)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains

### TC-8 — Intent→deployed latency  {: #tc-8 }

`draft`  ·  `test_case`  ·  issue [#255](https://github.com/oramasearch/zetta/issues/255)

Instrument and assert intent/artifact → deployed-running within the velocity target.

Verifies KPI-1 (Intelligence Velocity).

**Realizes / depends on / relates to:** verifies → [`KPI-1`](strategy.md#kpi-1)
**Referenced by:** [`TP-1`](testing.md#tp-1) contains
