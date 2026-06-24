# Security

Threat model, trust boundaries, threats, controls, and permission rules.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Threat Models

### TM-1 — Orama Zetta threat model  {: #tm-1 }

`draft`  ·  `threat_model`  ·  issue [#261](https://github.com/oramasearch/zetta/issues/261)

STRIDE-style model over four surfaces: the customer-environment boundary, the extension sandbox, the cluster/inter-node channel, and the orchestration/cloud-credential path.

Scope: a single-tenant, in-firewall deployment that runs arbitrary extension code near customer data, replicates over a cluster, and orchestrates infrastructure with privileged credentials. Primary assets: customer data (no egress), source/cloud credentials, the control-plane state, and the integrity of generated/deployed graphs. Surfaces modeled below as trust boundaries (TB), threats (THR), and controls (CTL).

**Realizes / depends on / relates to:** contains → [`TB-1`](security.md#tb-1) · contains → [`TB-2`](security.md#tb-2) · contains → [`TB-3`](security.md#tb-3) · contains → [`THR-1`](security.md#thr-1) · contains → [`THR-2`](security.md#thr-2) · contains → [`THR-3`](security.md#thr-3) · contains → [`THR-4`](security.md#thr-4) · contains → [`THR-5`](security.md#thr-5)
**Referenced by:** [`REV-2`](governance.md#rev-2) relates to

## Trust Boundaries

### TB-1 — Customer-environment boundary (no egress)  {: #tb-1 }

`draft`  ·  `trust_boundary`  ·  issue [#233](https://github.com/oramasearch/zetta/issues/233)

The outermost boundary: nothing crosses out of the customer's environment by default.

All data, compute, and state live inside the customer's network/cloud. Outbound network is denied by default and must be explicitly configured + audited. Crossing this boundary is the highest-severity event. Backs NFR-1.

**Realizes / depends on / relates to:** relates to → [`NFR-1`](requirements.md#nfr-1)
**Referenced by:** [`TM-1`](security.md#tm-1) contains

### TB-2 — Extension sandbox boundary  {: #tb-2 }

`draft`  ·  `trust_boundary`  ·  issue [#234](https://github.com/oramasearch/zetta/issues/234)

Between untrusted extension/runner code and the node's data + API.

Lua/Orly (later Python) extension code is untrusted; it may only reach the ZettaDB API/data via capability tokens. The sandbox is the boundary between arbitrary code and the node. Backs ADR-12.

**Realizes / depends on / relates to:** relates to → [`ADR-12`](architecture.md#adr-12)
**Referenced by:** [`TM-1`](security.md#tm-1) contains

### TB-3 — Cluster / inter-node boundary  {: #tb-3 }

`draft`  ·  `trust_boundary`  ·  issue [#235](https://github.com/oramasearch/zetta/issues/235)

Between cluster nodes communicating over the network.

Node-to-node traffic (gossip, CRDT sync, large-object transfer, orchestration) crosses this boundary. Today plaintext TCP; target mTLS with per-node identity (ADR-18).

**Realizes / depends on / relates to:** relates to → [`ADR-18`](architecture.md#adr-18)
**Referenced by:** [`TM-1`](security.md#tm-1) contains

## Threats

### THR-1 — Extension sandbox escape / capability over-grant  {: #thr-1 }

`draft`  ·  `threat`  ·  issue [#256](https://github.com/oramasearch/zetta/issues/256)

Untrusted extension code escapes the sandbox or is granted more than the user's scope.

An extension reads/writes data beyond the invoking user's key scope, or breaks out to the host. Severity: high (data breach). Mitigated by CTL-1. Tracks RSK-7.

**Realizes / depends on / relates to:** relates to → [`RSK-7`](risks.md#rsk-7)
**Referenced by:** [`CTL-1`](security.md#ctl-1) mitigates · [`TM-1`](security.md#tm-1) contains

### THR-2 — Node impersonation / unauthorized cluster join  {: #thr-2 }

`draft`  ·  `threat`  ·  issue [#257](https://github.com/oramasearch/zetta/issues/257)

An attacker joins the cluster or impersonates a node over the plaintext channel.

Without node identity/mTLS, a rogue process could join the cluster or MITM inter-node traffic and read/replicate data. Severity: high. Mitigated by CTL-2 / ADR-18.

**Referenced by:** [`ADR-18`](architecture.md#adr-18) mitigates · [`CTL-2`](security.md#ctl-2) mitigates · [`TM-1`](security.md#tm-1) contains

### THR-3 — Source/cloud credential leakage  {: #thr-3 }

`draft`  ·  `threat`  ·  issue [#258](https://github.com/oramasearch/zetta/issues/258)

Snowflake keys, cloud-provider creds, or enrollment tokens leak via state, logs, or extensions.

Credentials embedded in project/run records, logs, or reachable by extensions could exfiltrate. Severity: high. Mitigated by CTL-3 (vault refs, no inline secrets) + CTL-1.

**Referenced by:** [`CTL-3`](security.md#ctl-3) mitigates · [`TM-1`](security.md#tm-1) contains

### THR-4 — Unauthorized orchestration  {: #thr-4 }

`draft`  ·  `threat`  ·  issue [#259](https://github.com/oramasearch/zetta/issues/259)

A node/principal acts as orchestrator (provisions infra, deploys nodes) without rights.

Because any authenticated node can orchestrate, a compromised or over-privileged principal could provision infrastructure or deploy rogue nodes. Severity: high. Mitigated by CTL-6 (capability-scoped orchestration) + ADR-18.

**Referenced by:** [`ADR-18`](architecture.md#adr-18) mitigates · [`CTL-6`](security.md#ctl-6) mitigates · [`TM-1`](security.md#tm-1) contains

### THR-5 — Data egress via a graph step or extension  {: #thr-5 }

`draft`  ·  `threat`  ·  issue [#260](https://github.com/oramasearch/zetta/issues/260)

A generated graph or extension opens an outbound channel and ships data out.

A malicious/erroneous graph step or extension attempts network egress to move data outside the boundary. Severity: critical. Mitigated by CTL-4 (deny egress by default + network-capture verification) + CTL-1.

**Referenced by:** [`CTL-1`](security.md#ctl-1) mitigates · [`CTL-4`](security.md#ctl-4) mitigates · [`TM-1`](security.md#tm-1) contains

## Security Controls

### CTL-1 — Capability-scoped deny-by-default sandbox  {: #ctl-1 }

`draft`  ·  `security_control`  ·  issue [#72](https://github.com/oramasearch/zetta/issues/72)

No ambient authority; access only via capability tokens scoped to the user's key; no fs/network by default; all calls audited.

Primary control for the extension surface. Implements ADR-12. Mitigates sandbox escape (THR-1), credential leakage (THR-3), and egress (THR-5).

**Realizes / depends on / relates to:** mitigates → [`THR-1`](security.md#thr-1) · mitigates → [`THR-5`](security.md#thr-5) · relates to → [`ADR-12`](architecture.md#adr-12)
**Referenced by:** [`QAS-1`](architecture.md#qas-1) verifies · [`TC-5`](testing.md#tc-5) verifies

### CTL-2 — mTLS + per-node identity + enrollment token  {: #ctl-2 }

`draft`  ·  `security_control`  ·  issue [#73](https://github.com/oramasearch/zetta/issues/73)

Mutual TLS on all inter-node traffic; cryptographic node identity; token-gated cluster join.

Implements ADR-18. Mitigates node impersonation / unauthorized join (THR-2). Wires the TLS Corosio supports; R1 leans on the single-tenant network boundary meanwhile.

**Realizes / depends on / relates to:** mitigates → [`THR-2`](security.md#thr-2) · relates to → [`ADR-18`](architecture.md#adr-18)
**Referenced by:** [`QAS-2`](architecture.md#qas-2) verifies

### CTL-3 — Secret references via vault (never inline)  {: #ctl-3 }

`draft`  ·  `security_control`  ·  issue [#74](https://github.com/oramasearch/zetta/issues/74)

Credentials are stored as references resolved from a vault; never embedded in project/run records or logs.

Mitigates credential leakage (THR-3). Backs IR-1 (secret-ref integration) and DR-1 (control-plane state). Aligns with the OS-keychain pattern from the existing desktop.

**Realizes / depends on / relates to:** mitigates → [`THR-3`](security.md#thr-3) · relates to → [`IR-1`](requirements.md#ir-1)
**Referenced by:** [`RULE-6`](backlog.md#rule-6) relates to

### CTL-4 — Egress denied by default + network-capture verification  {: #ctl-4 }

`draft`  ·  `security_control`  ·  issue [#75](https://github.com/oramasearch/zetta/issues/75)

No outbound network from graph/extension execution by default; verified by running a full cycle under packet capture.

Mitigates data egress (THR-5) and backs NFR-1. The verification (a full ingest→deploy→run cycle under network capture asserting zero unexpected outbound) is part of TP-1.

**Realizes / depends on / relates to:** mitigates → [`THR-5`](security.md#thr-5) · relates to → [`NFR-1`](requirements.md#nfr-1)
**Referenced by:** [`QAS-1`](architecture.md#qas-1) verifies

### CTL-5 — Immutable audit trail + approval gates  {: #ctl-5 }

`draft`  ·  `security_control`  ·  issue [#76](https://github.com/oramasearch/zetta/issues/76)

Every graph change, deploy, and data access is logged; risky/shared actions route through approval.

Implements FEAT-9. Mitigates over-broad actions across surfaces; approval gates apply to shared/enterprise-published extensions and risky deploys.

**Realizes / depends on / relates to:** relates to → [`FEAT-9`](backlog.md#feat-9)

### CTL-6 — Capability-scoped orchestration rights  {: #ctl-6 }

`draft`  ·  `security_control`  ·  issue [#77](https://github.com/oramasearch/zetta/issues/77)

The right to orchestrate (provision infra, deploy nodes) is a capability granted to the authenticated principal, not implicit in cluster membership.

Mitigates unauthorized orchestration (THR-4). Same capability model as the sandbox; backs ADR-18 + ADR-15.

**Realizes / depends on / relates to:** mitigates → [`THR-4`](security.md#thr-4) · relates to → [`ADR-15`](architecture.md#adr-15)
**Referenced by:** [`QAS-2`](architecture.md#qas-2) verifies

## Permission Rules

### PERM-1 — Key-scoped access (V1 default)  {: #perm-1 }

`draft`  ·  `permission_rule`  ·  issue [#181](https://github.com/oramasearch/zetta/issues/181)

A principal operates over exactly the data the login key already permits; no bespoke permission model in V1.

Implements ADR-6. The V1 access model; finer tiers (team/partner/per-dataset) layer on later.

**Realizes / depends on / relates to:** relates to → [`ADR-6`](architecture.md#adr-6)

### PERM-2 — Orchestration permission  {: #perm-2 }

`draft`  ·  `permission_rule`  ·  issue [#182](https://github.com/oramasearch/zetta/issues/182)

Only principals holding the orchestration capability may provision infra or deploy nodes.

Backs CTL-6 / ADR-18. Distinguishes 'can run a graph' from 'can change infrastructure.'

**Realizes / depends on / relates to:** relates to → [`ADR-18`](architecture.md#adr-18)

### PERM-3 — Extension publish/approval permission  {: #perm-3 }

`draft`  ·  `permission_rule`  ·  issue [#183](https://github.com/oramasearch/zetta/issues/183)

Publishing a shared/enterprise extension requires the publish capability and passes an approval gate; personal runs do not.

Backs ADR-12 governance nuance: approval gates on shared/enterprise-published extensions, not every personal run.

**Realizes / depends on / relates to:** relates to → [`ADR-12`](architecture.md#adr-12)
**Referenced by:** [`APR-1`](governance.md#apr-1) relates to · [`RULE-4`](backlog.md#rule-4) relates to
