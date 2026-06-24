# Strategy

Vision, goals, KPIs, assumptions, and scope.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Product Vision

### VIS-1 — Intelligence Velocity  {: #vis-1 }

`draft`  ·  `product_vision`  ·  issue [#278](https://github.com/oramasearch/zetta/issues/278)

Anyone can turn a question into deployed, running, correct intelligence — in the time it takes to describe it.

**Orama Zetta — Intelligence Velocity for Big Thinkers.** Today, getting from a question ('what's driving churn?') to a correct, governed, production system that answers it takes the scarce few who can do data engineering, ML engineering, and platform engineering at once — everyone else waits in their queue. Orama Zetta puts those three in a bottle: describe the problem in plain language (or hand over an artifact you already have), and get back a correct, professionally-architected execution graph, deployed on infrastructure you control, running and learning — with enterprise guardrails. The bottleneck stops being people; it becomes the speed of thought. *Zetta = zettabyte (one billion terabytes): design for the ceiling, so any scale is free headroom.*

**Referenced by:** [`BL-1`](delivery.md#bl-1) relates to · [`GLO-1`](glossary.md#glo-1) relates to · [`GOAL-1`](strategy.md#goal-1) refines · [`GOAL-2`](strategy.md#goal-2) refines · [`GOAL-3`](strategy.md#goal-3) refines · [`GOAL-4`](strategy.md#goal-4) refines · [`ADR-21`](architecture.md#adr-21) relates to · [`ADR-22`](architecture.md#adr-22) relates to · [`ADR-24`](architecture.md#adr-24) relates to

## Goals

### GOAL-1 — Compress Intelligence Velocity  {: #goal-1 }

`draft`  ·  `product_goal`  ·  issue [#162](https://github.com/oramasearch/zetta/issues/162)

Collapse intent → deployed, correct intelligence from quarters to hours.

The headline goal: median time from a user's intent/artifact to a validated graph deployed and producing correct results, measured in hours vs. the weeks–quarters it takes by hand.

**Realizes / depends on / relates to:** refines → [`VIS-1`](strategy.md#vis-1)
**Referenced by:** [`KPI-1`](strategy.md#kpi-1) relates to

### GOAL-2 — Make self-service the default  {: #goal-2 }

`draft`  ·  `product_goal`  ·  issue [#163](https://github.com/oramasearch/zetta/issues/163)

Shift the build-and-deploy capability off the central team to the edge.

Maximize the share of pipelines deployed without the platform team in the loop — directly relieving the shift-left bottleneck. Inverse signal: tickets filed / 'waiting on the platform lead.'

**Realizes / depends on / relates to:** refines → [`VIS-1`](strategy.md#vis-1)
**Referenced by:** [`KPI-3`](strategy.md#kpi-3) relates to

### GOAL-3 — Hold correctness  {: #goal-3 }

`draft`  ·  `product_goal`  ·  issue [#164](https://github.com/oramasearch/zetta/issues/164)

Self-service must never mean confidently-wrong pipelines.

Every generated graph must compile AND run AND produce correct results before it can deploy. Correctness is the differentiation vs. prototype tools; velocity without it is worthless.

**Realizes / depends on / relates to:** refines → [`VIS-1`](strategy.md#vis-1)
**Referenced by:** [`KPI-2`](strategy.md#kpi-2) relates to

### GOAL-4 — Capture the enterprise  {: #goal-4 }

`draft`  ·  `product_goal`  ·  issue [#165](https://github.com/oramasearch/zetta/issues/165)

Governed, in-your-cloud deployment is the paid-buyer unlock.

Deliver in-firewall, identity-scoped, audited deployment so the buyers who'll pay can adopt it. Land one enterprise on one high-value use case, prove the loop, repeat across the champion's network.

**Realizes / depends on / relates to:** refines → [`VIS-1`](strategy.md#vis-1)
**Referenced by:** [`KPI-4`](strategy.md#kpi-4) relates to

## KPIs

### KPI-1 — Median intent→deployed time  {: #kpi-1 }

`draft`  ·  `kpi`  ·  issue [#171](https://github.com/oramasearch/zetta/issues/171)

Primary metric: hours, not quarters.

From 'user submits NL/artifact' to 'validated graph deployed + producing correct results.' Target: hours. R1 checkpoint: graph running locally with correct output in <1 day. Sub-metrics: time-to-graph, time-to-validated, time-to-deployed.

**Realizes / depends on / relates to:** relates to → [`GOAL-1`](strategy.md#goal-1)
**Referenced by:** [`TC-8`](testing.md#tc-8) verifies · [`TP-1`](testing.md#tp-1) verifies

### KPI-2 — Generated-graph correctness rate  {: #kpi-2 }

`draft`  ·  `kpi`  ·  issue [#172](https://github.com/oramasearch/zetta/issues/172)

% of generated graphs that compile AND run AND produce correct results.

Release-blocking gate. Target: set a floor (e.g. ≥90% on the evaluated task set) before self-service deploy ships to non-engineers. Canonical case: entity resolution division-correct (no averaged 'rosy picture'). Track first-try vs. after-one-edit.

**Realizes / depends on / relates to:** relates to → [`GOAL-3`](strategy.md#goal-3)

### KPI-3 — Self-service deploy rate  {: #kpi-3 }

`draft`  ·  `kpi`  ·  issue [#173](https://github.com/oramasearch/zetta/issues/173)

Share of pipelines deployed without the platform team in the loop.

The direct measure of shifting the bottleneck off people. Companion: # of distinct non-engineer users who deploy or run a graph.

**Realizes / depends on / relates to:** relates to → [`GOAL-2`](strategy.md#goal-2)

### KPI-4 — Governance guardrails (zero-violation)  {: #kpi-4 }

`draft`  ·  `kpi`  ·  issue [#174](https://github.com/oramasearch/zetta/issues/174)

No data egress; RBAC enforced; audit complete.

Guardrail metric that must not regress while chasing velocity: governance violations = 0 (no data egress, verifiable under network capture), RBAC enforced, audit trail complete for every deploy/graph-change/data-access. Cost-reduction via tiered storage is directional only (the ~60% figure is unvalidated).

**Realizes / depends on / relates to:** relates to → [`GOAL-4`](strategy.md#goal-4)

## Assumptions

### ASM-1 — Orama Zetta substrate will be built  {: #asm-1 }

`draft`  ·  `assumption`  ·  issue [#40](https://github.com/oramasearch/zetta/issues/40)

Tiered storage, compute-near-data, and indexing land on Orama Zetta's roadmap.

The product's deepest value depends on Orama Zetta capabilities that are currently unbuilt (DDF API, embedded Lua, tiered storage, indexing, cloud deploy, auth). Assumes these are co-sequenced and delivered; R1 is scoped to run on what exists today.

### ASM-2 — Customers want in-firewall deployment  {: #asm-2 }

`draft`  ·  `assumption`  ·  issue [#41](https://github.com/oramasearch/zetta/issues/41)

Target buyers require data to never leave their environment.

Assumes the wedge buyers (e.g. Motive) require on-prem / in-VPC deployment with no data egress — which is structurally why incumbents (Snowflake) can't serve them and why local/private-cloud-first is the right bet.

### ASM-3 — The rinse-and-repeat motion holds  {: #asm-3 }

`draft`  ·  `assumption`  ·  issue [#42](https://github.com/oramasearch/zetta/issues/42)

Land one enterprise → repeat across the champion's network.

Assumes the first enterprise deal is the hard one and each subsequent one is an order of magnitude less work, with the champion introducing the next — making a handful of deals self-sustaining.

## Scope

### SCP-1 — In: the GUI control plane (near-term hero)  {: #scp-1 }

`draft`  ·  `scope_item`  ·  issue [#216](https://github.com/oramasearch/zetta/issues/216)

Ingest → architect → deploy → run → monitor, driving today's Orama Zetta.

IN SCOPE. The desktop GUI is the near-term focus.

### SCP-2 — In: NL + artifact → execution-graph compiler (n8n first)  {: #scp-2 }

`draft`  ·  `scope_item`  ·  issue [#217](https://github.com/oramasearch/zetta/issues/217)

Start with n8n JSON; SQL/notebook/schema planned.

IN SCOPE. Charles's n8n workflows are the ground-truth first artifact type.

### SCP-3 — In: one-button deploy of Orama Zetta nodes + governance  {: #scp-3 }

`draft`  ·  `scope_item`  ·  issue [#218](https://github.com/oramasearch/zetta/issues/218)

Placement dial local→k8s→cloud; key-scoped access, audit, approvals.

IN SCOPE. Deploy to infrastructure the customer controls; governed self-service.

### SCP-4 — Out: general PaaS for arbitrary web apps  {: #scp-4 }

`draft`  ·  `scope_item`  ·  issue [#219](https://github.com/oramasearch/zetta/issues/219)

Not Railway's lane — we're data/AI-native.

OUT OF SCOPE.

### SCP-5 — Out: public multi-tenant SaaS  {: #scp-5 }

`draft`  ·  `scope_item`  ·  issue [#220](https://github.com/oramasearch/zetta/issues/220)

Private-cloud / in-firewall first (the wedge).

OUT OF SCOPE for now.

### SCP-6 — Out: re-deriving orama-platform-1's federation stack  {: #scp-6 }

`draft`  ·  `scope_item`  ·  issue [#221](https://github.com/oramasearch/zetta/issues/221)

Borrow ideas (IR, placement dial, controller→k8s), don't inherit the stack.

OUT OF SCOPE. orama-platform-1 is prior art only; Orama Zetta supersedes its Postgres-spine decision.
