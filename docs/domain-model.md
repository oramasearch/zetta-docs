# Domain Model

Six bounded contexts and the entities, commands, and events inside them.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Bounded Contexts

### BC-1 — Authoring  {: #bc-1 }

`draft`  ·  `bounded_context`  ·  issue [#43](https://github.com/oramasearch/zetta/issues/43)

Intent/artifact → execution-graph IR + correctness gate.

Owns turning a user's intent and imported artifacts into a validated, versioned execution graph. Entities: Project, ImportedArtifact, ExecutionGraph, GraphVersion, ValidationReport.

**Realizes / depends on / relates to:** contains → [`ENT-1`](domain-model.md#ent-1) · contains → [`ENT-2`](domain-model.md#ent-2) · contains → [`ENT-3`](domain-model.md#ent-3) · contains → [`ENT-4`](domain-model.md#ent-4) · contains → [`ENT-5`](domain-model.md#ent-5)

### BC-2 — Orchestration & Infrastructure  {: #bc-2 }

`draft`  ·  `bounded_context`  ·  issue [#44](https://github.com/oramasearch/zetta/issues/44)

Cloud Interface, node bootstrap, burst provisioning, placement.

Owns provisioning target infrastructure and standing up / joining Orama Zetta nodes (persistent and ephemeral-burst). Entities: DeploymentTarget, CloudProvider, EnrollmentToken, BurstRequest.

**Realizes / depends on / relates to:** contains → [`ENT-6`](domain-model.md#ent-6) · contains → [`ENT-7`](domain-model.md#ent-7) · contains → [`ENT-8`](domain-model.md#ent-8) · contains → [`ENT-9`](domain-model.md#ent-9)

### BC-3 — Execution & Compute  {: #bc-3 }

`draft`  ·  `bounded_context`  ·  issue [#45](https://github.com/oramasearch/zetta/issues/45)

Runners, sandbox, cluster-parallel native compute, DDF, training/inference.

Owns executing graphs/extensions in the sandbox and running cluster-parallel native compute (training, inference, DDF, data-eng). Entities: Runner, Extension, Run, ComputeJob, Model, Index, RunOutput.

**Realizes / depends on / relates to:** contains → [`ENT-10`](domain-model.md#ent-10) · contains → [`ENT-11`](domain-model.md#ent-11) · contains → [`ENT-12`](domain-model.md#ent-12) · contains → [`ENT-13`](domain-model.md#ent-13) · contains → [`ENT-14`](domain-model.md#ent-14) · contains → [`ENT-15`](domain-model.md#ent-15) · contains → [`ENT-16`](domain-model.md#ent-16)

### BC-4 — Data & Storage  {: #bc-4 }

`draft`  ·  `bounded_context`  ·  issue [#46](https://github.com/oramasearch/zetta/issues/46)

Tiered storage, indexes, materialization, large objects, control-plane store.

Owns source ingestion, materialization, tiering (hot→cold→re-warm), indexing, and the Orama Zetta control-plane/large-object stores. Entities: SourceConnection, MaterializedView, StorageTier.

**Realizes / depends on / relates to:** contains → [`ENT-17`](domain-model.md#ent-17) · contains → [`ENT-18`](domain-model.md#ent-18) · contains → [`ENT-19`](domain-model.md#ent-19)

### BC-5 — Governance & Identity  {: #bc-5 }

`draft`  ·  `bounded_context`  ·  issue [#47](https://github.com/oramasearch/zetta/issues/47)

Capabilities, key-scoped access, audit, approvals, mTLS/enrollment.

Owns who-can-do-what: identities, capability grants, key-scoped access, audit, approval gates, and node identity. Entities: Principal, AccessKey, Capability, AuditEvent, ApprovalRequest, NodeIdentity.

**Realizes / depends on / relates to:** contains → [`ENT-20`](domain-model.md#ent-20) · contains → [`ENT-21`](domain-model.md#ent-21) · contains → [`ENT-22`](domain-model.md#ent-22) · contains → [`ENT-23`](domain-model.md#ent-23) · contains → [`ENT-24`](domain-model.md#ent-24) · contains → [`ENT-25`](domain-model.md#ent-25)

### BC-6 — Experience & Learning  {: #bc-6 }

`draft`  ·  `bounded_context`  ·  issue [#48](https://github.com/oramasearch/zetta/issues/48)

Grounded loop that improves graph generation over time.

Owns recording grounded run outcomes, scoring them, and refining the graph-generation policy; plus eval tasks. Entities: GroundedExperience, EvalTask, Policy.

**Realizes / depends on / relates to:** contains → [`ENT-26`](domain-model.md#ent-26) · contains → [`ENT-27`](domain-model.md#ent-27) · contains → [`ENT-28`](domain-model.md#ent-28)
**Referenced by:** [`REL-8`](delivery.md#rel-8) relates to

## Domain Entities

### ENT-1 — Project  {: #ent-1 }

`draft`  ·  `domain_entity`  ·  issue [#82](https://github.com/oramasearch/zetta/issues/82)

The AI/data project — the central, user-managed artifact: instantiated from a use-case type on a team's data; owns its execution graph(s), optional components, runs, and provenance.

Authoring context. The **central item** of Orama Zetta: an **AI/data project** a user creates and manages. Instantiated from a **use-case type** (e.g. churn) on the team's own data; composed of **optional components** (graph steps the user toggles); owns its execution-graph versions, runs, and provenance. Persisted in the control-plane store. Managed through its lifecycle to success (ADR-25, data-project management).

**Referenced by:** [`BC-1`](domain-model.md#bc-1) contains · [`CMD-1`](domain-model.md#cmd-1) relates to · [`ADR-25`](architecture.md#adr-25) relates to · [`GLO-14`](glossary.md#glo-14) relates to

### ENT-2 — ImportedArtifact  {: #ent-2 }

`draft`  ·  `domain_entity`  ·  issue [#83](https://github.com/oramasearch/zetta/issues/83)

A source artifact a user hands over (R1: n8n JSON; later SQL/notebook/schema).

Authoring context. Parsed into the execution-graph IR; retains provenance for re-compilation.

**Realizes / depends on / relates to:** realizes → [`FEAT-1`](backlog.md#feat-1)
**Referenced by:** [`BC-1`](domain-model.md#bc-1) contains · [`CMD-2`](domain-model.md#cmd-2) relates to

### ENT-3 — ExecutionGraph  {: #ent-3 }

`draft`  ·  `domain_entity`  ·  issue [#84](https://github.com/oramasearch/zetta/issues/84)

The dual-form IR (code: Lua/Orly + tabular: Parquet/CSV/Automerge) of a data/AI system.

Authoring context. connect→clean→model→index→serve→act. Inspectable/editable; deployed + run. See ADR-10.

**Realizes / depends on / relates to:** realizes → [`FEAT-2`](backlog.md#feat-2)
**Referenced by:** [`BC-1`](domain-model.md#bc-1) contains · [`CMD-3`](domain-model.md#cmd-3) relates to · [`EVT-1`](domain-model.md#evt-1) relates to · [`EVT-6`](domain-model.md#evt-6) relates to

### ENT-4 — GraphVersion  {: #ent-4 }

`draft`  ·  `domain_entity`  ·  issue [#85](https://github.com/oramasearch/zetta/issues/85)

An immutable, versioned snapshot of an ExecutionGraph.

Authoring context. Enables diff/rollback and lineage of which version produced which outputs.

**Referenced by:** [`BC-1`](domain-model.md#bc-1) contains

### ENT-5 — ValidationReport  {: #ent-5 }

`draft`  ·  `domain_entity`  ·  issue [#86](https://github.com/oramasearch/zetta/issues/86)

The correctness-gate result for a GraphVersion (schema/leakage/point-in-time + eval).

Authoring context. Blocks or allows deploy; records why. See ADR-3, FEAT-3.

**Realizes / depends on / relates to:** realizes → [`FEAT-3`](backlog.md#feat-3)
**Referenced by:** [`BC-1`](domain-model.md#bc-1) contains · [`CMD-4`](domain-model.md#cmd-4) relates to · [`EVT-2`](domain-model.md#evt-2) relates to · [`EVT-3`](domain-model.md#evt-3) relates to

### ENT-6 — DeploymentTarget  {: #ent-6 }

`draft`  ·  `domain_entity`  ·  issue [#87](https://github.com/oramasearch/zetta/issues/87)

A placement (local / customer-k8s / customer-VPC / managed-cloud) the orchestrator deploys to.

Orchestration context. Holds the Cloud Interface binding + credentials-ref for a target. See ADR-7/ADR-15.

**Realizes / depends on / relates to:** realizes → [`FEAT-4`](backlog.md#feat-4)
**Referenced by:** [`BC-2`](domain-model.md#bc-2) contains · [`CMD-5`](domain-model.md#cmd-5) relates to · [`CMD-6`](domain-model.md#cmd-6) relates to · [`EVT-4`](domain-model.md#evt-4) relates to

### ENT-7 — CloudProvider  {: #ent-7 }

`draft`  ·  `domain_entity`  ·  issue [#88](https://github.com/oramasearch/zetta/issues/88)

A concrete Cloud Interface implementation (CLI-based or HTTP-API-based).

Orchestration context. Provisions infra + deploys headless nodes; e.g. CLI (aws/az/gcloud/kubectl) or direct HTTP. See ADR-15/ADR-19.

**Referenced by:** [`BC-2`](domain-model.md#bc-2) contains

### ENT-8 — EnrollmentToken  {: #ent-8 }

`draft`  ·  `domain_entity`  ·  issue [#89](https://github.com/oramasearch/zetta/issues/89)

A token that authorizes a node to join the cluster (per-node identity + mTLS).

Orchestration + Governance contexts. TTL'd; bulk-issued for burst nodes; revoked on teardown. See ADR-18.

**Referenced by:** [`BC-2`](domain-model.md#bc-2) contains · [`RET-3`](data.md#ret-3) relates to

### ENT-9 — BurstRequest  {: #ent-9 }

`draft`  ·  `domain_entity`  ·  issue [#90](https://github.com/oramasearch/zetta/issues/90)

A request to provision N ephemeral nodes for a temporary parallel workload, then tear down.

Orchestration context. Drives the burst/batch provisioner; carries count, capacity (e.g. spot), and a cost cap. See ADR-20.

**Referenced by:** [`BC-2`](domain-model.md#bc-2) contains · [`CMD-7`](domain-model.md#cmd-7) relates to · [`EVT-7`](domain-model.md#evt-7) relates to

### ENT-10 — Runner  {: #ent-10 }

`draft`  ·  `domain_entity`  ·  issue [#91](https://github.com/oramasearch/zetta/issues/91)

A concrete executor for a code-form IR/extension step (Lua, Orly; Python later).

Execution context. Implements the common Runner interface; runs inside the capability sandbox. See ADR-11/ADR-13.

**Realizes / depends on / relates to:** realizes → [`FEAT-8`](backlog.md#feat-8)
**Referenced by:** [`BC-3`](domain-model.md#bc-3) contains

### ENT-11 — Extension  {: #ent-11 }

`draft`  ·  `domain_entity`  ·  issue [#92](https://github.com/oramasearch/zetta/issues/92)

A unit of customer/enterprise extensibility = code (Lua/Orly) and/or data (Parquet/CSV/Automerge).

Execution context. Capability-sandboxed; shared/enterprise-published ones pass an approval gate. See ADR-11/ADR-12.

**Referenced by:** [`BC-3`](domain-model.md#bc-3) contains

### ENT-12 — Run  {: #ent-12 }

`draft`  ·  `domain_entity`  ·  issue [#93](https://github.com/oramasearch/zetta/issues/93)

One execution of a deployed graph: status, logs, outputs, lineage.

Execution context. Emits RunStarted/Succeeded/Failed; produces RunOutputs with lineage. See FEAT-5.

**Realizes / depends on / relates to:** realizes → [`FEAT-5`](backlog.md#feat-5)
**Referenced by:** [`BC-3`](domain-model.md#bc-3) contains · [`CMD-8`](domain-model.md#cmd-8) relates to · [`EVT-8`](domain-model.md#evt-8) relates to · [`EVT-9`](domain-model.md#evt-9) relates to

### ENT-13 — ComputeJob  {: #ent-13 }

`draft`  ·  `domain_entity`  ·  issue [#94](https://github.com/oramasearch/zetta/issues/94)

A cluster-parallel native (C++/CUDA) operation: training, inference, DDF, or data-engineering.

Execution context. Partitioned/parallelized across nodes; may run on ephemeral burst nodes. See ADR-17.

**Referenced by:** [`BC-3`](domain-model.md#bc-3) contains

### ENT-14 — Model  {: #ent-14 }

`draft`  ·  `domain_entity`  ·  issue [#95](https://github.com/oramasearch/zetta/issues/95)

A model trained on the customer's data (native cluster-parallel), with drivers/explainability.

Execution context. The 'learns from your data' output; served via inference ComputeJobs. See FEAT-6, ADR-17.

**Realizes / depends on / relates to:** realizes → [`FEAT-6`](backlog.md#feat-6)
**Referenced by:** [`BC-3`](domain-model.md#bc-3) contains · [`CMD-10`](domain-model.md#cmd-10) relates to · [`CMD-9`](domain-model.md#cmd-9) relates to · [`EVT-10`](domain-model.md#evt-10) relates to

### ENT-15 — Index  {: #ent-15 }

`draft`  ·  `domain_entity`  ·  issue [#96](https://github.com/oramasearch/zetta/issues/96)

A full-text / vector / graph index served from the node.

Execution + Data contexts. Built over materialized data; serves fast local queries. See FEAT-7.

**Referenced by:** [`BC-3`](domain-model.md#bc-3) contains · [`EVT-13`](domain-model.md#evt-13) relates to

### ENT-16 — RunOutput  {: #ent-16 }

`draft`  ·  `domain_entity`  ·  issue [#97](https://github.com/oramasearch/zetta/issues/97)

An artifact a run produces: dataset, model, index, report — with lineage.

Execution context. Carries provenance (which graph version, sources, freshness, confidence). See FEAT-5.

**Referenced by:** [`BC-3`](domain-model.md#bc-3) contains · [`EVT-11`](domain-model.md#evt-11) relates to

### ENT-17 — SourceConnection  {: #ent-17 }

`draft`  ·  `domain_entity`  ·  issue [#98](https://github.com/oramasearch/zetta/issues/98)

A governed connection to an external source (e.g. Snowflake) via a secret-ref, never inline.

Data context. Read-only; credentials stored as vault references. See CTL-3, IR-1.

**Referenced by:** [`BC-4`](domain-model.md#bc-4) contains · [`CMD-11`](domain-model.md#cmd-11) relates to · [`EVT-12`](domain-model.md#evt-12) relates to

### ENT-18 — MaterializedView  {: #ent-18 }

`draft`  ·  `domain_entity`  ·  issue [#99](https://github.com/oramasearch/zetta/issues/99)

Pre-summarized/snapshotted source data served from the local store.

Data context. The cost+locality layer; tracks freshness/lag. See FEAT-7, ADR-5.

**Realizes / depends on / relates to:** realizes → [`FEAT-7`](backlog.md#feat-7)
**Referenced by:** [`BC-4`](domain-model.md#bc-4) contains · [`CMD-12`](domain-model.md#cmd-12) relates to

### ENT-19 — StorageTier  {: #ent-19 }

`draft`  ·  `domain_entity`  ·  issue [#100](https://github.com/oramasearch/zetta/issues/100)

A tier in the hot(in-memory)→cold storage hierarchy, with re-warm.

Data context. Tiered storage placement of a dataset/index; re-warmed on request. See ADR-5.

**Referenced by:** [`BC-4`](domain-model.md#bc-4) contains · [`CMD-13`](domain-model.md#cmd-13) relates to

### ENT-20 — Principal  {: #ent-20 }

`draft`  ·  `domain_entity`  ·  issue [#101](https://github.com/oramasearch/zetta/issues/101)

An authenticated actor: user, service, or node.

Governance context. The subject of capability grants and audit. See ADR-6/ADR-18.

**Referenced by:** [`BC-5`](domain-model.md#bc-5) contains

### ENT-21 — AccessKey  {: #ent-21 }

`draft`  ·  `domain_entity`  ·  issue [#102](https://github.com/oramasearch/zetta/issues/102)

The login key whose existing data access scopes a principal's reach (V1 model).

Governance context. Key-scoped access — operate over exactly what the key permits. See ADR-6, PERM-1.

**Referenced by:** [`BC-5`](domain-model.md#bc-5) contains

### ENT-22 — Capability  {: #ent-22 }

`draft`  ·  `domain_entity`  ·  issue [#103](https://github.com/oramasearch/zetta/issues/103)

A deny-by-default grant scoping access to a specific API/data/orchestration right.

Governance context. Unit of authority in the sandbox + for orchestration; TTL'd; audited. See ADR-12, CTL-1/CTL-6.

**Realizes / depends on / relates to:** realizes → [`FEAT-9`](backlog.md#feat-9)
**Referenced by:** [`BC-5`](domain-model.md#bc-5) contains · [`CMD-14`](domain-model.md#cmd-14) relates to · [`EVT-14`](domain-model.md#evt-14) relates to

### ENT-23 — AuditEvent  {: #ent-23 }

`draft`  ·  `domain_entity`  ·  issue [#104](https://github.com/oramasearch/zetta/issues/104)

An immutable record of a graph change, deploy, data access, or capability use.

Governance context. The audit trail; backs governance + no-egress verification. See FEAT-9, CTL-5.

**Referenced by:** [`BC-5`](domain-model.md#bc-5) contains · [`EVT-15`](domain-model.md#evt-15) relates to

### ENT-24 — ApprovalRequest  {: #ent-24 }

`draft`  ·  `domain_entity`  ·  issue [#105](https://github.com/oramasearch/zetta/issues/105)

A gate on a risky/shared action (publish a shared extension, risky deploy).

Governance context. Routed to an approver; resolves to granted/rejected. See FEAT-9, PERM-3.

**Referenced by:** [`BC-5`](domain-model.md#bc-5) contains · [`CMD-15`](domain-model.md#cmd-15) relates to

### ENT-25 — NodeIdentity  {: #ent-25 }

`draft`  ·  `domain_entity`  ·  issue [#106](https://github.com/oramasearch/zetta/issues/106)

A cryptographic per-node identity used for mTLS and orchestration authorization.

Governance context. Issued at enrollment; basis of inter-node trust. See ADR-18, CTL-2.

**Referenced by:** [`BC-5`](domain-model.md#bc-5) contains · [`EVT-5`](domain-model.md#evt-5) relates to

### ENT-26 — GroundedExperience  {: #ent-26 }

`draft`  ·  `domain_entity`  ·  issue [#107](https://github.com/oramasearch/zetta/issues/107)

A recorded run outcome (what happened, scored) used to improve graph generation.

Experience context. Feeds policy refinement; the moat that compounds. See FEAT-6.

**Referenced by:** [`BC-6`](domain-model.md#bc-6) contains · [`EVT-16`](domain-model.md#evt-16) relates to

### ENT-27 — EvalTask  {: #ent-27 }

`draft`  ·  `domain_entity`  ·  issue [#108](https://github.com/oramasearch/zetta/issues/108)

A human-defined task with scoring criteria used to gate policy/generator quality.

Experience context. The promotion gate for the graph-generation policy; also feeds the correctness floor.

**Referenced by:** [`BC-6`](domain-model.md#bc-6) contains

### ENT-28 — Policy  {: #ent-28 }

`draft`  ·  `domain_entity`  ·  issue [#109](https://github.com/oramasearch/zetta/issues/109)

The graph-generation policy that turns intent/artifacts into execution graphs.

Experience context. Refined from grounded experience + evals; the thing that gets better over time.

**Referenced by:** [`BC-6`](domain-model.md#bc-6) contains · [`CMD-16`](domain-model.md#cmd-16) relates to · [`EVT-17`](domain-model.md#evt-17) relates to

## Commands

### CMD-1 — CreateProject  {: #cmd-1 }

`draft`  ·  `domain_command`  ·  issue [#51](https://github.com/oramasearch/zetta/issues/51)

Create a project from NL intent and/or imported artifacts.

Authoring. Produces ProjectCreated; stores provenance.

**Realizes / depends on / relates to:** relates to → [`ENT-1`](domain-model.md#ent-1)

### CMD-2 — ImportArtifact  {: #cmd-2 }

`draft`  ·  `domain_command`  ·  issue [#52](https://github.com/oramasearch/zetta/issues/52)

Import an artifact (R1: n8n JSON) into a project.

Authoring. Parsed toward the graph IR; emits ArtifactImported.

**Realizes / depends on / relates to:** relates to → [`ENT-2`](domain-model.md#ent-2)

### CMD-3 — CompileGraph  {: #cmd-3 }

`draft`  ·  `domain_command`  ·  issue [#53](https://github.com/oramasearch/zetta/issues/53)

Compile intent/artifacts into the dual-form execution-graph IR.

Authoring. Emits GraphCompiled. See ADR-10.

**Realizes / depends on / relates to:** relates to → [`ENT-3`](domain-model.md#ent-3)

### CMD-4 — ValidateGraph  {: #cmd-4 }

`draft`  ·  `domain_command`  ·  issue [#54](https://github.com/oramasearch/zetta/issues/54)

Run the correctness gate over a graph version.

Authoring. Emits GraphValidated or ValidationFailed; blocks deploy on failure. See ADR-3.

**Realizes / depends on / relates to:** relates to → [`ENT-5`](domain-model.md#ent-5)

### CMD-5 — ProvisionInfrastructure  {: #cmd-5 }

`draft`  ·  `domain_command`  ·  issue [#55](https://github.com/oramasearch/zetta/issues/55)

Provision/identify target infra via the Cloud Interface.

Orchestration. Emits InfrastructureProvisioned. See ADR-15.

**Realizes / depends on / relates to:** relates to → [`ENT-6`](domain-model.md#ent-6)

### CMD-6 — DeployGraph  {: #cmd-6 }

`draft`  ·  `domain_command`  ·  issue [#56](https://github.com/oramasearch/zetta/issues/56)

Deploy a validated graph + Orama Zetta nodes onto a target.

Orchestration. Emits GraphDeployed; self-heals. See FEAT-4.

**Realizes / depends on / relates to:** relates to → [`ENT-6`](domain-model.md#ent-6)

### CMD-7 — BurstProvision  {: #cmd-7 }

`draft`  ·  `domain_command`  ·  issue [#57](https://github.com/oramasearch/zetta/issues/57)

Provision N ephemeral nodes for a temporary parallel workload.

Orchestration. Emits NodeJoined (xN); tears down after. See ADR-20.

**Realizes / depends on / relates to:** relates to → [`ENT-9`](domain-model.md#ent-9)

### CMD-8 — StartRun  {: #cmd-8 }

`draft`  ·  `domain_command`  ·  issue [#58](https://github.com/oramasearch/zetta/issues/58)

Execute a deployed graph.

Execution. Emits RunSucceeded/RunFailed; produces RunOutputs. See FEAT-5.

**Realizes / depends on / relates to:** relates to → [`ENT-12`](domain-model.md#ent-12)

### CMD-9 — TrainModel  {: #cmd-9 }

`draft`  ·  `domain_command`  ·  issue [#59](https://github.com/oramasearch/zetta/issues/59)

Train a model on the customer's data (cluster-parallel native).

Execution. Emits ModelTrained. See FEAT-6, ADR-17.

**Realizes / depends on / relates to:** relates to → [`ENT-14`](domain-model.md#ent-14)

### CMD-10 — RunInference  {: #cmd-10 }

`draft`  ·  `domain_command`  ·  issue [#60](https://github.com/oramasearch/zetta/issues/60)

Serve inference from a trained model (cluster-parallel native).

Execution. See ADR-17.

**Realizes / depends on / relates to:** relates to → [`ENT-14`](domain-model.md#ent-14)

### CMD-11 — IngestSource  {: #cmd-11 }

`draft`  ·  `domain_command`  ·  issue [#61](https://github.com/oramasearch/zetta/issues/61)

Pull/CDC data from a source connection into the local store.

Data. Emits SourceIngested. See FEAT-7.

**Realizes / depends on / relates to:** relates to → [`ENT-17`](domain-model.md#ent-17)

### CMD-12 — Materialize  {: #cmd-12 }

`draft`  ·  `domain_command`  ·  issue [#62](https://github.com/oramasearch/zetta/issues/62)

Build a materialized view / snapshot of source data.

Data. Emits DataMaterialized. See ADR-5, FEAT-7.

**Realizes / depends on / relates to:** relates to → [`ENT-18`](domain-model.md#ent-18)

### CMD-13 — Rewarm  {: #cmd-13 }

`draft`  ·  `domain_command`  ·  issue [#63](https://github.com/oramasearch/zetta/issues/63)

Re-warm cold-tier data on request.

Data. Tiered storage. See ADR-5.

**Realizes / depends on / relates to:** relates to → [`ENT-19`](domain-model.md#ent-19)

### CMD-14 — GrantCapability  {: #cmd-14 }

`draft`  ·  `domain_command`  ·  issue [#64](https://github.com/oramasearch/zetta/issues/64)

Grant a deny-by-default capability scoped to a principal/key.

Governance. Emits CapabilityGranted. See ADR-12.

**Realizes / depends on / relates to:** relates to → [`ENT-22`](domain-model.md#ent-22)

### CMD-15 — RequestApproval  {: #cmd-15 }

`draft`  ·  `domain_command`  ·  issue [#65](https://github.com/oramasearch/zetta/issues/65)

Request approval for a risky/shared action (publish extension, risky deploy).

Governance. Resolves to ApprovalGranted/Rejected. See FEAT-9, PERM-3.

**Realizes / depends on / relates to:** relates to → [`ENT-24`](domain-model.md#ent-24)

### CMD-16 — RefinePolicy  {: #cmd-16 }

`draft`  ·  `domain_command`  ·  issue [#66](https://github.com/oramasearch/zetta/issues/66)

Refine the graph-generation policy from grounded experience + evals.

Experience. Emits PolicyRefined. See FEAT-6.

**Realizes / depends on / relates to:** relates to → [`ENT-28`](domain-model.md#ent-28)

## Events

### EVT-1 — GraphCompiled  {: #evt-1 }

`draft`  ·  `domain_event`  ·  issue [#115](https://github.com/oramasearch/zetta/issues/115)

An execution-graph IR was compiled from intent/artifacts.

Authoring. From CompileGraph.

**Realizes / depends on / relates to:** relates to → [`ENT-3`](domain-model.md#ent-3)

### EVT-2 — GraphValidated  {: #evt-2 }

`draft`  ·  `domain_event`  ·  issue [#116](https://github.com/oramasearch/zetta/issues/116)

A graph version passed the correctness gate.

Authoring. Allows deploy.

**Realizes / depends on / relates to:** relates to → [`ENT-5`](domain-model.md#ent-5)

### EVT-3 — ValidationFailed  {: #evt-3 }

`draft`  ·  `domain_event`  ·  issue [#117](https://github.com/oramasearch/zetta/issues/117)

A graph version failed the correctness gate, with reasons.

Authoring. Blocks deploy; surfaces why (schema/leakage/source).

**Realizes / depends on / relates to:** relates to → [`ENT-5`](domain-model.md#ent-5)

### EVT-4 — InfrastructureProvisioned  {: #evt-4 }

`draft`  ·  `domain_event`  ·  issue [#118](https://github.com/oramasearch/zetta/issues/118)

Target infrastructure was provisioned/identified via the Cloud Interface.

Orchestration.

**Realizes / depends on / relates to:** relates to → [`ENT-6`](domain-model.md#ent-6)

### EVT-5 — NodeJoined  {: #evt-5 }

`draft`  ·  `domain_event`  ·  issue [#119](https://github.com/oramasearch/zetta/issues/119)

An Orama Zetta node joined the cluster (enrollment token + mTLS).

Orchestration + Governance. See ADR-18.

**Realizes / depends on / relates to:** relates to → [`ENT-25`](domain-model.md#ent-25)

### EVT-6 — GraphDeployed  {: #evt-6 }

`draft`  ·  `domain_event`  ·  issue [#120](https://github.com/oramasearch/zetta/issues/120)

A validated graph was deployed onto a target and is running.

Orchestration.

**Realizes / depends on / relates to:** relates to → [`ENT-3`](domain-model.md#ent-3)

### EVT-7 — NodeEvicted  {: #evt-7 }

`draft`  ·  `domain_event`  ·  issue [#121](https://github.com/oramasearch/zetta/issues/121)

An ephemeral burst node was evicted (e.g. spot reclamation).

Orchestration. Jobs must tolerate; see RSK-9.

**Realizes / depends on / relates to:** relates to → [`ENT-9`](domain-model.md#ent-9)

### EVT-8 — RunSucceeded  {: #evt-8 }

`draft`  ·  `domain_event`  ·  issue [#122](https://github.com/oramasearch/zetta/issues/122)

A run completed successfully with outputs + lineage.

Execution.

**Realizes / depends on / relates to:** relates to → [`ENT-12`](domain-model.md#ent-12)

### EVT-9 — RunFailed  {: #evt-9 }

`draft`  ·  `domain_event`  ·  issue [#123](https://github.com/oramasearch/zetta/issues/123)

A run failed; the failing step + reason are surfaced.

Execution.

**Realizes / depends on / relates to:** relates to → [`ENT-12`](domain-model.md#ent-12)

### EVT-10 — ModelTrained  {: #evt-10 }

`draft`  ·  `domain_event`  ·  issue [#124](https://github.com/oramasearch/zetta/issues/124)

A model finished training on the customer's data.

Execution. See FEAT-6.

**Realizes / depends on / relates to:** relates to → [`ENT-14`](domain-model.md#ent-14)

### EVT-11 — OutputProduced  {: #evt-11 }

`draft`  ·  `domain_event`  ·  issue [#125](https://github.com/oramasearch/zetta/issues/125)

A run produced an output (dataset/model/index/report) with provenance.

Execution.

**Realizes / depends on / relates to:** relates to → [`ENT-16`](domain-model.md#ent-16)

### EVT-12 — SourceIngested  {: #evt-12 }

`draft`  ·  `domain_event`  ·  issue [#126](https://github.com/oramasearch/zetta/issues/126)

Source data was pulled/CDC'd into the local store.

Data.

**Realizes / depends on / relates to:** relates to → [`ENT-17`](domain-model.md#ent-17)

### EVT-13 — IndexBuilt  {: #evt-13 }

`draft`  ·  `domain_event`  ·  issue [#127](https://github.com/oramasearch/zetta/issues/127)

An index (full-text/vector/graph) was built and is served.

Data + Execution.

**Realizes / depends on / relates to:** relates to → [`ENT-15`](domain-model.md#ent-15)

### EVT-14 — CapabilityGranted  {: #evt-14 }

`draft`  ·  `domain_event`  ·  issue [#128](https://github.com/oramasearch/zetta/issues/128)

A capability was granted to a principal/key.

Governance.

**Realizes / depends on / relates to:** relates to → [`ENT-22`](domain-model.md#ent-22)

### EVT-15 — AuditRecorded  {: #evt-15 }

`draft`  ·  `domain_event`  ·  issue [#129](https://github.com/oramasearch/zetta/issues/129)

An auditable action (graph change/deploy/data access) was logged.

Governance. See CTL-5.

**Realizes / depends on / relates to:** relates to → [`ENT-23`](domain-model.md#ent-23)

### EVT-16 — ExperienceRecorded  {: #evt-16 }

`draft`  ·  `domain_event`  ·  issue [#130](https://github.com/oramasearch/zetta/issues/130)

A grounded run outcome was recorded for learning.

Experience.

**Realizes / depends on / relates to:** relates to → [`ENT-26`](domain-model.md#ent-26)

### EVT-17 — PolicyRefined  {: #evt-17 }

`draft`  ·  `domain_event`  ·  issue [#131](https://github.com/oramasearch/zetta/issues/131)

The graph-generation policy was refined from experience + evals.

Experience.

**Realizes / depends on / relates to:** relates to → [`ENT-28`](domain-model.md#ent-28)
