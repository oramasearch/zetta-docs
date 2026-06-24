# Architecture

The decisions (ADRs), the architecture elements they shape, and the quality scenarios that test them.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Architecture Decisions

### ADR-1 — Orama Zetta is the spine (no separate Postgres control plane)  {: #adr-1 }

`draft`  ·  `adr`  ·  issue [#1](https://github.com/oramasearch/zetta/issues/1)

Control-plane state lives in Orama Zetta's CRDT-replicated store; the control plane self-hosts on the engine it deploys.

**Decision:** Use Orama Zetta as both the control-plane state store (deployed graph, node registry, run history, secret-refs, audit) and the data/compute substrate. **Why:** one engine, no extra database to operate; self-hosting on the thing we deploy. **Supersedes** orama-platform-1's Postgres-spine decision. **Risk:** Orama Zetta lacks transactions + leader election today (see RSK control-plane-on-CRDT).

**Referenced by:** [`DR-1`](requirements.md#dr-1) relates to · [`DS-1`](data.md#ds-1) relates to · [`RSK-3`](risks.md#rsk-3) relates to

### ADR-2 — Execution-graph IR as the compile target  {: #adr-2 }

`draft`  ·  `adr`  ·  issue [#2](https://github.com/oramasearch/zetta/issues/2)

Compile intent/artifacts into an inspectable execution graph (connect→clean→model→index→serve→act).

**Decision:** A professionally-architected, versioned execution-graph IR is the artifact the GUI shows, validates, and deploys. **Open:** reuse 'orly' (orama-platform-1) vs. a Orama Zetta-native IR. **Why:** an inspectable graph (not a black box) is what makes generated systems reviewable and correct-by-construction.

**Realizes / depends on / relates to:** relates to → [`FEAT-2`](backlog.md#feat-2)
**Referenced by:** [`ADR-10`](architecture.md#adr-10) refines

### ADR-3 — Correctness gate before deploy  {: #adr-3 }

`draft`  ·  `adr`  ·  issue [#3](https://github.com/oramasearch/zetta/issues/3)

Validate (schema/leakage/point-in-time + correctness eval) before a graph can deploy.

**Decision:** No graph deploys until it passes a correctness gate. **Why:** self-service that ships confidently-wrong pipelines is worse than the bottleneck it replaces; correctness is the differentiation vs. n8n/Zapier. R1 = compile/type/smoke checks; leakage + point-in-time planned and shown as not-yet-enforced.

**Realizes / depends on / relates to:** mitigates → [`RSK-2`](risks.md#rsk-2) · mitigates → [`RSK-8`](risks.md#rsk-8) · relates to → [`FEAT-3`](backlog.md#feat-3)

### ADR-4 — Compute-near-data via embedded Lua / DDF API  {: #adr-4 }

`draft`  ·  `adr`  ·  issue [#4](https://github.com/oramasearch/zetta/issues/4)

Run user/agent code on the node where the data lives.

**Decision:** Execute generated/user code on the Orama Zetta node holding the data via embedded Lua / a DataFrame API, sandboxed to the node's access scope. **Why:** no warehouse round-trip, no exfiltration — the data-locality moat. **Status:** Orama Zetta engine work, planned.

**Realizes / depends on / relates to:** relates to → [`FEAT-8`](backlog.md#feat-8)
**Referenced by:** [`ADR-17`](architecture.md#adr-17) relates to · [`API-1`](apis.md#api-1) relates to

### ADR-5 — Tiered storage (source → in-memory → cold → re-warm)  {: #adr-5 }

`draft`  ·  `adr`  ·  issue [#5](https://github.com/oramasearch/zetta/issues/5)

Materialize expensive source data into cheap in-memory indexes; age to cold; re-warm on request.

**Decision:** Pull source data (Snowflake first) into in-memory indexes, age to cold storage, re-warm on demand; serve from the local materialized copy. **Why:** the cost + locality story — stop paying warehouse prices for repeated queries. **Status:** Orama Zetta engine work, planned (largest engine bet).

**Realizes / depends on / relates to:** relates to → [`FEAT-7`](backlog.md#feat-7)
**Referenced by:** [`DS-3`](data.md#ds-3) relates to

### ADR-6 — Governed key-scoped access in V1; tiers deferred  {: #adr-6 }

`draft`  ·  `adr`  ·  issue [#6](https://github.com/oramasearch/zetta/issues/6)

Operate over exactly what the login key permits; team/partner/per-dataset tiers later.

**Decision:** V1 has no bespoke permissioning model — inherit the access the connection key already has; layer finer tiers later. **Why:** the full three-tier governance model was never clearly specified by the design partner; key-scoped is safe and shippable, and leaves the door open. Audit + approval gates ship in V1 regardless.

**Realizes / depends on / relates to:** relates to → [`FEAT-9`](backlog.md#feat-9)
**Referenced by:** [`ADR-12`](architecture.md#adr-12) relates to · [`PERM-1`](security.md#perm-1) relates to · [`RULE-3`](backlog.md#rule-3) relates to

### ADR-7 — Self-deploy via a placement dial (local → k8s → cloud)  {: #adr-7 }

`draft`  ·  `adr`  ·  issue [#7](https://github.com/oramasearch/zetta/issues/7)

One deploy action; target chosen per project; nodes provisioned + self-healed.

**Decision:** Deployment is a per-project placement choice (local → private k8s → AWS/Azure/GCP/on-prem), one-button, with controller reconcile + self-heal. **Why:** 'Railway for private-cloud data/AI.' **Risk:** the cloud-provisioning matrix is large — R1 ships local; one cloud target at a time.

**Realizes / depends on / relates to:** mitigates → [`RSK-4`](risks.md#rsk-4) · relates to → [`FEAT-4`](backlog.md#feat-4)
**Referenced by:** [`ADR-15`](architecture.md#adr-15) refines · [`IR-1`](requirements.md#ir-1) relates to

### ADR-8 — R1 local-first on today's Orama Zetta; substrate co-sequenced  {: #adr-8 }

`draft`  ·  `adr`  ·  issue [#8](https://github.com/oramasearch/zetta/issues/8)

Deliver value on what Orama Zetta has now; co-sequence the engine bets.

**Decision:** R1 = import an n8n workflow → correct graph → run on a local Orama Zetta node, using today's engine (CRDT cluster + storage + SQL subset). **Why:** the deep substrate (tiered storage, compute-near-data, indexing, cloud deploy) is unbuilt; the product roadmap must be co-owned with Orama Zetta's, not block on it.

**Realizes / depends on / relates to:** mitigates → [`RSK-1`](risks.md#rsk-1)

### ADR-9 — orama-platform-1 is prior art, not the inherited stack  {: #adr-9 }

`draft`  ·  `adr`  ·  issue [#9](https://github.com/oramasearch/zetta/issues/9)

Borrow ideas (IR, placement dial, controller→k8s); don't re-derive the federation architecture.

**Decision:** Treat the earlier orama-platform plan as prior art — borrow the execution-graph-IR, placement-dial, and controller→k8s mapping ideas — but build Orama Zetta-native and supersede its Postgres-spine decision. **Open:** whether this eventually merges into the orama-platform repo or stays distinct.

**Realizes / depends on / relates to:** relates to → [`RSK-5`](risks.md#rsk-5)

### ADR-10 — Dual-form, Orama Zetta-native execution-graph IR  {: #adr-10 }

`draft`  ·  `adr`  ·  issue [#10](https://github.com/oramasearch/zetta/issues/10)

The IR has two interchangeable forms — code (Lua | Orly) and tabular data (Parquet/CSV/Automerge) — usable together or either alone; it is also the primary extensibility mechanism.

**Decision:** The execution graph / IR is Orama Zetta-native with two forms: (1) **code** — embedded **Lua** (or **Orly**, our DSL) that calls into Orama Zetta's native C++ cluster API; (2) **data** — a **tabular Parquet/CSV/Automerge** representation of the graph/IR. The two are composable (call back and forth) OR usable independently (OR). **Why:** this is also the **primary extensibility mechanism** — e.g. enterprise-specific infrastructure-creation rules can be a set of Lua/Orly scripts and/or Parquet files (code AND data). No dependency on orama-platform-1. **Refines** ADR-2. **Implication:** the GUI inspects/edits both forms; the compiler can emit either.

**Realizes / depends on / relates to:** refines → [`ADR-2`](architecture.md#adr-2) · relates to → [`FEAT-2`](backlog.md#feat-2)
**Referenced by:** [`ADR-11`](architecture.md#adr-11) relates to · [`ADR-16`](architecture.md#adr-16) relates to · [`ARC-5`](architecture.md#arc-5) relates to

### ADR-11 — Runner & Extension abstraction via common interfaces  {: #adr-11 }

`draft`  ·  `adr`  ·  issue [#11](https://github.com/oramasearch/zetta/issues/11)

Everything is built behind common interfaces; concrete runners = Lua + Orly now, Python later. Extensions = code and/or data.

**Decision:** Define **common interfaces** (Runner, Extension) with swappable **concrete implementations**. R1 runners: **Lua** and **Orly**; **Python** (and others) added later behind the same interface. An **Extension** is a unit of customer/enterprise extensibility = **code** (Lua/Orly) and/or **data** (Parquet/CSV/Automerge). **Why:** keeps the platform open and future-proof without re-architecting; the extension system is how enterprises inject their own infra rules and logic. **Relates to** ADR-10 (the IR forms) and ADR-16 (the interface-first principle).

**Realizes / depends on / relates to:** relates to → [`ADR-10`](architecture.md#adr-10) · relates to → [`FEAT-8`](backlog.md#feat-8)
**Referenced by:** [`ADR-13`](architecture.md#adr-13) relates to · [`ADR-16`](architecture.md#adr-16) relates to · [`API-3`](apis.md#api-3) relates to · [`ARC-2`](architecture.md#arc-2) relates to · [`GLO-7`](glossary.md#glo-7) relates to · [`GLO-8`](glossary.md#glo-8) relates to

### ADR-12 — Capability-scoped, deny-by-default extension sandbox  {: #adr-12 }

`draft`  ·  `adr`  ·  issue [#12](https://github.com/oramasearch/zetta/issues/12)

Extension code gets no ambient authority; capability tokens scoped to the invoking user's key; no fs/network egress by default; all API calls audited; approval gates for shared/enterprise-published extensions.

**Decision:** All runner/extension code (Lua/Orly now, Python later) executes in a **capability-scoped, deny-by-default sandbox**. It can only touch the Orama Zetta API/data explicitly granted via **capability tokens scoped to the invoking user's key/access**; **no filesystem or network egress by default**; **every API call is audited**. **Approval gates apply to shared / enterprise-published extensions**, not every personal run. **Why:** arbitrary code runs next to customer data — this is load-bearing for the 'no egress / governed' promise. **Relates to** ADR-6 (key-scoped governance), NFR-1 (no egress), FEAT-9 (governed self-service); **mitigates** the arbitrary-code risk (RSK-7).

**Realizes / depends on / relates to:** mitigates → [`RSK-7`](risks.md#rsk-7) · relates to → [`ADR-6`](architecture.md#adr-6) · relates to → [`FEAT-9`](backlog.md#feat-9) · relates to → [`NFR-1`](requirements.md#nfr-1)
**Referenced by:** [`API-5`](apis.md#api-5) relates to · [`ARC-4`](architecture.md#arc-4) relates to · [`CTL-1`](security.md#ctl-1) relates to · [`GLO-10`](glossary.md#glo-10) relates to · [`PERM-3`](security.md#perm-3) relates to · [`TB-2`](security.md#tb-2) relates to

### ADR-13 — Orly — first-party DSL (Lua-alternative runner)  {: #adr-13 }

`draft`  ·  `adr`  ·  issue [#13](https://github.com/oramasearch/zetta/issues/13)

Orama ships its own DSL, Orly, as an alternative to Lua for the code-form IR/extensions.

**Decision:** Provide **Orly**, a first-party DSL, as a **Lua alternative** for the code form of the IR and for extensions. Orly is a concrete **Runner** behind the common interface (ADR-11), capability-sandboxed like Lua (ADR-12). **Why:** a higher-level, inspectable, safer-by-construction plan language tailored to Orama Zetta orchestration; users can choose Lua (general) or Orly (our DSL). Draws on the orly concept from orama-platform-1 but is implemented Orama Zetta-native, not inherited.

**Realizes / depends on / relates to:** relates to → [`ADR-11`](architecture.md#adr-11)
**Referenced by:** [`GLO-6`](glossary.md#glo-6) relates to

### ADR-14 — Native SDL3/ImGui desktop = cluster node; migrate via SQLite import  {: #adr-14 }

`draft`  ·  `adr`  ·  issue [#14](https://github.com/oramasearch/zetta/issues/14)

The GUI is Orama Zetta's native SDL3/Dear ImGui headed mode (no Tauri/web); the desktop is itself a cluster node; migration from the Amaro Tauri app = import its SQLite DB.

**Decision:** The Orama Zetta desktop GUI is built on Orama Zetta's existing **native SDL3 + Dear ImGui headed mode** — **not** a Tauri/web shell. The desktop **is a cluster node** (zero IPC, native C++). **Migration** from the existing Amaro Tauri desktop consists of **reading/importing the data from that app's SQLite database** into Orama Zetta (see TR-1). **Why:** one native binary, desktop-is-a-node, fast for dense graph/data views; consistent with 'R1 on what exists.' **Relates to** FEAT-10 (GUI surface), TR-1.

**Realizes / depends on / relates to:** relates to → [`FEAT-10`](backlog.md#feat-10) · relates to → [`TR-1`](requirements.md#tr-1)

### ADR-15 — Zetta orchestrates infrastructure via a Cloud Interface abstraction  {: #adr-15 }

`draft`  ·  `adr`  ·  issue [#15](https://github.com/oramasearch/zetta/issues/15)

The desktop/node app is a coordinator/orchestrator; it talks to cloud APIs through a Cloud Interface (concrete impls: local CLI e.g. aws/az/gcloud/kubectl, OR direct HTTP); it deploys headless Zetta nodes into target infra; any authenticated node can orchestrate.

**Decision:** The installer/GUI/desktop **node application is a coordinator/orchestrator** — **infrastructure orchestration IS the platform-engineering job.** It talks to cloud/infra APIs through a **Cloud Interface** abstraction with swappable concrete implementations: (a) **local CLI** wrappers (`aws`, `az`, `gcloud`, `kubectl`, …) and (b) **direct HTTP endpoint** calls (no local CLI required) — both valid. As part of orchestration it can **deploy additional headless Zetta nodes** into the target infrastructure. Because the local desktop is **just another cluster node**, a properly authenticated user can **fire up a different desktop and orchestrate from that node** too. **Refines** ADR-7 (placement dial). **Relates to** FEAT-4 (deploy), IR-1 (infra integration), ADR-16.

**Realizes / depends on / relates to:** refines → [`ADR-7`](architecture.md#adr-7) · relates to → [`FEAT-4`](backlog.md#feat-4) · relates to → [`IR-1`](requirements.md#ir-1)
**Referenced by:** [`ADR-16`](architecture.md#adr-16) relates to · [`ADR-18`](architecture.md#adr-18) relates to · [`ADR-19`](architecture.md#adr-19) refines · [`ADR-20`](architecture.md#adr-20) refines · [`API-4`](apis.md#api-4) relates to · [`ARC-1`](architecture.md#arc-1) relates to · [`ARC-3`](architecture.md#arc-3) relates to · [`CTL-6`](security.md#ctl-6) relates to · [`GLO-9`](glossary.md#glo-9) relates to

### ADR-16 — Interface-first / pluggable-implementations architecture  {: #adr-16 }

`draft`  ·  `adr`  ·  issue [#16](https://github.com/oramasearch/zetta/issues/16)

The platform's extensibility spine: common interfaces (Runner, Extension, Cloud Interface, storage tier, …) with swappable concrete implementations, declared up front.

**Decision:** Build everything by **declaring common interfaces**, with each concrete implementation implementing those interfaces. Applies across the platform: **Runner** (Lua/Orly/Python), **Extension** (code/data), **Cloud Interface** (CLI/HTTP), storage tiers, and future runners/providers. **Why:** this is the platform's extensibility and future-proofing spine — add a runner, a cloud provider, or a storage backend without re-architecting. **Generalizes** ADR-10/11/12/15.

**Realizes / depends on / relates to:** relates to → [`ADR-10`](architecture.md#adr-10) · relates to → [`ADR-11`](architecture.md#adr-11) · relates to → [`ADR-15`](architecture.md#adr-15)
**Referenced by:** [`ADR-17`](architecture.md#adr-17) relates to

### ADR-17 — Native (C++/CUDA) cluster-parallel compute for all heavy operations  {: #adr-17 }

`draft`  ·  `adr`  ·  issue [#17](https://github.com/oramasearch/zetta/issues/17)

Re-implement training, inference, DDF ops, data engineering, and inference serving natively in C++/CUDA/kernel languages and execute them cluster-parallel/concurrent — not by wrapping external (e.g. Python) libraries.

**Decision:** Any compute-heavy algorithm — model **training**, **inference**, **DDF (distributed dataframe) operations**, **data engineering**, **inference serving** — is **re-implemented natively in C++ and/or CUDA (or other kernel languages)** and runs as a **cluster-parallel / cluster-concurrent** operation across Orama Zetta nodes. **Why:** (1) native reimplementation is now cheap/fast with Claude Code; (2) because we **control the infrastructure** (and its cost), we can parallelize or run concurrently at the **appropriate cluster level** — the source of the cost/performance advantage and the 'learns from your data, at scale' story. **Supersedes** the 'bridge via external pipeline / Python-runner training' options. **Relates to** ADR-4 (compute-near-data), ADR-16 (native impls behind common interfaces), FEAT-6 (learns from your data), FEAT-8 (compute-near-data). The R1 churn model may still bridge via the existing pipeline while native primitives are built (see roadmap).

**Realizes / depends on / relates to:** relates to → [`ADR-16`](architecture.md#adr-16) · relates to → [`ADR-4`](architecture.md#adr-4) · relates to → [`FEAT-6`](backlog.md#feat-6) · relates to → [`FEAT-8`](backlog.md#feat-8)
**Referenced by:** [`ADR-20`](architecture.md#adr-20) relates to · [`ARC-6`](architecture.md#arc-6) relates to · [`GLO-12`](glossary.md#glo-12) relates to

### ADR-18 — Cluster trust model: mTLS + per-node identity + capability-scoped orchestration  {: #adr-18 }

`draft`  ·  `adr`  ·  issue [#18](https://github.com/oramasearch/zetta/issues/18)

Every node has a crypto identity; nodes mutually authenticate (mTLS); cluster join needs an enrollment token; orchestration rights are capability-scoped to the authenticated principal. R1 runs single-tenant inside the customer boundary while this is wired.

**Decision (target):** each Orama Zetta node has a **cryptographic per-node identity**; nodes **mutually authenticate via mTLS** (wire the TLS that Corosio already supports — replacing today's plaintext TCP); **joining the cluster requires an enrollment token**; the right to **act as orchestrator** is **capability-scoped to the authenticated principal** (same capability model as the extension sandbox, ADR-12). **R1 reality:** runs **single-tenant inside the customer's network boundary** while mTLS/identity is being wired — documented as a hardening item, not pretended-done. **Mitigates** node impersonation (THR-2) and unauthorized orchestration (THR-4). **Relates to** ADR-15 (orchestration), ADR-12 (capabilities), FEAT-9.

**Realizes / depends on / relates to:** mitigates → [`THR-2`](security.md#thr-2) · mitigates → [`THR-4`](security.md#thr-4) · relates to → [`ADR-15`](architecture.md#adr-15)
**Referenced by:** [`ADR-20`](architecture.md#adr-20) relates to · [`CTL-2`](security.md#ctl-2) relates to · [`PERM-2`](security.md#perm-2) relates to · [`RSK-9`](risks.md#rsk-9) relates to · [`TB-3`](security.md#tb-3) relates to

### ADR-19 — Node bootstrapping is Orama Zetta-native; k0s is inspiration only  {: #adr-19 }

`draft`  ·  `adr`  ·  issue [#19](https://github.com/oramasearch/zetta/issues/19)

Orama Zetta bootstraps and joins its own nodes (enrollment token + mTLS); the Cloud Interface provisions target infra. k0s/k0sctl/k0smotron is a low-friction-UX hint only — not used directly now, not an API to copy verbatim; maybe revisited later.

**Decision:** Node bootstrapping is **Orama Zetta-native.** The desktop is already a node; additional **headless Orama Zetta nodes** are stood up and **join the cluster via an enrollment token + mTLS** (ADR-18). The **Cloud Interface** (ADR-15) provisions/identifies the *target infrastructure* (CLI or HTTP concrete impls); Orama Zetta then drops its own nodes onto it.

**On k0s:** k0s / k0sctl / k0smotron is a **hint** for the *low-friction bootstrap UX* we want to match — a declarative host inventory → a single orchestrate action; token-based join; the clean split between a CLI surface (k0sctl/k0s over SSH) and an API surface (k0smotron CRDs over the k8s API). **We are NOT using k0s directly right now, and will NOT copy its API verbatim.** We may revisit k0s later as one concrete Cloud Interface target. The design stays centered on Orama Zetta and our own bootstrap primitives — k0s is reference inspiration only. **Refines** ADR-15; relates to ADR-18.

**Realizes / depends on / relates to:** refines → [`ADR-15`](architecture.md#adr-15) · relates to → [`ARC-3`](architecture.md#arc-3)
**Referenced by:** [`ARC-7`](architecture.md#arc-7) relates to · [`RUN-1`](delivery.md#run-1) relates to

### ADR-20 — Two provisioning modes: persistent cluster nodes + ephemeral burst (parallel/batch) compute  {: #adr-20 }

`draft`  ·  `adr`  ·  issue [#20](https://github.com/oramasearch/zetta/issues/20)

Beyond long-lived cluster nodes, the Cloud Interface bursts N ephemeral nodes at once for temporary workloads (training, large DDF/data-eng jobs), runs cluster-parallel, then tears down. Each burst node still gets its own (short-lived) identity. Azure Batch/VMSS/Spot are reference only.

**Decision:** the Cloud Interface (ADR-15) supports **two provisioning modes**:

1. **Persistent cluster nodes** — long-lived Orama Zetta nodes that join via enrollment token + mTLS (ADR-18).
2. **Ephemeral burst / parallel-batch compute** — for **temporary workloads** (model **training**, large **DDF**/data-engineering jobs), the orchestrator **provisions N nodes at once**, runs the job **cluster-parallel** (ADR-17), then **tears them down**. Uses a parallel/batch infrastructure API where available.

**Identity at scale (design note, per ADR-18):** each burst node **probably still gets its own (short-lived) identity** — i.e. **bulk/batch enrollment** of per-node identities + capability tokens, revoked on teardown. *Open question:* the most efficient way to mint + revoke 20+ identities at once (batch enrollment vs. a group identity with per-node attestation). Tracked in RSK-9.

**Reference patterns (NOT chosen deps, NOT copied verbatim — same stance as k0s):** Azure **Batch** (`az batch pool create --target-dedicated-nodes N` + low-priority nodes → `job` → parallel `task`s), **VMSS** (`az vmss create --instance-count N`, Flexible orchestration), and **Spot/low-priority** capacity (`--priority Spot --eviction-policy --max-price`) for cost on interruption-tolerant training; equivalents on AWS (Batch) / GCP (Batch). We borrow the *shape* (burst-many, run, tear down, spot-for-cost), not the API. **Refines** ADR-15; relates to ADR-17, ADR-18, FEAT-6.

**Realizes / depends on / relates to:** refines → [`ADR-15`](architecture.md#adr-15) · relates to → [`ADR-17`](architecture.md#adr-17) · relates to → [`ADR-18`](architecture.md#adr-18) · relates to → [`FEAT-6`](backlog.md#feat-6)
**Referenced by:** [`APR-3`](governance.md#apr-3) relates to · [`ARC-8`](architecture.md#arc-8) relates to · [`ENV-4`](delivery.md#env-4) relates to · [`GLO-13`](glossary.md#glo-13) relates to · [`JRN-2`](ux.md#jrn-2) relates to · [`RSK-9`](risks.md#rsk-9) relates to · [`TC-6`](testing.md#tc-6) relates to · [`UC-4`](backlog.md#uc-4) relates to

### ADR-21 — Product name is Orama Zetta; "ZettaDB" is retired  {: #adr-21 }

`draft`  ·  `adr`  ·  issue [#288](https://github.com/oramasearch/zetta/issues/288)

The product is Orama Zetta (working name); the older name 'ZettaDB' is retired — a rename only, no functional change.

## Context
The product/engine was previously called "ZettaDB". Leadership (Casey/Issac/Steve, 2026-06-24) confirmed the product is **Orama Zetta** — `oramasearch/zetta` *is* the product, not a separate engine wrapped by a product.

## Decision
Use **Orama Zetta** as the product name everywhere. Retire "ZettaDB". This is a **rename only — no functional or architectural change**. "Orama Zetta" is the current **working** name and may change.

## Consequences
- All artifacts, docs, and issues referencing "ZettaDB" are renamed to "Orama Zetta".
- `zetta` remains the repo/binary codename.
- Architecture and semantics are unchanged.

**Realizes / depends on / relates to:** relates to → [`VIS-1`](strategy.md#vis-1)

### ADR-22 — Lead with value, not "a database"  {: #adr-22 }

`draft`  ·  `adr`  ·  issue [#289](https://github.com/oramasearch/zetta/issues/289)

Public framing leads with what Orama Zetta does for the user (intent -> deployed, correct intelligence), not the database category.

## Context
People don't care that Orama Zetta is a database — they care what it does for them. The kitchen/meals metaphor (2026-06-24): the engine is the kitchen; the **use cases are the consumable meals** — the emphasis is on the meals.

## Decision
All product framing **leads with the outcome** — "turns a question into running, deployed intelligence" (see the one-pager) — and demotes the technical substrate to "under the hood". Never lead with "a database".

## Consequences
- Vision/positioning artifacts, READMEs, repo descriptions, and the docs site lead value-first.
- Canonical framing: docs/projects/orama-platform-2/one-pager.md.

**Realizes / depends on / relates to:** relates to → [`VIS-1`](strategy.md#vis-1)

### ADR-23 — Use-case-driven development; each release is a consumable product  {: #adr-23 }

`draft`  ·  `adr`  ·  issue [#290](https://github.com/oramasearch/zetta/issues/290)

Releases are consumable use-case slices; priorities trace from a use case's dependency closure. Churn (UC-1) is the first use case.

## Context
Kitchen/meals (2026-06-24): the meals (use cases) are what's consumable, not the kitchen (engine). "Go fat on use cases; ship a menu."

## Decision
Develop **use-case-first**. Each release must be a **consumable product** — a working slice of a use case (e.g. a customer gets a working production churn model within ~an hour). Backlog **priorities are set by a use case's dependency closure**, not by abstract release order. **UC-1 (Motive churn) is the first use case.**

## Consequences
- Prioritization traces UC-1's dependency graph (FEAT-1/2/3/4/6 + their deps).
- New use cases are added to the catalog; rinse and repeat.

**Realizes / depends on / relates to:** relates to → [`FEAT-6`](backlog.md#feat-6) · relates to → [`UC-1`](backlog.md#uc-1)

### ADR-24 — Backlog grooming: a tracking issue is a request to produce an artifact  {: #adr-24 }

`draft`  ·  `adr`  ·  issue [#291](https://github.com/oramasearch/zetta/issues/291)

An issue = a request to produce software / docs / a report; if it produces none, close it (kept + linked, never deleted).

## Context
The blueprint projects to ~278 GitHub issues; most are reference/design artifacts, not actionable work.

## Decision
Treat every tracking issue as a **request to produce an artifact** — software (a PR), docs (a PR), or a report (e.g. a test report). If no artifact is foreseeable, **close it with a reason (kept + linked, never deleted)**. Keep buildable work + risks + releases open. Driven by the `prune-backlog` skill.

## Consequences
- ~195 reference issues close (traceable, reopen-able); ~83 stay open.
- Closed != deleted; the blueprint stays intact.

**Realizes / depends on / relates to:** relates to → [`VIS-1`](strategy.md#vis-1)

## Architecture Elements

### ARC-1 — Coordinator / Orchestrator node  {: #arc-1 }

`draft`  ·  `arch_element`  ·  issue [#32](https://github.com/oramasearch/zetta/issues/32)

The desktop/installer/headless node app that orchestrates infrastructure and the cluster; any authenticated node can orchestrate.

The Orama Zetta node application (desktop headed or headless) acts as the **coordinator/orchestrator**: it drives the Cloud Interface to provision infra, deploys headless Zetta nodes, compiles/validates/deploys graphs, and reconciles state. Symmetric — any authenticated cluster node can take the orchestrator role. Realizes ADR-15.

**Realizes / depends on / relates to:** relates to → [`ADR-15`](architecture.md#adr-15) · relates to → [`FEAT-4`](backlog.md#feat-4)

### ARC-2 — Runner interface + concrete runners  {: #arc-2 }

`draft`  ·  `arch_element`  ·  issue [#33](https://github.com/oramasearch/zetta/issues/33)

Common Runner interface; concrete: LuaRunner, OrlyRunner (now), PythonRunner (later).

The Runner interface executes a code-form IR/extension step inside the capability sandbox, calling the Orama Zetta C++ API. Concrete implementations: Lua and Orly (R1), Python (later). Realizes ADR-11/ADR-13.

**Realizes / depends on / relates to:** relates to → [`ADR-11`](architecture.md#adr-11)

### ARC-3 — Cloud Interface + concrete providers  {: #arc-3 }

`draft`  ·  `arch_element`  ·  issue [#34](https://github.com/oramasearch/zetta/issues/34)

Common Cloud Interface for infra orchestration; concrete: CLI-based (aws/az/gcloud/kubectl) and direct-HTTP.

The Cloud Interface abstracts infrastructure orchestration (provision/scale/deploy headless nodes). Concrete implementations: local-CLI wrappers and direct HTTP-API clients — both valid, chosen per environment/availability. Realizes ADR-15.

**Realizes / depends on / relates to:** relates to → [`ADR-15`](architecture.md#adr-15)
**Referenced by:** [`ADR-19`](architecture.md#adr-19) relates to · [`ARC-7`](architecture.md#arc-7) relates to · [`ARC-8`](architecture.md#arc-8) relates to

### ARC-4 — Extension sandbox  {: #arc-4 }

`draft`  ·  `arch_element`  ·  issue [#35](https://github.com/oramasearch/zetta/issues/35)

Capability-scoped, deny-by-default execution environment for runner/extension code.

Hosts Lua/Orly/Python extension code with no ambient authority; mediates all Orama Zetta API/data access via capability tokens scoped to the invoking user's key; blocks fs/network egress by default; audits every call. Realizes ADR-12.

**Realizes / depends on / relates to:** relates to → [`ADR-12`](architecture.md#adr-12)

### ARC-5 — Dual-form IR engine  {: #arc-5 }

`draft`  ·  `arch_element`  ·  issue [#36](https://github.com/oramasearch/zetta/issues/36)

Compiles/executes the graph in code form (Lua/Orly) and tabular form (Parquet/CSV/Automerge), interchangeably.

Holds the execution graph in both code and tabular forms, lets them call back and forth or run independently, and is the substrate the extensibility system plugs into. Realizes ADR-10.

**Realizes / depends on / relates to:** relates to → [`ADR-10`](architecture.md#adr-10) · relates to → [`FEAT-2`](backlog.md#feat-2)

### ARC-6 — Cluster-parallel native compute engine  {: #arc-6 }

`draft`  ·  `arch_element`  ·  issue [#37](https://github.com/oramasearch/zetta/issues/37)

Executes any operation (training/inference/DDF/data-eng/serving) parallel or concurrent across cluster nodes, in native C++/CUDA.

The engine that runs heavy operations at cluster scale: partitions/parallelizes training, inference, distributed-dataframe ops, data-engineering steps, and serving across Orama Zetta nodes (compute-near-data). Native C++/CUDA; cost/perf tuned because the platform controls the infrastructure. Realizes ADR-17.

**Realizes / depends on / relates to:** relates to → [`ADR-17`](architecture.md#adr-17) · relates to → [`FEAT-6`](backlog.md#feat-6)
**Referenced by:** [`ARC-8`](architecture.md#arc-8) relates to · [`GLO-11`](glossary.md#glo-11) relates to

### ARC-7 — Node bootstrap provider (Orama Zetta-native)  {: #arc-7 }

`draft`  ·  `arch_element`  ·  issue [#38](https://github.com/oramasearch/zetta/issues/38)

Provisions/identifies target infra via the Cloud Interface and joins headless Orama Zetta nodes onto it; k0s is UX inspiration, not a dependency or API to copy.

Provisions/identifies target infrastructure via the **Cloud Interface** (ARC-3) and joins **headless Orama Zetta nodes** onto it (enrollment token + mTLS, ADR-18). **Orama Zetta-native** — k0s/k0sctl/k0smotron noted as **UX inspiration**, not a dependency or an API to copy. Realizes ADR-19.

**Realizes / depends on / relates to:** relates to → [`ADR-19`](architecture.md#adr-19) · relates to → [`ARC-3`](architecture.md#arc-3)

### ARC-8 — Burst / batch compute provisioner  {: #arc-8 }

`draft`  ·  `arch_element`  ·  issue [#39](https://github.com/oramasearch/zetta/issues/39)

A Cloud Interface implementation that provisions many ephemeral nodes at once for parallel temporary workloads, then tears them down.

Implements the Cloud Interface (ARC-3) for **ephemeral parallel compute**: requests N nodes in one operation (mapping to Azure Batch pools/tasks, VMSS instance-count, Spot/low-priority, or AWS/GCP Batch equivalents — reference only), brings them up with per-node short-lived identities (ADR-18), feeds the cluster-parallel compute engine (ARC-6) for training/DDF/data-eng, and reclaims them on completion/eviction. Realizes ADR-20.

**Realizes / depends on / relates to:** relates to → [`ADR-20`](architecture.md#adr-20) · relates to → [`ARC-3`](architecture.md#arc-3) · relates to → [`ARC-6`](architecture.md#arc-6)

## Quality Scenarios

### QAS-1 — Malicious extension cannot egress data  {: #qas-1 }

`draft`  ·  `quality_scenario`  ·  issue [#184](https://github.com/oramasearch/zetta/issues/184)

Under a malicious extension attempting outbound network + over-scope reads, zero data leaves and the attempts are denied + audited.

Stimulus: an extension tries to open a socket and read beyond its capability scope. Response: sandbox denies both; events audited; a full cycle under network capture shows zero unexpected egress. Verifies CTL-1 + CTL-4.

**Realizes / depends on / relates to:** verifies → [`CTL-1`](security.md#ctl-1) · verifies → [`CTL-4`](security.md#ctl-4)
**Referenced by:** [`TP-1`](testing.md#tp-1) verifies

### QAS-2 — Unauthorized node cannot join or orchestrate  {: #qas-2 }

`draft`  ·  `quality_scenario`  ·  issue [#185](https://github.com/oramasearch/zetta/issues/185)

A node without a valid identity/enrollment token cannot join the cluster, and a member without the orchestration capability cannot provision infra.

Stimulus: a rogue process attempts to join over the wire and a member without orchestration rights attempts to deploy a node. Response: mTLS/enrollment rejects the join; capability check denies the orchestration. Verifies CTL-2 + CTL-6 / ADR-18.

**Realizes / depends on / relates to:** verifies → [`CTL-2`](security.md#ctl-2) · verifies → [`CTL-6`](security.md#ctl-6)
**Referenced by:** [`TP-1`](testing.md#tp-1) verifies
