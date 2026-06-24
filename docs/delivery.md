# Delivery

Releases R1→R8, environments, runbooks, and baselines.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Releases

### REL-1 — R1 — Skateboard (local)  {: #rel-1 }

`draft`  ·  `release`  ·  issue [#186](https://github.com/oramasearch/zetta/issues/186)

Import an n8n workflow → correct graph → run on a local ZettaDB node.

Roadmap R1; runs on today's ZettaDB. The Motive build is R1 scoped to one customer. Env: Local.

**Realizes / depends on / relates to:** contains → [`FEAT-1`](backlog.md#feat-1) · contains → [`FEAT-2`](backlog.md#feat-2)
**Referenced by:** [`ENV-1`](delivery.md#env-1) relates to

### REL-2 — R2 — Correctness gate  {: #rel-2 }

`draft`  ·  `release`  ·  issue [#187](https://github.com/oramasearch/zetta/issues/187)

Validate graphs (schema/leakage/point-in-time + eval) before deploy.

Roadmap R2. Gates self-service. See FEAT-3.

**Realizes / depends on / relates to:** contains → [`FEAT-3`](backlog.md#feat-3)

### REL-3 — R3 — One-button deploy  {: #rel-3 }

`draft`  ·  `release`  ·  issue [#188](https://github.com/oramasearch/zetta/issues/188)

Provision a ZettaDB node + graph onto one real target (k8s) and self-heal.

Roadmap R3. Cloud Interface (CLI/HTTP). Env: Customer-k8s.

**Realizes / depends on / relates to:** contains → [`FEAT-4`](backlog.md#feat-4)
**Referenced by:** [`ENV-2`](delivery.md#env-2) relates to

### REL-4 — R4 — Tiered storage  {: #rel-4 }

`draft`  ·  `release`  ·  issue [#189](https://github.com/oramasearch/zetta/issues/189)

Source → in-memory index → cold → re-warm; serve from local materialized copy.

Roadmap R4. ZettaDB engine bet. See ADR-5.

**Realizes / depends on / relates to:** contains → [`FEAT-7`](backlog.md#feat-7)

### REL-5 — R5 — Compute-near-data  {: #rel-5 }

`draft`  ·  `release`  ·  issue [#190](https://github.com/oramasearch/zetta/issues/190)

Run user/agent code (Lua/Orly) on the node via the native API; native cluster-parallel ops.

Roadmap R5. See ADR-4/ADR-17.

**Realizes / depends on / relates to:** contains → [`FEAT-8`](backlog.md#feat-8)

### REL-6 — R6 — Governance  {: #rel-6 }

`draft`  ·  `release`  ·  issue [#191](https://github.com/oramasearch/zetta/issues/191)

Identity (Okta), RBAC tiers, audit, approval gates; mTLS/enrollment hardening.

Roadmap R6. See FEAT-9/ADR-18.

**Realizes / depends on / relates to:** contains → [`FEAT-9`](backlog.md#feat-9)

### REL-7 — R7 — GUI as product surface  {: #rel-7 }

`draft`  ·  `release`  ·  issue [#192](https://github.com/oramasearch/zetta/issues/192)

The full ImGui control plane: import → graph → deploy → monitor in one app.

Roadmap R7. See FEAT-10/ADR-14.

**Realizes / depends on / relates to:** contains → [`FEAT-10`](backlog.md#feat-10)

### REL-8 — R8 — Multi-cloud + learning loop  {: #rel-8 }

`draft`  ·  `release`  ·  issue [#193](https://github.com/oramasearch/zetta/issues/193)

AWS/Azure/GCP targets + the grounded experience loop improving graph generation.

Roadmap R8 (north-star, deferred). See BC-6.

**Realizes / depends on / relates to:** relates to → [`BC-6`](domain-model.md#bc-6)

## Environments

### ENV-1 — Local (desktop node)  {: #env-1 }

`draft`  ·  `environment`  ·  issue [#110](https://github.com/oramasearch/zetta/issues/110)

The SDL3/ImGui desktop running as a single ZettaDB node.

R1 target; dev + single-box. Desktop is a cluster node.

**Realizes / depends on / relates to:** relates to → [`REL-1`](delivery.md#rel-1)

### ENV-2 — Customer Kubernetes  {: #env-2 }

`draft`  ·  `environment`  ·  issue [#111](https://github.com/oramasearch/zetta/issues/111)

ZettaDB nodes deployed into the customer's own k8s cluster/account.

R3 target; in-firewall. Provisioned via the Cloud Interface.

**Realizes / depends on / relates to:** relates to → [`REL-3`](delivery.md#rel-3)

### ENV-3 — Customer VPC / on-prem  {: #env-3 }

`draft`  ·  `environment`  ·  issue [#112](https://github.com/oramasearch/zetta/issues/112)

ZettaDB on a customer-controlled VM / on-prem host.

The Motive-style in-firewall case. Data never leaves.

### ENV-4 — Ephemeral burst  {: #env-4 }

`draft`  ·  `environment`  ·  issue [#113](https://github.com/oramasearch/zetta/issues/113)

Short-lived N-node pools for temporary parallel workloads (training, big DDF).

Spot/low-priority capacity; torn down after. See ADR-20.

**Realizes / depends on / relates to:** relates to → [`ADR-20`](architecture.md#adr-20)

### ENV-5 — Managed cloud (later)  {: #env-5 }

`draft`  ·  `environment`  ·  issue [#114](https://github.com/oramasearch/zetta/issues/114)

AWS/Azure/GCP managed provisioners as additional targets.

R8; lowest near-term priority (in-firewall first).

## Runbooks

### RUN-1 — Low-friction node bootstrapping (ZettaDB-native)  {: #run-1 }

`draft`  ·  `runbook`  ·  issue [#215](https://github.com/oramasearch/zetta/issues/215)

Target UX: a declarative node/infra inventory + one orchestrate action; new headless ZettaDB nodes join via enrollment token + mTLS. k0s flow shown as illustrative inspiration only, not the chosen implementation.

**Target UX (ZettaDB-native):** a user points the orchestrator node at a target (a declarative node/infra inventory or a cloud account), authenticates, and runs one orchestrate action; the **Cloud Interface** (ADR-15) provisions/identifies the infra and ZettaDB stands up **headless nodes** that **join via an enrollment token + mTLS** (ADR-18). Low friction, on our own primitives.

**Illustrative inspiration only (NOT the chosen implementation):** k0s shows the ergonomics we like — `k0sctl init` → edit a hosts inventory (roles + ssh) → `k0sctl apply` (one converge step) → `k0sctl kubeconfig`; or per-host `k0s install` + `k0s token create` + `k0s install worker --token-file` + `k0s start`; or k0smotron CRDs over the k8s API for an SSH-free path. We borrow the *shape* (declarative inventory, one apply, token join, CLI-vs-API surfaces) — not the tool, not its API. See ADR-19."

**Realizes / depends on / relates to:** relates to → [`ADR-19`](architecture.md#adr-19) · relates to → [`FEAT-4`](backlog.md#feat-4)

## Baselines

### BL-1 — Blueprint baseline v0  {: #bl-1 }

`draft`  ·  `baseline`  ·  issue [#49](https://github.com/oramasearch/zetta/issues/49)

The 2026-06-24 design baseline captured in this blueprint.

Snapshot of vision/strategy/architecture/domain/security/delivery decisions as of the grill session. Future change requests diff against this.

**Realizes / depends on / relates to:** relates to → [`VIS-1`](strategy.md#vis-1)
**Referenced by:** [`REV-1`](governance.md#rev-1) relates to
