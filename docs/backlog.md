# Backlog

Features, user stories, use cases, and business rules.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Features

### FEAT-1 — Ingest — intent + artifacts  {: #feat-1 }

`draft`  ·  `feature`  ·  issue [#132](https://github.com/oramasearch/zetta/issues/132)

Capture NL intent and import artifacts (R1: n8n JSON) into a project with provenance.

Two input kinds: natural language ('score every active account for churn risk and tell me why') and artifacts the team already has — R1 first artifact type is n8n workflow JSON (Charles's churn workflows are the ground-truth fixture); SQL/notebook/schema planned. Stores raw inputs with provenance for re-compilation.

**Realizes / depends on / relates to:** realizes → [`FR-1`](requirements.md#fr-1) · realizes → [`FR-2`](requirements.md#fr-2)
**Referenced by:** [`ENT-2`](domain-model.md#ent-2) realizes · [`REL-1`](delivery.md#rel-1) contains · [`SCR-2`](ux.md#scr-2) realizes · [`UC-5`](backlog.md#uc-5) relates to · [`US-1`](backlog.md#us-1) refines · [`UC-1`](backlog.md#uc-1) depends on

### FEAT-2 — Architect — compile to execution-graph IR  {: #feat-2 }

`draft`  ·  `feature`  ·  issue [#133](https://github.com/oramasearch/zetta/issues/133)

Compile intent/artifacts into an inspectable execution graph (connect→clean→model→index→serve→act).

The compiler emits a professionally-architected execution graph as the intermediate representation, laid out as a senior data+AI engineer would. The graph is visible and editable, not a black box. IR choice (reuse 'orly' vs. Orama Zetta-native) is an open decision.

**Realizes / depends on / relates to:** realizes → [`FR-3`](requirements.md#fr-3)
**Referenced by:** [`ADR-10`](architecture.md#adr-10) relates to · [`ADR-2`](architecture.md#adr-2) relates to · [`ARC-5`](architecture.md#arc-5) relates to · [`ENT-3`](domain-model.md#ent-3) realizes · [`GLO-2`](glossary.md#glo-2) relates to · [`REL-1`](delivery.md#rel-1) contains · [`SCR-3`](ux.md#scr-3) realizes · [`TC-4`](testing.md#tc-4) verifies · [`UC-2`](backlog.md#uc-2) relates to · [`US-2`](backlog.md#us-2) refines · [`UC-1`](backlog.md#uc-1) depends on

### FEAT-3 — Correctness gate — validate before deploy  {: #feat-3 }

`draft`  ·  `feature`  ·  issue [#134](https://github.com/oramasearch/zetta/issues/134)

Schema/type checks + leakage + point-in-time + a correctness eval; block deploy on failure.

A generated graph must pass validation before it can deploy: schema type-checks against source profiles; data-leakage + point-in-time checks for ML steps; a correctness eval (compile AND run AND produce the right answer — e.g. entity resolution division-correct). Failures surface a reason, not a stack trace. The line vs. 'n8n with an LLM bolted on.'

**Realizes / depends on / relates to:** realizes → [`FR-4`](requirements.md#fr-4)
**Referenced by:** [`ADR-3`](architecture.md#adr-3) relates to · [`ENT-5`](domain-model.md#ent-5) realizes · [`GLO-5`](glossary.md#glo-5) relates to · [`REL-2`](delivery.md#rel-2) contains · [`RULE-1`](backlog.md#rule-1) relates to · [`SCR-4`](ux.md#scr-4) realizes · [`TC-1`](testing.md#tc-1) verifies · [`TP-1`](testing.md#tp-1) verifies · [`US-3`](backlog.md#us-3) refines · [`UC-1`](backlog.md#uc-1) depends on

### FEAT-4 — One-button deploy — placement dial  {: #feat-4 }

`draft`  ·  `feature`  ·  issue [#135](https://github.com/oramasearch/zetta/issues/135)

Provision Orama Zetta nodes + the graph onto a target (R1 local; k8s/cloud planned); self-heal; no egress.

One action provisions Orama Zetta node(s) and the graph onto local → private k8s → AWS/Azure/GCP/on-prem. Control plane reconciles desired→actual and self-heals. Data stays in the customer environment (verifiable — no egress).

**Realizes / depends on / relates to:** realizes → [`FR-5`](requirements.md#fr-5)
**Referenced by:** [`ADR-15`](architecture.md#adr-15) relates to · [`ADR-7`](architecture.md#adr-7) relates to · [`API-7`](apis.md#api-7) relates to · [`APR-2`](governance.md#apr-2) relates to · [`ARC-1`](architecture.md#arc-1) relates to · [`ENT-6`](domain-model.md#ent-6) realizes · [`REL-3`](delivery.md#rel-3) contains · [`RSK-4`](risks.md#rsk-4) affects · [`RUN-1`](delivery.md#run-1) relates to · [`SCR-5`](ux.md#scr-5) realizes · [`TC-3`](testing.md#tc-3) verifies · [`TP-1`](testing.md#tp-1) verifies · [`US-5`](backlog.md#us-5) refines · [`US-8`](backlog.md#us-8) refines · [`UC-1`](backlog.md#uc-1) depends on

### FEAT-5 — Run + monitor + lineage  {: #feat-5 }

`draft`  ·  `feature`  ·  issue [#136](https://github.com/oramasearch/zetta/issues/136)

Execute workflows, build indexes, stream results with lineage/freshness/confidence.

Workflows execute and indexes build on the nodes; results stream back with lineage (sources, steps, freshness, confidence). Run status, logs, and produced artifacts (datasets/models/indexes) are observable and diagnosable.

**Realizes / depends on / relates to:** realizes → [`FR-6`](requirements.md#fr-6)
**Referenced by:** [`ENT-12`](domain-model.md#ent-12) realizes · [`SCR-6`](ux.md#scr-6) realizes · [`US-4`](backlog.md#us-4) refines · [`UC-1`](backlog.md#uc-1) depends on

### FEAT-6 — Learns from your data  {: #feat-6 }

`draft`  ·  `feature`  ·  issue [#137](https://github.com/oramasearch/zetta/issues/137)

Train a model on the customer's data (not inference over a rented model) — real predictive power + drivers.

The differentiator: it trains a model on the customer's data (e.g. XGBoost + SHAP) rather than prompting a rented frontier model — yielding real predictive power and the drivers, and compounding the more it sees. 'Unless you're training a model, you're not learning from your data.' A grounded experience loop improves graph generation over time.

**Realizes / depends on / relates to:** relates to → [`BR-1`](requirements.md#br-1)
**Referenced by:** [`ADR-17`](architecture.md#adr-17) relates to · [`ADR-20`](architecture.md#adr-20) relates to · [`ARC-6`](architecture.md#arc-6) relates to · [`ENT-14`](domain-model.md#ent-14) realizes · [`RSK-2`](risks.md#rsk-2) affects · [`RSK-8`](risks.md#rsk-8) affects · [`RSK-9`](risks.md#rsk-9) affects · [`TP-1`](testing.md#tp-1) verifies · [`UC-1`](backlog.md#uc-1) relates to · [`ADR-23`](architecture.md#adr-23) relates to · [`UC-1`](backlog.md#uc-1) depends on

### FEAT-7 — Tiered storage  {: #feat-7 }

`draft`  ·  `feature`  ·  issue [#138](https://github.com/oramasearch/zetta/issues/138)

Pull source data into in-memory indexes → cold storage → re-warm on request.

Pull expensive source data (Snowflake first) into cheap in-memory indexes, age to cold storage, re-warm on demand; serve queries from the local materialized copy with visible freshness/lag. The cost + locality story. (Orama Zetta engine work — planned.)

**Realizes / depends on / relates to:** relates to → [`NFR-1`](requirements.md#nfr-1)
**Referenced by:** [`ADR-5`](architecture.md#adr-5) relates to · [`ENT-18`](domain-model.md#ent-18) realizes · [`GLO-4`](glossary.md#glo-4) relates to · [`REL-4`](delivery.md#rel-4) contains · [`RSK-1`](risks.md#rsk-1) affects · [`RSK-6`](risks.md#rsk-6) relates to

### FEAT-8 — Compute-near-data  {: #feat-8 }

`draft`  ·  `feature`  ·  issue [#139](https://github.com/oramasearch/zetta/issues/139)

Run user/agent code on the node where the data lives (embedded Lua / DataFrame API).

Embedded Lua / a DataFrame (DDF) API so user- or agent-generated cleaning/featurize/scoring code runs on the node holding the data — no warehouse round-trip, no exfiltration; sandboxed within the node's access scope. (Orama Zetta engine work — planned.)

**Realizes / depends on / relates to:** relates to → [`NFR-1`](requirements.md#nfr-1)
**Referenced by:** [`ADR-11`](architecture.md#adr-11) relates to · [`ADR-17`](architecture.md#adr-17) relates to · [`ADR-4`](architecture.md#adr-4) relates to · [`ENT-10`](domain-model.md#ent-10) realizes · [`GLO-3`](glossary.md#glo-3) relates to · [`REL-5`](delivery.md#rel-5) contains · [`RSK-1`](risks.md#rsk-1) affects · [`RSK-7`](risks.md#rsk-7) affects · [`US-7`](backlog.md#us-7) refines

### FEAT-9 — Governed self-service  {: #feat-9 }

`draft`  ·  `feature`  ·  issue [#140](https://github.com/oramasearch/zetta/issues/140)

Identity-scoped access (Okta/OAuth), audit trail, approval gates; V1 key-scoped.

Runs in the customer environment; access scoped to identity (a tailored view per user, not a service account); complete audit trail of every graph change/deploy/data access; approval gates for risky actions. V1 starts key-scoped (inherit the login key's access); team/partner/per-dataset tiers layer on later.

**Realizes / depends on / relates to:** realizes → [`FR-7`](requirements.md#fr-7)
**Referenced by:** [`ADR-12`](architecture.md#adr-12) relates to · [`ADR-6`](architecture.md#adr-6) relates to · [`CTL-5`](security.md#ctl-5) relates to · [`ENT-22`](domain-model.md#ent-22) realizes · [`JRN-3`](ux.md#jrn-3) relates to · [`REL-6`](delivery.md#rel-6) contains · [`SCR-7`](ux.md#scr-7) realizes · [`TP-1`](testing.md#tp-1) verifies · [`UC-3`](backlog.md#uc-3) relates to · [`US-6`](backlog.md#us-6) refines · [`US-9`](backlog.md#us-9) refines · [`UC-1`](backlog.md#uc-1) depends on

### FEAT-10 — GUI control plane surface  {: #feat-10 }

`draft`  ·  `feature`  ·  issue [#141](https://github.com/oramasearch/zetta/issues/141)

One app: artifact import → NL canvas → graph visualizer → deploy picker → execution monitor.

The product surface that makes the loop usable without a CLI. Open decision: extend Orama Zetta's SDL3/ImGui headed mode vs. a new Tauri/web shell. The velocity is only felt through the GUI.

**Referenced by:** [`ADR-14`](architecture.md#adr-14) relates to · [`API-8`](apis.md#api-8) relates to · [`JRN-1`](ux.md#jrn-1) relates to · [`REL-7`](delivery.md#rel-7) contains

## User Stories

### US-1 — Import an existing workflow and get a correct graph  {: #us-1 }

`draft`  ·  `user_story`  ·  issue [#269](https://github.com/oramasearch/zetta/issues/269)

As Charles, I drop my n8n JSON in and get a correct, professionally-architected graph without rebuilding it.

Given Charles's churn extractor + risk-scoring JSON, when he imports them, then the app produces an explainable execution graph; when it references data a source lacks, it flags the mismatch; and the Gemini-only scoring is replaced by a real predictive step (XGBoost+SHAP).

**Realizes / depends on / relates to:** refines → [`FEAT-1`](backlog.md#feat-1)

### US-2 — Describe a problem in plain language  {: #us-2 }

`draft`  ·  `user_story`  ·  issue [#270](https://github.com/oramasearch/zetta/issues/270)

As Dana, I describe a modeling problem in NL and get a scaffolded, correct graph.

Given 'predict mid-market churn from our Snowflake + support data,' when Dana submits it, then the app produces a graph with featurize → train → SHAP → serve and names the inputs it needs; editing a step re-validates and shows the impact.

**Realizes / depends on / relates to:** refines → [`FEAT-2`](backlog.md#feat-2)

### US-3 — Trust the graph is correct before it runs  {: #us-3 }

`draft`  ·  `user_story`  ·  issue [#271](https://github.com/oramasearch/zetta/issues/271)

As Dana, the platform validates the graph so I'm not deploying a confidently-wrong pipeline.

Given an ML step, validation runs leakage + point-in-time checks or blocks with a reason; the entity-resolution test resolves division-correct (not an averaged 'rosy picture'); a failure shows why (schema/leakage/source), not a stack trace.

**Realizes / depends on / relates to:** refines → [`FEAT-3`](backlog.md#feat-3)

### US-4 — Run it locally first  {: #us-4 }

`draft`  ·  `user_story`  ·  issue [#272](https://github.com/oramasearch/zetta/issues/272)

As Dana, I run the graph on a local Orama Zetta node to see real results before touching cloud infra.

Given a validated graph, when Dana clicks Run, a local Orama Zetta node executes it and streams results + lineage; with synthetic data (no real-data access yet) it still produces an inspectable result.

**Realizes / depends on / relates to:** refines → [`FEAT-5`](backlog.md#feat-5)

### US-5 — Deploy to my own infrastructure, one button  {: #us-5 }

`draft`  ·  `user_story`  ·  issue [#273](https://github.com/oramasearch/zetta/issues/273)

As Charles, I deploy Orama Zetta nodes + graph into my own cloud without hand-provisioning.

Given a validated graph + a target (k8s/VM), when Charles clicks Deploy, Orama Zetta node(s) are provisioned and the graph runs there; a node failure self-heals; on completion, nothing left his environment (verifiable).

**Realizes / depends on / relates to:** refines → [`FEAT-4`](backlog.md#feat-4)

### US-6 — Self-serve safely under governance  {: #us-6 }

`draft`  ·  `user_story`  ·  issue [#274](https://github.com/oramasearch/zetta/issues/274)

As Sam, I ask questions / schedule checks within my access scope — no ticket, no data I shouldn't see.

Given Sam's identity (Okta), results are scoped to what Sam's keys/role can access; any deploy or graph change is recorded in an audit trail; risky changes route through an approval gate.

**Realizes / depends on / relates to:** refines → [`FEAT-9`](backlog.md#feat-9)

### US-7 — Run my code where the data lives  {: #us-7 }

`draft`  ·  `user_story`  ·  issue [#275](https://github.com/oramasearch/zetta/issues/275)

As Dana/the Agent, my cleaning/featurize/scoring runs on the node — no round-trip, no exfiltration.

Given a graph step with custom logic, it executes as embedded Lua / a DDF call on the node holding the data; generated code is sandboxed within the node's access scope.

**Realizes / depends on / relates to:** refines → [`FEAT-8`](backlog.md#feat-8)

### US-8 — Orchestrate from a second authenticated desktop  {: #us-8 }

`draft`  ·  `user_story`  ·  issue [#276](https://github.com/oramasearch/zetta/issues/276)

As Charles, I authenticate a different desktop node and orchestrate the cluster from it.

Given a properly authenticated node, when Charles takes the orchestrator role, then he can provision/deploy with capability-scoped rights. See ADR-15/ADR-18.

**Realizes / depends on / relates to:** refines → [`FEAT-4`](backlog.md#feat-4)

### US-9 — Publish a governed enterprise extension  {: #us-9 }

`draft`  ·  `user_story`  ·  issue [#277](https://github.com/oramasearch/zetta/issues/277)

As Charles, I publish a shared enterprise extension (e.g. infra-creation rules) that passes approval and runs sandboxed.

Given an extension (Lua/Orly + Parquet), when Charles publishes it, then it requires approval (PERM-3) and runs capability-sandboxed (ADR-12).

**Realizes / depends on / relates to:** refines → [`FEAT-9`](backlog.md#feat-9)

## Use Cases

### UC-1 — Investigate churn (the Motive case)  {: #uc-1 }

`draft`  ·  `use_case`  ·  issue [#264](https://github.com/oramasearch/zetta/issues/264)

Import the churn workflows → correct graph with a trained model → deploy in-firewall → devs self-serve.

**Primary use case — the Motive churn build (Charles, PER-1).** Import Charles's existing churn workflows (n8n) → architect a correct execution graph → train a real churn model on the data (not LLM inference) → validate (correctness gate) → deploy in-firewall → devs self-serve.

**The bar:** a customer shows up and has a **working production churn model within ~an hour** — real answers about *where we're losing customers*. Baseline model **XGBoost** (good enough; a bespoke model can follow).

**Bootstrap:** where real data access is gated, **generate synthetic data** (profiler over the schema) to develop + train against, then swap to real data once keys land.

**Exercises the whole loop:** ingest (FEAT-1) → architect (FEAT-2) → correctness gate (FEAT-3) → deploy (FEAT-4) → run + monitor (FEAT-5) → learns from your data (FEAT-6), under **key-scoped access** (RULE-3) and governed self-service (FEAT-9). Correctness anchored by entity-resolution-division-correct (TC-4).

**Use-case-driven:** UC-1 is the **first use case**; its dependency closure drives backlog priority (see ADR-23). Each release is a consumable slice of churn.

**Realizes / depends on / relates to:** relates to → [`FEAT-6`](backlog.md#feat-6) · relates to → [`PER-1`](personas.md#per-1) · depends on → [`FEAT-1`](backlog.md#feat-1) · depends on → [`FEAT-2`](backlog.md#feat-2) · depends on → [`FEAT-3`](backlog.md#feat-3) · depends on → [`FEAT-4`](backlog.md#feat-4) · depends on → [`FEAT-5`](backlog.md#feat-5) · depends on → [`FEAT-6`](backlog.md#feat-6) · depends on → [`FEAT-9`](backlog.md#feat-9) · relates to → [`RULE-3`](backlog.md#rule-3) · relates to → [`TC-4`](testing.md#tc-4)
**Referenced by:** [`ADR-23`](architecture.md#adr-23) relates to

### UC-2 — Build + deploy a pipeline from natural language  {: #uc-2 }

`draft`  ·  `use_case`  ·  issue [#265](https://github.com/oramasearch/zetta/issues/265)

Describe a data/AI problem → get a correct, deployed, running pipeline.

Dana (PER-2). The general flow beyond churn. See FEAT-2/FEAT-4.

**Realizes / depends on / relates to:** relates to → [`FEAT-2`](backlog.md#feat-2)

### UC-3 — Ask an ad-hoc question (governed)  {: #uc-3 }

`draft`  ·  `use_case`  ·  issue [#266](https://github.com/oramasearch/zetta/issues/266)

A business user asks in plain language and gets a grounded, access-scoped answer.

Sam (PER-3). No ticket; identity-scoped. See FEAT-9/JRN-3.

**Realizes / depends on / relates to:** relates to → [`FEAT-9`](backlog.md#feat-9) · relates to → [`PER-3`](personas.md#per-3)

### UC-4 — Burst-train a model on temporary nodes  {: #uc-4 }

`draft`  ·  `use_case`  ·  issue [#267](https://github.com/oramasearch/zetta/issues/267)

Provision N ephemeral nodes → cluster-parallel train → tear down → model served.

Temporary workload. See ADR-20/JRN-2.

**Realizes / depends on / relates to:** relates to → [`ADR-20`](architecture.md#adr-20)

### UC-5 — Import + modernize an existing n8n workflow  {: #uc-5 }

`draft`  ·  `use_case`  ·  issue [#268](https://github.com/oramasearch/zetta/issues/268)

Bring an n8n workflow → re-architect into a correct graph (real model where there was an LLM guess).

The migration-of-logic case. See FEAT-1/US-1.

**Realizes / depends on / relates to:** relates to → [`FEAT-1`](backlog.md#feat-1)

## Business Rules

### RULE-1 — No deploy without a passing correctness gate  {: #rule-1 }

`draft`  ·  `business_rule`  ·  issue [#209](https://github.com/oramasearch/zetta/issues/209)

A graph version cannot deploy unless its ValidationReport passes.

See ADR-3/FEAT-3/RULE-enforcement.

**Realizes / depends on / relates to:** relates to → [`FEAT-3`](backlog.md#feat-3)

### RULE-2 — No data egress by default  {: #rule-2 }

`draft`  ·  `business_rule`  ·  issue [#210](https://github.com/oramasearch/zetta/issues/210)

No outbound network from graph/extension execution unless explicitly configured + audited.

See NFR-1/CTL-4/TB-1.

**Realizes / depends on / relates to:** relates to → [`NFR-1`](requirements.md#nfr-1)

### RULE-3 — Key-scoped access (V1)  {: #rule-3 }

`draft`  ·  `business_rule`  ·  issue [#211](https://github.com/oramasearch/zetta/issues/211)

A principal operates over exactly the data the login key already permits.

See ADR-6/PERM-1.

**Realizes / depends on / relates to:** relates to → [`ADR-6`](architecture.md#adr-6)
**Referenced by:** [`UC-1`](backlog.md#uc-1) relates to

### RULE-4 — Shared/enterprise extensions require approval  {: #rule-4 }

`draft`  ·  `business_rule`  ·  issue [#212](https://github.com/oramasearch/zetta/issues/212)

Publishing a shared/enterprise extension passes an approval gate; personal runs do not.

See PERM-3/APR-1/ADR-12.

**Realizes / depends on / relates to:** relates to → [`PERM-3`](security.md#perm-3)

### RULE-5 — Burst jobs must be eviction-tolerant  {: #rule-5 }

`draft`  ·  `business_rule`  ·  issue [#213](https://github.com/oramasearch/zetta/issues/213)

Workloads on ephemeral/spot nodes must checkpoint/restart to survive eviction.

See RSK-9/ADR-20/NodeEvicted.

**Realizes / depends on / relates to:** relates to → [`RSK-9`](risks.md#rsk-9)

### RULE-6 — Secrets stored as references, never inline  {: #rule-6 }

`draft`  ·  `business_rule`  ·  issue [#214](https://github.com/oramasearch/zetta/issues/214)

Credentials are vault references; never embedded in project/run records or logs.

See CTL-3/ENT-17.

**Realizes / depends on / relates to:** relates to → [`CTL-3`](security.md#ctl-3)
