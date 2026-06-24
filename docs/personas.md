# Personas & Stakeholders

Who Orama Zetta is for, and who buys it.

!!! note "Generated from the wtm blueprint"
    Source of truth is worktree-manager project **ORAMA-ZETTA**. Each item links to its tracking issue on [`oramasearch/zetta`](https://github.com/oramasearch/zetta/issues). Do not hand-edit — re-run `zetta-sync`.

## Personas

### PER-1 — Charles — bottlenecked platform / AI lead  {: #per-1 }

`draft`  ·  `persona`  ·  issue [#177](https://github.com/oramasearch/zetta/issues/177)

Primary persona. Senior platform engineer; everything funnels through him.

At a 5,000-person company with a CEO mandate to understand mid-market churn. Fluent in n8n/Postgres/Snowflake/Gemini; not a research ML scientist. Runs a hand-built n8n + sidecar + Postgres churn system only he can operate. Wants self-service, a downloadable build his devs run unaided, and in-firewall governance. 'You're too slow' — for two years.

**Realizes / depends on / relates to:** relates to → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`STK-1`](personas.md#stk-1) relates to · [`UC-1`](backlog.md#uc-1) relates to

### PER-2 — Dana — by-hand data scientist / ML engineer  {: #per-2 }

`draft`  ·  `persona`  ·  issue [#178](https://github.com/oramasearch/zetta/issues/178)

Can build the model; can't stand up the plumbing + deploy.

High ML comfort, lower k8s/platform comfort. Most time goes to wrangling + infra, not modeling; prototypes die in notebooks; deployment is someone else's quarter-long project. Wants a correct model deployed in a day, with leakage/point-in-time checks built in, and a synthetic-data path when real data is behind a firewall.

**Realizes / depends on / relates to:** relates to → [`SR-1`](requirements.md#sr-1)

### PER-3 — Sam — waiting analyst / business user  {: #per-3 }

`draft`  ·  `persona`  ·  issue [#179](https://github.com/oramasearch/zetta/issues/179)

Lives in reports; wants answers without filing a ticket.

No engineering background. Dependent on IT/platform for everything; self-serve tools can't safely touch governed enterprise data. Wants 'what should I focus on today' — scoped to what they're allowed to see — not a dashboard to maintain.

**Realizes / depends on / relates to:** relates to → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`UC-3`](backlog.md#uc-3) relates to

### PER-4 — The Agent — AI as a first-class operator  {: #per-4 }

`draft`  ·  `persona`  ·  issue [#180](https://github.com/oramasearch/zetta/issues/180)

Authors execution graphs and runs code where the data lives.

An LLM agent (Claude/Gemini/local) that generates graphs, calls the compute-near-data API, and learns from grounded outcomes. Wants to spend cycles reasoning, not on remote administration; needs a local substrate and a governed way to run generated code against real data.

**Realizes / depends on / relates to:** relates to → [`SR-1`](requirements.md#sr-1)
**Referenced by:** [`API-6`](apis.md#api-6) relates to

## Stakeholders

### STK-1 — Enterprise champion (buyer-sponsor)  {: #stk-1 }

`draft`  ·  `stakeholder`  ·  issue [#230](https://github.com/oramasearch/zetta/issues/230)

The platform/AI lead with a CEO mandate who sponsors and pilots the deal.

The internal champion (e.g. Charles @ Motive) who builds the ROI case, drives the pilot, and introduces the next customer. Path to contract: developer thumbs-up + business thumbs-up → license + roadmap conversation.

**Realizes / depends on / relates to:** relates to → [`PER-1`](personas.md#per-1)

### STK-2 — Enterprise security / CISO team  {: #stk-2 }

`draft`  ·  `stakeholder`  ·  issue [#231](https://github.com/oramasearch/zetta/issues/231)

Gatekeeper on in-firewall deployment, data residency, and access control.

Approves the contractor/deployment model; requires no data egress, identity-scoped access, audit, and (eventually) SOC 2. The governance model is the build-vs-buy differentiator they care about.

**Realizes / depends on / relates to:** relates to → [`NFR-1`](requirements.md#nfr-1)

### STK-3 — Orama (product + engineering)  {: #stk-3 }

`draft`  ·  `stakeholder`  ·  issue [#232](https://github.com/oramasearch/zetta/issues/232)

Builds Orama Zetta and co-sequences the Orama Zetta engine roadmap.

Owns the GUI/compiler/correctness-gate and must co-own Orama Zetta's substrate roadmap (tiered storage, compute-near-data, indexing, deploy, auth) since the product's value is gated on it.

**Realizes / depends on / relates to:** relates to → [`RSK-1`](risks.md#rsk-1)
