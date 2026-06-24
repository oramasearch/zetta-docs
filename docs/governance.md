# Governance

Reviews and approval gates.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Reviews

### REV-1 — Blueprint design review (grill session)  {: #rev-1 }

`draft`  ·  `review`  ·  issue [#198](https://github.com/oramasearch/zetta/issues/198)

The 2026-06-24 interview that resolved the design decision tree (IR, GUI, sandbox, orchestration, native compute, cluster trust, bootstrap, burst).

Captured decisions ADR-10…ADR-20 and the six bounded contexts. Baseline: BL-1.

**Realizes / depends on / relates to:** relates to → [`BL-1`](delivery.md#bl-1)

### REV-2 — Security / threat-model review  {: #rev-2 }

`draft`  ·  `review`  ·  issue [#199](https://github.com/oramasearch/zetta/issues/199)

Review of the threat model, trust boundaries, controls, and permission rules.

Covers TM-1 + the extension-sandbox, cluster-trust, and orchestration surfaces. Gate before enterprise pilots.

**Realizes / depends on / relates to:** relates to → [`TM-1`](security.md#tm-1)

## Approvals

### APR-1 — Extension-publish approval  {: #apr-1 }

`draft`  ·  `approval`  ·  issue [#29](https://github.com/oramasearch/zetta/issues/29)

Approval gate before a shared/enterprise extension can run in production.

Personal runs are not gated; shared/published extensions are. See PERM-3/ADR-12, ENT-24.

**Realizes / depends on / relates to:** relates to → [`PERM-3`](security.md#perm-3)

### APR-2 — Risky-deploy approval  {: #apr-2 }

`draft`  ·  `approval`  ·  issue [#30](https://github.com/oramasearch/zetta/issues/30)

Approval gate for risky deploys / infrastructure changes.

Routes through an approver before apply. See FEAT-9, ADR-18 (orchestration capability).

**Realizes / depends on / relates to:** relates to → [`FEAT-4`](backlog.md#feat-4)

### APR-3 — Large-burst cost-cap approval  {: #apr-3 }

`draft`  ·  `approval`  ·  issue [#31](https://github.com/oramasearch/zetta/issues/31)

Approval for ephemeral bursts above a cost/size threshold.

Guards against runaway spend. See ADR-20/RSK-9.

**Realizes / depends on / relates to:** relates to → [`ADR-20`](architecture.md#adr-20)
